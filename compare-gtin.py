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

# Extract GTIN columns as sets for comparison
output_gtin_set = set(output_df['GTIN'].astype(str))
currentcat_gtin_set = set(currentcat_df['GTIN'].astype(str))

# Find GTINs that are in output_df but not in currentcat_df
new_gtins = output_gtin_set - currentcat_gtin_set

# Filter the new items based on the new GTINs
new_items_df = output_df[output_df['GTIN'].astype(str).isin(new_gtins)]

# new_items_df.to_excel('new_items.xlsx', index=False)
new_items_df.to_csv('new_items.csv', index=False)


# Display the DataFrame of new items to verify
# print(new_items_df)
print('success! you compared the things!')