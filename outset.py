import pandas as pd

# Path to your CSV file
file_path = 'outset.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Print the column names to verify
print(df.columns)

# Create a new DataFrame with the required columns
df_new = pd.DataFrame({
    'Item Name': df['Item Description'],
    'Variation Name': '',
    'Sku': df['Number'],
    'GTIN': df['UPC / EAN'].str.replace('-', '').astype(str),
    'Vendor Code': '',
    'Notes': '',
    'Qty': df['Qty'],
    'Unit Cost': df['Price'].str.replace('$', '')

})

# Save DataFrame to CSV
df_new.to_csv('output.csv', index=False)

# Save DataFrame to Excel
df_new.to_excel('purchase_order_import_template.xlsx', index=False)

# Display the DataFrame to verify
print(df_new)