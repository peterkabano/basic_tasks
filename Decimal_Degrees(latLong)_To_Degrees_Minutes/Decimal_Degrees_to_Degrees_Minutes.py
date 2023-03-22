import os
import pandas as pd
import math


# Set working directory to directory containing data (csv file)
os.chdir(r'pathToFile')

# Read the CSV file
df = pd.read_csv('coordinates.csv')

# Define a function to convert decimal degrees to degrees and minutes
def dec_deg_to_deg_mins(dec_deg):
    """
    This function converts decimal degrees to degrees and minutes format.
    """
    deg = int(dec_deg)
    mins = abs((dec_deg - deg) * 60)
    return f"{deg}°{math.floor(mins)}'"

# Apply the function to the latitude and longitude columns
df['Latitude_DM'] = df['Latitude'].apply(dec_deg_to_deg_mins)
df['Longitude_DM'] = df['Longitude'].apply(dec_deg_to_deg_mins)

# Save the results to a new CSV file
# Encoding settings retains '°' symbol in csv output
df.to_csv('coordinates_dms.csv', encoding='utf-8-sig')
