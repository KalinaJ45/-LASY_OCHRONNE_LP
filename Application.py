# -*- coding: utf-8 -*-

import os
from os import path
from pathlib import Path
import sys
import tempfile
from osgeo import gdal

from PyQt5.QtCore import QThread, Qt
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPainter, QImage, QPagedPaintDevice, QPageLayout
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QColorDialog, QMainWindow
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from qgis.core import *
from qgis.gui import *
from qgis.gui import QgsMapTool, QgsMapToolPan, QgsMapToolZoom

from Application_UI import Ui_MainWindow
from category_kind import CategoryKindEnum
from field_kind import FieldKindEnum
from create_image import CreateImage
from map_tool import CustomSelectTool
from worker import Worker
from tabele_attribute import TabeleAttribute
from tabele_attriute_to_excel import TabeleToExcel
from raport import GeneratedRaport
from prepare_data import PrepareData
from save_xlsx import SaveXLSX

gdal.PushErrorHandler('CPLQuietErrorHandler')
QtGui.QImageWriter.supportedImageFormats()

QGIS_PATH = r'C:\Program Files\QGIS 3.22.6\apps\qgis-ltr'
sys.path.append(os.path.join(QGIS_PATH, 'python'))
os.environ['PATH'] = '{};{};{}'.format(os.path.join(
    QGIS_PATH, 'bin'), os.path.join(QGIS_PATH, '../Qt5/bin'), os.environ['PATH'])
os.environ['QT_PLUGIN_PATH'] = '{};{}'.format(os.path.join(
    QGIS_PATH, 'qtplugins'), os.path.join(QGIS_PATH, '../Qt5/plugins'))
os.environ['QGIS_PREFIX_PATH'] = QGIS_PATH

QgsApplication.setPrefixPath(QGIS_PATH, True)


class Window(QMainWindow, Ui_MainWindow):
    """The main application class that inherits from classes: MainWindow (QMainWindow)and Ui_MainWindow (imported class of application UI).
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.setupUi(self)
        self.window = QtWidgets.QMainWindow()
        self.qgisInstance = QgsProject.instance()
        self.selected_layer = ''
        self.list_of_protected_subarea = []
        self.list_of_unprotected_subarea = []

        self.window.setWindowIcon(QtGui.QIcon(":/images/leaf.ico"))

        self.actionNewProject.triggered.connect(self.create_new_project)
        self.actionSaveImage.triggered.connect(self.save_image)
        self.actionPrintImage.triggered.connect(self.print_image)
        self.actionPan.triggered.connect(self.pan)
        self.actionZoomIn.triggered.connect(self.zoom_in)
        self.actionZoomOut.triggered.connect(self.zoom_out)
        self.actionZoomExtent.triggered.connect(self.zoom_extent)
        self.actionIdentify.triggered.connect(self.identify)
        self.actionShowTabeleAttribute.triggered.connect(
            self.open_tabele_attribute)
        self.actionExportTabeleAttribute.triggered.connect(
            self.save_tabele_attribute_to_excel)
        self.actionHelp.triggered.connect(self.help)
        self.loadLayerBtn.clicked.connect(self.load_data)
        self.deleteLayerBtn.clicked.connect(self.reset_data)
        self.selectBtn.clicked.connect(self.select_protected_subarea)
        self.unselectBtn.clicked.connect(self.unselect_protected_subarea)
        self.generateRaportBtn.clicked.connect(self.generate_raport)
        self.colorFillSelectedSubareaBtn.colorChanged.connect(self.set_symbol)
        self.colorBorderSelectedSubareaBtn.colorChanged.connect(
            self.set_symbol)
        self.colorFillOtherSubareaBtn.colorChanged.connect(self.set_symbol)
        self.colorBorderOtherSubareaBtn.colorChanged.connect(self.set_symbol)
        self.colorBackgroundBtn.colorChanged.connect(
            self.set_backgroud_map_color)
        self.colorFillSelectedSubareaBtn.clicked.connect(
            lambda: self.set_color_button(self.colorFillSelectedSubareaBtn))
        self.colorBorderSelectedSubareaBtn.clicked.connect(
            (lambda: self.set_color_button(self.colorBorderSelectedSubareaBtn)))
        self.colorFillOtherSubareaBtn.clicked.connect(
            (lambda: self.set_color_button(self.colorFillOtherSubareaBtn)))
        self.colorBorderOtherSubareaBtn.clicked.connect(
            lambda: self.set_color_button(self.colorBorderOtherSubareaBtn))
        self.colorBackgroundBtn.clicked.connect(
            lambda: self.set_color_button(self.colorBackgroundBtn))

    def create_new_project(self):
        """Creates new project: reset data, set deafult states of widgets, deafult colors of buttons and color of map background.
        """
        self. reset_data()
        self.set_deafult_states_of_widgets()
        self.set_deafult_buttons_colors()
        self.set_backgroud_map_color()

    def save_image(self):
        """Saves image in selected path. In the event of a problem, an message appears.
        """
        try:
            image_types = "jpg (*.jpg);;bitmap (*.bmp);;tiff (*.tiff)"
            options = QFileDialog.Options()
            file_name = QFileDialog.getSaveFileName(
                self.window, "Zapisz jako obraz...", "", filter=image_types, options=options)
            if file_name[0]:
                CreateImage().create_image(self.selected_layer,
                                           self.colorBackgroundBtn.color(), file_name[0])
                QMessageBox.information(
                    self.window, "Sukces", "Zapisywanie obrazu zakończone sukcesem!")
        except:
            msg = QMessageBox.critical(
                self.window, "Spróbuj jeszcze raz", "Problem z zapisywaniem obrazu!")

    def print_image(self):
        """"Opens print dialog box.
        """
        try:
            tempdir = tempfile.TemporaryDirectory()
            path = tempdir.name + '\\' + 'image.jpg'
            self.map.saveAsImage(path)
            printer = QPrinter(QPrinter.HighResolution)
            printer.setResolution(600)
            printer.setFullPage(True)
            printer.setPageSize(QPagedPaintDevice.A4)
            printer.setPageOrientation(QPageLayout.Landscape)
            printer.setPageMargins(0, 280, 0, 280, QPrinter.DevicePixel)
            dialog = QPrintDialog(printer)
            if dialog.exec_() == QPrintDialog.Accepted:
                image = QImage(path)
                image = image.scaledToWidth(
                    printer.pageRect().width(), Qt.SmoothTransformation)
                painter = QPainter()
                painter.begin(printer)
                painter.drawImage(0, 0, image)
                painter.end()
        except:
            msg = QMessageBox.critical(
                self.window, "Spróbuj jeszcze raz", "Problem z wydrukiem obrazu!")

    def pan(self) -> None:
        """Turns on Pan tool.
        """
        self.toolPan = QgsMapToolPan(self.map)
        self.toolPan.setAction(self.actionPan)
        self.map.setMapTool(self.toolPan)

    def zoom_in(self):
        """Turns on Zoom In tool.
        """
        self.toolZoomIn = QgsMapToolZoom(self.map, False)  # false = in
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.map.setMapTool(self.toolZoomIn)

    def zoom_out(self):
        """Turns on Zoom Out tool.
        """
        self.toolZoomOut = QgsMapToolZoom(self.map, True)  # true = out
        self.toolZoomOut.setAction(self.actionZoomOut)
        self.map.setMapTool(self.toolZoomOut)

    def zoom_extent(self):
        """Zoom to selected layer extent.
        """
        self.map.setExtent(self.selected_layer.extent())
        self.map.refresh()

    def identify(self):
        """Turns on map tool for identifying features in selected layer.
        """
        self.toolInfo = CustomSelectTool(
            self.map, self.selected_layer, self.create_list_of_fields_aliases())
        self.toolInfo.setAction(self.actionIdentify)
        self.map.setMapTool(self.toolInfo)

    def open_tabele_attribute(self):
        """Opens a seceond window with tabele of selected layer attributes.
        """
        self.pan()
        tabele_attribute = TabeleAttribute(
            self.selected_layer, self.actionShowTabeleAttribute, self.actionIdentify, self.map, self.deleteLayerBtn)
        tabele_attribute.create_tabele()

    def save_tabele_attribute_to_excel(self):
        """saves the tabele of selected layer attributes as a excel file in selected path. In the event of a problem, an message appear.
        """
        file_name = SaveXLSX().save_xlsx(self.window)
        try:
            if file_name:
                save_tabele = TabeleToExcel()
                save_tabele.create_tabele(
                    self.selected_layer, file_name, self.create_list_of_fields_aliases())
                QMessageBox.information(
                    self.window, "Sukces", "Zapisywanie tabeli atrybutów zakończone sukcesem!")
        except:
            msg = QMessageBox.critical(
                self.window, "Spróbuj jeszcze raz", "Problem z zapisywaniem tabeli atrybutów!")

    def help(self):
        """Opens user manual in pdf file.
        """
        filepath = Path(__file__).parent / "Instrukcja_uzytkownika.pdf"
        os.startfile(filepath)

    def load_data(self):
        """Loads selected data to application - start the worker thread.
        """
        data = PrepareData()
        if data.get_selected_data():
            if data.get_data_correctness():
                self.set_widget_visability({self.progressBar: True})
                self.progressBar.setValue(0)
                self.selected_layer = data.get_selected_layer()
                categories_and_num_dictionery = data.get_categories_and_num_dictionery()
                list_of_num = data.get_list_of_num()
                self.thread = QThread()
                self.worker = Worker(self.selected_layer,
                                     categories_and_num_dictionery, list_of_num)
                self.thread.started.connect(self.worker.run)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker.progress.connect(self.report_progress)
                self.thread.start()
                self.thread.finished.connect(lambda: self.finish_worker())
            else:
                msg = QMessageBox.critical(
                    self.window, "Sprawdź poprawność danych", "Problem z ładowaniem danych!")

    def report_progress(self, n):
        """Method to report the progress to gui.

        Args:
            n (int): step.
        """
        self.progressBar.setValue(n)

    def finish_worker(self):
        """Does when worker is finish.
        """
        self.qgisInstance.addMapLayers([self.selected_layer])
        self.map.setExtent(self.selected_layer.extent())
        self.map.setLayers([self.selected_layer])
        self.set_enabled_of_widget({self.menuProject: True, self.actionNewProject: True, self.menuOptions: True, self.actionSaveImage: True, self.actionPrintImage: True, self.actionPan: True, self.actionZoomIn: True, self.actionZoomOut: True,
                                   self.actionZoomExtent: True,  self.actionIdentify: True, self.actionShowTabeleAttribute: True, self.actionExportTabeleAttribute: True, self.deleteLayerBtn: True, self.loadLayerBtn: False,
                                   self.categoriesComboBox: True, self.selectProtectedForstsGroupBox: True, self.generateRaportGroupBox: True, self.coordinates_label: True,  self.showXY_label: True, })
        self.set_widget_visability({self.progressBar: False})
        self.add_deafult_style_of_layer()
        self. set_field_alias(self.selected_layer)
        self.map.xyCoordinates.connect(self.show_XY)
        self.pan()
        self.load_list_category()

    def create_list_of_fields_aliases(self) -> list:
        """Create list of selected layer's (shapefile) fields aliases from class FieldKindEnum.

        Returns:
            list: created list of selected layer's fields aliases (list of strings).
        """
        list_of_fields_aliases = [
            field.value.alias_field for field in FieldKindEnum]
        return list_of_fields_aliases

    def set_field_alias(self, layer):
        """Sets aliases for fields of selected layer (shapefile) from class FieldKindEnum.

        Args:
            layer (QgsVectorLayer): selected data with subareas of specified forest district.
        """
        for field in FieldKindEnum:
            layer.setFieldAlias(field.value.index, field.value.alias_field)

    def add_deafult_style_of_layer(self):
        """Adds deafult style of selected layer (shapefile): creates symbol and refreshes canvas.
        """
        selected_layer_symbol = self.create_symbol('#ffffff', '#a2a2a2')
        renderer = QgsSingleSymbolRenderer(selected_layer_symbol)
        self.selected_layer.setRenderer(renderer)
        self.map.refresh()

    def set_deafult_buttons_colors(self):
        """Sets deafult colors of buttons.
        """
        self.set_buttons_color({self.colorBackgroundBtn: (255, 255, 255), self.colorFillSelectedSubareaBtn: (74, 149, 51), self.colorBorderSelectedSubareaBtn: (
            0, 0, 0), self.colorFillOtherSubareaBtn: (255, 255, 255),  self.colorBorderOtherSubareaBtn: (162, 162, 162)})

    def set_deafult_states_of_widgets(self):
        """Sets deafult states of widgets: enabled or not, their visability, text, current index.
        """
        self.set_enabled_of_widget({self.menuProject: False, self.actionNewProject: False, self.menuOptions: False, self.actionSaveImage: False, self.actionPrintImage: False, self.actionPan: False, self.actionZoomIn: False, self.actionZoomOut: False,
                                   self.actionZoomExtent: False,  self.actionIdentify: False, self.actionShowTabeleAttribute: False, self.actionExportTabeleAttribute: False, self.loadLayerBtn: True, self.deleteLayerBtn: False,
                                    self.selectProtectedForstsGroupBox: False, self.selectBtn: True,  self.unselectBtn: False, self.giveStyleGroupBox: False, self.generateRaportGroupBox: False, self.coordinates_label: False,  self.showXY_label: False})
        self.set_widget_visability(
            {self.progressBar: False})
        self.set_label_text(
            {self.showXY_label: '', self.number_of_selected_subarea_label: '', self.sum_of_area_label: ''})
        self.categoriesComboBox.setCurrentIndex(-1)

    def set_enabled_of_widget(self, enabled_of_widets):
        """Sets if widgets is enabled or not.

        Args:
            enabled_of_widets (dict): dictionary in which the keys are widgets (QtWidgets) and the values are True or False (bool), depending on whether the widget  should be enabled or not.
        """
        for widget in enabled_of_widets:
            widget.setEnabled(enabled_of_widets[widget])

    def set_widget_visability(self, widget_visability):
        """Sets visabilit of widgets.

        Args:
            widget_visability (dict): dictionary in which the keys are widgets (QtWidgets) and the values are True or False (bool), depending on their visability.
        """
        for widget in widget_visability:
            widget.setVisible(widget_visability[widget])

    def set_label_text(self, label_text):
        """Sets texts of labels.

        Args:
            label_text (dict): dictionary in which the keys are labels (QLineEdit) and the values are their texts (str).
        """
        for label in label_text:
            label.setText(label_text[label])

    def create_symbol(self, color_fill, color_border) -> QgsFillSymbol:
        """Create single symbol for selected layer (shapefile) and returns it.

        Args:
            color_fill (str): fill color for features of selected layer in RGB format.
            color_border (str): border color for features of selected layer in RGB format.
        Returns:
            QgsFillSymbol: single symbol for selected layer
        """
        symbol = QgsFillSymbol.createSimple(
            {'color': color_fill, 'color_border': color_border})
        return symbol

    def set_backgroud_map_color(self):
        """Sets color of canvas background and refreshes canvas.
        """
        self.map.setCanvasColor(self.colorBackgroundBtn.color())
        self.map.refresh()

    def set_color_button(self, button):
        """Sets color of selected button and refreshes canvas.

        Args:
            button (QgsColorButton): selected button
        """
        button.setColor(QColorDialog.getColor(
            options=QColorDialog.ShowAlphaChannel))
        self.map.refresh()

    def set_symbol(self):
        """Sets single symbols for selected and unselected layer features and creates renderer categories.
        """
        symbol_of_selected_subarea = self.create_symbol(
            ','.join([str(value) for value in self.colorFillSelectedSubareaBtn.color().getRgb()]), ','.join([str(value) for value in self.colorBorderSelectedSubareaBtn.color().getRgb()]))
        symbol_of_unselected_subarea = self.create_symbol(
            ','.join([str(value) for value in self.colorFillOtherSubareaBtn.color().getRgb()]), ','.join([str(value) for value in self.colorBorderOtherSubareaBtn.color().getRgb()]))
        categories = [QgsRendererCategory([val for val in self.list_of_protected_subarea], symbol_of_selected_subarea, "Wybrane wydzielenia ochronne - \n{}".format(self.categoriesComboBox.currentText())),
                      QgsRendererCategory([val for val in self.list_of_unprotected_subarea], symbol_of_unselected_subarea, 'Pozostałe wydzielenia')]
        renderer = QgsCategorizedSymbolRenderer(
            'KATEGORIE OCHRONNOŚCI', categories)
        self.selected_layer.setRenderer(renderer)
        self.map.refresh()

    def select_protected_subarea(self):
        """Selects forest subareas (features) of with a specific protection category and displays in the status bar: number of selected subareas, total number of all subareas and sum of selected area. 
        If no protection category has been selected, a message is displayed.
        """
        if self.categoriesComboBox.currentIndex() != -1:
            categories_dictionary = self.create_categories_dictionary()
            list_of_area = []
            for category in categories_dictionary.keys():
                if category == self.categoriesComboBox.currentText():
                    for feat in self.selected_layer.getFeatures():
                        if str(categories_dictionary[category]) in str(feat["KATEGORIE OCHRONNOŚCI"]):
                            self.list_of_protected_subarea.append(
                                feat["KATEGORIE OCHRONNOŚCI"])
                            list_of_area.append(feat["POWIERZCHNIA (ha)"])
                        else:
                            self.list_of_unprotected_subarea.append(
                                feat["KATEGORIE OCHRONNOŚCI"])
            number_of_selected_subareas = len(self.list_of_protected_subarea)
            sum_of_selected_area = round(sum(list_of_area), 2)
            number_of_all_subareas = self.selected_layer.featureCount()
            self.set_label_text({self.number_of_selected_subarea_label: f"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Wybrano {number_of_selected_subareas} wydzieleń lasów ochronnych z {number_of_all_subareas} wszystkich wydzieleń</span></p></body></html>",
                                self.sum_of_area_label: f"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Powierzchnia zaznaczonych lasów ochronnych: {sum_of_selected_area} ha</span></p></body></html>"})
            self.set_symbol()
            self.map.refresh()
            self.set_enabled_of_widget(
                {self.selectBtn: False, self.unselectBtn: True, self.categoriesComboBox: False, self.giveStyleGroupBox: True})
        else:
            msg = QMessageBox.critical(
                self.window, "Wybierz kategorię ochronności", "Nie wybrano kategorii ochronności!")

    def unselect_protected_subarea(self):
        """Unselects all features of selected layer and adds it deafult style.
        """
        self.list_of_protected_subarea = []
        self.list_of_unprotected_subarea = []
        self.categoriesComboBox.setCurrentIndex(-1)
        self.set_label_text(
            {self.number_of_selected_subarea_label: '', self.sum_of_area_label: ''})
        self.add_deafult_style_of_layer()
        self.map.refresh()
        self.set_enabled_of_widget(
            {self.selectBtn: True, self.unselectBtn: False, self.categoriesComboBox: True, self.giveStyleGroupBox: False})

    def load_list_category(self):
        """Adds list of protection categories from class CategoryKindEnum to combo box and set it on position -1.
        """
        self.categoriesComboBox.addItems(
            [object.value.category for object in CategoryKindEnum])
        self.categoriesComboBox.setCurrentIndex(-1)

    def create_categories_dictionary(self) -> dict:
        """Creates dictionary in which the keys are protection categories (str) and the values are their codes (str) from class CategoryKindEnum.
        Returns:
            dict: created dictionary of protection categories and their codes
        """
        categories_dictionary = dict(zip([object.value.category for object in CategoryKindEnum], [
            object.value.code for object in CategoryKindEnum]))
        return categories_dictionary

    def reset_data(self):
        """Reset data: remove layer, clear lists of protected and unprotected subarea, sets deafult states of widgets, refreshes canvas and stops emitting of current mouse position.
        """
        self.list_of_protected_subarea = []
        self.list_of_unprotected_subarea = []
        self.qgisInstance.removeAllMapLayers()
        self.set_deafult_states_of_widgets()
        self.map.refresh()
        self.map.xyCoordinates.disconnect()

    def set_buttons_color(self, button_color):
        """Sets buttons colors

        Args:
            button_color (dict): a dictionary in which the keys are the buttons (and the values are their colors in RGB format (str).
        """
        for button in button_color:
            button.setColor(QColor(*button_color[button]))

    def show_XY(self):
        """Gets last position of mouse cursor, transforms from screen coordinates to layers coordinates and shows they in lebel on status bar (witdh of thie lebel matches the content).
        """
        tool = QgsMapTool(self.map)
        point = tool.toLayerCoordinates(
            self.selected_layer, self.map.mouseLastXY())
        coords = "  X: " + str(point.x()) + " / Y: " + str(point.y())
        self.showXY_label.setText(coords)
        fm = self.showXY_label.fontMetrics()
        w = fm.boundingRect(coords).width()
        self.showXY_label.setFixedWidth(w)

    def open_window(self):
        """Set deafult states of widgets and deafult when main window of aplication is openining.
        """
        self.set_deafult_states_of_widgets()
        self.set_deafult_buttons_colors()

    def generate_raport(self):
        """Generates raport and saves it as a excel file in selected path. In the event of a problem, an message appear.
        """
        try:
            file_name = SaveXLSX().save_xlsx(self.window)
            if file_name:
                generate_raport = GeneratedRaport()
                generate_raport.create_tabele(
                    self.selected_layer, file_name, self.create_categories_dictionary())
                QMessageBox.information(
                    self.window, "Sukces", "Generowanie raportu zakonczone sukcesem!")
        except:
            msg = QMessageBox.critical(
                self.window, "Spróbuj jeszcze raz", "Problem z wygenerowaniem raportu!")


def main():
    """Main application function
    """
    import sys
    app = QgsApplication([], True)
    app.initQgis()
    MainWindow = Window()
    MainWindow.open_window()
    MainWindow.showMaximized()
    sys.exit(app.exec_())
    app.exitQgis()


if __name__ == "__main__":
    main()
