import pdfplumber
import pandas as pd

# Open the PDF file
with pdfplumber.open('data.pdf') as pdf:
    extracted_data = []
    
    for page in pdf.pages:
        text = page.extract_text()
        # Split the text by lines
        lines = text.split('\n')
        
        # Skip the first 8 lines
        lines = lines[9:]

        for line in lines:
            parts = line.split()  # Split the line into parts
            if len(parts) >= 6 and '-' in parts[0]:
                vendor_code = parts[0]
                qty = parts[1]
                # Joining the remaining parts until the numeric cost
                item_name = ' '.join(parts[2:-3])
                unit_cost = parts[-3]
                min_qty = parts[-2]
                mb = parts[-1]
                
                # Append the data to the list
                extracted_data.append((vendor_code, qty, item_name, unit_cost, min_qty, mb))

# Create a DataFrame with the extracted data
df = pd.DataFrame(extracted_data, columns=["vendor code", "qty", "item name", "unit cost", "min", "mb"])

# # Save to CSV
df.to_csv('atroosh.csv', index=False)

print(df)
print("it worked! 🐦")



















# import pdfplumber
# import pandas as pd

# # Open the PDF file
# with pdfplumber.open('data.pdf') as pdf:
#     extracted_data = []
    
#     for page in pdf.pages:
#         text = page.extract_text()
#         # Split the text by lines
#         lines = text.split('\n')
        
#         # for line in lines:
#         #     # Checking for the specific pattern in each line (based on the example you provided)
#         #     if line.startswith('70-'):
#         #         parts = line.split()  # Split the line into parts
#         #         vendor_code = parts[0]
#         #         qty = parts[1]
#         #         # Joining the remaining parts until the numeric cost
#         #         item_name = ' '.join(parts[2:-3])
#         #         unit_cost = parts[-3]
#         #         min_qty = parts[-2]
#         #         mb = parts[-1]
                
#         #         # Append the data to the list
#         #         extracted_data.append((vendor_code, qty, item_name, unit_cost, min_qty, mb))

# # Create a DataFrame with the extracted data
# df = pd.DataFrame(extracted_data, columns=["vendor code", "qty", "item name", "unit cost", "min", "mb"])

# # Save to CSV and Excel files
# df.to_csv('atroosh.csv', index=False)
# # df.to_excel('extracted_data_pdfplumber.xlsx', index=False)

# print("Data extraction complete. CSV and Excel files created.")