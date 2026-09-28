# Arbeitsregeln für das Repository Template

Basis: REPOSITORY_STANDARD.md 1.6 · Stand: 28. September 2026

## Zuerst den Repository-Typ bestimmen

Diese Datei gilt für das zentrale Template. In einem daraus erzeugten, noch nicht eingerichteten Projekt ist sie eine vorläufige Einstiegsanweisung: Bei beauftragter Einrichtung [SETUP.md](SETUP.md) anwenden und anschließend durch projektspezifische Regeln ersetzen. Das bloße Lesen startet keinen Einrichtungsauftrag.

## Lesewege

- Zielbild: [REQUIREMENTS.md](REQUIREMENTS.md); Phasen: [ROADMAP.md](ROADMAP.md); Status und Vorschläge: [GitHub Issues](https://github.com/Hengsto/repository-template/issues). Betroffene Pfade, Standardabschnitte und Schnittstellen gezielt suchen.
- Prüfung und tatsächliche CI-Grenzen: [README.md#prüfungen](README.md#prüfungen). Lokal: `python3 scripts/check_template.py` (Python 3.11+).
- Bei Standardänderungen die betroffenen Abschnitte in [REPOSITORY_STANDARD.md](REPOSITORY_STANDARD.md), die synchronisierten Muster unter [templates/](templates/README.md) und [SETUP.md](SETUP.md) abgleichen. Den ganzen Standard für Einrichtung, umfassende Änderungen oder unklare Auswirkungen lesen.
- Für GitHub-Einträge [Fehlerbericht](.github/ISSUE_TEMPLATE/bug_report.md), [Verbesserung/Funktion](.github/ISSUE_TEMPLATE/feature_request.md) oder [PR-Vorlage](.github/pull_request_template.md) verwenden; bei API/CLI-Erstellung passende Inhalte ausdrücklich übernehmen. Bestehende gleichwertige Inhalte erhalten, offene Fragen und ausstehende Nachweise kenntlich machen.

## Kernregeln

- Neue Aufgabe: Branch, Diff, unversionierte Dateien und relevante Issues prüfen; fremde Arbeit erhalten. Vor wesentlichen Änderungen überprüfbare Abnahmekriterien festhalten; komplexe oder riskante Arbeit technisch planen.
- Auftrag und nötige Anpassungen umsetzen. Unabhängige Vorschläge am Aufgabenort erfassen; Vorschläge sind keine Ausführungsaufträge. Einträge nur mit Nachweis und Begründung schließen; unklare Konflikte zwischen beschlossenen Plänen klären. Keine zweite Statusliste anlegen.
- Standard, Muster und Setup konsistent halten. Die elf Muster in Abschnitt 14 und `templates/` nicht unabhängig ändern; keine Projektbesonderheiten als globale Vorgabe übernehmen.
- Betroffene Dokumentation im selben PR pflegen. Passende Prüfungen mit Umgebung, Codezustand, Ergebnis und Beleg zuordnen; fehlende Nachweise benennen. Lokaler Erfolg ist kein CI-Nachweis.
- Bei Unterbrechung den technischen Stand und nächsten Schritt im vorhandenen Plan oder Auftrag festhalten. Fehlenden Issue-Zugriff und nötige Übertragungen mit Zielort, Zuständigkeit und nächstem Abgleich sichtbar machen; wesentliche Abnahmelücken blockieren den betroffenen Merge.
- Den gesamten Diff vor Übergabe auf unbeabsichtigte Änderungen prüfen. Dokumentation deutsch; Datei-/Ordnernamen und Codebezeichner englisch. Keine Secrets oder vollständigen privaten Nutzdaten aufnehmen.

## Git und Grenzen

Funktionale Änderungen erfolgen über Branch und PR. Einrichtung, Veröffentlichung, Merge und Deployment sind getrennte Aktionen; bestehende konkrete Befugnisse berücksichtigen. Keine pauschale Auto-Merge-Freigabe. Erforderliche Prüfungen müssen am maßgeblichen aktuellen PR-Stand nachgewiesen sein; fehlende CI-Absicherung ist eine offene Einrichtungslücke.

Dieses Template enthält keine automatische Worker-Steuerung, Hintergrundüberwachung, technische Merge-Sperre oder Deploymentfreigabe.
