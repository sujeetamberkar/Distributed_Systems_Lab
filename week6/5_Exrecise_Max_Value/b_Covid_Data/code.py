# code.py
import pandas as pd

def main():
    df = pd.read_csv('covid_19_data.csv')    
    for value in df['Deaths']:
        print(value, end=' ')



if __name__ == "__main__":
    main()
