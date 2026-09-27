# Repository Template

Schlanker Ausgangspunkt für neue Projekte und zentrale Pflege des **Repo-Standards 1.3** (27. September 2026).

Dieses Repository enthält Dokumentation und Vorlagen, keinen Anwendungscode. Es legt keine Sprache, Datenbank, Containertechnik oder CI-Plattform für Zielprojekte fest.

## Verwendung

### Neues Projekt

1. Dieses Verzeichnis als eigenes Repository übernehmen und bei Bedarf auf GitHub als Template kennzeichnen. Das ZIP allein erstellt kein GitHub-Repository und aktiviert keine Einstellung.
2. Aus dem Template ein eigenes Projekt-Repository erzeugen. Projektname, Zweck und wesentliche Anforderungen mitgeben.
3. Den Auftrag aus [SETUP.md](SETUP.md) an den Agenten im **Zielrepository** übergeben. Ein vorbereiteter Auftrag ist noch kein gestarteter Lauf.
4. Der Agent ersetzt die Einstiegstexte durch konkrete Projektinformationen und prüft die Einrichtung. Unbekannte Befehle, Checks und Autorisierungen werden als offene Punkte ausgewiesen.

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
| [scripts/check_template.py](scripts/check_template.py) | Lokaler Abgleich der extrahierten Vorlagen mit dem Standard und Prüfung der Paketstruktur. |

Im Zielprojekt sind README.md und AGENTS.md die Einstiege. Weitere Dokumente entstehen nur bei konkretem Bedarf. Die Muster sind keine Pflicht-Dateiliste.

## Architektur und Pflege

Der Standard ist die maßgebliche Regelfassung. Die neun Muster aus Abschnitt 14 liegen zusätzlich als direkt verwendbare Dateien vor; das Prüfsystem erkennt Abweichungen. Die README-Vorlage ist eine ergänzende Strukturhilfe. SETUP.md verweist auf den maßgeblichen Einrichtungs-Prompt in Abschnitt 16 statt ihn erneut zu pflegen.

Die Zielprojekte erhalten eigene, eigenständig verständliche Regeln. Sie benötigen im normalen Betrieb keinen Zugriff auf dieses Template. Eine spätere Standardversion wird bewusst geprüft und übernommen, niemals automatisch als neue Regel aktiviert.

Aufgabenort für die Pflege dieses Templates: Nach Veröffentlichung die Issues des tatsächlichen Template-Repositories. Suche nach betroffenen Pfaden, Standardabschnitten und Begriffen; vorhandene Labels nur ergänzend nutzen. Bis ein Repository existiert, bleibt die beauftragende Unterhaltung der Aufgabenort. Es wird kein zusätzlicher Backlog angelegt.

## Prüfungen

Voraussetzung: Python 3.11 oder neuer; keine zusätzlichen Pakete. Aus dem Repository-Wurzelverzeichnis:

```bash
python3 scripts/check_template.py
```

Erwartung: Exit 0 mit `Template-Prüfung: OK`. Geprüft werden Vorlagenabgleich, benötigte Dateien, Standardversion und elementare Formatmerkmale. Zusätzlich geänderte Verweise und den gesamten Diff fachlich prüfen. Der Check belegt weder Anwendungstests noch die inhaltliche Vollständigkeit einer späteren Projekteinstellung.

**CI und Merge-Schutz sind in diesem Paket nicht eingerichtet.** Bei Veröffentlichung werden erforderliche Checks und deren technische Absicherung gesondert festgelegt. Ein lokaler Erfolg ist kein CI-Nachweis. Es gibt keinen Build, Anwendungsstart oder Deploymentvorgang für dieses Dokumentationstemplate.

## Konfiguration, Sicherheit und Lizenz

Keine Laufzeitkonfiguration und keine Credentials erforderlich. Die beigefügte .gitignore verhindert einige typische versehentliche Aufnahmen, ersetzt aber keine Prüfung des Diffs auf Geheimnisse. Technologiespezifische Ausschlüsse werden erst im Zielprojekt ergänzt.

Eine Lizenz ist bewusst nicht vorgegeben. Vor öffentlicher Weitergabe oder externer Wiederverwendung ist die gewünschte Lizenz zu klären; dieses Paket behauptet keine erteilte Open-Source-Lizenz.

## Herkunft

Grundlage ist die vom Betreiber bereitgestellte Fassung 1.3. Dateiname vereinheitlicht auf `REPOSITORY_STANDARD.md`; maskierte Markdown-Zeichen, fett markierte Überschriften und überzählige Leerzeilen wurden für lesbares Markdown normalisiert. Die Regeln wurden inhaltlich nicht erweitert oder gekürzt. Projektspezifische Auto-Coding-Entscheidungen sind nicht Bestandteil dieses allgemeinen Templates.
