# import pandas as pd

# output_csv_path = 'output.csv'
# currentcat_csv_path = 'currentcat.csv'

# # types (numbers === indexes of current cat column titles?)
# dtype_dict = {
#     6: 'str',  
#     7: 'str',  
#     23: 'str', 
#     24: 'str' 
# }

# # Read the CSV files into DataFrames
# output_df = pd.read_csv(output_csv_path)
# currentcat_df = pd.read_csv(currentcat_csv_path, dtype=dtype_dict)  

# # Extract GTIN columns as sets for comparison
# output_gtin_set = set(output_df['GTIN'].astype(str))
# currentcat_gtin_set = set(currentcat_df['GTIN'].astype(str))

# # print('currentcat gtin set:', list(output_gtin_set))

# # Find GTINs that are in output_df but not in currentcat_df
# new_gtins = output_gtin_set - currentcat_gtin_set

# # # Filter the new items based on the new GTINs
# new_items_df = output_df[output_df['GTIN'].astype(str).isin(new_gtins)]

# # new_items_df.to_excel('new_items.xlsx', index=False)
# new_items_df.to_csv('new_items.csv', index=False)


# # Display the DataFrame of new items to verify
# # print(new_items_df)
# # print('success! you compared the things!')

import pandas as pd

output_csv_path = 'output.csv'
currentcat_csv_path = 'currentcat.csv'

# Read the CSV files into DataFrames, ensuring GTIN is read as a string
output_df = pd.read_csv(output_csv_path, dtype={'GTIN': 'str'})
currentcat_df = pd.read_csv(currentcat_csv_path, dtype={'GTIN': 'str', 6: 'str', 7: 'str', 23: 'str', 24: 'str'})

# Ensure column names are as expected
# print("Output DataFrame columns:", output_df.columns)
# print("Currentcat DataFrame columns:", currentcat_df.columns)

# Extract GTIN columns as sets for comparison, stripping any leading/trailing whitespaces
output_gtin_set = set(output_df['GTIN'].str.strip())
currentcat_gtin_set = set(currentcat_df['GTIN'].str.strip())

# Debugging output
# print('Output GTIN set:', output_gtin_set)
# print('Currentcat GTIN set:', currentcat_gtin_set)

# Find GTINs that are in output_df but not in currentcat_df
new_gtins = output_gtin_set - currentcat_gtin_set

# Debugging output
# print('New GTINs:', new_gtins)

# Filter the new items based on the new GTINs
new_items_df = output_df[output_df['GTIN'].str.strip().isin(new_gtins)]

# Output the new items to a new CSV file
new_items_df.to_csv('new_items.csv', index=False)

# Display the DataFrame of new items to verify
print(new_items_df)
print('Success! You compared the things!')
print('new items', len(new_items_df))