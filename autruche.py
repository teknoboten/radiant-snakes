import pandas as pd

# Path to your text file
file_path = 'data.txt'

# Initialize lists to hold the extracted data
item_name = []
vendor_code = []
unit_cost = []
qty = []

# Read the text file
with open(file_path, 'r') as file:
    lines = file.readlines()
    for i in range(1, len(lines), 2):  # every item has two lines of info
        item_name.append(lines[i].strip())     # Strip the item name
        
        parts = lines[i+1].split() # Split the second line into parts
        sku.append(parts[0])
        unit_cost.append(parts[1].replace('$', ''))
        qty.append(parts[2])

# Create a DataFrame
df = pd.DataFrame({
    'Item Name': item_name,
    'SKU': sku,
    'Unit Cost': unit_cost,
    'Qty': qty,
})

# Ensure sku is treated as a string
df['sku'] = df['SKU'].astype(str)

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)

# Save DataFrame to Excel
# df.to_excel('output.xlsx', index=False)

# Display the DataFrame to verify
print(df)