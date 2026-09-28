# Projekt aus dem Standard einrichten

Dieser Auftrag ist für eine ausdrücklich beauftragte Einrichtung oder Aktualisierung vorgesehen. Weder das Lesen noch das Erzeugen oder Klonen des Repositories startet ihn automatisch.

## Vor dem Start

- Agent im Zielrepository öffnen; bei einem neuen Projekt die Projektidee mitgeben.
- Standardversion 1.6 bereitstellen. Bei einem bestehenden Projekt genügt eine externe Referenzkopie; keine Dateien pauschal überschreiben.
- Vorhandene Entscheidungen und Befugnisse aus Auftrag und Repository verwenden. Fehlende wesentliche Angaben gezielt klären.

## Kopierbarer Auftrag für Codex oder Work

```text
Richte die projektspezifische Dokumentation dieses Zielrepositories nach der bereitgestellten REPOSITORY_STANDARD.md Version 1.6 ein. Führe dazu den vollständigen Einrichtungs-Prompt aus Abschnitt 16 aus.

Lies zuerst die geltenden Agentenanweisungen und prüfe Branch, Index, Diff und unversionierte Dateien. Erhalte vorhandene Arbeit. Bei einem leeren Projekt verwende die mit diesem Auftrag mitgegebene Projektidee; fehlen wesentliche Anforderungen, frage gezielt nach.

Unterscheide das zentrale Vorlagenrepository von einem daraus erzeugten Zielprojekt. Falls unklar ist, welches gerade vorliegt, kläre dies vor dem Ersetzen der Einstiegstexte. Im zentralen Template keine projektspezifische Einrichtung durchführen.

Ordne erforderliche Informationen einmalig ihren maßgeblichen Pflegeorten zu. Erstelle konkrete README.md und AGENTS.md. Längerfristige Projekte benötigen zusätzlich REQUIREMENTS.md und ROADMAP.md im Hauptverzeichnis, verlinkt aus beiden Einstiegen. Übernimm vorhandene Inhalte verlustfrei und vermeide konkurrierende Kopien. Bei kleinen Experimenten, Dateisammlungen oder Hilfsskripten ohne mehrphasige Weiterentwicklung genügen entsprechend benannte README-Abschnitte; begründe diese Ausnahme in AGENTS.md. Anforderungen beschreiben das Zielbild, die Roadmap Phasen und Abhängigkeiten; Aufgabenstatus bleibt am Aufgabenort. Verwende für diese Inhalte die Muster 14.10 und 14.11; verwende nur tatsächlich benötigte Muster aus templates/. Fülle Platzhalter anhand von Belegen aus oder benenne konkrete offene Entscheidungen. Erfinde keine Befehle, Testresultate, CI-Checks oder technischen Absicherungen.

Die im zentralen Template vorhandenen REQUIREMENTS.md und ROADMAP.md beschreiben das Template selbst. Ersetze diese Inhalte bei einer neuen Ableitung durch das tatsächliche Projektziel und dessen Planung; übernimm keine TPL-Anforderungen als Produktanforderungen. Bereits projektspezifisch geänderte Inhalte erhalten.

README und AGENTS sind zwei Einstiege, keine Begrenzung auf zwei Dateien. Lege keinen docs-Baum auf Vorrat an. Weitere Dokumente entstehen bei tatsächlichem Umfang, eigenständiger Pflege oder gezieltem Lesebedarf; passende bestehende Abschnitte bleiben erhalten. Lege .env.example nur bei passender Konfigurationsweise an. Dokumentiere ein Linux-/Homelab-Betriebsprofil nur bei tatsächlicher Nutzung, mit Übergabe durch Starter/Deployment und Zuordnung von Host- zu Anwendungspfaden.

Halte die projektspezifische AGENTS.md knapp: unmittelbar geltende Regeln und konkrete Verweise, keine laufenden Aufgaben oder kopierte Projektdokumentation. Lokale AGENTS.md nur für zusätzliche Bereichsregeln; optionale Skills nur für tatsächlich wiederkehrende Spezialabläufe und mit geprüftem Leseweg für die verwendeten Agenten. Automatisierbare Vorgaben nach Möglichkeit durch vorhandene Tests, Konfiguration oder CI absichern; fehlende technische Einrichtung nicht als vorhanden ausgeben.

Im neu erzeugten Zielprojekt sollen der allgemeine Standard, dieser Einrichtungsauftrag, Vorlagensammlung und Template-Prüfskript keine dauerhafte zweite Regelsammlung bilden. Sobald alle erforderlichen Projektregeln eigenständig dokumentiert und geprüft sind, entferne ausschließlich eindeutig unveränderte, nicht mehr benötigte Template-Hilfsdateien aus der Ableitung: insbesondere REPOSITORY_STANDARD.md, SETUP.md, templates/ und scripts/check_template.py. Ersetze die mitkopierte README.md und AGENTS.md durch projektspezifische Einstiege, statt die Template-Arbeitsregeln weiter gelten zu lassen. Diese Bereinigung ist Teil dieses Einrichtungsauftrags. Vorher Verweise prüfen; keine fremden, geänderten oder weiterhin benötigten Inhalte löschen. Im bestehenden Projekt keine solche pauschale Bereinigung vornehmen. Wenn Herkunft oder Bedarf unklar sind, Dateien erhalten und den offenen Punkt benennen.

Berücksichtige dabei auch .github/workflows/template-check.yml: Wenn das zugehörige Template-Prüfskript entfällt, entferne im neu erzeugten Zielprojekt auch den eindeutig unveränderten, nicht mehr benötigten Template-Workflow. Erhalte bereits angepasste Projekt-Workflows und kläre deren weiteren Umgang. Prüfe, dass verbleibende Workflows auf vorhandene Skripte verweisen; ein Template-Check ersetzt keine Anwendungs-CI.

Prüfe die GitHub-Vorlagen unter .github/ISSUE_TEMPLATE/ und .github/pull_request_template.md auf Eignung für den tatsächlichen Aufgaben- und PR-Ablauf. Erhalte geeignete bestehende Vorlagen. Verwende Issue-Vorlagen nur passend zum gewählten Aufgabenort; erzeuge dadurch keinen zweiten Backlog. Passe Vorlagen und ihre Lesewege an das Zielprojekt an: Ersetze insbesondere python3 scripts/check_template.py und den Checknamen Template check in der PR-Vorlage durch tatsächlich vorhandene Projektprüfungen oder kennzeichne fehlende Prüfungen als offen. Lokale Ergebnisse und CI-Nachweise bleiben getrennt. Verlinke verwendete Vorlagen aus AGENTS.md und verlange ihre passenden Inhalte auch bei API-/CLI-Erstellung. In einer neuen Ableitung entferne eindeutig unveränderte, nicht benötigte GitHub-Vorlagen im Rahmen der oben beschriebenen Bereinigung; in bestehenden Projekten keine pauschale Entfernung. GitHub-Vorlagen und Agenteneinrichtung erzwingen weder vollständige inhaltliche Korrektheit noch einen technischen Merge-Schutz.

Dokumentiere im maßgeblichen Prüfungsabschnitt die Testgrenzen und gegebenenfalls erforderlichen Build- und Artefaktprüfungen nach Standardabschnitt 9. Verwende vorhandene Prüfungen und benenne fehlende Umsetzung als konkrete Einrichtungslücke.

Halte Standardversion und Übernahmedatum in der projektspezifischen AGENTS.md fest. Ein Verweis auf den zentralen Standard ersetzt keine direkt benötigten Arbeitsanweisungen. Dokumentiere den Herkunftsverweis nur mit tatsächlich bekanntem Repository und Stand.

Richte die Lesewege so ein, dass Agenten zuerst AGENTS.md und geltende Bereichsanweisungen lesen und anschließend gezielt die aufgabenrelevanten Quellen laden. Verlange weder ausschließlich die Root-AGENTS noch pauschal den vollständigen Dokumentationsbestand. Die Roadmap verweist für den aktuellen Bearbeitungsstand auf den Aufgabenort; Änderungen und Prüfnachweise bleiben in den zugehörigen PRs nachvollziehbar.

Richte keine Anwendung, CI, Host-Konfiguration oder Deployment beiläufig ein. Erfasse solche Lücken konkret. Veröffentliche, merge oder deploye nur im Rahmen eines entsprechenden Auftrags. Berichte neue und geänderte Dateien, gewählte Pflegeorte, Prüfungen und offene Punkte. Unterscheide vorbereitet, übergeben, gestartet, geprüft, gemergt und deployed.
```

## Abnahme der Einrichtung

- README und AGENTS beschreiben das konkrete Projekt und verlinken tatsächliche Pflegeorte.
- REQUIREMENTS.md und ROADMAP.md sind mit konkreten Inhalten vorhanden und aus beiden Einstiegen verlinkt, oder die README-Ausnahme ist begründet. Phasen verweisen auf Anforderungen und vorhandene Aufgaben; keine erfundenen Termine oder Statuskopien.
- Gesamtstatus und Verbesserungsvorschläge haben genau einen Aufgabenort; Abnahmekriterien genau einen maßgeblichen Ort.
- Bereichszuordnung und ergänzende Suche sind beschrieben; keine vollständige Backlog-Lektüre für jede Aufgabe.
- Setup, Architektur, Konfiguration und Prüfung sind soweit relevant beschrieben. Unbekannte oder fehlende technische Umsetzung ist ausdrücklich erkennbar.
- Pflichtprüfungen, Prüfumgebungen, Testgrenzen, gegebenenfalls Build-/Artefaktprüfungen und tatsächliche CI-/Merge-Absicherung werden nachvollziehbar benannt.
- Verwendete GitHub-Vorlagen passen zum Aufgabenort und zu tatsächlichen Projektprüfungen; AGENTS verlinkt sie auch für API-/CLI-Erstellung. Keine veralteten Template-Befehle oder Checknamen bleiben als Projektprüfung stehen.
- Keine unbemerkten Platzhalter, kaputten Lesewege oder konkurrierenden Regelkopien. Nicht benötigte Vorlagen werden nicht zu leeren Projektdokumenten; kein docs-Baum oder .env.example ohne passenden Inhalt.

Die Abnahme hier betrifft die Dokumentationseinrichtung. Sie ist kein Nachweis, dass eine geplante Anwendung schon implementiert oder eine CI-Sperre eingerichtet wurde.
