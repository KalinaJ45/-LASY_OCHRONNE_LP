from os import path
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSettings, QFileInfo
from PyQt5 import QtGui


class SaveXLSX:
    """Saving .xlsx file class.
    """

    def save_xlsx(self, window) -> str:
        """Saves data as .xlsx file in selected localization.

        Args:
            window (QMainWindow): dialog box to selecte file saving path.

        Returns:
            str:  selected saving path.
        """

        dirPath = QSettings().value("/excelSavePath", ".", type=str)
        (file_name, filter) = QFileDialog.getSaveFileName(window,
                                                          "Zapisz jako plik excel...",
                                                          dirPath,
                                                          filter="Excel files (*.xlsx)",
                                                          )
        window.setWindowIcon(QtGui.QIcon(":/images/leaf.ico"))
        fn, file_extension = path.splitext(file_name)
        if len(fn) == 0:
            return
        QSettings().setValue("/excelSavePath", QFileInfo(file_name).absolutePath())
        if file_extension != '.xlsx':
            file_name = file_name + '.xlsx'
        return file_name
