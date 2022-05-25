

import sys
import os
import unittest
import numpy as np
import pandas as pd
import pandas.api.types as ptypes

sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))


from data_preview import DataPreview

df = pd.DataFrame({'numbers': [2, 4, 6, 7, 9], 'letters': ['a', 'b', 'c', 'd', 'e'],
                   'floats': [0.2323, -0.23123, np.NaN, np.NaN, 4.3434]})


class TestCases(unittest.TestCase):

    def test_show_datatypes(self):
        data_preProcessing = DataPreview(df)
        data_preProcessing.show_datatypes()
        self.assertEqual(df.dtypes[0], data_preProcessing.df.dtypes[0])

    def test_show_data_information(self):
        data_preProcessing = DataPreview(df)
        data_preProcessing.show_data_information()
        self.assertEqual(
            data_preProcessing.df.info(), df.info())

    def test_list_coloumn_names(self):
        data_preProcessing = DataPreview(df)
        data_preProcessing.list_coloumn_names()
        self.assertEqual(
            data_preProcessing.df.columns.any(), df.columns.any())


if __name__ == '__main__':
    unittest.main()
