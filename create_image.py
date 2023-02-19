from qgis.core import *
from PyQt5.QtGui import QFont
from qgis.core import QgsLayoutItem


class CreateImage():
    """Image creation class.
    """

    def create_image(self, layer, color_background, file_name):
        """creates complex map layout consisting of map views, title, legend and scalebar and exports it to raster image.

        Args:
            layer (QgsVectorLayer): selected vector layer.
            color_background (QColor): color background of viev map.
            file_name (str): export path.
        """
        project = QgsProject.instance()
        layout = QgsPrintLayout(project)
        layout.initializeDefaults()
        map = QgsLayoutItemMap(layout)
        map.setRect(20, 20, 20, 20)
        ms = QgsMapSettings()
        ms.setLayers([layer])  # set layers to be mapped
        rect = QgsRectangle(ms.fullExtent())
        rect.scale(1.0)
        ms.setExtent(rect)
        map.setExtent(rect)
        map.setBackgroundColor(color_background)
        layout.addLayoutItem(map)
        map.attemptMove(QgsLayoutPoint(5, 20, QgsUnitTypes.LayoutMillimeters))
        map.attemptResize(QgsLayoutSize(
            180, 180, QgsUnitTypes.LayoutMillimeters))
        title = QgsLayoutItemLabel(layout)
        title.setText("Lasy ochronne")
        title.setFont(QFont('Arial', 24))
        title.adjustSizeToText()
        layout.addLayoutItem(title)
        title.attemptMove(QgsLayoutPoint(
            80, 5, QgsUnitTypes.LayoutMillimeters))
        title.setFrameEnabled(False)
        legend = QgsLayoutItemLegend(layout)
        legend.setLinkedMap(map)
        layerTree = QgsLayerTree()
        layerTree.addLayer(layer)
        legend.model().setRootGroup(layerTree)
        layout.addLayoutItem(legend)
        legend.attemptMove(QgsLayoutPoint(
            215, 15, QgsUnitTypes.LayoutMillimeters))
        scaleBar = QgsLayoutItemScaleBar(layout)
        scaleBar.setStyle('Single Box')
        scaleBar.setFont(QFont("Arial", 10))
        scaleBar.applyDefaultSize(QgsUnitTypes.DistanceMeters)
        scaleBar.setMapUnitsPerScaleBarUnit(1000.0)
        scaleBar.setSegmentSizeMode(QgsScaleBarSettings.SegmentSizeFitWidth)
        scaleBar.setMaximumBarWidth(70)
        scaleBar.setNumberOfSegments(5)
        scaleBar.setUnitsPerSegment(1*1000.0)
        scaleBar.setUnitLabel("km")
        scaleBar.setLinkedMap(map)
        layout.addLayoutItem(scaleBar)
        scaleBar.attemptMove(QgsLayoutPoint(
            215, 190, QgsUnitTypes.LayoutMillimeters))
        exporter = QgsLayoutExporter(layout)
        exporter.exportToImage(
            file_name, QgsLayoutExporter.ImageExportSettings())
