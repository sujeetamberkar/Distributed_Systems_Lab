import pandas as pd

def main():
    # Load the dataset
    df = pd.read_csv('covid_19_data.csv')
    
    # Print values in the target column, separated by spaces
    for value in df['Country/Region']:  # Replace 'column_name' with the actual column name
        print(value, end=' ')

if __name__ == "__main__":
    main()
