import unittest
import pandas as pd
import numpy as np
from series_practice_2 import *

class TestBookstoreSalesAnalysis(unittest.TestCase):
    def setUp(self):
        # Recreate the test Series so it's always consistent
        dates = ["2023-11-01", "2023-11-02", "2023-11-03", "2023-11-04", "2023-11-05",
                 "2023-11-06", "2023-11-07", "2023-11-08", "2023-11-09", "2023-11-10"]
        sales = [320, 400, 350, 380, 420, 360, 390, 410, 430, 410]
        self.series = pd.Series(sales, index=dates)

    def test_total_sales(self):
        result = total_sales(self.series)
        self.assertIsInstance(result, (int, float, np.integer, np.floating, pd.Series, pd.DataFrame))
        if isinstance(result, (pd.Series, pd.DataFrame)):
            result = result.values.sum()
        self.assertEqual(result, 3870)

    def test_date_with_lowest_sales(self):
        result = date_with_lowest_sales(self.series)
        # Handle if function returns pandas.Index or Series
        if isinstance(result, (pd.Index, pd.Series)):
            result = result.tolist()[0]
        self.assertEqual(result, "2023-11-01")

    def test_median_sales(self):
        result = median_sales(self.series)
        if isinstance(result, (pd.Series, pd.Index)):
            result = float(result.median())
        self.assertAlmostEqual(result, 395.0, 1)

    def test_days_with_sales_below(self):
        result = days_with_sales_below(self.series, 380)
        # Normalize to list of strings
        if isinstance(result, (pd.Index, pd.Series)):
            result = result.tolist()
        self.assertEqual(result, ["2023-11-01", "2023-11-03", "2023-11-06"])

    def test_fancy_indexing_sales(self):
        result = fancy_indexing_sales(self.series, [1, 4, 8])
        # Normalize to list of numbers
        if isinstance(result, (pd.Series, pd.Index)):
            result = result.tolist()
        self.assertEqual(result, [400, 420, 430])

   
if __name__ == "__main__":
    unittest.main()
