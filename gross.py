import pandas as pd

# Path to your text file
file_path = 'data.txt'

# Initialize lists to hold the extracted data
sku = []
item_name = []
qty = []
unit_cost = []

# Read the text file
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        
        # Extract relevant parts based on the given format
        sku.append(parts[0])
        item_name.append(' '.join(parts[1:-8]))
        qty.append(parts[-1])
        unit_cost.append(parts[-6].replace('$',''))

# Create a DataFrame
df = pd.DataFrame({
    'SKU': sku,
    'Item Name': item_name,
    'Qty': qty,
    'Unit Cost': unit_cost
})

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)

# Save DataFrame to Excel
# df.to_excel('output.xlsx', index=False)

# Display the DataFrame to verify
print(df)