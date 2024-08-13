import pandas as pd

# Path to your text file
file_path = 'data.txt'

# Initialize lists to hold the extracted data
item_name = []
variation_name = []
sku = []
gtin = []
vendor_code = []
notes = []
qty = []
unit_cost = []

# Read the text file
with open(file_path, 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 7):  # Process every 5 lines as a single entry
        # gtin.append(lines[i].strip())
        # item_name.append(lines[i+1].strip())
        # qty.append(lines[i+2].strip())
        # unit_cost.append(lines[i+3].strip().replace('$', ''))
        item_name.append(lines[i].strip())
        vendor_code.append(lines[i+2].strip())
        unit_cost.append(lines[i+5].strip().replace('$', ''))
        qty.append(lines[i+6].strip().replace('Qty: ',''))

# Create a DataFrame
# df = pd.DataFrame({
#     'GTIN': gtin,
#     'Item Name': item_name,
#     'Qty': qty,
#     'Unit Cost': unit_cost
# })
df = pd.DataFrame({
    'Item Name': item_name,
    'Variation Name': '',
    'SKU': '',
    'GTIN': gtin,
    'Vendor Code': '',
    'Notes': '',
    'Qty': qty,
    'Unit Cost': unit_cost
})

# Ensure GTIN is treated as a string
df['GTIN'] = df['GTIN'].astype(str)

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)

# Save DataFrame to Excel
# df.to_excel('output.xlsx', index=False)
df.to_excel('purchase_order_import_template.xlsx', index=False)

# Display the DataFrame to verify
print(df)