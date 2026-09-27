# Repository Template

Schlanker Ausgangspunkt für neue Projekte und zentrale Pflege des **Repo-Standards 1.4** (27. September 2026).

Dieses Repository enthält Dokumentation und Vorlagen, keinen Anwendungscode. Es legt keine Sprache, Datenbank, Containertechnik oder CI-Plattform für Zielprojekte fest.

## Verwendung

### Neues Projekt

1. Auf GitHub über **Use this template** ein eigenes Projekt-Repository erzeugen. Dieses Repository ist bereits als Template aktiviert.
2. Projektname, Zweck und wesentliche Anforderungen mitgeben und den Auftrag aus [SETUP.md](SETUP.md) an den Agenten im **Zielrepository** übergeben. Ein vorbereiteter Auftrag ist noch kein gestarteter Lauf.
3. Der Agent ersetzt die Einstiegstexte durch konkrete Projektinformationen und prüft die Einrichtung. Unbekannte Befehle, Checks und Autorisierungen werden als offene Punkte ausgewiesen.

Ein gewöhnlicher Git-Klon übernimmt die Historie des Vorlagenrepos. Für eigenständige neue Projekte ist eine Erstellung aus dem Template oder ein neues Git-Repository aus diesen Dateien zweckmäßiger.

### Bestehendes Projekt

Den [Standard](REPOSITORY_STANDARD.md) und [Einrichtungsauftrag](SETUP.md) als Referenz bereitstellen. Nicht den gesamten Template-Inhalt über das bestehende Repo kopieren. Vorhandene Anweisungen, Dateien, Kommentare, Arbeitsstände und geeignete Abläufe erhalten; nur beauftragte Anpassungen vornehmen.

## Maßgebliche Dateien

| Datei | Zweck |
| --- | --- |
| [REPOSITORY_STANDARD.md](REPOSITORY_STANDARD.md) | Zentrale Vorgabe, vollständig bei Einrichtung oder bewusster Aktualisierung lesen. |
| [AGENTS.md](AGENTS.md) | Arbeitsanweisungen für die Pflege dieses Templates und Erkennung noch nicht eingerichteter Ableitungen. |
| [SETUP.md](SETUP.md) | Einmaliger Auftrag zur projektspezifischen Einrichtung. |
| [templates/README.md](templates/README.md) | Auswahl und Verwendung der optionalen Strukturhilfen. |
| [scripts/check_template.py](scripts/check_template.py) | Abgleich der extrahierten Vorlagen mit dem Standard und Prüfung der Paketstruktur, lokal und in CI. |
| [.github/workflows/template-check.yml](.github/workflows/template-check.yml) | GitHub-Actions-Workflow für dieselbe Template-Prüfung. |

Im Zielprojekt sind README.md und AGENTS.md die Einstiege. Längerfristige Projekte führen außerdem REQUIREMENTS.md und ROADMAP.md im Hauptverzeichnis; kleine Experimente dürfen die begründete README-Ausnahme aus Standardabschnitt 3 nutzen. Weitere Dokumente entstehen nur bei Bedarf.

Zielbild dieses Templates: [REQUIREMENTS.md](REQUIREMENTS.md). Weiterentwicklung: [ROADMAP.md](ROADMAP.md).

## Architektur und Pflege

Der Standard ist die maßgebliche Regelfassung. Die elf Muster aus Abschnitt 14 liegen zusätzlich als direkt verwendbare Dateien vor; das Prüfsystem erkennt Abweichungen. Die README-Vorlage ist eine ergänzende Strukturhilfe. SETUP.md verweist auf den maßgeblichen Einrichtungs-Prompt in Abschnitt 16 statt ihn erneut zu pflegen.

Die Zielprojekte erhalten eigene, eigenständig verständliche Regeln. Sie benötigen im normalen Betrieb keinen Zugriff auf dieses Template. Eine spätere Standardversion wird bewusst geprüft und übernommen, niemals automatisch als neue Regel aktiviert.

Aufgabenort für die Pflege dieses Templates: [GitHub Issues in Hengsto/repository-template](https://github.com/Hengsto/repository-template/issues). Suche dort nach betroffenen Pfaden, Standardabschnitten und Begriffen; vorhandene Labels nur ergänzend nutzen. Es wird kein zusätzlicher Backlog angelegt.

## Prüfungen

Voraussetzung: Python 3.11 oder neuer; keine zusätzlichen Pakete. Aus dem Repository-Wurzelverzeichnis:

```bash
python3 scripts/check_template.py
```

Erwartung: Exit 0 mit `Template-Prüfung: OK`. Geprüft werden Vorlagenabgleich, benötigte Dateien, Standardversion und elementare Formatmerkmale. Zusätzlich geänderte Verweise und den gesamten Diff fachlich prüfen. Der Check belegt weder Anwendungstests noch die inhaltliche Vollständigkeit einer späteren Projekteinstellung.

Der Workflow [.github/workflows/template-check.yml](.github/workflows/template-check.yml) führt denselben Befehl bei Pull Requests, Pushes auf `main` und manuellem Start aus. Der Check heißt **Template check** und verwendet Python 3.11 auf Ubuntu 24.04. Die verwendeten Actions sind auf konkrete Commit-SHAs festgelegt; der Workflow erhält nur Lesezugriff auf Repository-Inhalte.

Für Änderungen an diesem Template muss der Check am maßgeblichen aktuellen PR-Stand bestehen. Den konkreten Lauf und geprüften Commit als Nachweis verlinken; ein lokaler Erfolg ist kein CI-Nachweis. Läufe sind unter [GitHub Actions](https://github.com/Hengsto/repository-template/actions) sichtbar.

**Eine technische Merge-Sperre durch verpflichtende Statuschecks ist weiterhin eine gesonderte Einrichtungslücke.** Der Workflow allein erzwingt sie nicht. Es gibt keinen Build, Anwendungsstart oder Deploymentvorgang für dieses Dokumentationstemplate.

In abgeleiteten Projekten ist dieser Check keine Anwendungsprüfung. Wird das Template-Prüfskript bei der Einrichtung entfernt, muss auch der zugehörige unveränderte Template-Workflow gemäß [SETUP.md](SETUP.md) entfernt werden. Bereits angepasste Projekt-Workflows bleiben erhalten; ihr weiterer Umgang ist ausdrücklich zu klären.

## Konfiguration, Sicherheit und Lizenz

Keine Laufzeitkonfiguration und keine Credentials erforderlich. Die beigefügte .gitignore verhindert einige typische versehentliche Aufnahmen, ersetzt aber keine Prüfung des Diffs auf Geheimnisse. Technologiespezifische Ausschlüsse werden erst im Zielprojekt ergänzt.

Eine Lizenz ist bewusst nicht vorgegeben. Vor öffentlicher Weitergabe oder externer Wiederverwendung ist die gewünschte Lizenz zu klären; dieses Paket behauptet keine erteilte Open-Source-Lizenz.

## Herkunft

Grundlage ist die vom Betreiber bereitgestellte Fassung 1.3. Dateiname vereinheitlicht auf `REPOSITORY_STANDARD.md`; maskierte Markdown-Zeichen, fett markierte Überschriften und überzählige Leerzeilen wurden für lesbares Markdown normalisiert. Version 1.4 ergänzt die beschlossene Regel für projektweite Anforderungen und Roadmaps; die ursprüngliche Übernahme der Fassung 1.3 war rein redaktionell. Projektspezifische Auto-Coding-Entscheidungen sind nicht Bestandteil dieses allgemeinen Templates.
