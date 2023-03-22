import glob
import os
import pandas as pd


# Set the input and output directories
input_dir = 'dirToInputFiles'
output_dir = 'dirToOutputFiles'

# Get a list of all CSV files in the input directory
csv_files = glob.glob(os.path.join(input_dir, '*.csv'))

# Loop through each file
for csv_file in csv_files:
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # Apply your commands to the dataframe
    df['timestamp (UTC)'] = pd.to_datetime(df['timestamp (UTC)'], format='%Y-%m-%d %H:%M')
    df['Date'] = df['timestamp (UTC)'].dt.strftime('%d.%m.%Y')
    df['Time'] = df['timestamp (UTC)'].dt.strftime('%H:%M')
    df['RH'] = df['relativehumidity (-)'] * 100
    df = df.rename(columns={'temperature (degrees Celsius)': 'Ta', 'windspeed (m/s)': 'v', 'radiation (W/m2)': 'G'})
    df = df.drop(['timestamp (UTC)', 'humiditysensortemperature (degrees Celsius)', 'relativehumidity (-)'], axis=1)
    df = df.reindex(columns=['Date', 'Time', 'Ta', 'RH', 'v', 'G'])
    df = df.dropna(how='any')
    df['RH'] = df['RH'].astype(int)
    df['v'] = df['v'].round(1)

    # Construct the output filename
    output_file = os.path.join(output_dir, os.path.basename(csv_file).replace('.csv', '_processed.csv'))

    # Save the updated dataframe to the output file
    df.to_csv(output_file, index=False)
