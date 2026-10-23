# Changelog

Alle nennenswerten Änderungen an Fire Elite. Bei jeder Änderung wird die
Version (`APP_VERSION` in `app/main.py`) erhöht und hier ein Eintrag ergänzt.

## 1.2 – 2026-10-23

### Neu
- Die Seite „Über Elite“ zeigt jetzt den kompletten Changelog statt nur der
  Versionsnummer (#9).

## 1.1 – 2026-10-23

### Neu
- Detailseite für jeden Einsatz (`/einsaetze/{id}`) mit allen Feldern;
  Bearbeiten und Löschen (nur Admin) unten auf der Seite. Die Einsatzliste
  öffnet den Einsatz per Klick auf die Zeile und kommt auf dem Handy ohne
  seitliches Scrollen aus (#3).

### Behoben
- Ist „Eingesetzt“ abgewählt, wird das Einsatzmittel gesperrt und auf
  „In Bereitstellung“ gesetzt, auch beim CSV-Import (#2).
- Zeiten wurden um 1 bzw. 2 Stunden zu früh angezeigt; die Datenbankverbindung
  nutzt jetzt fest die Zeitzone Europe/Berlin (#5).

## 1.0

- Erste Version.
