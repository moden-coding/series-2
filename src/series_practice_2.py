import pandas as pd

def total_sales(sales_data):
    pass
def date_with_lowest_sales(sales_data):
    pass


def median_sales(sales_data):
    pass


def days_with_sales_below(sales_data, threshold):
    pass

def fancy_indexing_sales(sales_data, indices):
    pass

dates = ["2023-11-01", "2023-11-02", "2023-11-03", "2023-11-04", "2023-11-05", "2023-11-06", "2023-11-07", "2023-11-08", "2023-11-09", "2023-11-10"]
sales = [320, 400, 350, 380, 420, 360, 390, 410, 430, 410]

#Create a series from the given data
book_sales_series = pd.Series()


# === Manual print-based tests ===
print("Testing total_sales()...")
print("Expected:", 3870)
print("Got:", total_sales(book_sales_series), "\n")

print("Testing date_with_lowest_sales()...")
print("Expected: 2023-11-01")
print("Got:", date_with_lowest_sales(book_sales_series), "\n")

print("Testing median_sales()...")
print("Expected:", 395.0)
print("Got:", median_sales(book_sales_series), "\n")

print("Testing days_with_sales_below() (threshold=380)...")
print("Expected: ['2023-11-01', '2023-11-03', '2023-11-06']")
print("Got:", days_with_sales_below(book_sales_series, 380), "\n")

print("Testing fancy_indexing_sales() (indices [1,4,8])...")
print("Expected: [400, 420, 430]")
print("Got:", fancy_indexing_sales(book_sales_series, [1,4,8]), "\n")

