# Arbeitsregeln für das Repository Template

Basis: REPOSITORY_STANDARD.md 1.4 · Übernommen: 27. September 2026

## Zuerst den Repository-Typ bestimmen

Diese Datei gilt für das zentrale Template. In einem daraus erzeugten, noch nicht eingerichteten Projekt ist sie eine vorläufige Einstiegsanweisung: Bei beauftragter Einrichtung [SETUP.md](SETUP.md) anwenden und anschließend durch projektspezifische Regeln ersetzen. Das bloße Lesen startet keinen Einrichtungsauftrag.

## Befehle und Lesewege

- Zielbild: [REQUIREMENTS.md](REQUIREMENTS.md); projektweite Planung: [ROADMAP.md](ROADMAP.md). Bei Ziel- oder Planänderungen beide mit den Aufgabenbezügen abgleichen; Aufgabenstatus bleibt in GitHub Issues.

- Lokale Prüfung, Voraussetzungen und Grenzen: [README.md, Abschnitt Prüfungen](README.md#prüfungen).
- Standardänderung: betroffene Abschnitte in [REPOSITORY_STANDARD.md](REPOSITORY_STANDARD.md), zugehörige Muster unter templates/ und SETUP.md lesen. Gesamten Standard nur für Einrichtung, umfassende Aktualisierung oder unklare übergreifende Auswirkungen laden.
- Vorlagenänderung: [templates/README.md](templates/README.md) und maßgeblichen Standardabschnitt lesen.
- Neue Aufgabe/Sitzung: Branch, Diff und vorhandene Arbeit prüfen. Aufgabenort und Suchweg stehen in [README.md](README.md#architektur-und-pflege). Betroffene Pfade, Begriffe, Schnittstellen und übergreifende Einschränkungen berücksichtigen.

## Kernregeln

- Auftrag und erforderliche Anpassungen umsetzen; unabhängige Verbesserungen am maßgeblichen Aufgabenort erfassen. Vorschläge sind keine Ausführungsaufträge.
- Vor wesentlichen Änderungen überprüfbare Abnahmekriterien festhalten; komplexe oder risikoreiche Arbeit technisch planen. Keine leeren Vorratsdokumente und keine zweite Statusführung.
- Vorhandene fremde Arbeit, brauchbare Struktur und weiterhin relevante Kommentare erhalten. Gesamten Diff auf unbeabsichtigte Änderungen prüfen.
- Standard, betroffene Muster und Einrichtungsanweisung konsistent halten. Muster 14.1–14.11 nicht unabhängig vom Standard verändern. Projektbesonderheiten nicht als universelle Vorgabe einschleusen.
- Passende Prüfungen ausführen; Befehl, Umgebung, geprüften Codezustand inklusive uncommitteter Änderungen, Ergebnis und Beleg zuordnen. Fehlende Nachweise benennen. Lokaler Erfolg ist kein CI-Erfolg.
- Betroffene Dokumentation im selben PR aktualisieren. Wiederverwendbare bestätigte Fehlererkenntnisse am passenden vorhandenen Ort festhalten.
- Bei Unterbrechung technischen Fortschritt und nächsten Schritt im vorhandenen Plan oder Auftrag dokumentieren; keinen zweiten Gesamtstatus führen.
- Bei fehlendem Aufgabenort-Zugriff die Lücke nennen. Ausstehende Übertragungen mit Zielort, Zuständigkeit und nächstem Abgleich im vorhandenen Übergabestand festhalten. Wesentliche Abnahmelücken blockieren den Merge; unabhängige Ideen nicht.
- Einträge nur mit Nachweis und begründeter Entscheidung schließen. Konflikte zwischen beschlossenen Plänen klären.
- Dokumentation deutsch; Datei-/Ordnernamen und Codebezeichner englisch. Keine echten Secrets oder vollständigen privaten Nutzdaten aufnehmen.

## Git und Grenzen

Funktionale Änderungen erfolgen über Branch und PR. Einrichtung, Veröffentlichung, Merge und Deployment sind getrennte Aktionen; bestehende konkrete Befugnisse berücksichtigen. Keine pauschale Auto-Merge-Freigabe. Erforderliche Prüfungen müssen am maßgeblichen aktuellen PR-Stand nachgewiesen sein; fehlende CI-Absicherung ist eine offene Einrichtungslücke.

Dieses Template enthält keine automatische Worker-Steuerung, Hintergrundüberwachung, technische Merge-Sperre oder Deploymentfreigabe.
