Aplikacja pozwalająca na wygenerowanie mapy lasów ochronnych w obrębie danego nadleśnictwa (jednostki organizacyjnej Państwowego Gospodarstwa Leśnego Lasy Państwowe) oraz dostarczanie informacji w formie raportu o ich powierzchni i liczbie wydzieleń leśnych. Aplikacja ładuje dane geometryczne wydzieleń w formie pliku Shapefile (pobrane przez użytkownika z Banku Danych o Lasach), dołącza do jego tabeli atrybutów pobrane z osobnego pliku .txt informacje o wszystkich kategoriach ochronności danego wydzielania i na tej podstawie generuje mapę lasów ochronnych, jak również raport o ogólnej liczbie i powierzchni wydzieleń leśnych w ramach danej kategorii ochronności. Aplikacja wykorzystuje m.in. biblioteki Qgis i PyQt. Przykładowe dane są w folderze 'test_data'. Do użytku pracowników PGL LP.

URUCHOMIENIE:

Zainstaluj oprogramowanie QGIS LTR oraz Visual Studio Code
W pliku Visual Studio Code_pyqgis.bat - sprawdź/skoryguj ścieżkę dostępu do QGIS (OSGEO4W_ROOT)
W pliku Application.py sprawdź/skoryguj ścieżkę dostępu do qgis-ltr (QGIS_PATH)
Przy pomocy pliku Visual Studio Code_pyqgis.bat otwórz Visual Studio Code
W Visual Studio Code uruchom plik Application.py