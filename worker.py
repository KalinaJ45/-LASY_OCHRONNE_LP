
from PyQt5.QtCore import QObject, pyqtSignal
from qgis.core import *
from qgis.core import QgsField, NULL


class Worker(QObject):
    """ Worker for joining protection categories of forest subares from  f_arod_category.txt file to tabele attributes of selected vector layer.
    """
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, selected_layer, categories_and_num_dictionery, list_of_num):
        """Constructor.
        """
        QObject.__init__(self)
        self.selected_layer = selected_layer
        self.categories_and_num_dictionery = categories_and_num_dictionery
        self. list_of_num = list_of_num

    def run(self):
        """Runs worker.
        """
        self.progress.emit(0)
        self.selected_layer.startEditing()
        for i, feat in enumerate(self.selected_layer.getFeatures()):
            if str(feat['a_i_num']) in self.list_of_num:
                feat['prot_categ'] = ', '.join(
                    self.categories_and_num_dictionery[(str(feat['a_i_num']))])
                self.selected_layer.updateFeature(feat)
            for field in self.selected_layer.fields():
                if feat[field.name()] == NULL:
                    if field.typeName() == "String":
                        feat[field.name()] = "BRAK"
                    if (field.typeName() == "Integer64") or (field.typeName() == "Integer"):
                        feat[field.name()] = 0
                    if field.typeName() == "Real":
                        feat[field.name()] = 0.0
                    self.selected_layer.updateFeature(feat)
            self.progress.emit(
                (i+1)*(100/self.selected_layer.featureCount()))
        self.selected_layer.commitChanges()
        self.finished.emit()
