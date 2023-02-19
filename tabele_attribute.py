from PyQt5.QtWidgets import QHBoxLayout, QTableView
from PyQt5.QtCore import QEventLoop
from qgis.gui import QgsAttributeTableModel, QgsAttributeTableFilterModel
from qgis.core import QgsVectorLayerCache

from open_dialog import OpenDialog


class TabeleAttribute():
    """Creating tabele attributes class.
    """

    def __init__(self, selected_layer, actionShowTabeleAttribute, actionIdentify, map, deleteLayerBtn):
        """Constructor.
        """
        self.selected_layer = selected_layer
        self.actionShowTabeleAttribute = actionShowTabeleAttribute
        self.deleteLayerBtn = deleteLayerBtn
        self.actionIdentify = actionIdentify
        self.map = map
        self.list_of_feature = []
        self.table_view = QTableView()
        self.attribute_table_filter_model = None

    def create_tabele(self):
        """Creates tabele of vector layer attributes.
        """
        self.selected_layer.getFeatures()
        vector_layer_cache = QgsVectorLayerCache(self.selected_layer, 10000)
        attribute_table_model = QgsAttributeTableModel(vector_layer_cache)
        attribute_table_model.loadLayer()
        self.attribute_table_filter_model = QgsAttributeTableFilterModel(
            self.map, attribute_table_model)
        self.table_view.setModel(self.attribute_table_filter_model)
        self.table_view.resizeColumnsToContents()
        selection_model = self.table_view.selectionModel()
        selection_model.selectionChanged.connect(self.changeSelectionEvent)
        dlg = OpenDialog("Tabela właściwości wydzieleń",
                         ':/images/openTabele.png', self.selected_layer, False, False,  self.deleteLayerBtn, self.actionShowTabeleAttribute, self.actionIdentify)
        dlg.resize(800, 800)
        layout = QHBoxLayout()
        layout.addWidget(self.table_view)
        dlg.setLayout(layout)
        dlg.setModal(False)
        dlg.show()
        loop = QEventLoop()
        loop.exec_()

    def changeSelectionEvent(self):
        """Changes selection of features in tabele of attribute.
        """
        self.list_of_feature.clear()
        self.list_of_feature = [self.attribute_table_filter_model.rowToId(
            rowID) for rowID in self.table_view.selectedIndexes()]
        if len(self.list_of_feature) != 0:
            self.selected_layer.selectByIds(self.list_of_feature)
