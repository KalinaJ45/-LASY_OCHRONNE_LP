
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout
from qgis.gui import QgsMapToolIdentify

from GIS_dialog import GISDialog


class CustomSelectTool(QgsMapToolIdentify):
    """Custom tool map class.
    """

    def __init__(self, canvas, selected_layer, list_of_fields):
        """Constructor.
        """
        QgsMapToolIdentify.__init__(self, canvas)
        self.selected_layer = selected_layer
        self.list_of_fields = list_of_fields

    def canvasReleaseEvent(self, event):
        """Create tabele of subarea properties.

        Args:
            event (QgsMapMouseEvent): specific mouseEvent.
        """
        dlg = GISDialog("Własciwosci wydzielenia",
                        ':/images/info.png', self.selected_layer, False, True)
        found_features = self.identify(
            event.x(), event.y(), self.TopDownStopAtFirst, self.VectorLayer)
        if len(found_features) > 0:
            feature = found_features[0].mFeature
            self.selected_layer.selectByIds([feature.id()])
            layout = QHBoxLayout()
            table_widget = QtWidgets.QTableWidget()
            table_widget.setObjectName("table_widget")
            table_widget.setColumnCount(2)
            table_widget.setRowCount(len(self.list_of_fields))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            table_widget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(font)
            table_widget.setHorizontalHeaderItem(1, item)
            item = table_widget.horizontalHeaderItem(0)
            item.setText("Właściwość")
            item = table_widget.horizontalHeaderItem(1)
            item.setText("Wartość")
            for field in self.list_of_fields:
                attribute = feature.attribute(field)
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                table_widget.setItem(
                    self.list_of_fields.index(field), 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                table_widget.setItem(
                    self.list_of_fields.index(field), 1, item)
                item = table_widget.item(
                    self.list_of_fields.index(field), 0)
                item.setText(str(field))
                item = table_widget.item(
                    self.list_of_fields.index(field), 1)
                item.setText(str(attribute))
            table_widget.setSizeAdjustPolicy(
                QtWidgets.QAbstractScrollArea.AdjustToContents)
            table_widget.resizeColumnsToContents()
            layout.addWidget(table_widget)
            dlg.setLayout(layout)
            dlg.exec_()
