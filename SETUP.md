# Projekt aus dem Standard einrichten

Dieser Auftrag ist für eine ausdrücklich beauftragte Einrichtung oder Aktualisierung vorgesehen. Er startet beim Lesen nicht automatisch.

## Vor dem Start

- Agent im Zielrepository öffnen; bei einem neuen Projekt die Projektidee mitgeben.
- Standardversion 1.3 bereitstellen. Bei einem bestehenden Projekt genügt eine externe Referenzkopie; keine Dateien pauschal überschreiben.
- Vorhandene Entscheidungen und Befugnisse aus Auftrag und Repository verwenden. Fehlende wesentliche Angaben gezielt klären.

## Kopierbarer Auftrag für Codex oder Work

```text
Richte die projektspezifische Dokumentation dieses Zielrepositories nach der bereitgestellten REPOSITORY_STANDARD.md Version 1.3 ein. Führe dazu den vollständigen Einrichtungs-Prompt aus Abschnitt 16 aus.

Lies zuerst die geltenden Agentenanweisungen und prüfe Branch, Index, Diff und unversionierte Dateien. Erhalte vorhandene Arbeit. Bei einem leeren Projekt verwende die mit diesem Auftrag mitgegebene Projektidee; fehlen wesentliche Anforderungen, frage gezielt nach.

Unterscheide das zentrale Vorlagenrepository von einem daraus erzeugten Zielprojekt. Falls unklar ist, welches gerade vorliegt, kläre dies vor dem Ersetzen der Einstiegstexte. Im zentralen Template keine projektspezifische Einrichtung durchführen.

Ordne erforderliche Informationen einmalig ihren maßgeblichen Pflegeorten zu. Erstelle konkrete README.md und AGENTS.md; verwende nur tatsächlich benötigte Muster aus templates/. Fülle Platzhalter anhand von Belegen aus oder benenne konkrete offene Entscheidungen. Erfinde keine Befehle, Testresultate, CI-Checks oder technischen Absicherungen.

Im neu erzeugten Zielprojekt sollen der allgemeine Standard, dieser Einrichtungsauftrag, Vorlagensammlung und Template-Prüfskript keine dauerhafte zweite Regelsammlung bilden. Sobald alle erforderlichen Projektregeln eigenständig dokumentiert und geprüft sind, entferne ausschließlich eindeutig unveränderte, nicht mehr benötigte Template-Hilfsdateien aus der Ableitung. Diese Bereinigung ist Teil dieses Einrichtungsauftrags. Vorher Verweise prüfen; keine fremden, geänderten oder weiterhin benötigten Inhalte löschen. Im bestehenden Projekt keine solche pauschale Bereinigung vornehmen. Wenn Herkunft oder Bedarf unklar sind, Dateien erhalten und den offenen Punkt benennen.

Berücksichtige dabei auch .github/workflows/template-check.yml: Wenn das zugehörige Template-Prüfskript entfällt, entferne im neu erzeugten Zielprojekt auch den eindeutig unveränderten, nicht mehr benötigten Template-Workflow. Erhalte bereits angepasste Projekt-Workflows und kläre deren weiteren Umgang. Prüfe, dass verbleibende Workflows auf vorhandene Skripte verweisen; ein Template-Check ersetzt keine Anwendungs-CI.

Halte Standardversion und Übernahmedatum in der projektspezifischen AGENTS.md fest. Ein Verweis auf den zentralen Standard ersetzt keine direkt benötigten Arbeitsanweisungen. Dokumentiere den Herkunftsverweis nur mit tatsächlich bekanntem Repository und Stand.

Richte keine Anwendung, CI, Host-Konfiguration oder Deployment beiläufig ein. Erfasse solche Lücken konkret. Veröffentliche, merge oder deploye nur im Rahmen eines entsprechenden Auftrags. Berichte neue und geänderte Dateien, gewählte Pflegeorte, Prüfungen und offene Punkte. Unterscheide vorbereitet, übergeben, gestartet, geprüft, gemergt und deployed.
```

## Abnahme der Einrichtung

- README und AGENTS beschreiben das konkrete Projekt und verlinken tatsächliche Pflegeorte.
- Gesamtstatus und Verbesserungsvorschläge haben genau einen Aufgabenort; Abnahmekriterien genau einen maßgeblichen Ort.
- Bereichszuordnung und ergänzende Suche sind beschrieben; keine vollständige Backlog-Lektüre für jede Aufgabe.
- Setup, Architektur, Konfiguration und Prüfung sind soweit relevant beschrieben. Unbekannte oder fehlende technische Umsetzung ist ausdrücklich erkennbar.
- Pflichtprüfungen, Prüfumgebungen und tatsächliche CI-/Merge-Absicherung werden getrennt und nachvollziehbar benannt.
- Keine unbemerkten Platzhalter, kaputten Lesewege oder konkurrierenden Regelkopien. Nicht benötigte Vorlagen werden nicht zu leeren Projektdokumenten.

Die Abnahme hier betrifft die Dokumentationseinrichtung. Sie ist kein Nachweis, dass eine geplante Anwendung schon implementiert oder eine CI-Sperre eingerichtet wurde.
