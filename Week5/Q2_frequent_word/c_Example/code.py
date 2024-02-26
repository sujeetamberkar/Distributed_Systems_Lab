import pandas as pd

def main():

    # Assuming each line of example.txt is structured as: Date,Time,City,Category,Amount,Payment
    with open('example.txt', 'r') as file:
        for line in file:
            # print(line)
            l = line
            a = l.split()
            a = a[-1]
            print(a, end=' ')
  
if __name__ == "__main__":
    main()
