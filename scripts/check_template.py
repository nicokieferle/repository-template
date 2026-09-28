"""Prüft das Dokumentationstemplate; keine Anwendungs- oder CI-Abnahme."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
STANDARD_VERSION = "1.6"
TEMPLATES = (
    "AGENTS.md.template",
    "feature.md.template",
    "plan.md.template",
    "improvement.md.template",
    "lesson.md.template",
    "decision.md.template",
    "testing.md.template",
    "architecture.md.template",
    "configuration.md.template",
    "REQUIREMENTS.md.template",
    "ROADMAP.md.template",
)


def anchors(path: Path) -> set[str]:
    """Ermittelt GitHub-ähnliche Anker aus Markdown-Überschriften."""
    result = set()
    counts = {}
    fenced = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = re.match(r"^#{1,6} +(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1)).replace("`", "")
        slug = re.sub(r"[^\w -]", "", title.casefold()).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(f"{slug}-{number}" if number else slug)
    return result


def main() -> int:
    errors = []
    required = [
        "README.md", "AGENTS.md", "SETUP.md", "REPOSITORY_STANDARD.md",
        "REQUIREMENTS.md", "ROADMAP.md",
        "templates/README.md", "templates/README.md.template",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/feature_request.md",
        ".github/pull_request_template.md",
        ".gitignore", ".gitattributes", ".editorconfig",
        *[f"templates/{name}" for name in TEMPLATES],
    ]
    for relative in required:
        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            errors.append(f"Fehlende oder ungeeignete Datei: {relative}")
    if errors:
        print("\n".join(errors))
        return 1
    standard = (ROOT / "REPOSITORY_STANDARD.md").read_text(encoding="utf-8")
    if not re.search(rf"^Version: {re.escape(STANDARD_VERSION)}\b", standard, re.M):
        errors.append("Unerwartete Standardversion; bewusste Anpassung erforderlich.")
    for relative, marker in {
        "README.md": f"Repo-Standards {STANDARD_VERSION}",
        "AGENTS.md": f"Basis: REPOSITORY_STANDARD.md {STANDARD_VERSION}",
        "SETUP.md": f"Standardversion {STANDARD_VERSION}",
        "templates/AGENTS.md.template": f"Basis: REPOSITORY_STANDARD.md {STANDARD_VERSION}",
    }.items():
        if marker not in (ROOT / relative).read_text(encoding="utf-8"):
            errors.append(f"Veralteter Standardverweis in {relative}")
    sections = re.findall(r"^## (\d+)\. ", standard, re.M)
    if sections != [str(number) for number in range(1, 18)]:
        errors.append("Standardabschnitte 1–17 nicht vollständig oder falsch geordnet.")
    blocks = re.findall(r"```markdown\n(.*?)\n```", standard, re.S)
    if len(blocks) != len(TEMPLATES):
        errors.append("Anzahl der Muster stimmt nicht mit Abschnitt 14 überein.")
    else:
        for name, block in zip(TEMPLATES, blocks):
            actual = (ROOT / "templates" / name).read_text(encoding="utf-8")
            if actual != block.strip() + "\n":
                errors.append(f"Vorlage weicht vom Standard ab: {name}")
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in (".md", ".template"):
            continue
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            errors.append(f"Abschließender Zeilenumbruch fehlt: {path.relative_to(ROOT)}")
        if len(re.findall(r"^```", text, re.M)) % 2:
            errors.append(f"Offener Codeblock: {path.relative_to(ROOT)}")
        # Muster und Codebeispiele enthalten absichtlich noch keine realen Projektpfade.
        if path.suffix == ".template":
            continue
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", prose):
            if "://" in target:
                continue
            target_path, _, fragment = unquote(target).partition("#")
            destination = path.parent / target_path if target_path else path
            if not destination.exists():
                errors.append(f"Fehlendes Linkziel in {path.relative_to(ROOT)}: {target}")
            elif fragment and destination.is_file() and fragment not in anchors(destination):
                errors.append(f"Fehlender Anker in {path.relative_to(ROOT)}: {target}")
    if errors:
        print("Template-Prüfung: FEHLER")
        print("\n".join(errors))
        return 1
    print(f"Template-Prüfung: OK (Standard {STANDARD_VERSION}, elf synchronisierte Muster, lokale Links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
