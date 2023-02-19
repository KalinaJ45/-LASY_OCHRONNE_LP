# -*- coding: utf-8 -*-

import sys
import unittest

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor

import Application

app = QApplication(sys.argv)


class ApplicationTest(unittest.TestCase):
    """Test the application GUI.
    """

    def setUp(self):
        """Create the GUI.
        """
        self.form = Application.Window()

    def test_defaults(self):
        """Test the GUI in its default state.
        """
        self.assertEqual(self.form.actionZoomIn.text(), "Powiększ")
        self.assertEqual(self.form.actionNewProject.text(), "Nowy projekt")
        self.assertEqual(self.form.actionSaveImage.text(), "Zapisz jako obraz")
        self.assertEqual(self.form.actionPrintImage.text(), "Drukuj obraz")
        self.assertEqual(self.form.actionPan.text(), "Przesuń")
        self.assertEqual(self.form.actionZoomIn.text(), "Powiększ")
        self.assertEqual(self.form.actionZoomOut.text(), "Pomniejsz")
        self.assertEqual(self.form.actionZoomExtent.text(), "Cały zasięg")
        self.assertEqual(self.form.actionIdentify.text(),
                         "Pokaż właściwości wydzielenia")
        self.assertEqual(self.form.actionShowTabeleAttribute.text(),
                         "Pokaż tabelę właściwości wydzieleń")
        self.assertEqual(self.form.actionExportTabeleAttribute.text(),
                         "Eksportuj tabelę własciwości wydzieleń do pliku Excel")
        self.assertEqual(self.form.actionHelp.text(), "Podręcznik Użytkownika")
        self.assertEqual(self.form.loadLayerBtn.text(), "")
        self.assertEqual(self.form.deleteLayerBtn.text(), "")
        self.assertEqual(self.form.selectBtn.text(), "")
        self.assertEqual(self.form.unselectBtn.text(), "")
        self.assertEqual(self.form.generateRaportBtn.text(), "")
        self.assertEqual(self.form.coordinates_label.text(),
                         "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">WSPÓŁRZĘDNE:</span></p></body></html>")
        self.assertEqual(self.form.progressBar.value(), 50)
        self.assertEqual(self.form.categoriesComboBox.currentIndex(), -1)

    def test_ProgressBar(self):
        """Test the tequprogress bar.
        """

        # Test the maximum.  This one goes to 11.
        self.form.progressBar.setValue(120)
        self.assertEqual(self.form.progressBar.value(), 100)

        # Test the minimum of zero.
        self.form.progressBar.setValue(-10)
        self.assertEqual(self.form.progressBa.value(), 0)

        self.form.progressBar.setValue(50)


if __name__ == "__main__":
    unittest.main()
