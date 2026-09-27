# Repository Template

Schlanker Ausgangspunkt für neue Projekte und zentrale Pflege des **Repo-Standards 1.4** (27. September 2026).

Dieses Repository ist ein modularer Dokumentations- und Arbeitsrahmen für KI-gestützte Entwicklung. Es enthält Dokumentation und Vorlagen, keinen Anwendungscode. Es legt keine Sprache, Datenbank, Containertechnik oder CI-Plattform für Zielprojekte fest.

## Verwendung

### Neues Projekt

1. Auf GitHub über **Use this template** ein eigenes Projekt-Repository erzeugen. Dieses Repository ist bereits als Template aktiviert.
2. Projektname, Zweck und wesentliche Anforderungen mitgeben und den Auftrag aus [SETUP.md](SETUP.md) an den Agenten im **Zielrepository** übergeben. Ein vorbereiteter Auftrag ist noch kein gestarteter Lauf.
3. Der Agent untersucht den vorhandenen Projektstand, ordnet benötigte Informationen einmalig ihren Pflegeorten zu und passt die Dokumentation an. Er verwendet belegte Befehle und bestehende Entscheidungen; nur wesentliche offene Entscheidungen werden mit Optionen, Vor-/Nachteilen und Empfehlung geklärt. Unbekannte Befehle, Checks und Autorisierungen werden als offene Punkte ausgewiesen.

Das Erzeugen oder Klonen eines Repositories führt den Einrichtungsauftrag nicht automatisch aus. Ein gewöhnlicher Git-Klon übernimmt die Historie des Vorlagenrepos. Für eigenständige neue Projekte ist eine Erstellung aus dem Template oder ein neues Git-Repository aus diesen Dateien zweckmäßiger.

### Bestehendes Projekt

Den [Standard](REPOSITORY_STANDARD.md) und [Einrichtungsauftrag](SETUP.md) als Referenz bereitstellen. Nicht den gesamten Template-Inhalt über das bestehende Repo kopieren. Vorhandene Anweisungen, Dateien, Kommentare, Arbeitsstände und geeignete Abläufe erhalten; nur beauftragte Anpassungen vornehmen.

## Dateien im zentralen Template

Diese Dateien pflegen das Template selbst. Sie sind kein Pflichtbestand für jedes daraus eingerichtete Projekt.

| Datei | Zweck |
| --- | --- |
| [README.md](README.md) | Verwendung, Aufbau und Prüfung dieses Templates. |
| [AGENTS.md](AGENTS.md) | Arbeitsanweisungen für die Pflege dieses Templates und Erkennung noch nicht eingerichteter Ableitungen. |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Zielbild und beschlossene Anforderungen an das Template selbst. |
| [ROADMAP.md](ROADMAP.md) | Projektweite Planung und Aufgabenbezüge für die Weiterentwicklung des Templates. |
| [REPOSITORY_STANDARD.md](REPOSITORY_STANDARD.md) | Zentrale Vorgabe, vollständig bei Einrichtung oder bewusster Aktualisierung lesen. |
| [SETUP.md](SETUP.md) | Einmaliger Auftrag zur projektspezifischen Einrichtung. |
| [templates/README.md](templates/README.md) | Auswahl und Verwendung der optionalen Strukturhilfen. |
| [scripts/check_template.py](scripts/check_template.py) | Abgleich der extrahierten Vorlagen mit dem Standard und Prüfung der Paketstruktur, lokal und in CI. |
| [.github/workflows/template-check.yml](.github/workflows/template-check.yml) | GitHub-Actions-Workflow für dieselbe Template-Prüfung. |

## Aufbau im Zielprojekt

`README.md` und `AGENTS.md` bilden die zwei Einstiege. Das ist keine Obergrenze von zwei Markdown-Dateien im Hauptverzeichnis. Längerfristige Projekte führen zusätzlich `REQUIREMENTS.md` und `ROADMAP.md`; kleine Experimente ohne mehrphasige Weiterentwicklung dürfen die begründete README-Ausnahme aus [Standardabschnitt 3](REPOSITORY_STANDARD.md#3-erforderliche-informationen-und-ihre-pflegeorte) nutzen.

| Inhalt | Maßgebliche Ablage |
| --- | --- |
| Zweck, Einrichtung, Start, Architektur-, Test- und Konfigurationsüberblick | `README.md`; bei eigener Detaildokumentation genau dorthin verweisen. |
| Agentenregeln, gültige Befehle oder genaue Verweise, Projektgrenzen und Lesewege | `AGENTS.md`; geltende Bereichsanweisungen ergänzen sie. |
| Beschlossenes Zielbild, Anforderungen und Abnahmekriterien | `REQUIREMENTS.md`; umfangreiche Kriterien können eindeutig verlinkte Detailquellen haben. |
| Allgemeiner Projektplan: geplante Phasen, Ergebnisse, Reihenfolge und Abhängigkeiten | `ROADMAP.md`, mit Verweisen auf Anforderungen, Aufgaben und technische Pläne. |
| Aktueller Aufgabenstatus, Priorität und Verbesserungsvorschläge | Genau ein Aufgabenort: beispielsweise GitHub Issues oder ein vorhandener Markdown-Backlog. |
| Umgesetzte Änderungen und Prüfnachweise | Zugehörige PRs, Commits und Prüfläufe; umgesetzt, geprüft, gemergt und deployed unterscheiden. |
| Technische Umsetzung und Fortsetzung komplexer oder risikoreicher Aufgaben | Vorhandener Plan, bei Bedarf `docs/plans/<task>.md`; kein zweiter Gesamtstatus. |
| Vertiefte Architektur, Tests, Konfiguration, Spezifikationen, Entscheidungen und Fehlerwissen | Passende vorhandene Abschnitte; eigene Dokumente wie `docs/architecture.md`, `docs/testing.md` oder `docs/decisions/` nur bei konkretem Bedarf. |

Zusätzliche Dokumente entstehen bei größerem Umfang, eigenständiger Pflege oder regelmäßig gezieltem Zugriff. Es gibt keinen vorab angelegten `docs/`-Baum mit leeren Dateien. Auch `.env.example` entsteht nur, wenn sie zur tatsächlichen Konfigurationsweise passt. Die Muster unter `templates/` dienen der Einrichtung und sind keine aktiven Projektdokumente.

Die Roadmap zeigt, was insgesamt vorgesehen ist und wie die Schritte zusammenhängen. Den aktuellen Bearbeitungsstand liefern die verlinkten Aufgaben; Änderungen und Prüfungen sind über ihre PRs nachvollziehbar. So wird keine zweite Statusliste in der Roadmap gepflegt.

## Ablauf bei einer Aufgabe

1. `AGENTS.md` und alle geltenden Anweisungen des betroffenen Bereichs lesen; Branch, Diff und vorhandene Arbeit prüfen.
2. Am Aufgabenort nach betroffenen Bereichen, Pfaden und Begriffen suchen. Relevante Schnittstellen, Abhängigkeiten und übergreifende Regeln berücksichtigen; passende Dokumente über die Lesewege vollständig laden. Fehlende Suchtreffer allein belegen keine fehlende Relevanz.
3. Abnahmekriterien verwenden beziehungsweise vor wesentlichen Funktionsänderungen klären. Komplexe oder risikoreiche Arbeit technisch planen; bei kleinen Bugfixes genügen Ursache, Änderung und Prüfung im PR.
4. Aufgabe umsetzen, betroffene Dokumentation mitpflegen und erforderliche Prüfungen belegen. Relevante Vorschläge nur mit Nachweis und Begründung schließen; Gesamtstatus am festgelegten Aufgabenort aktualisieren.

Der Einstieg über `AGENTS.md` begrenzt die Lektüre nicht auf diese eine Datei. Ebenso gehören weder der vollständige Standard noch das gesamte Backlog zur Pflichtlektüre jeder gewöhnlichen Aufgabe.

## Architektur und Pflege

Der Standard ist die maßgebliche Regelfassung. Die elf Muster aus Abschnitt 14 liegen zusätzlich als direkt verwendbare Dateien vor; das Prüfsystem erkennt Abweichungen. Die README-Vorlage ist eine ergänzende Strukturhilfe. SETUP.md verweist auf den maßgeblichen Einrichtungs-Prompt in Abschnitt 16 statt ihn erneut zu pflegen.

Die Zielprojekte erhalten eigene, eigenständig verständliche Regeln. Sie benötigen im normalen Betrieb keinen Zugriff auf dieses Template. Eine spätere Standardversion wird bewusst geprüft und übernommen, niemals automatisch als neue Regel aktiviert.

Aufgabenort für die Pflege dieses Templates: [GitHub Issues in Hengsto/repository-template](https://github.com/Hengsto/repository-template/issues). Suche dort nach betroffenen Pfaden, Standardabschnitten und Begriffen; vorhandene Labels nur ergänzend nutzen. Es wird kein zusätzlicher Backlog angelegt. Die Trennung vermeidet parallele Statuslisten und reduziert Konfliktquellen; gemeinsame Änderungen an Code oder Dokumentation können weiterhin Merge-Konflikte verursachen.

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

Zielanwendungen verwenden dokumentierte Konfigurationsschnittstellen, etwa Umgebungsvariablen oder unterstützte Konfigurations- und Secret-Dateien. Beim optionalen Linux-/Homelab-Betriebsprofil lädt der Starter beziehungsweise das Deployment die Host-Konfiguration aus `/data/config/<project>/.env` und ordnet persistente Daten unter `/data/<project>/` den tatsächlichen Anwendungspfaden zu. Host-Pfade werden nicht in der Anwendungslogik fest eingebaut. Diese Trennung unterstützt unterschiedliche Umgebungen; Container- oder CI-Fähigkeit muss am konkreten Projekt geprüft werden. Die maßgeblichen Regeln stehen in [Standardabschnitt 12](REPOSITORY_STANDARD.md#12-konfiguration-und-betriebsprofile).

Eine Lizenz ist bewusst nicht vorgegeben. Vor öffentlicher Weitergabe oder externer Wiederverwendung ist die gewünschte Lizenz zu klären; dieses Paket behauptet keine erteilte Open-Source-Lizenz.

## Herkunft

Grundlage ist die vom Betreiber bereitgestellte Fassung 1.3. Dateiname vereinheitlicht auf `REPOSITORY_STANDARD.md`; maskierte Markdown-Zeichen, fett markierte Überschriften und überzählige Leerzeilen wurden für lesbares Markdown normalisiert. Version 1.4 ergänzt die beschlossene Regel für projektweite Anforderungen und Roadmaps; die ursprüngliche Übernahme der Fassung 1.3 war rein redaktionell. Projektspezifische Auto-Coding-Entscheidungen sind nicht Bestandteil dieses allgemeinen Templates.
