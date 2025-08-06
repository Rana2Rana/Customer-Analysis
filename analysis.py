import pandas as pd

pd.set_option('display.max_columns', None)


# Load the dataset
filepath = 'Dataset/Digital Sales - Customer Data.xlsx'
data = pd.read_excel(filepath)
print('The dimension of the Dataset: ', data.shape)
# data.info()

print(data.describe())

# understand the data
print(data.head())
print(data.columns)
# Check for missing values
print(data.isnull().sum()) 
# Check for duplicate rows
print(data.duplicated().sum()) 
# Remove duplicate rows if any
data = data.drop_duplicates()
print('After removing duplicates, the dimension of the Dataset: ', data.shape)  
print(data.describe())

#  As a result of the above oberation, we should cleaned the dataset from duplicates if founded.

# check the data types of the columns
print(data.dtypes)
# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
# Check for any rows with invalid dates
invalid_dates = data[data['Date'].isnull()]
if not invalid_dates.empty:
    print("Invalid dates found:")
    print(invalid_dates)
else:
    print("All dates are valid.")   

# as a result of the above operation, we should have cleaned the dataset from invalid dates if founded.
# check the unique vlues in a loop
for column in data.select_dtypes(include=['object']).columns:
    unique_values = data[column].unique()
    print(f"Unique values in '{column}': {unique_values[:10]}... (Total: {len(unique_values)})")

# Next steps in the analysis:
# 1. Analyze the distribution of numerical columns.
# 2. Explore relationships between categorical variables and numerical variables.
# 3. Visualize the data to identify trends and patterns.