import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_and_prepare_data(filepath):
    """Load and prepare COVID-19 data"""
    try:
        # Load data
        df = pd.read_csv(filepath)
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Display dataset infor
        print("Columns:", df.columns)
        print("\nMissing Values:\n", df.isnull().sum())
        
        return df
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_and_filter_data(df, countries):
    """Clean and filter data for selected countries"""
    try:
        # Filter for countries of interest
        df_filtered = df[df['location'].isin(countries)].copy()
        
        # Drop rows with missing critical values
        df_filtered = df_filtered.dropna(subset=['total_cases', 'total_deaths', 'date'])
        
        # Forward fill numeric values
        numeric_cols = df_filtered.select_dtypes(include='number').columns
        df_filtered[numeric_cols] = df_filtered[numeric_cols].ffill()
        
        return df_filtered
    
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return None

def calculate_metrics(df):
    """Calculate key COVID-19 metrics"""
    try:
        # Global stats
        total_cases = df['total_cases'].sum()
        total_deaths = df['total_deaths'].sum()
        print(f"\nGlobal Statistics:")
        print(f"Total Cases Worldwide: {total_cases:,.0f}")
        print(f"Total Deaths Worldwide: {total_deaths:,.0f}")
        
        # Latest data for each country
        latest_data = df.sort_values('date').groupby('location').tail(1).copy()
        
        # Calculate death rate
        latest_data['death_rate'] = (latest_data['total_deaths'] / latest_data['total_cases']) * 100
        
        # Calculate vaccination percentages if data exists
        if 'people_fully_vaccinated' in df.columns and 'population' in df.columns:
            latest_data['pct_fully_vaccinated'] = (latest_data['people_fully_vaccinated'] / latest_data['population']) * 100
        
        return latest_data
    
    except Exception as e:
        print(f"Error calculating metrics: {e}")
        return None

def plot_time_series(df, countries, y_col, title, ylabel):
    """Plot time series data for multiple countries"""
    plt.figure()
    for country in countries:
        country_data = df[df['location'] == country]
        if not country_data.empty:
            plt.plot(country_data['date'], country_data[y_col], label=country)
    
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_country_comparison(df, x_col, y_col, title, palette):
    """Plot comparison bar chart across countries"""
    plt.figure()
    if not df.empty:
        sns.barplot(data=df, x=x_col, y=y_col, hue=x_col, palette=palette, legend=False)
        plt.title(title)
        plt.ylabel(y_col)
        plt.xlabel('Country')
        plt.tight_layout()
        plt.show()

def analyze_vaccinations(df, countries):
    """Analyze and visualize vaccination data"""
    try:
        if 'total_vaccinations' not in df.columns:
            print("\nVaccination data not available in this dataset")
            return
        
        # Filter and clean vaccination data
        vax_df = df[df['location'].isin(countries)].copy()
        vax_df = vax_df.dropna(subset=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'])
        
        if vax_df.empty:
            print("\nNo vaccination data available for selected countries")
            return
        
        # Plot cumulative vaccinations over time
        plot_time_series(
            vax_df, countries, 
            'total_vaccinations', 
            'Cumulative COVID-19 Vaccinations Over Time', 
            'Total Vaccinations'
        )
        
        # Calculate vaccination percentages
        latest_vax = vax_df.sort_values('date').groupby('location').tail(1).copy()
        latest_vax['pct_fully_vaccinated'] = (latest_vax['people_fully_vaccinated'] / latest_vax['population']) * 100
        
        print("\nFully Vaccinated % by Country:")
        print(latest_vax[['location', 'pct_fully_vaccinated']].round(2))
        
        # Plot vaccination percentages
        plot_country_comparison(
            latest_vax, 
            'location', 
            'pct_fully_vaccinated', 
            '% of Population Fully Vaccinated by Country', 
            'Greens'
        )
        
    except Exception as e:
        print(f"Error analyzing vaccination data: {e}")

def main():
    data_file = 'synthetic_covid19_data.csv'
    countries_of_interest = ['Russia', 'France', 'Brazil', 'Italy', 'Kenya']
    
    print("COVID-19 Global Data Tracker Analysis")
    print(f"Analyzing data for: {', '.join(countries_of_interest)}\n")
    
    # Load and prepare data
    df = load_and_prepare_data(data_file)
    if df is None:
        return
    
    # Clean and filter data
    df_filtered = clean_and_filter_data(df, countries_of_interest)
    if df_filtered is None:
        return
    
    # Calculate metrics
    latest_data = calculate_metrics(df_filtered)
    if latest_data is None:
        return
    
    # Plot cases over time
    plot_time_series(
        df_filtered, countries_of_interest, 
        'total_cases', 
        'Total COVID-19 Cases Over Time', 
        'Total Cases'
    )
    
    # Plot deaths over time
    plot_time_series(
        df_filtered, countries_of_interest, 
        'total_deaths', 
        'Total COVID-19 Deaths Over Time', 
        'Total Deaths'
    )
    
    # Plot latest cases by country
    plot_country_comparison(
        latest_data, 
        'location', 
        'total_cases', 
        'Latest Total COVID-19 Cases by Country', 
        'Blues_d'
    )
    
    # Display and plot death rates
    if not latest_data.empty:
        print("\nCOVID-19 Death Rate by Country (%):")
        print(latest_data[['location', 'death_rate']].round(2))
        
        plot_country_comparison(
            latest_data, 
            'location', 
            'death_rate', 
            'COVID-19 Death Rate (%) by Country', 
            'Reds'
        )
    
    # Analyze vaccination data
    analyze_vaccinations(df, countries_of_interest)
    
    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()