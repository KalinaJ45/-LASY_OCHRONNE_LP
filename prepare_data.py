import os
from os import path
import sys

from collections import deque
import tempfile
import zipfile

from PyQt5.QtWidgets import QFileDialog
from qgis.core import *

from field_kind import FieldKindEnum


class PrepareData:
    """Preparing data class.
    """

    def __init__(self):
        """Constructor.
        """
        self.selected_layer = ''
        self.selected_data = ''
        self.correct_data = True
        self.categories_and_num_dictionery = {}
        self.list_of_num = []

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        self.selected_data = dialog.getOpenFileName(
            None, "Wybierz archiwum", "", "Archiwum ZIP (*.zip)")
        if self.selected_data[0]:
            path = str(os.path.basename(
                self.selected_data[0])).replace('.zip', '\\')
            zf = zipfile.ZipFile(self.selected_data[0])
            tempdir = tempfile.TemporaryDirectory()
            zf.extractall(tempdir.name)
            self.temp_dir_path = tempdir.name + '\\' + path
            shp_path = self.temp_dir_path + 'G_SUBAREA.shp'
            self.selected_layer = QgsVectorLayer(
                shp_path, "Wydzielenia", "ogr")
            txt_path = self.temp_dir_path + 'f_arod_category.txt'
            if ([field.name() for field in self.selected_layer.fields()] == [field.value.field_name for field in FieldKindEnum]):
                with open(txt_path, "r") as file:
                    col = sorted([[line.split('\t')[0], line.split('\t')[1].rstrip(
                    ), line.split('\t')[2]]for line in file], key=lambda x: x[2])
                    for i in range(0, len(col)):
                        del col[i][2]
                    deque((self.categories_and_num_dictionery.setdefault(num, []).append(
                        category) for num, category in col), maxlen=0)
                    self.list_of_num = [key for key in self.categories_and_num_dictionery.keys() if len(
                        self.categories_and_num_dictionery[key]) > 1]
            else:
                self.correct_data = False

    def get_data_correctness(self) -> bool:
        """Gets if selected data is coorect.

        Returns:
            bool: false or true depending on whether the data is correct.
        """
        return self.correct_data

    def get_selected_layer(self) -> QgsVectorLayer:
        """Gets selected layer

        Returns:
            QgsVectorLayer: selected vector layer. 
        """
        return self.selected_layer

    def get_selected_data(self) -> str:
        """Gets path to selected zip archive with data.

        Returns:
            str: path to selected zip archive with data.
        """
        return self.selected_data[0]

    def get_categories_and_num_dictionery(self) -> dict:
        """Gets dictionary in which kays are specific number of forest subareas and values are its protection categories.

        Returns:
            dict: dictionary in which kays are specific number of forest subareas (str) and values (str) are its protection categories (joined from f_arod_category.txt file).
        """
        return self.categories_and_num_dictionery

    def get_list_of_num(self) -> list:
        """Gets list of specific number of forest subareas they have more than one protection category.

        Returns:
            list: list of specific number of forest (str) subareas they have more than one protection category.
        """
        return self.list_of_num
