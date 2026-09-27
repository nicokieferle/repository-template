# Optionale Projektvorlagen

Die Dateien mit Endung `.template` sind Strukturhilfen, keine aktiven Projektanweisungen. Sie dürfen Platzhalter enthalten. Die Ablageregeln aus Standardabschnitt 3 gelten: Längerfristige Projekte führen REQUIREMENTS.md und ROADMAP.md im Hauptverzeichnis; für die kleine Ausnahme genügen README-Abschnitte. Andere Abschnitte können in passende vorhandene Dokumente übernommen werden.

| Vorlage | Einsatz |
| --- | --- |
| [AGENTS.md.template](AGENTS.md.template) | Konkrete Projektregeln und Lesewege; Standard 14.1. |
| [README.md.template](README.md.template) | Projekteinstieg; ergänzende Strukturhilfe zu Standard 3. |
| [feature.md.template](feature.md.template) | Anforderungen oder Funktionsabschnitt; Standard 14.2. |
| [plan.md.template](plan.md.template) | Komplexe/risikoreiche Umsetzung mit Übergabestand; Standard 14.3. |
| [improvement.md.template](improvement.md.template) | Eintrag am bestehenden Aufgabenort; Standard 14.4. |
| [lesson.md.template](lesson.md.template) | Bestätigte wiederverwendbare Fehlererkenntnis; Standard 14.5. |
| [decision.md.template](decision.md.template) | Grundlegende technische Entscheidung; Standard 14.6. |
| [testing.md.template](testing.md.template) | Prüfungsabschnitt; Standard 14.7. |
| [architecture.md.template](architecture.md.template) | Architekturabschnitt; Standard 14.8. |
| [configuration.md.template](configuration.md.template) | Konfiguration und optionales Betriebsprofil; Standard 14.9. |
| [REQUIREMENTS.md.template](REQUIREMENTS.md.template) | Beschlossenes projektweites Zielbild und Anforderungen; Standard 14.10. |
| [ROADMAP.md.template](ROADMAP.md.template) | Projektweite Phasen, Reihenfolge und Abhängigkeiten; Standard 14.11. |

Die elf direkt aus Abschnitt 14 gewonnenen Muster werden mit dem Standard abgeglichen. Bei Änderungen immer beide Fassungen gemeinsam pflegen und `python3 scripts/check_template.py` im Wurzelverzeichnis ausführen.

Bei Übernahme Platzhalter ersetzen, Nichtzutreffendes weglassen und echte Verweise prüfen. Die Vorlagen verlangen weder eigene Dateien für jeden Bereich noch ein zweites Backlog. Keine erfundenen historischen Begründungen, bestandenen Tests oder zukünftigen Hintergrundaktionen eintragen.
