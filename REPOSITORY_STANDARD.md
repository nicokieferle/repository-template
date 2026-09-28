# Repo-Standard für KI-gestützte Entwicklung

Version: 1.6 · Stand: 28. September 2026

Dieser Standard beschreibt, welche Informationen und Arbeitsregeln ein Repository für zuverlässige KI-gestützte Entwicklung benötigt. Er unterscheidet erforderliche Informationen von ihrer Ablage: `README.md` und `AGENTS.md` bilden den Einstieg; längerfristige Projekte führen zusätzlich `REQUIREMENTS.md` und `ROADMAP.md` gemäß Abschnitt 3. Weitere Dateien entstehen bei konkretem Bedarf.

Dokumentation und KI-Arbeitsregeln sind deutsch. Codebezeichner sowie Datei- und Ordnernamen sind englisch. Die Codestruktur folgt Sprache, Framework und Projekt.

Änderungen gegenüber Version 1.5:

- `AGENTS.md` bleibt eine kompakte Ebene für unmittelbar geltende Regeln und konkrete Lesewege; temporäre Aufgaben und ausführliche Verfahren erhalten eigene Pflegeorte.
- Bereichsanweisungen und Agent-Skills sind bedarfsabhängig. Maschinell prüfbare Vorgaben werden nach Möglichkeit in Tests, Konfiguration oder CI abgesichert.

Bereits in Version 1.5 eingeführte Regeln:

- Integrations- und End-to-End-Prüfungen benennen reale Komponenten und Mock-Grenzen.
- Änderungen an auslieferbaren Artefakten benötigen einen Build-Nachweis und die nach Projektrisiko erforderlichen Prüfungen des erzeugten Ergebnisses.

Bereits in Version 1.4 eingeführte Regeln:

- Eigenständige, längerfristige Projekte führen `REQUIREMENTS.md` und `ROADMAP.md` im Repository-Hauptverzeichnis; kleine Experimente dürfen klar benannte README-Abschnitte verwenden.
- Zielbild, projektweite Umsetzungsreihenfolge, Aufgabenstatus und technische Detailplanung werden ausdrücklich getrennt.
- Vorlagen, Lesewege und Einrichtungsauftrag übernehmen die Regel einschließlich verlustfreier Übernahme bestehender Dokumentation.

Bereits in Version 1.3 eingeführte Regeln:

- Aufgaben, eigenständige Pläne und Spezifikationen erhalten eine klare Bereichszuordnung; Labels und `Scope:` ergänzen die Suche, ersetzen sie aber nicht.

- Ausstehende Übertragungen nennen Zuständigkeit und nächsten Abgleich; mergekritische Lücken und unabhängige Verbesserungsideen werden nach ihrer Auswirkung behandelt.

- Prüfnachweise nennen Prüfung, Umgebung, geprüften Codezustand, Ergebnis und Beleg. Lokale Erfolge und CI-Ergebnisse bleiben unterscheidbar.

- Merge-Bereitschaft setzt die festgelegten Pflichtprüfungen am maßgeblichen aktuellen PR-Stand voraus; ein beliebiger grüner Workflow genügt nicht.

- Der gesamte Diff wird auf unbeabsichtigte Änderungen geprüft; fachlich zusammengehörige Änderungen bleiben maßgeblich, ohne universelle Datei- oder Zeilenlimits.

- Betroffene Vorlagen und Einrichtungsanweisungen übernehmen diese Präzisierungen.

## 1. Verwendung und Grenzen

Diese Datei ist die allgemeine Bauanleitung und ein Nachschlagewerk. Sie wird bei der Einrichtung oder bewussten Aktualisierung eines Projekts vollständig ausgewertet. Für gewöhnliche Entwicklungsaufgaben ist die kurze, projektspezifische `AGENTS.md` der Einstieg; der gesamte Standard samt Vorlagen gehört nicht zur ständigen Pflichtlektüre.

Der Einrichtungs-Prompt in Abschnitt 16 übernimmt die einmalige Zuordnung benötigter Informationen zu ihren maßgeblichen Pflegeorten. Er verwendet vorhandene Struktur und Projektentscheidungen, entscheidet eindeutige Zuordnungen selbst und klärt nur wesentliche offene Entscheidungen mit dem Nutzer. Bei späteren Aktualisierungen werden nur betroffene Zuordnungen neu bewertet. Er wird ausdrücklich beauftragt; das Erzeugen oder Klonen eines Repositories startet ihn nicht automatisch.

Das zentrale Template enthält diesen Standard, Vorlagen und Hilfen für deren Einrichtung und Prüfung. Dieser Bestand ist vom eingerichteten Zielprojekt zu unterscheiden: README und AGENTS sind dessen Einstiege; Anforderungen und Roadmap folgen Abschnitt 3. Die mitgelieferten Muster sind Strukturhilfen, keine aktiven Projektdokumente oder automatisch geltenden Arbeitsanweisungen.

Bestehende Dokumentation, passende Dateien, funktionierende Abläufe, fremde Arbeit und weiterhin relevante Codekommentare werden erhalten. Der Standard ist kein Auftrag zur pauschalen Neustrukturierung eines vorhandenen Projekts. Projektspezifische Abweichungen und tatsächliche Ablageorte müssen eindeutig erkennbar sein.

`AGENTS.md` nennt die übernommene Standardversion und das Übernahmedatum. Eine Versionsangabe oder ein Link ersetzt keine unmittelbar geltende Anweisung. Wichtige Regeln müssen dort verständlich stehen. Spätere Änderungen am allgemeinen Standard werden bewusst auf das Projekt übertragen; bestehende Repositories aktualisieren sich nicht automatisch.

Eine Markdown-Datei erzwingt das Lesen durch ein Agentenwerkzeug nicht technisch. Der verwendete Einstieg muss eingerichtet sein. Ausführbare Prüfungen und erforderliche CI-Checks sichern überprüfbare Anforderungen ab; ihre Einrichtung oder erfolgreiche Ausführung darf nur behauptet werden, wenn sie tatsächlich erfolgt ist.

Agentenanweisungen sind kein Projekt-Wiki: `AGENTS.md` enthält direkt nötige, dauerhaft geltende Grenzen und verweist für Details auf maßgebliche Quellen. Welche Dateien automatisch geladen werden, hängt vom verwendeten Werkzeug und dessen Konfiguration ab; eine Verlinkung allein garantiert kein Nachladen.

## 2. Vereinbarte Grundentscheidungen

| Thema | Regel |
| --- | --- |
| Einstieg und Aufbau | `README.md` und `AGENTS.md` als Einstieg. Längerfristige Projekte führen `REQUIREMENTS.md` und `ROADMAP.md` im Hauptverzeichnis; Ausnahme für kleine Projekte gemäß Abschnitt 3. Weitere Dateien nur bei Bedarf. |
| Planung | Projektweite Phasen, Reihenfolge und Abhängigkeiten in `ROADMAP.md`; Aufgabenstatus am Aufgabenort. Eigene technische Pläne für komplexere oder risikoreiche Änderungen. Bei kleinen Bugfixes genügen Ursache, Änderung und Prüfung im PR. |
| Anforderungen | Vor neuen oder wesentlich geänderten Funktionen überprüfbare Abnahmekriterien festhalten. Eindeutige vorhandene Kriterien wiederverwenden. |
| Kontext | Geltende Agentenanweisungen lesen; Bereichszuordnung, Suche und Abhängigkeiten für den Relevanzabgleich nutzen; nur passende Dokumentation vollständig laden. |
| Aufgabenort | Ein maßgeblicher Ort für Gesamtstatus, Priorität und Verbesserungsvorschläge. Keine parallel gepflegten Backlogs. |
| Arbeitsumfang | Auftrag und notwendige Anpassungen umsetzen; unabhängige Verbesserungen am festgelegten Aufgabenort erfassen. |
| Vorschläge schließen | Nur mit konkretem Nachweis und dokumentierter Begründung. Unklare Konflikte zwischen beschlossenen Plänen klären. |
| Fehlergedächtnis | Nur Erkenntnisse mit künftigem Nutzen aufnehmen: bestätigte Ursache, funktionierender Fix und Schutz vor Wiederholung. |
| Dokumentationspflege | Betroffene Dokumentation im selben PR wie die Codeänderung aktualisieren. |
| Prüfungen | Jede funktionale Änderung muss Kern- und erforderliche Bereichsprüfungen bestehen; Umgebung, Codezustand, Ergebnis und Beleg zuordnen. Erforderliche CI-Nachweise dürfen nicht durch lokale Erfolge ersetzt werden. |
| Entscheidungen | Grundlegende technische Entscheidungen mit Gründen, Alternativen und Konsequenzen dokumentieren. |
| Fortsetzung | Technischen Fortschritt, Prüfnachweise und nächsten Schritt im vorhandenen Plan pflegen; ausstehende Übertragungen mit Zuständigkeit und nächstem Abgleich nachverfolgen. Zusätzliche Übergabenotiz nur bei Bedarf. |
| Git | Funktionale Änderungen über Branch und PR. Auto-Merge wird je Projekt festgelegt; Merge ist kein Deploymentauftrag. |
| Konfiguration | Dokumentierte Konfigurationsschnittstellen und Startprüfung der Pflichtwerte; Host-Pfade sind Teil eines passenden Betriebsprofils. |
| Sprache | Dokumentation und Arbeitsregeln deutsch; Codebezeichner sowie Datei- und Ordnernamen englisch. |

## 3. Erforderliche Informationen und ihre Pflegeorte

Jede Information erhält einen maßgeblichen Pflegeort. Andere Stellen verweisen darauf. Befehle, Abnahmekriterien, Aufgabenstatus und umfangreiche Beschreibungen werden nicht mehrfach unabhängig gepflegt.

| Inhalt | Bei kleinen Experimenten / Hilfsskripten | Längerfristige Projekte / eigene Ablage |
| --- | --- | --- |
| Zweck, wichtigste Funktionen, Voraussetzungen, Einrichtung und Start | `README.md` | Weiterführende Anleitungen. |
| Architektur, Komponenten, Datenflüsse und Codeübersicht | Abschnitt in `README.md` | Zum Beispiel `docs/architecture.md`. |
| Kernprüfungen, Bereichstests, Voraussetzungen und CI-Zuordnung | Abschnitt in `README.md`; kurze maßgebliche Arbeitsbefehle können auch in `AGENTS.md` stehen | Zum Beispiel `docs/testing.md`. Andere Stellen verweisen auf den gewählten Ort. |
| Konfiguration und Startvalidierung | Abschnitt in `README.md`, bei Bedarf `.env.example` | Zum Beispiel `docs/configuration.md`. |
| Agentenanweisungen und Lesewege | `AGENTS.md` | Zusätzliche bereichsspezifische Anweisungen bei tatsächlichen Unterschieden. |
| Wiederkehrendes spezialisiertes Agentenverfahren | Bei Bedarf ein konkreter Arbeitsablauf am vorhandenen Ort | Optional ein thematisch abgegrenzter Skill mit `SKILL.md` und bei Bedarf Skripten/Referenzen; keine Pflichtsammlung. |
| Gesamtstatus, Priorität und Verbesserungsvorschläge | Festgelegter Aufgabenort | Issues oder ein Markdown-Backlog, beispielsweise `docs/backlog.md` beziehungsweise eine bereits vorhandene `docs/improvements.md`. |
| Zielbild, Anforderungen und Abnahmekriterien | Klar benannter README-Abschnitt | `REQUIREMENTS.md` im Hauptverzeichnis; ausführliche Kriterien bei Bedarf eindeutig in verlinkten Spezifikationen oder Aufgaben. |
| Projektweite Phasen, Reihenfolge und Abhängigkeiten | Klar benannter README-Abschnitt | `ROADMAP.md` im Hauptverzeichnis; Verweise auf Anforderungen, Aufgaben und technische Detailpläne. |
| Technischer Ansatz und mehrstufige Umsetzung | Bei kleinen Bugfixes die PR-Beschreibung | Zum Beispiel `docs/plans/<task>.md` für komplexe oder risikoreiche Aufgaben. |
| Wichtige Fehlererkenntnisse | Passender bestehender Dokumentationsabschnitt | Zum Beispiel `docs/lessons-learned.md`. |
| Grundlegende technische Entscheidungen | Passender bestehender Dokumentationsabschnitt | Zum Beispiel `docs/decisions/<number>-<topic>.md`. |
| Betrieb und Deployment | Passender Abschnitt, sofern relevant | Zum Beispiel `docs/operations.md` und dokumentiertes Betriebsprofil. |
| Übergabe offener Arbeit | Vorhandener Plan, Issue oder PR | `docs/handoffs/<task>.md` nur bei sonst fehlender Fortsetzbarkeit. |
| Historische, ersetzte oder geschlossene Informationen | Am bisherigen Ort, solange übersichtlich | Zum Beispiel `docs/archive/`. |

### Zielbild und Roadmap

Eigenständige, längerfristig gepflegte Projekte führen **`REQUIREMENTS.md` und `ROADMAP.md` im Repository-Hauptverzeichnis**. Das gilt insbesondere bei mehreren geplanten Entwicklungsphasen oder fortlaufender Funktionserweiterung, unabhängig von der aktuellen Codegröße. Beide Dateien sind aus `README.md` und `AGENTS.md` verlinkt.

- `REQUIREMENTS.md` beschreibt das beschlossene Zielbild, Anforderungen, Grenzen und überprüfbare Abnahmekriterien. Anforderungen erhalten stabile Kennungen. Vorschläge und offene Entscheidungen sind ausdrücklich von beschlossenen Anforderungen getrennt. Ausführliche Kriterien dürfen einen verlinkten maßgeblichen Ort haben; keine doppelte Kriterienliste.
- `ROADMAP.md` beschreibt größere Umsetzungsschritte beziehungsweise Phasen, deren Ergebnis, Reihenfolge und Abhängigkeiten. Sie verweist auf Anforderungskennungen und vorhandene Aufgaben sowie bei Bedarf technische Pläne. Sie führt keine zweite Liste von Aufgabenstatus, Prioritäten oder Prozentfortschritten. Termine werden nur übernommen, wenn vereinbart; geplante Phasen sind keine Implementierungsnachweise.
- Der Aufgabenort bleibt maßgeblich für konkreten Bearbeitungsstatus und Priorität. Technische Detailpläne erklären die Umsetzung einzelner komplexer Aufgaben und deren Fortsetzung; sie ersetzen nicht die projektweite Roadmap.

Kleine Experimente, reine Dateisammlungen oder einzelne Hilfsskripte ohne mehrphasige Weiterentwicklung dürfen stattdessen klar benannte Abschnitte „Anforderungen“ und „Roadmap“ in der README führen. `AGENTS.md` nennt die gewählte Ausnahme und verlinkt diese Abschnitte. Keine leeren Pflichtdokumente anlegen; bei längerfristiger Weiterentwicklung in die beiden Dateien überführen.

Bei bestehenden Projekten werden passende Inhalte verlustfrei übernommen und alle betroffenen Verweise angepasst. Umfangreiche bestehende Spezifikationen und Detailpläne können als verlinkte maßgebliche Detailquellen bestehen bleiben. Keine konkurrierende Kopie des Zielbilds oder der Roadmap erzeugen; bei ungeklärter Herkunft Inhalte erhalten und die offene Zuordnung benennen.

Bei Änderungen am Zielbild werden betroffene Anforderungen, Roadmap und Aufgabenbezüge im selben Änderungsvorgang abgeglichen. Bei Änderungen der Reihenfolge oder Abhängigkeiten wird die Roadmap angepasst; reine Aufgabenstatuswechsel bleiben am Aufgabenort. Grundlegende Richtungsänderungen mit Begründung nachvollziehbar halten, ohne neben Git eine zweite Änderungshistorie zu verlangen.

Architektur- und Testinformationen bleiben erforderlich, soweit sie zum Projekt gehören. Dafür besteht keine Pflicht zu eigenen Dateien. Weitere Inhalte werden ausgelagert, wenn sie umfangreich sind, unabhängig gepflegt werden müssen oder regelmäßig gezielt gebraucht werden. Die genannten docs-Pfade sind Beispiele, kein vorab anzulegender Verzeichnisbaum. Es gibt keine starre Dateigrenze und keine leeren Vorratsdateien.

Eine lokale `AGENTS.md` entsteht nur, wenn ein Unterbereich tatsächlich zusätzliche geltende Regeln benötigt. Globale Regeln bleiben in der Root-Datei; lokale Regeln beschreiben ausschließlich die Ergänzungen für ihren Bereich und widersprechen den globalen Grenzen nicht. Bei mehreren berührten Bereichen sind alle jeweils geltenden Anweisungen zu berücksichtigen. Eine temporäre Aufgabe oder einzelne Migration gehört dagegen in Issue, PR oder einen nur bei Bedarf angelegten technischen Plan.

Ein Skill lohnt sich für einen spezialisierten, wiederkehrenden Ablauf, der bei gewöhnlichen Aufgaben nicht gebraucht wird. Seine `SKILL.md` nennt Auslöser, Voraussetzungen, Schritte, Prüfkriterien und bei Bedarf relative Verweise auf Skripte oder Beispiele. Gemeinsame Projektregeln bleiben am maßgeblichen Ort und werden verlinkt statt kopiert. Skills werden nur ergänzt, wenn das Zielprojekt sie tatsächlich verwendet; beispielsweise kann `.agents/skills/<name>/SKILL.md` als projektinterne Ablage dienen. Die Erkennung dieses Pfads ist werkzeugabhängig und muss für die verwendeten Agenten eingerichtet oder über `AGENTS.md` auffindbar gemacht werden. Ein Skill ersetzt keine automatisierte Prüfung und keine unmittelbar geltende Sicherheits- oder Projektgrenze.

Automatisch überprüfbare Regeln gehören möglichst in Formatter, Linter, Tests, Schemata oder CI. Markdown erklärt deren Zweck, Auswahl, Befehle und Grenzen; es behauptet keine technische Durchsetzung ohne entsprechende Einrichtung.

Anwendungscode, Tests, Betriebsskripte und CI-Konfiguration folgen den Konventionen der verwendeten Technologien. Der Architekturüberblick nennt tatsächliche Codepfade. Geplante Funktionen werden ausdrücklich als geplant gekennzeichnet.

Der Aufgabenort wird beim Einrichten festgelegt und in `AGENTS.md` mit Suchweg genannt. Für GitHub-Projekte mit paralleler Arbeit und vorhandenem Zugriff sind Issues für Gesamtstatus und Vorschläge, PRs für Änderungen und Prüfergebnisse und Repo-Pläne für technische Details eine geeignete Aufteilung. Für überwiegend einzelne oder lokale Arbeit kann ein Markdown-Backlog den Aufgabenort bilden. Eine zusätzliche Verbesserungsliste ist dann nicht erforderlich.

Abnahmekriterien haben ebenfalls genau einen maßgeblichen Ort: Sie können im Issue stehen oder bei einer ausführlicheren Spezifikation dort gepflegt und vom Issue verlinkt werden. Der Abschlussstatus des Gesamtauftrags gehört zum Aufgabenort. Ein technischer Plan verweist auf ihn und pflegt keinen zweiten Gesamtstatus.

Ein Aufgabenort regelt die Informationsablage; er ist keine technische Garantie gegen doppelte Bearbeitung. Externe Aufgabenverwaltung vermeidet ein parallel gepflegtes Repo-Backlog und reduziert damit Konfliktquellen, verhindert aber keine Merge-Konflikte bei gemeinsam geänderten Dateien. Vor paralleler Arbeit sind vorhandene Zuordnungen und laufende Änderungen an der betroffenen Aufgabe zu berücksichtigen.

## 4. Gezielter Kontext bei Arbeitsbeginn

### Bereichszuordnung und Suchweg

Aufgaben sowie eigenständige Pläne und Spezifikationen erhalten eine leicht erkennbare Bereichszuordnung. Vorhandene Issue-Labels, ein kurzes `Scope:`-Feld oder eine eindeutige Zuordnung durch den bestehenden Dokumentationsabschnitt genügen. Es entsteht keine Pflicht zu zusätzlichen Dateien oder doppelten Metadaten. Bei mehreren betroffenen Bereichen werden diese und relevante Schnittstellen berücksichtigt.

Die verwendeten Bereichsnamen und der Suchweg werden projektspezifisch in `AGENTS.md` oder über einen genauen Verweis festgelegt. Beispielsweise können `scope:api`, `scope:database` und `scope:deployment` zu einem Projekt passen; es gibt keine allgemeine Pflicht-Taxonomie. Übergreifende Einschränkungen müssen ebenfalls auffindbar sein. Bei geänderter Zuständigkeit wird die betroffene Zuordnung mitgepflegt.

Labels und Bereichsangaben erleichtern die Suche, garantieren aber keine vollständige Relevanzermittlung. Relevante Pfade, Begriffe, Schnittstellen und bekannte Abhängigkeiten ergänzen die Auswahl. Fehlende Treffer oder uneinheitliche Metadaten sind kein Nachweis, dass keine relevanten Informationen existieren; bei unklaren Auswirkungen wird die Suche gezielt erweitert.

### Ablauf

Bei jeder neuen Aufgabe oder Sitzung im Repo:

1. `AGENTS.md` und geltende Anweisungen des betroffenen Bereichs lesen.

2. Am festgelegten Aufgabenort anhand von Titeln, Bereichszuordnungen oder gezielter Suche ermitteln, welche offenen Aufgaben und Verbesserungsvorschläge die aktuelle Arbeit betreffen. Betroffene Komponenten, Schnittstellen und einschlägige übergreifende Einschränkungen berücksichtigen.

3. Relevante Einträge, Abnahmekriterien, technische Pläne und Entscheidungen vollständig lesen. Bei unklaren Auswirkungen die Suche gezielt erweitern.

4. Die benötigten Projektinformationen über die dokumentierten Lesewege laden und mit dem tatsächlichen Repo-Zustand abgleichen.

| Aufgabenart | Zusätzlich benötigte Informationen |
| --- | --- |
| Erste Orientierung | Projektzweck, Zielbild, Roadmap, Setup, Architekturüberblick und Arbeitsbefehle. |
| Bugfix | Betroffenes Soll-Verhalten, einschlägige Fehlererkenntnisse und erforderliche Testanweisungen. |
| Neue oder wesentlich geänderte Funktion | Betroffene Anforderungen und Roadmap-Phase, Abnahmekriterien, Architektur, Prüfungen und gegebenenfalls technischer Plan. |
| Architektur-, Schnittstellen- oder Datenänderung | Betroffene Verträge, Entscheidungen, technische Pläne und entsprechende Prüfungen. |
| Konfiguration oder Betrieb | Konfigurationsschnittstellen, relevantes Betriebsprofil und geltende Betriebsbefugnisse. |
| Fortsetzung | Vorhandener technischer Arbeitsstand, tatsächlicher Branch/Commit, offene Änderungen und einschlägige Prüfergebnisse. |
| Reine Dokumentationsänderung | Maßgebliche Quelldokumente und bei Verhaltensaussagen die relevanten Codebereiche. |

`AGENTS.md` nennt dafür konkrete vorhandene Dateien, Abschnitte oder externe Einträge. Die Tabelle schreibt Informationen vor, keine zusätzlichen Dateien. Ein vorhandener Planindex wird nur so weit herangezogen, wie er für das Auffinden passender Pläne benötigt wird. Archive werden gezielt bei Bedarf gelesen.

Die Suche ersetzt das vollständige Laden aller Backlog-Einträge. Bei einem Upload-Bugfix können beispielsweise Upload, Dateivalidierung und betroffene Schnittstellen die Suchbereiche bilden. Eine allgemeine Aufräumrunde sämtlicher Vorschläge gehört nicht zu jeder Aufgabe. Beim Abschluss werden die relevanten Einträge auf nachweisliche Erledigung geprüft.

Die Pflicht beginnt mit einer neuen Aufgabe oder Sitzung, nicht erneut mit jedem Chatbeitrag derselben unveränderten Arbeit. Neue oder geänderte Anweisungen werden dennoch berücksichtigt. Fehlender Zugriff auf den Aufgabenort wird nach Abschnitt 7 behandelt und nicht als leeres Suchergebnis ausgegeben.

## 5. Arbeitsablauf einer Aufgabe

### Einordnen und planen

Auftrag, gewünschtes Ergebnis und Umfang verstehen; relevanten Kontext laden; Branch, Arbeitsstand und vorhandene Änderungen prüfen. Fremde und unversionierte Arbeit erhalten. Widersprüche zwischen Soll-Verhalten, Code und Dokumentation anhand der Belege klären. Vorhandener Code zeigt den Ist-Zustand, aber nicht automatisch das beabsichtigte Verhalten.

Vor neuen oder wesentlich geänderten Funktionen müssen überprüfbare Abnahmekriterien vorliegen. Die KI darf sie aus einer eindeutigen Aufgabenbeschreibung ableiten. Bereits geklärte Entscheidungen benötigen keine erneute Bestätigung. Bei folgenreicher Mehrdeutigkeit wird die konkrete Entscheidung mit praktikablen Optionen, Vor- und Nachteilen und Empfehlung vorgelegt.

Ein technischer Plan ist bei komplexeren oder risikoreichen Änderungen erforderlich, etwa bei wesentlichen Komponentenabhängigkeiten, Datenmigrationen oder Änderungen wichtiger Schnittstellen. Die Zahl geänderter Dateien allein entscheidet darüber nicht. Bei einem kleinen, klar abgegrenzten Bugfix reichen Ursache, Änderung und Prüfung im PR.

Ein ausdrücklich beauftragtes Experiment kann mit grober Zielbeschreibung beginnen. Seine Ergebnisse bleiben als experimentell gekennzeichnet; vor regulärer Übernahme einer Funktion werden ihre Abnahmekriterien geklärt.

### Umsetzen

- Auftrag und notwendige Anpassungen umsetzen. Unabhängige Verbesserungen am festgelegten Aufgabenort erfassen.

- Bestehende Konventionen und weiterhin relevante Kommentare erhalten. Kommentare nur anpassen, wenn ihre Aussage durch die Änderung tatsächlich überholt wird.

- Kleine, zusammenhängende Änderungen und gezielte Patches bevorzugen. Große Aufgaben in fachlich zusammenhängende, überprüfbare Schritte aufteilen. Module nach Zuständigkeit und Verständlichkeit schneiden; weder Dateilänge noch Ausgabelimits allein begründen einen zusätzlichen Modulumbau. Projektspezifische Größenwerte können Warnschwellen sein; dieser Standard setzt keine universellen Datei- oder Zeilenlimits für Patches, Commits oder PRs.

- Hilfreiche Diagnoseausgaben vorsehen. Dauerhafte Diagnostik folgt dem vorhandenen Logging, ist bei Bedarf schaltbar und enthält keine geheimen Werte oder unnötigen vollständigen Nutzdaten.

- Keine unfertigen Platzhalter oder wegen Sitzungs- beziehungsweise Ausgabelimits abgebrochene Arbeit als abgeschlossene Implementierung ausgeben.

### Prüfen, dokumentieren und übergeben

- Bei funktionalen Änderungen feste Kernprüfungen und erforderliche Tests der betroffenen Bereiche ausführen. Bei Bedarf aussagekräftige Regressionstests ergänzen.

- Betroffene Dokumentation im selben PR aktualisieren; unbetroffene Dateien nicht kosmetisch umschreiben. Vor Übergabe den gesamten Diff auf unbeabsichtigte Änderungen, Löschungen und vollständige Dateiersetzungen prüfen; beabsichtigte größere Änderungen müssen fachlich begründet sein.

- Relevante Fehlererkenntnisse und Verbesserungseinträge am jeweiligen Pflegeort aktualisieren.

- Nach abgeschlossenen Teilschritten und vor geplanten Unterbrechungen den technischen Arbeitsstand festhalten.

- Abschließend Änderungen, erforderliche Prüfungen und verbleibende Einschränkungen knapp benennen. Implementiert, geprüft, gemergt und deployed sind unterschiedliche Zustände.

Ein Vorschlag ist noch kein Umsetzungsauftrag. Ein fehlender Testnachweis oder eine Dokumentationsänderung darf die vereinbarten Anforderungen nicht stillschweigend abschwächen.

## 6. Anforderungen, Architektur und Entscheidungen

Eine Funktionsbeschreibung nennt Zweck, erwartetes Verhalten, relevante Fehlerfälle und überprüfbare Abnahmekriterien. Entscheidende Schnittstellen und Datenwirkungen werden beschrieben. Nicht-Ziele grenzen den Umfang ab, wenn sonst Missverständnisse zu erwarten sind.

Kriterien beschreiben beobachtbares Verhalten, beispielsweise: Ein ungültiges Uploadformat wird verständlich abgelehnt und vorhandene Daten bleiben unverändert. Bereits eindeutige Kriterien in einer Aufgabe oder Spezifikation werden verlinkt, statt eine zweite Fassung zu pflegen. Die längerfristige Funktionsdokumentation wird bei geänderten Funktionen im selben PR aktualisiert.

Der Architekturüberblick erklärt den tatsächlichen Aufbau, Zuständigkeiten, wichtige Datenflüsse, externe Abhängigkeiten und Codepfade. Er kann in der README stehen. Eine Aufzählung jeder Hilfsfunktion ist nicht erforderlich. Zentrale Nutzerfunktionen werden mit Implementierung und Prüfungen verknüpft, soweit dies bei der Orientierung hilft.

Grundlegende technische Entscheidungen werden am festgelegten Wissensort kurz dokumentiert: Ausgangslage, Alternativen, Entscheidung, Gründe und Konsequenzen. Eine eigene ADR-Datei ist bei Bedarf sinnvoll, etwa für Datenbankwahl, wichtige Schnittstellen oder die Aufteilung in Dienste.

Eine ersetzte Entscheidung verweist auf ihre Nachfolge; die ursprüngliche Begründung bleibt nachvollziehbar. Dieser historische Entscheidungsstand ist kein zweiter Aufgabenstatus. Entscheidungsnotizen dokumentieren getroffene Entscheidungen und führen keine zusätzliche Freigabepflicht ein.

## 7. Aufgabenort und Verbesserungsvorschläge

### Ein maßgeblicher Ort

Gesamtstatus, Priorität und Verbesserungsvorschläge werden am in `AGENTS.md` festgelegten Aufgabenort gepflegt. Der Suchweg muss konkret sein, beispielsweise Repository, relevante Issue-Labels beziehungsweise Bereichszuordnungen oder Pfad und Suchmethode eines Markdown-Backlogs. Eine zusätzliche `docs/improvements.md` ist keine Pflicht.

Ein Vorschlag braucht zunächst einen verständlichen Titel, den betroffenen Bereich gemäß Abschnitt 4 sowie Problem und Nutzen. Er muss eindeutig referenzierbar sein, beispielsweise durch seine Issue-Nummer oder eine stabile Markdown-Kennung. Weitere Angaben wie Aufwand, Abhängigkeiten oder Wiedervorlage werden bei Bedarf ergänzt; unbekannte Werte werden nicht erfunden.

### Bedeutung der Zustände

Die folgenden Bedeutungen werden mit den vorhandenen Möglichkeiten des Aufgabenorts abgebildet. Dafür muss kein zusätzliches paralleles Statussystem eingerichtet werden.

| Bedeutung | Inhalt |
| --- | --- |
| Offen | Vorschlag ohne beschlossenen Umsetzungsauftrag. |
| Geplant | Einer konkreten beauftragten Aufgabe oder einem Plan zugeordnet. |
| Zurückgestellt | Weiterhin sinnvoll, aber nachrangig oder blockiert; Grund und gegebenenfalls Wiedervorlage nennen. |
| Erledigt | Nachweislich umgesetzt; passende Änderung und gegebenenfalls Prüfung referenzieren. |
| Verworfen | Nicht mehr sinnvoll, ausdrücklich ersetzt oder doppelt; Grund und Bezug dokumentieren. |

Bei Arbeitsbeginn werden relevante Einträge gezielt ermittelt. Andere Prioritäten führen normalerweise zu „zurückgestellt“, nicht automatisch zu „verworfen“. Ein lediglich geplanter Ersatz macht eine Verbesserung nicht erledigt.

Die KI darf Einträge mit konkretem Nachweis und dokumentierter Begründung selbstständig schließen, soweit der Aufgabenort innerhalb des erteilten Auftrags bearbeitet werden darf. Beispiele sind ein vorhandener Fix mit passender Prüfung, ein bestätigter Plan, der die Idee ausdrücklich ersetzt, oder ein eindeutig gleichwertiger bestehender Vorschlag.

Unklare Gründe oder ungelöste Widersprüche zwischen beschlossenen Plänen werden dokumentiert und zur Klärung vorgelegt. Eigene Vorlieben rechtfertigen keine Aufhebung eines beschlossenen Plans. Geschlossene Einträge und ihre Begründungen bleiben nachvollziehbar erhalten; bei Bedarf werden sie archiviert.

### Vorübergehend fehlender Zugriff

Die Zugriffslücke wird benannt. Sie erzeugt weder automatisch einen zweiten Backlog noch den Eindruck, es gebe keine offenen Aufgaben. Eindeutig geklärte, unabhängig bearbeitbare Teile können weitergehen. Fehlen wesentliche Anforderungen oder Abhängigkeiten, wird nur der betroffene Teil zurückgestellt und die konkrete Informationslücke geklärt.

Neu entdeckte Vorschläge oder notwendige Statusaktualisierungen werden bis zur Übertragung knapp im vorhandenen Übergabestand festgehalten, ausdrücklich als „noch nicht an den Aufgabenort übertragen“. Nur wenn kein geeigneter Übergabestand existiert, ist eine kurze zusätzliche Notiz nötig. Sie enthält keine Kopie des gesamten Backlogs und keinen konkurrierenden maßgeblichen Status.

Jeder ausstehende Eintrag nennt Inhalt und Zielort, die für die Übertragung zuständige Rolle oder Instanz sowie den nächsten konkreten Abgleichsanlass oder Schritt. Bestehende Zuständigkeiten aus Projektregeln und Auftrag werden verwendet; unbekannte Zuständigkeit wird ausdrücklich als ungeklärt benannt. Ein möglicher Abgleichsanlass ist die Fortsetzung mit wiederhergestelltem Zugriff. Das dokumentiert einen nächsten Schritt und behauptet keine eingerichtete Hintergrundüberwachung.

Nach Wiederherstellung des Zugriffs werden aktuelle Einträge erneut abgeglichen, Duplikate vermieden und erforderliche Ergänzungen im Rahmen des bestehenden Auftrags übertragen. Anschließend ersetzt der Verweis auf den entstandenen oder aktualisierten Eintrag den Vermerk „noch nicht übertragen“. Vor Aufgabenabschluss werden offene Übertragungen geprüft und entweder erledigt oder nach den Projektregeln mit klarer Zuständigkeit und nächstem Schritt verbindlich übergeben. Eine ungeklärte Zuständigkeit gilt nicht als erfolgte Übergabe; der offene Rest bleibt im Abschluss sichtbar.

Die Auswirkung bestimmt eine mögliche Merge-Sperre: Fehlende wesentliche Anforderungen, ungeklärte notwendige Abhängigkeiten, ausstehende erforderliche Freigaben oder nicht erfüllte projektspezifische Nachweispflichten blockieren den betroffenen Merge. Eine unabhängig entdeckte Verbesserungsidee ohne Einfluss auf die Abnahme blockiert keinen ansonsten fertigen Bugfix; ihre ausstehende Übertragung bleibt nachvollziehbar offen.

Ein Textmarker, Label oder Commit-Vermerk erzwingt allein keine technische Sperre. Soll eine solche Bedingung technisch gelten, muss sie durch die projektspezifisch eingerichtete Prüfung und Merge-Regel abgesichert sein. Ihre Einrichtung folgt einem entsprechenden Auftrag. Eine nachgewiesene automatische Übertragung benötigt allein aufgrund dieser Regel keinen zusätzlichen manuellen Review.

### Wechsel des Aufgabenorts

Ein bewusst beschlossener Wechsel wird verlustfrei durchgeführt: Vorhandene Vorschläge, relevante Begründungen, Zustände und Verweise erhalten eine Zuordnung zum neuen Ort. Nach geprüfter Übernahme wird der alte Backlog eindeutig als abgelöst gekennzeichnet und verweist auf den Nachfolger. Er wird nicht gleichzeitig aktiv weitergeführt oder vor erfolgreicher Übernahme gelöscht.

## 8. Fehlergedächtnis mit künftigem Nutzen

Wiederverwendbare Erkenntnisse werden am festgelegten Wissensort gepflegt. Für wenige Einträge reicht ein passender bestehender Abschnitt; eine eigene `docs/lessons-learned.md` entsteht bei Bedarf.

Geeignet sind wiederkehrende Fehler, überraschende Ursachen, projektspezifische Stolperfallen und Fehler mit schwerwiegenden Folgen. Ein Eintrag beschreibt Symptom, bestätigte Ursache, funktionierenden Fix und Schutz vor Wiederholung. Betroffener Bereich und Belege machen ihn auffindbar; ein vorhandener Regressionstest wird verlinkt.

Einmalige banale Tippfehler brauchen normalerweise keinen Eintrag. Unbestätigte Ursachen gehören als offene Annahmen zum aktiven Arbeitsstand. Das Fehlergedächtnis ist kein vollständiges Chat- oder Logarchiv. Vorhandene passende Erkenntnisse werden ergänzt, statt Duplikate zu erzeugen.

Überholte Erkenntnisse werden in ihrem Geltungsbereich angepasst oder begründet archiviert. Es wird weder ein nicht vorhandener Test noch eine unbestätigte Ursache als gesichert dokumentiert.

## 9. Prüfungen und Abschlusskriterien

### Prüfstrategie

Jedes Projekt mit funktionalem Code definiert eine kleine, schnelle Menge von Kernprüfungen seiner wichtigsten Abläufe. Beispiele sind Anwendungsstart, ein zentraler API-Aufruf oder das Speichern und erneute Lesen von Testdaten. Die Auswahl folgt dem tatsächlichen Projekt.

Jede funktionale Änderung muss die Kernprüfungen und die erforderlichen Tests der betroffenen Bereiche bestehen. Weitere Spezialtests werden nach den Auswirkungen der Änderung ausgewählt. Bei Bedarf werden passende Regressionstests ergänzt; Prüfungen sollen beobachtbares Verhalten absichern und nicht bloß die Implementierung nachzeichnen.

Für Integrations- und End-to-End-Prüfungen legt der Prüfungsabschnitt fest, welche Komponenten real zusammenarbeiten und welche externen Systeme durch Mocks oder andere Testersatzkomponenten ersetzt werden. Ersatzkomponenten dürfen die zu prüfende Logik oder das nachzuweisende Zusammenspiel nicht ersetzen. Aussagen über reale Integration benötigen eine Prüfung der tatsächlich beteiligten Komponenten; nicht geprüfte Grenzen werden als Einschränkung benannt.

Ändert eine Aufgabe Inhalt, Abhängigkeiten oder Erzeugung eines auslieferbaren Artefakts, etwa eines Container-Images, Pakets oder einer EXE, muss dieses am maßgeblichen Stand erfolgreich gebaut werden. Der Prüfungsabschnitt legt nach den Auswirkungen der Änderung fest, welche Start-, Installations- oder Funktionstests am erzeugten Artefakt erforderlich sind. Der Nachweis identifiziert das geprüfte Artefakt eindeutig und ordnet es dem Codezustand zu; Build-Erfolg und weitere Artefaktprüfungen bleiben unterscheidbar. Prüfungen des Quellcodes allein belegen weder einen erfolgreichen Build noch die Nutzbarkeit des erzeugten Ergebnisses. Die bestehenden Regeln für erforderliche Nachweise und blockierte Prüfungen gelten auch hier.

Der maßgebliche Prüfungsabschnitt nennt exakte Befehle, Arbeitsordner, Voraussetzungen, erwartete Ergebnisse, erforderliche Prüfumgebungen und die CI-Zuordnung. Er kann in der README stehen. Dokumentierte Auswahlregeln bestimmen, welche Bereichsprüfungen bei welchen Änderungen erforderlich sind. Für als verbindlich bezeichnete Prüfungen muss eine ausführbare Prüfung oder eine konkret benannte Einrichtungslücke vorliegen.

Die vereinbarten erforderlichen Prüfungen werden vor dem Merge durch CI abgesichert. Fehlende CI beziehungsweise fehlende Checks werden zentral als Einrichtungslücke dokumentiert und bei Bedarf als Folgeaufgabe erfasst. Ihre Umsetzung erfolgt bei entsprechendem Auftrag. Ein reiner Dokumentationsauftrag umfasst keine stillschweigende CI-Einrichtung.

Die Lücke ist kein bestandener Check. Im konkreten PR oder Abschluss wird sie erwähnt, soweit dadurch ein erforderlicher Nachweis für die Änderung fehlt. Eine unveränderte allgemeine Beschreibung fehlender Infrastruktur muss nicht in jedem PR wiederholt werden.

Alle festgelegten Pflichtprüfungen müssen für den maßgeblichen aktuellen PR-Stand erfüllt sein, bevor die Änderung als mergebereit gilt. Lokale Erfolge ersetzen keine erforderlichen CI-Nachweise; ein beliebiger grüner Workflow genügt nicht. Der Nachweis gehört zum aktuellen PR-Head oder zu dem dafür geprüften Test-Merge- beziehungsweise Merge-Queue-Commit. Nach Änderungen am Code oder an maßgeblichen Abhängigkeiten ist zu prüfen, welche Nachweise erneuert werden müssen. Übersprungene Prüfungen gelten nicht als ausgeführt; ihre Nichtanwendbarkeit muss aus den dokumentierten Auswahlregeln hervorgehen.

CI-Läufe verbessern die gemeinsame Nachprüfbarkeit, garantieren allein aber weder deterministische Tests noch Funktionsfähigkeit auf dem Zielsystem. Relevante Laufzeit- und Abhängigkeitsstände, Testkonfiguration und erforderliche Integrations- oder Zielumgebungsprüfungen werden im Projekt festgelegt.

Reine Dokumentationsänderungen benötigen passende Dokumentationsprüfungen und gegebenenfalls einen Abgleich mit dem Code. Sie lösen nicht automatisch sämtliche Anwendungstests aus.

### Ergebnisse berichten

Jeder relevante Prüfnachweis ordnet folgende Informationen eindeutig zu; Prüfungen mit gleicher Umgebung und gleichem Codezustand können sie gemeinsam angeben:

| Angabe | Erforderlicher Inhalt |
| --- | --- |
| Prüfung | Konkreter Befehl mit Arbeitsordner oder eindeutig referenzierter Check. |
| Umgebung | Lokal, CI oder vorgesehene Integrations-/Zielumgebung; relevante Voraussetzungen und Versionen oder ihr maßgeblicher Verweis. |
| Geprüfter Codezustand | Commit beziehungsweise geprüfter Merge-Stand; bei lokaler Arbeit zusätzlich vorhandene uncommittete Änderungen eindeutig zuordnen. |
| Ergebnis | Tatsächlicher Ausgang und gegebenenfalls konkreter Grund für eine fehlende Ausführung. |
| Nachweis | CI-Lauf mit passendem Check oder knappe lokale Ergebnisausgabe beziehungsweise geeigneter Logverweis; keine Secrets oder unnötigen vollständigen Logs. |

Ein lokaler Erfolg wird als solcher ausgewiesen, beispielsweise „lokal bestanden“; ein CI-Erfolg wird mit dem passenden Lauf als „CI bestanden“ ausgewiesen. Das sind Angaben zu Prüfungen, keine zusätzlichen konkurrierenden Gesamtaufgabenstatus. Lokale Tests können bestanden sein, während erforderliche CI noch aussteht. Laufende oder ausstehende Prüfungen sind kein Erfolgsnachweis. Ergebnisse werden am vorgesehenen Ort wie dem PR gepflegt; technische Pläne können darauf verweisen.

- **Bestanden:** Die Prüfung wurde am relevanten Stand erfolgreich ausgeführt.

- **Fehlgeschlagen:** Die Prüfung wurde ausgeführt und meldet ein Problem. Ursache und Bezug zur Änderung untersuchen.

- **Nicht ausgeführt:** Eine für die Aufgabe erforderliche Prüfung wurde nicht gestartet oder konnte nicht laufen. Den konkreten Grund nennen.

Der Abschluss nennt die relevanten Ergebnisse und erforderliche, aber nicht ausgeführte Prüfungen. Er listet nicht sämtliche theoretisch möglichen Tests auf. „Nicht ausgeführt“ bedeutet nicht „bestanden“. Bekannte unabhängige Altfehler werden als solche gekennzeichnet.

Tests werden nicht deaktiviert oder abgeschwächt, nur um einen grünen Lauf zu erhalten. Beabsichtigte Verhaltensänderungen können geänderte Testerwartungen erfordern; Abnahmekriterien und Begründung müssen dazu passen.

### Abschluss

Eine Aufgabe ist abgeschlossen, wenn ihre Abnahmekriterien erfüllt, die erforderlichen Prüfungen bestanden, betroffene Dokumentation aktuell und relevante Erkenntnisse sowie Einträge gepflegt sind. Nicht mergekritische Restübertragungen dürfen gemäß Abschnitt 7 verbindlich übergeben sein; die Übertragung selbst bleibt als offen erkennbar. Verbleibende Einschränkungen müssen sichtbar sein.

Fehlt ein erforderlicher Nachweis, wird der Stand beispielsweise als „implementiert, Prüfung blockiert“ beschrieben. Technische Umsetzung, nachgewiesene Prüfung, Gesamtaufgabenstatus, Merge und Deployment werden nicht gleichgesetzt. Die Merge-Entscheidung folgt zusätzlich den projektspezifischen Regeln.

## 10. Technischer Fortschritt und Fortsetzung

Bei mehrstufigen Aufgaben dient der bestehende technische Plan als Übergabestand. Er verweist auf die maßgebliche Aufgabe. Deren Gesamtstatus und Priorität werden dort nicht ein zweites Mal gepflegt.

Nach abgeschlossenen Teilschritten und vor geplanten Unterbrechungen werden aktualisiert:

- erledigte und offene technische Umsetzungsschritte;

- ausgeführte Prüfungen mit Umgebung, Codezustand, Ergebnis und Nachweis nach Abschnitt 9 oder eindeutigem Verweis darauf;

- relevante Blocker, erfolglose Ansätze und offene Annahmen;

- nächster konkreter Schritt und gegebenenfalls ausstehende Übertragungen mit Zuständigkeit und nächstem Abgleich nach Abschnitt 7;

- Branch, vorhandener Commit und relevante uncommittete Änderungen.

Technische Schritt-Checkboxen bleiben sinnvoll. Sie beschreiben den Arbeitsstand und ersetzen weder den Gesamtstatus des Issues noch eine Abnahme. Der Aufgabenort verlinkt den Plan, statt sämtliche Schritte zu kopieren.

Bei kleinen abgeschlossenen Bugfixes reicht die PR-Dokumentation. Eine zusätzliche Übergabenotiz entsteht nur, wenn offene Arbeit sonst nicht verständlich fortsetzbar wäre. Nicht übertragene Einträge bei fehlendem Aufgabenort-Zugriff werden nach Abschnitt 7 behandelt.

Beim Fortsetzen werden Übergabe, aktuelle Aufgabe und tatsächlicher Repo-Zustand abgeglichen. Angaben eines älteren Commits oder anderen Branches werden nicht blind übernommen. Regelmäßige Zwischenstände reduzieren den Verlust bei abrupten Unterbrechungen; eine abschließende Notiz kann bei unerwartetem Abbruch nicht garantiert werden.

## 11. Git, PRs und Betriebsgrenzen

Funktionale Änderungen werden auf einem eigenen Branch und über einen Pull Request bearbeitet. Ein PR umfasst eine zusammengehörige Änderung, nicht jeden Arbeitsschritt. Ein vorhandener passender Aufgabenbranch kann weiterverwendet werden; ein Sitzungswechsel verlangt keinen neuen Branch.

Ein PR beschreibt Problem und Ziel, wesentliche Änderungen, relevante Prüfnachweise nach Abschnitt 9 und Einschränkungen. Er verlinkt die maßgebliche Aufgabe und bei Bedarf technische Pläne, Spezifikationen oder Entscheidungen. Kleine Bugfixes dokumentieren hier Ursache, Fix und Prüfung.

Auto-Merge ist projektspezifisch festzulegen. Dieser Standard verlangt keine manuelle Freigabe jedes PRs und erteilt keine pauschale Auto-Merge-Freigabe. Bestehende Autorisierungen werden berücksichtigt; bereits geklärte Befugnisse werden nicht erneut abgefragt.

Ein Merge ist kein Deploymentauftrag. Zielumgebung, Verfahren und geltende Autorisierung gehören in die Projektvorgaben. Entwickler- und Testarbeit wird nicht allein aufgrund dieses Standards auf ein Produktivsystem ausgeweitet.

## 12. Konfiguration und Betriebsprofile

### Schnittstelle der Anwendung

Die Anwendung verwendet dokumentierte Konfigurationsschnittstellen und benötigt keine fest eingebauten Host-Pfade. Einstellungen können beispielsweise über Umgebungsvariablen und unterstützte Konfigurations- beziehungsweise Secret-Dateien bereitgestellt werden. Die konkrete Übergabe, zulässige Quellen und gegebenenfalls deren Vorrang sind nachvollziehbar dokumentiert.

Für jede Einstellung werden Zweck, Pflichtstatus, Typ beziehungsweise erlaubte Werte und gegebenenfalls Default beschrieben. Fehlende oder ungültige Pflichtwerte führen beim Start zu einer verständlichen Fehlermeldung; die Anwendung startet damit nicht regulär. Die Meldung nennt Einstellung und Problem, ohne geheime Werte auszugeben.

Optionale Einstellungen dürfen dokumentierte Defaults besitzen. Ausdrücklich optionale Integrationen dürfen nicht verfügbar sein, wenn ihr Status klar erkennbar ist. Gültige Konfiguration und aktuelle Erreichbarkeit eines externen Dienstes sind getrennte Sachverhalte; der Umgang mit Ausfällen folgt den Projektanforderungen.

Im Repo stehen ungefährliche Beispiele und Beschreibungen, keine echten Secrets. Eine `.env.example` wird angelegt, wenn sie zur Konfigurationsweise passt. Lokale Geheimnisse und persistente Laufzeitdaten werden nicht versehentlich versioniert.

### Linux-/Homelab-Betriebsprofil

Für die entsprechend betriebenen Linux-Hosts bleibt die vereinbarte Konvention erhalten:

| Zweck | Host-Pfad |
| --- | --- |
| Hostbezogene Konfiguration und gegebenenfalls dort verwaltete Secrets | `/data/config/<project>/.env` |
| Persistente Anwendungsdaten | `/data/<project>/` |

Dieses Betriebsprofil gehört zur Deploymentumgebung und ist keine allgemeine Voraussetzung jedes Entwicklungsrechners, Containers oder CI-Runners. Auf den entsprechend eingerichteten Servern, Dev- und CI-VMs wird dieselbe Host-Struktur verwendet; die Werte unterscheiden sich je Umgebung. Unterstützte Secret-Dateien dürfen ergänzend oder entsprechend dem gewählten Secret-Verfahren eingesetzt werden.

Das Deployment beziehungsweise der Starter lädt die Host-Konfiguration und übergibt sie an die Anwendung. Die Dokumentation ordnet Host-Verzeichnisse, etwaige Container-Pfade und Anwendungseinstellungen eindeutig zu. Sie erklärt die tatsächliche Übergabe, Mounts und Datenablage, statt allein die Host-Pfade aufzulisten.

Tests dürfen isolierte temporäre Verzeichnisse und explizit eingespeiste Testkonfiguration verwenden. Sie benötigen keine Produktionsverzeichnisse oder echten Zugangsdaten. Weitere Betriebsprofile werden nur bei Bedarf dokumentiert; jedes Projekt muss das Homelab-Profil nicht vorsorglich übernehmen.

## 13. Sprache und Pflegeumfang

Dokumentation, Abnahmekriterien, Pläne und KI-Arbeitsregeln werden auf Deutsch geschrieben. Codebezeichner, Datei- und Ordnernamen bleiben Englisch. Vorhandene sinnvolle Namen und relevante Kommentare werden nicht allein zur sprachlichen Vereinheitlichung umgebaut.

Eine englische README kann bei Bedarf ergänzt werden. Der gesamte Dokumentationsbestand wird nicht standardmäßig zweisprachig geführt. Kurze Lesewege, bedarfsgerechte Aufteilung und gezielter Zugriff halten den Kontext überschaubar.

Geändertes Verhalten erfordert die Anpassung der betroffenen Funktionsbeschreibung; geänderte Struktur den Architekturüberblick; geänderte Testbefehle die Testanweisungen; geänderte Konfiguration ihre Beschreibung und passende Beispiele. Wichtige Entscheidungen und Fehlererkenntnisse werden am jeweils festgelegten Wissensort gepflegt.

Beim bewussten Aktualisieren des Repo-Standards werden Regeln, Vorlagen, Lesewege und Einrichtungs-Prompt gemeinsam auf Widersprüche geprüft. Eine kürzere Dateitabelle allein darf nicht durch alte verpflichtende Pfade an anderer Stelle wirkungslos werden.

## 14. Vorlagen

Die Muster sind auszufüllende Strukturhilfen. Benötigte Abschnitte können in bestehende Dokumente übernommen werden; die Muster begründen keine zusätzlichen Pflichtdateien. Eckige Platzhalter werden durch tatsächliche Angaben ersetzt oder als konkrete offene Projektfrage gekennzeichnet. Nicht vorhandene Dateien oder Tests werden nicht als vorhanden ausgegeben.

### 14.1 Kompakte projektspezifische AGENTS.md

```markdown

# Arbeitsregeln für [Projektname]

Basis: REPOSITORY_STANDARD.md 1.6 · Übernommen: [Datum]

## Befehle und Lesewege

- Setup / Start / Build: [konkrete Befehle oder genauer Verweis auf README/maßgebliche Anleitung].
- Kernprüfungen und Bereichstests: [Befehle, Voraussetzungen und Auswahlregel oder genauer Verweis].

- Zielbild und Planung: [Links auf REQUIREMENTS.md und ROADMAP.md; bei kleiner Ausnahme Begründung und Links auf beide README-Abschnitte].
- Status und Vorschläge: [genau ein Aufgabenort mit Suchweg, z. B. Issues oder Markdown-Backlog].
- Bereichszuordnung: [Labels/Scope/Abschnitte und ergänzende Suche nach Pfaden, Schnittstellen und Abhängigkeiten]. Bei neuer Aufgabe die geltenden Bereichsanweisungen und passende Details lesen.
- Aufgabenspezifische Quellen: [Aufgabenart → vorhandener Abschnitt/Datei für Architektur, Prüfungen, Fehlerwissen, Entscheidungen oder Pläne; nur Relevantes laden].

## Kernregeln

- Vor neuen/wesentlich geänderten Funktionen Abnahmekriterien klären; komplexe oder risikoreiche Änderungen technisch planen. Auftrag und nötige Anpassungen umsetzen; unabhängige Vorschläge am Aufgabenort erfassen und nur mit Nachweis schließen.
- Funktionale Änderungen: Kernprüfungen und erforderliche Bereichstests ausführen. Umgebung, Codezustand, Ergebnis und Beleg zuordnen; fehlende Nachweise mit Grund benennen.
- Betroffene Dokumentation im selben PR pflegen; bei Ziel- oder Planänderungen Anforderungen, Roadmap und Aufgabenbezüge abgleichen. Temporäre Aufgaben und Status bleiben am Aufgabenort oder im technischen Plan, nicht in dieser Datei.
- Fremde Arbeit und relevante Kommentare erhalten; den gesamten Diff prüfen. Bei Unterbrechung technische Schritte, Prüfergebnisse und nächsten Schritt im vorhandenen Plan festhalten.
- Fehlt Zugriff auf den Aufgabenort, nötige Übertragungen mit Zielort, Zuständigkeit und nächstem Abgleich festhalten und vor Abschluss übertragen oder verbindlich übergeben. Wesentliche Abnahmelücken blockieren den betroffenen Merge.
- Implementiert, geprüft, gemergt und deployed unterscheiden. Dokumentation deutsch; Bezeichner und Dateinamen englisch.

## Projektgrenzen

- Funktionale Änderungen: eigener Branch und PR.

- Merge: erforderliche Prüfungen am maßgeblichen aktuellen PR-Stand nachweisen; lokale Erfolge ersetzen keine erforderliche CI. Pflichtchecks und tatsächlich eingerichtete Merge-Regeln: [genauer Verweis].

- Auto-Merge / Deployment / besondere Migrationsregeln: [tatsächlich geltende Vorgaben].

- Weitere relevante Grenzen und Betriebsprofil: [konkrete Angaben oder genaue Verweise].

```

### 14.2 Funktionsbeschreibung oder Anforderungsabschnitt

```markdown

# [Funktion]

Bereich: [Projektzuordnung/Scope; bei eindeutiger bestehender Abschnittszuordnung nicht doppeln]

Realisierungsstand: [geplant / teilweise umgesetzt / umgesetzt; nicht der Gesamtaufgabenstatus]

Anforderungsbezug: [stabile Kennung und maßgeblicher Verweis]

Maßgebliche Aufgabe: [Verweis]

## Ziel und Verhalten

[Nutzerbedarf, Eingaben, Ausgaben und wesentliche Abläufe]

## Grenzen und Fehlerfälle

[Relevante Nicht-Ziele, ungültige Eingaben und Fehlerreaktionen]

## Abnahmekriterien

[Kriterien hier pflegen ODER auf ihren maßgeblichen Ort verweisen; keine doppelte Liste]

## Implementierung und Prüfungen

[Tatsächliche Pfade und Tests beziehungsweise ausdrücklich noch nicht umgesetzt/geprüft]

```

### 14.3 Technischer Plan mit Übergabestand

```markdown

# [Technische Aufgabe]

Bereich: [Projektzuordnung/Scope; bei eindeutiger bestehender Abschnittszuordnung nicht doppeln]

Maßgebliche Aufgabe und Gesamtstatus: [Verweis auf Aufgabenort]

Anforderungen / Roadmap-Bezug: [Kennungen und relevante Phase verlinken]

Abnahmekriterien: [maßgeblicher Verweis]

Technischer Stand: [Datum, Branch, vorhandener Commit und relevante uncommittete Änderungen]

## Ansatz und Abhängigkeiten

[Vorgehen, wesentliche Risiken und relevante Entscheidungen]

## Umsetzungsschritte

- [ ] [Konkreter technischer Schritt mit erkennbarem Ergebnis]

- [ ] [Konkreter technischer Schritt mit erkennbarem Ergebnis]

## Prüfstand und Blocker

[Prüfung, Umgebung, geprüfter Codezustand, Ergebnis und Beleg oder genauer Verweis; erforderliche fehlende Nachweise samt Grund]

[Für die Fortsetzung relevante Blocker oder erfolglose Ansätze]

## Nächster Schritt

[Konkrete nächste Handlung]

## Noch nicht an den Aufgabenort übertragen

[Nur bei Zugriffslücke: Inhalt/Zielort, Zuständigkeit, nächster Abgleich/Schritt und Auswirkung auf die Abnahme. Vor Abschluss übertragen oder verbindlich übergeben; nach Übertragung durch Verweis ersetzen.]

```

### 14.4 Verbesserungsvorschlag am gewählten Aufgabenort

```markdown

# [Verständlicher Titel]

- Bereich: [betroffene Komponente oder Schnittstelle gemäß Projektzuordnung; vorhandene Labels nutzen]

- Problem: [konkrete Beobachtung]

- Nutzen des Vorschlags: [erwartete Verbesserung]

[Bei Bedarf: Aufwand, Nachteile/Risiken, Abhängigkeiten und relevante Verweise]

[Zustand und Kennung über den Aufgabenort führen; bei Markdown dort eindeutig angeben]

[Bei Schließung: Datum, dokumentierte Begründung und konkrete Belege]

```

### 14.5 Fehlererkenntnis am gewählten Wissensort

```markdown

## [Fehlermuster]

- Bereich/Geltungsbereich: [Komponente und relevante Bedingungen]

- Symptom: [erkennbares Fehlverhalten]

- Bestätigte Ursache: [Ursache und Nachweis]

- Funktionierender Fix: [Lösung und Bezug zur Änderung]

- Schutz vor Wiederholung: [Test, technische Absicherung oder konkrete Prüfregel]

- Belege und Stand: [Referenzen und Datum; bei Überholung Grund/Ersatz]

```

### 14.6 Technische Entscheidungsnotiz

```markdown

# [Entscheidung]

Entscheidungsstand: [beschlossen / ersetzt] · Datum: [Datum]

## Ausgangslage und Alternativen

[Problem, maßgebliche Einschränkungen und Alternativen mit Vor-/Nachteilen]

## Entscheidung und Begründung

[Gewählte Lösung und Gründe]

## Konsequenzen und Verweise

[Nutzen, Nachteile, Folgearbeiten und passende Aufgabe/Spezifikation]

[Bei Ersetzung: Nachfolgeentscheidung verlinken, ursprüngliche Begründung erhalten]

```

### 14.7 Prüfungsabschnitt

```markdown

## Prüfungen

Voraussetzungen: [Umgebung, Abhängigkeiten, isolierte Testdaten und Konfiguration]

Testgrenzen: [für Integrations-/End-to-End-Prüfungen reale Komponenten, ersetzte externe Systeme und Grenzen der nachgewiesenen Aussage gemäß Abschnitt 9]

Artefaktprüfungen, soweit zutreffend: [Build-Befehl, erzeugtes Artefakt und Zuordnung zum Codezustand; Auswahlregeln und Befehle für erforderliche Start-/Installations-/Funktionstests am Artefakt gemäß Abschnitt 9]

| Geprüftes Verhalten | Befehl und Arbeitsordner | Erwartetes Ergebnis | Einsatz / erforderliche Umgebung |
| --- | --- | --- | --- |
| [Verhalten] | [konkreter Befehl] | [Ergebnis] | [Kernprüfung / Bereichsauslöser; Umgebung und CI-Check oder konkrete Lücke] |

Pflichtchecks und Merge-Regeln: [erforderliche Checks am maßgeblichen aktuellen PR-Stand; tatsächlich eingerichtete Absicherung oder konkrete Lücke]

Einrichtungslücken: [konkrete fehlende Prüfungen/CI-Checks und gegebenenfalls Aufgabenverweis]

Weitere Einschränkungen: [relevante bekannte Fehler oder notwendige manuelle Prüfungen]

Nachweisort: [PR/Plan/Lauf; Prüfung, Umgebung, Codezustand, Ergebnis und Beleg gemäß Abschnitt 9 eindeutig zuordnen, keine doppelte Ergebnispflege]

```

### 14.8 Architekturabschnitt

```markdown

## Architektur

[Zweck, Systemgrenzen, Komponenten, Zuständigkeiten und wesentliche Datenflüsse]

| Zentrale Funktion | Maßgebliche Beschreibung | Tatsächlicher Codepfad | Prüfung |
| --- | --- | --- | --- |
| [Funktion] | [Abschnitt oder Verweis] | [Pfad] | [Test oder offener Prüfbedarf] |

[Wichtige Schnittstellen, externe Abhängigkeiten und relevante Entscheidungsverweise]

```

### 14.9 Konfigurationsabschnitt und optionales Betriebsprofil

```markdown

## Konfiguration

Schnittstellen und Ladeweise: [tatsächlich unterstützte Quellen und gegebenenfalls Vorrang]

Konfigurationsbeispiele: [nur passende ungefährliche Beispiele; .env.example bei tatsächlich passender Ladeweise, keine Pflichtdatei]

| Einstellung | Zweck | Pflicht? | Typ/zulässige Werte | Default | Geheim? |
| --- | --- | --- | --- | --- | --- |
| [Name] | [Zweck] | [Ja/Nein/Bedingung] | [Definition] | [Wert oder keiner] | [Ja/Nein] |

Startprüfung: [Validierung, Fehlerreaktion und Umgang mit optionalen Integrationen]

Tests: [isolierte Verzeichnisse und Testkonfiguration]

### [Betriebsprofil, nur wenn relevant]

[Starter/Deployment und tatsächliche Übergabe der Konfiguration]

[Zuordnung Host-Verzeichnis → gegebenenfalls Container-Pfad → Anwendungseinstellung]

[Persistente Daten und gegebenenfalls unterstützte Secret-Dateien; keine echten Geheimnisse]

```

### 14.10 Projektanforderungen (REQUIREMENTS.md)

```markdown
# Anforderungen

## Zielbild und Grenzen

[Beschlossener Zweck, Zielgruppe, gewünschtes Ergebnis und Nicht-Ziele. Keine geplante Funktion als bereits implementiert darstellen.]

## Beschlossene Anforderungen

### REQ-01 – [Bezeichnung]

Bereich: [Scope]

[Erwartetes Verhalten und relevante Fehlerfälle]

Abnahmekriterien: [überprüfbare Kriterien ODER Verweis auf ihren maßgeblichen Ort]

## Offene Entscheidungen

[Nur tatsächliche ungeklärte Punkte; Vorschläge ausdrücklich kennzeichnen. Abschnitt bei fehlendem Bedarf weglassen.]

## Umsetzung und Nachweise

[Roadmap und maßgeblichen Aufgabenort verlinken; keine kopierte Aufgabenstatusliste. Implementierungs- und Prüfnachweise gezielt verlinken.]
```

### 14.11 Projektweite Roadmap (ROADMAP.md)

```markdown
# Roadmap

Planungsgrundlage: [Link auf REQUIREMENTS.md oder begründeten maßgeblichen Anforderungsabschnitt]

Aufgaben und aktueller Bearbeitungsstatus: [maßgeblicher Aufgabenort]

Änderungen und Prüfnachweise: [zugehörige PRs beziehungsweise konkrete Commit- und Prüfverweise]

## Phasen und Abhängigkeiten

| Phase | Angestrebtes Ergebnis | Anforderungen | Voraussetzung / Abhängigkeit | Aufgaben / Detailplan |
| --- | --- | --- | --- | --- |
| [Phase] | [prüfbares Etappenziel] | [Anforderungskennungen verlinken] | [benötigte Ergebnisse; Unklarheiten benennen] | [vorhandene Verweise; noch fehlende Aufgabe ausdrücklich benennen] |

[Reihenfolge begründen; voneinander unabhängige Phasen kenntlich machen. Keine erfundenen Termine, Aufgaben oder Fortschrittsangaben.]

## Pflege

[Bei geänderten Zielen, Reihenfolgen oder Abhängigkeiten mit Anforderungen und Aufgaben abgleichen. Konkreten Aufgabenstatus und Priorität ausschließlich am Aufgabenort führen.]
```

## 15. Einführung und Aktualisierung eines konkreten Repositories

1. Vorhandenen Projektstand, Anweisungen und Arbeitsabläufe prüfen. Zweck, zentrale Funktionen und Technologien aus tatsächlichen Quellen erfassen.

2. Die benötigten Informationen jeweils einem maßgeblichen Pflegeort zuordnen. Vorhandene geeignete Abschnitte übernehmen; `README.md` und `AGENTS.md` als Einstieg sicherstellen. `REQUIREMENTS.md` und `ROADMAP.md` gemäß Abschnitt 3 anlegen beziehungsweise verlustfrei übernehmen und aus beiden Einstiegen verlinken; eine kleine Ausnahme dort begründen. Weitere Dateien nur bei konkretem Bedarf anlegen.

3. Aufgabenort, Bereichszuordnung, ergänzenden Suchweg und gegebenenfalls relevantes Betriebsprofil festlegen. Eindeutige bestehende Entscheidungen weiterverwenden; wesentliche offene Entscheidungen mit Optionen, Vor-/Nachteilen und Empfehlung klären.

4. Eine kompakte `AGENTS.md` mit übernommener Standardversion, gültigen Befehlen beziehungsweise genauen Verweisen, unmittelbar geltenden Kernregeln und Lesewegen erstellen oder anpassen. Bereichsanweisungen und Skills nur bei tatsächlichem Bedarf ergänzen und für die verwendeten Agenten auffindbar machen.

5. Setup-, Start- und Testbefehle ermitteln. Prüfnachweise mit Umgebung, Codezustand, Ergebnis und Beleg korrekt dokumentieren. Erforderliche Prüfungen und tatsächlich vorhandene CI-/Merge-Absicherung unterscheiden; lokale Erfolge ersetzen keine erforderliche CI. Fehlende Einrichtung als konkrete Lücke erfassen; nur bei entsprechendem Auftrag umsetzen.

6. Bei Konfiguration die Schnittstellen, Pflichtwerte und tatsächliche Startvalidierung beschreiben. Für relevante Betriebsprofile die Übergabe und Pfadzuordnung erklären. Technische Lücken nicht als umgesetzt darstellen.

7. Vorhandene Pläne, Entscheidungen, Fehlererkenntnisse und Vorschläge ohne erfundene Details übernehmen. Ausstehende Übertragungen mit Zuständigkeit und nächstem Abgleich nach Abschnitt 7 verfolgen; ihre Auswirkung auf die Abnahme klären. Bei beauftragtem Wechsel des Aufgabenorts verlustfrei übertragen und den bisherigen Ort nach geprüfter Übernahme als abgelöst kennzeichnen.

8. Alle Regeln, Vorlagen und Verweise auf Widersprüche, doppelte Statuspflege, unbemerkte Platzhalter und überholte Pflichtdateien prüfen. Änderungen an den Einrichtungsanweisungen mitziehen.

9. Nach der ersten echten Aufgabe prüfen, welche Zuordnung hilfreich war und wo Unklarheit oder unnötiger Pflegeaufwand entstand. Den Standard beziehungsweise seine projektspezifische Übernahme bewusst weiterentwickeln.

## 16. Einrichtungs-Prompt für projektspezifische Dokumentation

### Verwendung

Stelle diese Datei und das Zielrepository dem Agenten zur Verfügung. Kopiere den folgenden Prompt in den Auftrag oder beauftrage ausdrücklich den Einrichtungs-Prompt aus Abschnitt 16. Bei einem leeren Repository gib zusätzlich die Projektidee an. Der Prompt wird nur bei beauftragter Einrichtung oder Aktualisierung ausgeführt, nicht bei jedem Lesen dieser Datei.

Er übernimmt die einmalige Zuordnung aller benötigten Informationen zu ihren Pflegeorten und fragt nur bei wesentlichen offenen Entscheidungen nach. Bei erneuter Ausführung werden vorhandene Zuordnungen geprüft und betroffene Inhalte aktualisiert; es entstehen keine parallelen Regelsammlungen oder Backlogs.

### Kopierbarer Prompt

```text

Erstelle beziehungsweise aktualisiere die projektspezifische Dokumentation des Zielrepositories gemäß der bereitgestellten REPOSITORY_STANDARD.md Version 1.6.

Übernimm selbst die einmalige Zuordnung aller benötigten Informationen zu ihren maßgeblichen Pflegeorten. Verwende vorhandene Struktur und bereits getroffene Entscheidungen. Entscheide eindeutig ableitbare und unkritische Zuordnungen selbst; kläre nur wesentliche offene Entscheidungen mit mir. Bei späteren Aktualisierungen überprüfe vorhandene Zuordnungen und ändere nur die tatsächlich betroffenen Teile.

1. Bestandsaufnahme

Lies den Standard vollständig und die geltenden Projektanweisungen. Prüfe vorhandene Dokumentation, relevante Codebereiche, Abhängigkeitsdateien, Startkonfiguration, Tests und CI. Erfasse Zweck, Funktionen, Komponenten, Schnittstellen, tatsächliche Ablageorte und Arbeitsstand. Erhalte vorhandene fremde Arbeit und relevante Kommentare.

Unterscheide gewünschtes Verhalten, implementierten Zustand und tatsächlich geprüfte Ergebnisse. Erfinde keine historischen Entscheidungsgründe oder Fehlerursachen. Bei einem leeren Repo kläre die Projektidee und entscheidende Anforderungen; kennzeichne zukünftige Umsetzung als geplant.

2. Pflegeorte bestimmen

Stelle README.md und AGENTS.md als Einstieg sicher. Für längerfristige Projekte erstelle REQUIREMENTS.md und ROADMAP.md im Hauptverzeichnis gemäß Abschnitt 3 und verlinke beide aus README und AGENTS. Übernimm bestehende Inhalte verlustfrei, erhalte maßgebliche Detailquellen über Verweise und aktualisiere betroffene Links. Für kleine Experimente, Dateisammlungen oder Hilfsskripte ohne mehrphasige Weiterentwicklung genügen die benannten README-Abschnitte; dokumentiere die Ausnahme in AGENTS. Trenne beschlossenes Zielbild, Phasen und Abhängigkeiten, konkreten Aufgabenstatus und technische Detailplanung. Ordne benötigte Architektur-, Test-, Konfigurations-, Anforderungs-, Fehler- und Entscheidungsinformationen jeweils einem maßgeblichen Pflegeort zu. Verwende passende vorhandene Abschnitte weiter. Weitere Dateien entstehen nur bei konkretem Bedarf gemäß Abschnitt 3, ohne leere Vorratsdateien oder starre Dateigrenze.

Halte einzelne Features, Bugs und laufende PRs aus dauerhaften Agentenanweisungen heraus. Lege eine lokale AGENTS.md nur für echte bereichsspezifische Regeln an. Einen Skill ergänze nur für einen tatsächlich wiederkehrenden spezialisierten Ablauf; prüfe, wie die verwendeten Agenten ihn entdecken. Erzeuge weder leere docs-Bäume noch eine Vorratssammlung an Skills.

Bestimme einen maßgeblichen Aufgabenort für Gesamtstatus, Priorität und Verbesserungsvorschläge. Übernimm einen geeigneten bestehenden Ort. Wähle anhand des tatsächlichen Workflows Issues oder einen Markdown-Backlog; kläre eine wesentliche offene Wahl mit mir. PRs dokumentieren Änderungen und Prüfergebnisse; technische Pläne behalten Umsetzungsschritte, Prüfstand, Blocker und nächsten Schritt, aber keinen zweiten Gesamtstatus. Auch Abnahmekriterien haben genau einen maßgeblichen Ort.

Ermittle ein gegebenenfalls benötigtes Betriebsprofil. Die Linux-/Homelab-Pfade gelten nur für die entsprechende Umgebung; die Anwendung benötigt keine fest eingebauten Host-Pfade. Lege .env.example nur an, wenn sie zur tatsächlichen Konfigurationsweise passt; erzeuge keine erfundenen Einstellungen. Halte Zuordnung und Suchwege in den Einstiegsdokumenten fest. Eine zusätzliche Zuordnungsdatei ist nicht nötig.

3. Nur wesentliche Unklarheiten erfragen

Beantworte Sachfragen zunächst aus verfügbaren Projektquellen. Frage nach, wenn eine verbleibende Unklarheit Ziel, Verhalten, Umfang, grundlegende Technik, Aufgabenort, Betriebsprofil oder Befugnisse wesentlich beeinflusst. Frage eindeutig entschiedene Punkte nicht erneut ab. Unkritische redaktionelle Details entscheidest du selbst.

Stelle je Runde höchstens drei konkrete Fragen. Benenne die fehlende Information und die davon abhängige Entscheidung; nenne praktikable Optionen mit Vor- und Nachteilen sowie deine begründete Empfehlung. Bearbeite eindeutig geklärte unabhängige Teile weiter. Behaupte keine vollständige Einrichtung, solange entscheidende Antworten fehlen. Eine zusätzliche pauschale Planbestätigung ist nicht erforderlich; nutze bei komplexer oder risikoreicher Anpassung den vorgesehenen technischen Plan.

4. Dokumentation anpassen

Erstelle oder ergänze die benötigten Informationen an den gewählten Orten. Verwende konkrete Pfade, Befehle und Voraussetzungen und kennzeichne, ob Befehle nur ermittelt oder tatsächlich ausgeführt wurden. Übernimm bestätigte Erkenntnisse und Entscheidungen ohne Duplikate. Beschreibe Konfigurationsschnittstellen, Pflichtwerte, tatsächliche Startvalidierung und gegebenenfalls die Übergabe zwischen Host, Container und Anwendung. Verwende nur ungefährliche Beispiele und keine echten Secrets.

Dokumentiere im maßgeblichen Prüfungsabschnitt die Testgrenzen und gegebenenfalls erforderlichen Build- und Artefaktprüfungen nach Abschnitt 9. Verwende vorhandene Prüfungen und benenne fehlende Umsetzung als konkrete Einrichtungslücke.

Prüfe vorhandene GitHub-Issue- und PR-Vorlagen auf Eignung für den gewählten Aufgabenort und PR-Ablauf. Erhalte geeignete Vorlagen und passe Inhalte sowie Lesewege an das Zielprojekt an; erzeuge keinen zweiten Backlog. Ersetze Template-spezifische Prüfkommandos und Checknamen durch tatsächliche Projektprüfungen oder benenne fehlende Prüfungen als offen. Lokale Ergebnisse und CI-Nachweise bleiben getrennt. Verlinke verwendete Vorlagen aus AGENTS.md und verlange ihre passenden Inhalte auch bei API-/CLI-Erstellung. GitHub-Vorlagen sind Arbeitshilfen zu Abschnitten 6, 7, 9 und 11, keine zusätzliche Freigabestufe und kein technischer Merge-Schutz.

Bei einer neuen Ableitung ersetze die mitkopierten README.md und AGENTS.md durch eigenständige Projekteinträge; übernimm keine Template-Aufgaben als Produktanforderungen. Wenn die Projektregeln übernommen und alle Links geprüft sind, entferne eindeutig unveränderte und nicht mehr benötigte Template-Hilfen wie REPOSITORY_STANDARD.md, SETUP.md, templates/ und scripts/check_template.py samt zugehörigem Template-Workflow. Bereits angepasste Dateien und vorhandene Projektarbeit erhalten; in bestehenden Projekten keine pauschale Bereinigung.

Erstelle eine kompakte AGENTS.md anhand von Vorlage 14.1: Standardversion 1.6, Übernahmedatum, Befehle beziehungsweise genaue Verweise, Aufgabenort und Suchweg, unmittelbar geltende Kernregeln, Projektgrenzen und konkrete Lesewege. Eine Versionsnummer ersetzt keine Arbeitsanweisung. Erhalte insbesondere die Pflichten zu erforderlichen Prüfungen, aktueller betroffener Dokumentation, belegtem Schließen von Vorschlägen und brauchbarer Übergabe.

Verlange bei jeder neuen Aufgabe oder Sitzung den gezielten Relevanzabgleich nach Abschnitt 4. Übernimm passende Bereichsnamen und vorhandene Labels, Scope-Felder oder eindeutige Abschnittszuordnungen für Aufgaben, eigenständige Pläne und Spezifikationen. Dokumentiere den ergänzenden Suchweg; berücksichtige Schnittstellen, Abhängigkeiten und übergreifende Regeln auch außerhalb passender Labels. Nur passende Einträge und Dokumente vollständig lesen; keine vollständige Backlog-Lektüre oder allgemeine Aufräumrunde pro Bugfix.

5. Aufgaben erhalten

Pflege relevante Vorschläge am gewählten Aufgabenort gemäß Abschnitt 7. Bei fehlendem Zugriff benenne die Lücke und halte neue Vorschläge oder nötige Aktualisierungen vorübergehend im vorhandenen Übergabestand als noch nicht übertragen fest, mit Inhalt/Zielort, Zuständigkeit und nächstem konkreten Abgleich. Erzeuge keinen dauerhaften zweiten Backlog. Vor Abschluss übertrage die Einträge nach erneutem Abgleich und im Rahmen der Befugnisse oder übergib sie verbindlich nach den Projektregeln. Ungeklärte Zuständigkeit und ausstehende Übertragung bleiben sichtbar; nach Übertragung verlinke das Ergebnis. Abnahmerelevante Lücken blockieren den betroffenen Merge, unabhängige Verbesserungsideen nicht. Behaupte durch einen Textmarker weder eine technische Merge-Sperre noch automatische Hintergrundüberwachung.

Stelle bei fehlenden wesentlichen Informationen nur den betroffenen Teil zurück. Ein beauftragter Wechsel des Aufgabenorts erhält Vorschläge, Zustände, Begründungen und relevante Verweise. Kennzeichne den alten Ort erst nach geprüfter Übernahme als abgelöst.

6. Umfang und Abschluss

Dieser Auftrag richtet die Dokumentation ein. Prüfe und beschreibe vorhandene CI und technische Einrichtungen; erfasse fehlende Umsetzung als konkrete Lücke beziehungsweise Folgeaufgabe. Technische Einrichtung, Codeumbauten, Host-Änderungen, Merge und Deployment folgen entsprechenden Aufträgen oder bereits bestehenden Befugnissen. Erweitere den Auftrag nicht stillschweigend und frage bereits erteilte Befugnisse nicht erneut ab. Ändere den allgemeinen Standard nicht nebenbei für ein Projekt.

Prüfe Anforderungen und Roadmap auf klare Zuordnung, nachvollziehbare Abhängigkeiten und Verweise zum Aufgabenort ohne doppelte Statusführung. Prüfe alle betroffenen Regeln, Vorlagen und Lesewege auf Widersprüche, doppelte Pflegeorte, konkurrierende Statusangaben, alte Pflichtdateien, falsche Verweise und unbemerkte Platzhalter. Führe passende vorhandene Dokumentationsprüfungen aus. Ordne relevante Prüfungen ihrer Umgebung, dem geprüften Codezustand, dem Ergebnis und einem Beleg zu; gemeinsame Angaben dürfen gebündelt werden. Unterscheide lokale Erfolge und CI-Nachweise. Beschreibe erforderliche Checks und die tatsächlich eingerichteten Merge-Regeln; fehlende CI oder überholte Läufe gelten nicht als Erfolgsnachweis. Nenne erforderliche, aber nicht ausgeführte Prüfungen samt Grund; keine Aufzählung aller denkbaren Tests und keine automatische vollständige Anwendungstestsuite für reine Dokumentation.

Liste neue und geänderte Dateien mit Zweck auf. Erkläre knapp gewählte Pflegeorte, Aufgabenverwaltung, gegebenenfalls Betriebsprofil sowie offene Entscheidungen, technische Lücken und ausstehende Übertragungen. Halte bei Unterbrechung Fortschritt und nächsten Schritt fest. Dokumentation und Arbeitsregeln sind deutsch, Datei- und Ordnernamen sowie Codebezeichner englisch.

```

## 17. Hintergrund und Begriffe

Die Struktur verbindet Context Engineering, spezifikationsgestützte Entwicklung und gepflegte Projektdokumentation. Die konkreten Regeln dieser Datei sind die gemeinsam getroffenen Entscheidungen; sie sind keine zwingende Vorgabe eines externen Frameworks.

- [AGENTS.md](https://agents.md/) beschreibt das offene Format für Agentenanweisungen.

- [GitHub Spec Kit](https://github.github.com/spec-kit/) ist ein Beispiel für einen durch Spezifikation, Planung, Aufgaben und Umsetzung geführten Entwicklungsprozess.

Diese Quellen wurden zu Beginn der Ausarbeitung am 27. September 2026 herangezogen. Der Standard setzt keine Installation von Spec Kit und kein bestimmtes Agentenprodukt voraus.
