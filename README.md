## DE
Diese Anwendung soll Benutzer*innen ermöglichen, mit Hilfe von einem LLM (Large Language Model), spezifische Informationen aus der Datenbank der [Pflanzenschutzorganisation für Europa und den Mittelmeerraum](http://eppo.int) abzufragen.
Dazu soll die [vorhandene API](https://data.eppo.int/documentation/rest) mit entsprechenden [Eppocodes](https://www.eppo.int/RESOURCES/eppo_databases/eppo_codes) benutzt werden.

### Bisheriger Fortschritt
- Erstellen von [Helferfunktionen](https://github.com/LH2OQ/HS-MD---Coding-Club/tree/main/helper) zum Lesen und Speichern von  HTML (Webseiten), Text und PDF (benötigt das Modul [pypdf](https://pypdf.readthedocs.io/en/stable/)), sowie für Zugriff auf das LLM
- Erstellen [eines Skripts]([helper/eppo_first_aid.py](https://github.com/LH2OQ/HS-MD---Coding-Club/blob/main/helper/eppo_first_aid.py)),
  um den Inhalt des ['User-Guides'](https://media.eppo.int/media/files/EPPO_media_platform_user-guide_2022_08.pdf) und spezifische Links zur Datenbank von der Webseite auszulesen und dann eine spezifische Anfrage an das LLM zu stellen, welche weitere Schritte erläutern / vereinfachen helfen soll.
  Die einzelnen Konversationen werden in nummerierten Textdateien abgespeichert (im Ordner 'LLM' => wird im aktuellen Verzeichnis erstellt, wenn nicht existent), um wiederholte Anfragen zum selben Problem zu vermeiden und den Energieverbrauch zu reduzieren.

### Weitere Schritte
- Konkrete Strategien und Code für die Anwendung mit Hilfe des LLM erstellen
- Die konkrete Anwendung ausführbar entwickeln und testen
- Eventuell eine Art "UI", bzw ein HTML-Formelement (Webseite mit Flask ? ) erstellen, so dass Benutzende dort in einfacher und übersichtlicher Form konkrete Anfragen zu den relevanten Daten stellen können

## EN
This application is designed to enable users to query specific information from the database of the [European and Mediterranean Plant Protection Organization](http://eppo.int) with the help of an LLM (Large Language Model).
To do this, the [existing API](https://data.eppo.int/documentation/rest) with corresponding [Eppocodes](https://www.eppo.int/RESOURCES/eppo_databases/eppo_codes) will be used.

### Progress to date
- Creation of [helper functions](https://github.com/LH2OQ/HS-MD---Coding-Club/tree/main/helper) for reading and saving HTML (web pages), text, and PDF (requires the [pypdf](https://pypdf.readthedocs.io/en/stable/) module), as well as for accessing the LLM
- Creation of [a script]([helper/eppo_first_aid.py](https://github.com/LH2OQ/HS-MD---Coding-Club/blob/main/helper/eppo_first_aid.py)),
  to read the content of the ['User-Guide'](https://media.eppo.int/media/files/EPPO_media_platform_user-guide_2022_08.pdf) and specific links to the database from the website and then make a specific request to the LLM, which should help explain/simplify further steps.
  The individual conversations are stored in numbered text files (in the 'LLM' folder => created in the current directory if it does not exist) to avoid repeated requests for the same problem and reduce energy consumption.

### Further steps
- Create concrete strategies and code for the application with the help of the LLM.
- Develop and test the concrete application executable.
- Possibly create a kind of “UI” or HTML form element (website with Flask?) so that users can submit specific requests for relevant data in a simple and clear format.

Translated with DeepL.com (free version)
