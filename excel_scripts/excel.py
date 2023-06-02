import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

headers = ['Madde', 'Tip', 'Açıklama']
# Create a dataframe
data = [['Default Adres', 'Bugfix', 'Sepette bir adres seçtikten sonra fiyat hesaplamayı tekrar çalıştırdığımda listedeki ilk adrese geri dönüyor. Dönmemesini sağlayabilir miyiz? Seçili varsa o kalabilir mi?'],
        ['Catalog Hierarchy Picklist Hatası', 'Bugfix', 'Ürün kataloğunda hiyerarşi picklistleri gelmiyor ve pickliste tıklayınca ekran donuyor.']]
df = pd.DataFrame(data, columns=headers)

# Create a new Excel file and add the dataframe as a table
writer = pd.ExcelWriter("table.xlsx", engine='openpyxl') 
df.to_excel(writer, index=False)

# Get the worksheet
worksheet = writer.sheets['Sheet1']

# Set font size and color to the headers
for col in worksheet.iter_cols(min_col=1, max_col=3, min_row=1, max_row=1):
    for cell in col:
        cell.font = Font(size=12, bold=True, color='0070C9')

# Apply filtering to the headers
worksheet.auto_filter.ref = "A1:C1"

# Save the file
writer.save()

print(df)