from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog


class GISDialog(QDialog):
    """Creating dialog window class.
    """

    def __init__(self, title, icon, selected_layer, isContextHelpButtonHint, isMSWindowsFixedSizeDialogHint, parent=None):
        """Constructor.
        """
        self.title = title
        self.icon = icon
        self.selected_layer = selected_layer
        self.isContextHelpButtonHint = isContextHelpButtonHint
        self.isMSWindowsFixedSizeDialogHint = isMSWindowsFixedSizeDialogHint
        super(GISDialog, self).__init__(parent)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint,
                           isContextHelpButtonHint)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint,
                           isMSWindowsFixedSizeDialogHint)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))

    def closeEvent(self, event):
        self.selected_layer.removeSelection()
