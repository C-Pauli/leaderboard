import pandas as pd

# Load the dataset
file_path = 'your_dataset.csv'
data = pd.read_csv(file_path)

# Split the dataset into different categories based on 'Sample Type'
fruit_data = data[data['Sample Type'] == 'Fruit']
edible_solid_data = data[data['Sample Type'] == 'Edible Solid']
extract_isolate_data = data[data['Sample Type'].isin(['Extract', 'Isolate', 'Concentrate'])]

# Export each category to a separate CSV file
fruit_data.to_csv('fruit_data.csv', index=False)
edible_solid_data.to_csv('edible_solid_data.csv', index=False)
extract_isolate_data.to_csv('extract_isolate_data.csv', index=False)

print("Data has been split and exported into separate files.")

