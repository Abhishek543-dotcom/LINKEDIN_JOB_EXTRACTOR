import pandas as pd

# Load the CSV file into a pandas DataFrame without a header
input_file_path = 'linkedin-jobs.csv'
output_file_path = 'purified_linkedin-jobs.csv'

df = pd.read_csv(input_file_path, header=None)

# Clean and process the DataFrame as needed
# For example, you can remove duplicate rows, handle missing values, etc.
df_cleaned = df.drop_duplicates().dropna()

# Save the purified DataFrame to a new CSV file without a header
df_cleaned.to_csv(output_file_path, index=False, header=False)

print(f'The CSV file has been purified and saved to {output_file_path}')

