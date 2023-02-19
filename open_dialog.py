from GIS_dialog import GISDialog


class OpenDialog(GISDialog):
    """Creating dialog window class.
    """

    def __init__(self, title, icon, selected_layer, isContextHelpButtonHint, isMSWindowsFixedSizeDialogHint, deleteLayerBtn, actionShowTabeleAttribute, actionIdentify, parent=None):
        """Constructor.
        """
        super().__init__(title, icon, selected_layer, isContextHelpButtonHint,
                         isMSWindowsFixedSizeDialogHint, parent=None)
        self.actionShowTabeleAttribute = actionShowTabeleAttribute
        self.actionIdentify = actionIdentify
        self.deleteLayerBtn = deleteLayerBtn

    def closeEvent(self, event):
        """Does when dialog window is being closed.

        Args:
            event (QgsMapMouseEvent): specific mouseEvent.
        """
        self.set_enabled_of_widget(
            {self.actionShowTabeleAttribute: True, self.actionIdentify: True, self.deleteLayerBtn: True})

        self.selected_layer.removeSelection()

    def showEvent(self, event):
        """Does when dialog window is being opened.

        Args:
            event (QgsMapMouseEvent): specific mouseEvent.
        """
        self.set_enabled_of_widget(
            {self.actionShowTabeleAttribute: False, self.actionIdentify: False,  self.deleteLayerBtn: False})

    def set_enabled_of_widget(self, enabled_of_widets):
        """Sets if widgets is enabled or not.

        Args:
            enabled_of_widets (dict): dictionary in which the keys are widgets (QtWidgets) and the values are True or False (bool), depending on whether the widget  should be enabled or not.
        """
        for widget in enabled_of_widets:
            widget.setEnabled(enabled_of_widets[widget])
