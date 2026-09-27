"""Prüft das Dokumentationstemplate; keine Anwendungs- oder CI-Abnahme."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
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


def main() -> int:
    errors = []
    required = [
        "README.md", "AGENTS.md", "SETUP.md", "REPOSITORY_STANDARD.md",
        "REQUIREMENTS.md", "ROADMAP.md",
        "templates/README.md", "templates/README.md.template",
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
    if not re.search(r"^Version: 1\.4\b", standard, re.M):
        errors.append("Unerwartete Standardversion; bewusste Anpassung erforderlich.")
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
            if "://" in target or target.startswith("#"):
                continue
            target_path = target.split("#", 1)[0]
            if not (path.parent / target_path).exists():
                errors.append(f"Fehlendes Linkziel in {path.relative_to(ROOT)}: {target}")
    if errors:
        print("Template-Prüfung: FEHLER")
        print("\n".join(errors))
        return 1
    print("Template-Prüfung: OK (Standard 1.4, elf synchronisierte Muster, lokale Dateiverweise)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
