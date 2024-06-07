import pandas as pd

# Path to your text file
file_path = 'data.txt'

# Initialize lists to hold the extracted data
item_name = []
sku = []
unit_cost = []
qty = []

# Read the text file
with open(file_path, 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):  # every item has two lines of info
        # Strip the item name
        item_name.append(lines[i].strip())
        
        # Split the second line into parts
        parts = lines[i+1].split()
        sku.append(parts[0])
        unit_cost.append(parts[1].replace('$', ''))
        qty.append(parts[2])

# Create a DataFrame
df = pd.DataFrame({
    'SKU': sku,
    'Item Name': item_name,
    'Unit Cost': unit_cost,
    'Qty': qty,
})

# Ensure sku is treated as a string
df['SKU'] = df['SKU'].astype(str)

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)

# Save DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Display the DataFrame to verify
print(df)