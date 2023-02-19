
import xlsxwriter
from qgis.core import QgsAggregateCalculator


class GeneratedRaport():
    """Generating raport class.
    """

    def create_tabele(self, selected_layer, filename, categories_dictionary):
        """Create raport file.

        Args:
            selected_layer (QgsVectorLayer): selected vector layer. 
            filename (str): selected saving path.
            categories_dictionary (dict): dictionary in which the keys are protection categories (str) and the values are their codes (str).
        """
        data = []
        for category, code in categories_dictionary.items():
            data_for_less_than_40 = [feat["POWIERZCHNIA (ha)"] for feat in selected_layer.getFeatures() if str(
                code) in str(feat["KATEGORIE OCHRONNOŚCI"]) and feat["WIEK RĘBNOŚCI"] <= 40]
            data_for_more_than_40 = [feat["POWIERZCHNIA (ha)"] for feat in selected_layer.getFeatures()if str(
                code) in str(feat["KATEGORIE OCHRONNOŚCI"]) and feat["WIEK RĘBNOŚCI"] > 40]
            cumulative_data = [category, len(data_for_less_than_40), round(sum(
                data_for_less_than_40), 2), len(data_for_more_than_40), round(sum(data_for_more_than_40), 2)]
            data.append(cumulative_data)
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet('Raport')
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })
        worksheet.merge_range('A1:A2', '', merge_format)
        worksheet.merge_range(
            'B1:C2', 'WIEK GATUNKU PANUJĄCEGO ≤40', merge_format)
        worksheet.merge_range(
            'D1:E2', 'WIEK GATUNKU PANUJĄCEGO >40', merge_format)
        worksheet.add_table('A3:E13', {'data': data, 'banded_rows': 0, 'banded_columns': 1, 'columns': [
            {'header': '1. KATEGORIA OCHRONNOŚCI'},
            {'header': '2. LICZBA WYDZIELEŃ'},
            {'header': '3. POWIERZCHNIA WYDZIELEŃ (HA)'},
            {'header': '4. LICZBA WYDZIELEŃ'},
            {'header': '5. POWIERZCHNIA WYDZIELEŃ (HA)'},
        ]})
        number_of_all_subarea = "Liczba wszystkich wydzieleń: {}".format(
            selected_layer.featureCount())
        worksheet.merge_range('A15:A16', number_of_all_subarea, merge_format)
        total_sum_of_area = "Całkowita powierzchnia leśna: {}".format(round((selected_layer.aggregate(
            QgsAggregateCalculator.Sum, "POWIERZCHNIA (ha)")[0]), 2))
        worksheet.merge_range('A17:A18',  total_sum_of_area, merge_format)
        workbook.close()
