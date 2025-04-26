from functools import wraps
from typing import Any, Callable, Dict

import pandas as pd
import requests


def data_loader(func: Callable) -> Callable:
    """
    A placeholder decorator for data loading functions.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Loading data...")
        return func(*args, **kwargs)
    return wrapper

@data_loader
def load_energy_data(**kwargs) -> pd.DataFrame:
    """
    Fetches energy data from Our World in Data API, transforms it, and returns a DataFrame
    ready for visualization.
    
    Returns:
        pd.DataFrame: Processed energy data ready for visualization
    """
    # Define the URL for the energy data from Our World in Data
    url = "https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv"
    
    try:
        # Fetch the data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Load the CSV data into a pandas DataFrame
        df = pd.read_csv(url)
        
        # Basic data cleaning and transformation
        # Drop rows with missing values in key columns
        df = df.dropna(subset=['country', 'year'])
        
        # Convert year to integer
        df['year'] = df['year'].astype(int)
        
        # Filter for recent years (e.g., last 20 years) to focus on relevant data
        current_year = df['year'].max()
        df = df[df['year'] >= current_year - 20]
        
        # Select relevant columns for visualization
        relevant_columns = [
            'country', 'year', 'population', 'gdp', 
            'primary_energy_consumption', 'electricity_generation',
            'renewables_electricity', 'fossil_electricity',
            'carbon_intensity_elec', 'greenhouse_gas_emissions'
        ]
        
        # Filter columns that exist in the dataframe
        existing_columns = [col for col in relevant_columns if col in df.columns]
        df = df[existing_columns]
        
        
        # Calculate per capita values for better comparison
        if 'population' in df.columns and 'primary_energy_consumption' in df.columns:
            df['energy_per_capita'] = df['primary_energy_consumption'] / df['population']
        
        if 'population' in df.columns and 'greenhouse_gas_emissions' in df.columns:
            df['emissions_per_capita'] = df['greenhouse_gas_emissions'] / df['population']
        
        # Sort data by country and year
        df = df.sort_values(['country', 'year'])
        
        # Define a list of European countries and the United Kingdom
        european_countries = ['United Kingdom', 'Europe' ]

        # Filter the DataFrame for countries in Europe or the United Kingdom
        df_filtered = df[df['country'].isin(european_countries)]

        # Print the filtered DataFrame
        print("Filtered DataFrame for European countries and the United Kingdom:")
        print(df_filtered.head())
        
        
        return df
    
    except Exception as e:
        print(f"Error loading energy  {e}")
        # Return an empty DataFrame with the expected columns if there's an error
        return pd.DataFrame(columns=existing_columns)


if __name__ == "__main__":
    load_energy_data()