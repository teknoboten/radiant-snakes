import pandas as pd

# Path to your text file
file_path = 'data.txt'

# Initialize lists to hold the extracted data
gtin = []
sku = []
item_name = []
count_pak = []
qty = []
unit_cost = []

# Read the text file
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        
        # Extract relevant parts based on the given format
        gtin.append(parts[1])
        sku.append(parts[2])
        item_name.append(' '.join(parts[3:-7]))
        count_pak.append(parts[-6])
        qty.append(parts[-4])
        unit_cost.append(parts[-1])

# Create a DataFrame
df = pd.DataFrame({
    'GTIN': gtin,
    'SKU': sku,
    'Item Name': item_name,
    'Count/Pak': count_pak,
    'Qty': qty,
    'Unit Cost': unit_cost
})

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)

# Save DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Display the DataFrame to verify
print(df)