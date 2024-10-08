import pandas as pd

output_csv_path = 'output.csv'
currentcat_csv_path = 'currentcat.csv'

# types!
dtype_dict = {
    6: 'str',  
    7: 'str',  
    23: 'str', 
    24: 'str' 
}

# Read the CSV files into DataFrames
output_df = pd.read_csv(output_csv_path)
currentcat_df = pd.read_csv(currentcat_csv_path, dtype=dtype_dict, low_memory=False)

# Extract SKU columns as sets for comparison
output_sku_set = set(output_df['SKU'].astype(str))
currentcat_sku_set = set(currentcat_df['SKU'].astype(str))

# Find skus that are in output_df but not in currentcat_df
new_skus = output_sku_set - currentcat_sku_set

# Filter the new items based on the new skus
new_items_df = output_df[output_df['SKU'].astype(str).isin(new_skus)]

# new_items_df.to_excel('new_items.xlsx', index=False)
new_items_df.to_csv('new_items.csv', index=False)


# Display the DataFrame of new items to verify
# print(new_items_df)
print('success! you compared the things!')