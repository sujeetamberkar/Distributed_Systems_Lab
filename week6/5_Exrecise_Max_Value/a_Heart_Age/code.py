# code.py
import pandas as pd

def main():
    df = pd.read_csv('heart_disease_data.csv')    
    for value in df['age']:
        print(value, end=' ')

if __name__ == "__main__":
    main()
