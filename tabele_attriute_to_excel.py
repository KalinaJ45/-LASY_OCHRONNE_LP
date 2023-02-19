import xlsxwriter


class TabeleToExcel():
    """Creating tabele of vctor layer attributtes as .xlsx file class.
    """

    def create_tabele(self, selected_layer, filename, names_of_fields):
        """Creates tabele of vctor layer attributtes as .xlsx file.

        Args:
            selected_layer (QgsVectorLayer): selected vector layer. 
            filename (str): selected saving path.
            names_of_fields (list): list of selected layer's fields aliases (list of strings).
        """

        data = [feature.attributes()
                for feature in selected_layer.getFeatures()]

        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet('Tabela atrybutów')
        worksheet.add_table('A1:{}{}'.format(
            chr(ord('@')+len(names_of_fields)), len(data)+1), {'data': data, 'banded_rows': 0, 'banded_columns': 1, 'columns': [{'header': '{}'.format(name)} for name in names_of_fields]})
        workbook.close()
