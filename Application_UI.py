# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from qgis.gui import QgsColorButton, QgsMapCanvas

import resources_rc


class Ui_MainWindow(object):
    """Class of application interface that inherits from class object.
    """

    def setupUi(self, MainWindow):
        """Setup the interface of application.

        Args:
            MainWindow (QMainWindow): class of  application main window.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 593)
        MainWindow.setWindowTitle("LASY OCHRONNE")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/leaf.ico"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setTitle("Projekt")
        self.menuProject.setObjectName("menuProject")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setTitle("Opcje")
        self.menuOptions.setObjectName("menuOptions")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTitle("Pomoc")
        self.menuHelp.setObjectName("menuHelp")

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionNewProject = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/document.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewProject.setIcon(icon2)
        self.actionNewProject.setObjectName("actionNowy_projekt")
        self.actionNewProject.setText("Nowy projekt")

        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveImage.setIcon(icon3)
        self.actionSaveImage.setObjectName("actionZapisz_jako_obraz")
        self.actionSaveImage.setText("Zapisz jako obraz")

        self.actionPrintImage = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/print.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrintImage.setIcon(icon4)
        self.actionPrintImage.setObjectName("actionPrintImage")
        self.actionPrintImage.setText("Drukuj obraz")

        self.actionPan = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/pan.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon5)
        self.actionPan.setObjectName("PAN")
        self.actionPan.setCheckable(True)
        self.actionPan.setText("Przesuń")

        self.actionZoomIn = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/zoom_in.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon6)
        self.actionZoomIn.setObjectName("ZoomIn")
        self.actionZoomIn.setCheckable(True)
        self.actionZoomIn.setText("Powiększ")

        self.actionZoomOut = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/zoom_out.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon7)
        self.actionZoomOut.setObjectName("ZoomOut")
        self.actionZoomOut.setCheckable(True)
        self.actionZoomOut.setText("Pomniejsz")

        self.actionZoomExtent = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/zoom_full.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomExtent.setIcon(icon8)
        self.actionZoomExtent.setObjectName("actionZoomExtent")
        self.actionZoomExtent.setText("Cały zasięg")

        self.actionIdentify = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/identify.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIdentify.setIcon(icon9)
        self.actionIdentify.setObjectName("Identify")
        self.actionIdentify.setCheckable(True)
        self.actionIdentify.setText("Pokaż właściwości wydzielenia")

        self.actionShowTabeleAttribute = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/openTabele.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowTabeleAttribute.setIcon(icon10)
        self.actionShowTabeleAttribute.setObjectName(
            "actionShowTabeleAttribute")
        self.actionShowTabeleAttribute.setText(
            "Pokaż tabelę właściwości wydzieleń")

        self.actionExportTabeleAttribute = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/exportToExcel.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportTabeleAttribute.setIcon(icon11)
        self.actionExportTabeleAttribute.setObjectName(
            "actionExportTabeleAttribute")
        self.actionExportTabeleAttribute.setText(
            "Eksportuj tabelę własciwości wydzieleń do pliku Excel")

        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/help.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon12)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setText("Podręcznik Użytkownika")

        self.menuProject.addAction(self.actionNewProject)
        self.menuProject.addAction(self.actionSaveImage)
        self.menuProject.addAction(self.actionPrintImage)

        self.menuOptions.addAction(self.actionIdentify)
        self.menuOptions.addAction(self.actionShowTabeleAttribute)
        self.menuOptions.addAction(self.actionExportTabeleAttribute)

        self.menuHelp.addAction(self.actionHelp)

        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.toolBar.addAction(self.actionNewProject)
        self.toolBar.addAction(self.actionSaveImage)
        self.toolBar.addAction(self.actionPrintImage)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionZoomExtent)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionIdentify)
        self.toolBar.addAction(self.actionShowTabeleAttribute)
        self.toolBar.addAction(self.actionExportTabeleAttribute)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)

        self.loadDataGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.loadDataGroupBox.setGeometry(QtCore.QRect(20, 20, 550, 120))
        self.loadDataGroupBox.setObjectName("loadDataGroupBox")
        self.loadDataGroupBox.setTitle("Wczytaj dane")

        self.loadLayerBtn = QtWidgets.QPushButton(self.loadDataGroupBox)
        self.loadLayerBtn.setGeometry(QtCore.QRect(30, 30,  235, 70))
        self.loadLayerBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/load.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadLayerBtn.setIcon(icon13)
        self.loadLayerBtn.setIconSize(QtCore.QSize(750, 55))
        self.loadLayerBtn.setObjectName("loadLayerBtn")

        self.deleteLayerBtn = QtWidgets.QPushButton(self.loadDataGroupBox)
        self.deleteLayerBtn.setGeometry(QtCore.QRect(285, 30, 235, 70))
        self.deleteLayerBtn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/reset.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteLayerBtn.setIcon(icon14)
        self.deleteLayerBtn.setIconSize(QtCore.QSize(750, 55))
        self.deleteLayerBtn.setObjectName("delateLayerBtn")

        self.selectProtectedForstsGroupBox = QtWidgets.QGroupBox(
            self.centralwidget)
        self.selectProtectedForstsGroupBox.setGeometry(
            QtCore.QRect(20, 155, 550, 111))
        self.selectProtectedForstsGroupBox.setObjectName(
            "selectProtectedForstsGroupBox")
        self.selectProtectedForstsGroupBox.setTitle("Zaznacz lasy ochronne")
        self.selectProtectedForstsGroupBox.setEnabled(True)
        self.categoriesComboBox = QtWidgets.QComboBox(
            self.selectProtectedForstsGroupBox)
        self.categoriesComboBox.setGeometry(QtCore.QRect(30, 40, 220, 41))
        self.categoriesComboBox.setObjectName("categoriesComboBox")
        font = QtGui.QFont()
        font.setPointSize(7)
        self.categoriesComboBox.setFont(font)

        self.selectBtn = QtWidgets.QPushButton(
            self.selectProtectedForstsGroupBox)
        self.selectBtn.setGeometry(QtCore.QRect(270, 40, 121, 41))
        self.selectBtn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/select.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectBtn.setIcon(icon15)
        self.selectBtn.setIconSize(QtCore.QSize(110, 50))
        self.selectBtn.setObjectName("selectBtn")

        self.unselectBtn = QtWidgets.QPushButton(
            self.selectProtectedForstsGroupBox)
        self.unselectBtn.setGeometry(QtCore.QRect(400, 40, 121, 41))
        self.unselectBtn.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/unselect.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unselectBtn.setIcon(icon16)
        self.unselectBtn.setIconSize(QtCore.QSize(110, 50))
        self.unselectBtn.setObjectName("unselectBtn")

        self.giveStyleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.giveStyleGroupBox.setGeometry(QtCore.QRect(20, 295, 550, 380))
        self.giveStyleGroupBox.setObjectName("giveStyleBox")
        self.giveStyleGroupBox.setTitle("Nadaj styl")

        self.colorBackgroundBtn = QgsColorButton()
        self.colorBackgroundBtn.setObjectName("colorBackgroundBtn")
        self.colorBackgroundBtn.setColor(QColor(255, 255, 255))
        self.colorBackgroundBtn.setAllowOpacity(True)
        self.colorBackgroundBtn.setBehavior(QgsColorButton.SignalOnly)
        self.colorBackgroundBtn.setShowNoColor(True)

        self.colorFillSelectedSubareaBtn = QgsColorButton()
        self.colorFillSelectedSubareaBtn.setObjectName(
            "colorFillSelectedSubareaBtn")
        self.colorFillSelectedSubareaBtn.setColor(QColor(74, 149, 51))
        self.colorFillSelectedSubareaBtn.setAllowOpacity(True)
        self.colorFillSelectedSubareaBtn.setBehavior(QgsColorButton.SignalOnly)
        self.colorFillSelectedSubareaBtn.setShowNoColor(True)

        self.colorBorderSelectedSubareaBtn = QgsColorButton()
        self.colorBorderSelectedSubareaBtn.setObjectName(
            "colorBorderSelectedSubareaBtn")
        self.colorBorderSelectedSubareaBtn.setColor(QColor(0, 0, 0))
        self.colorBorderSelectedSubareaBtn.setAllowOpacity(True)
        self.colorBorderSelectedSubareaBtn.setBehavior(
            QgsColorButton.SignalOnly)
        self.colorBorderSelectedSubareaBtn.setShowNoColor(True)

        self.colorFillOtherSubareaBtn = QgsColorButton()
        self.colorFillOtherSubareaBtn.setObjectName("colorFillOtherSubareaBtn")
        self.colorFillOtherSubareaBtn.setColor(QColor(255, 255, 255))
        self.colorFillOtherSubareaBtn.setAllowOpacity(True)
        self.colorFillOtherSubareaBtn.setBehavior(QgsColorButton.SignalOnly)
        self.colorFillOtherSubareaBtn.setShowNoColor(True)

        self.colorBorderOtherSubareaBtn = QgsColorButton()
        self.colorBorderOtherSubareaBtn.setObjectName(
            "colorBorderOtherSubareaBtn")
        self.colorBorderOtherSubareaBtn.setColor(QColor(162, 162, 162))
        self.colorBorderOtherSubareaBtn.setAllowOpacity(True)
        self.colorBorderOtherSubareaBtn.setBehavior(QgsColorButton.SignalOnly)
        self.colorBorderOtherSubareaBtn.setShowNoColor(True)

        self.treeWidget = QtWidgets.QTreeWidget(self.giveStyleGroupBox)
        self.treeWidget.setGeometry(QtCore.QRect(30, 60, 490, 265))
        self.treeWidget.setObjectName("treeWidget")

        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setHeaderHidden(True)

        self.treeWidget.header().resizeSection(0, 250)

        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setExpanded(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.setItemWidget(item_1, 1, self.colorBackgroundBtn)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setExpanded(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.setItemWidget(
            item_1, 1, self.colorFillSelectedSubareaBtn)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.setItemWidget(
            item_1, 1, self.colorBorderSelectedSubareaBtn)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setExpanded(True)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.setItemWidget(item_1, 1, self.colorFillOtherSubareaBtn)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.setItemWidget(
            item_1, 1, self.colorBorderOtherSubareaBtn)

        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setHeaderHidden(True)

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0,  "1")
        self.treeWidget.headerItem().setText(1, "2")

        self.treeWidget.topLevelItem(0).setText(0, "MAPA")
        self.treeWidget.topLevelItem(0).child(
            0).setText(0,  "Kolor tła wydruku")
        self.treeWidget.topLevelItem(1).setText(0,  "LASY OCHRONNE")
        self.treeWidget.topLevelItem(1).child(
            0).setText(0, "Kolor wypełnienia")
        self.treeWidget.topLevelItem(1).child(1).setText(0,  "Kolor konturu")
        self.treeWidget.topLevelItem(2).setText(0, "LASY POZOSTAŁE")
        self.treeWidget.topLevelItem(2).child(
            0).setText(0,  "Kolor wypełnienia")
        self.treeWidget.topLevelItem(2).child(1).setText(0,  "Kolor konturu")

        self.generateRaportGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.generateRaportGroupBox.setGeometry(
            QtCore.QRect(20, 700, 550, 141))
        self.generateRaportGroupBox.setObjectName("generateRaportGroupBox")
        self.generateRaportGroupBox.setTitle("Generuj raport")
        self.generateRaportBtn = QtWidgets.QPushButton(
            self.generateRaportGroupBox)
        self.generateRaportBtn.setGeometry(QtCore.QRect(115, 40, 320, 70))
        self.generateRaportBtn.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/raport.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateRaportBtn.setIcon(icon17)
        self.generateRaportBtn.setIconSize(QtCore.QSize(750, 55))
        self.generateRaportBtn.setObjectName("generateRaportBtn")

        statusbar = QtWidgets.QStatusBar(MainWindow)
        statusbar.setGeometry(QtCore.QRect(0, 935, 1900, 60))
        statusbar.setObjectName("statusbar")

        self.coordinates_label = QtWidgets.QLabel(statusbar)
        self.coordinates_label.setGeometry(QtCore.QRect(50, 10, 250, 25))
        self.coordinates_label.setObjectName("coordinates_label")
        self.coordinates_label.setText(
            "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">WSPÓŁRZĘDNE:</span></p></body></html>")

        self.showXY_label = QtWidgets.QLineEdit(statusbar)
        self.showXY_label.setGeometry(QtCore.QRect(200, 10, 300, 25))
        self.showXY_label.setReadOnly(True)
        self.showXY_label.setObjectName("showXY_label")

        self.number_of_selected_subarea_label = QtWidgets.QLabel(statusbar)
        self.number_of_selected_subarea_label.setGeometry(
            QtCore.QRect(680, 10, 620, 25))
        self.number_of_selected_subarea_label.setObjectName(
            "number_of_selected_subarea_label ")

        self.sum_of_area_label = QtWidgets.QLabel(statusbar)
        self.sum_of_area_label.setGeometry(
            QtCore.QRect(1350, 10, 550, 25))
        self.sum_of_area_label.setObjectName("sum_of_area_label")

        self.progressBar = QtWidgets.QProgressBar(statusbar)
        self.progressBar.setGeometry(QtCore.QRect(1680, 10, 218, 23))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        self.progressBar.setObjectName("progressBar")

        self.map = QgsMapCanvas(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(600, 30, 1290, 810))
        self.map.setObjectName("map")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
