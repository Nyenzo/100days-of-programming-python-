import sys
import time
def moonweight():
    print('Enter your current weight')
    weight = float(sys.stdin.readline())
    print('Enter your weight increase in a year')
    increase = float(sys.stdin.readline())
    print('Enter the number of years staying on space')
    years = int(sys.stdin.readline())
    years=years+1
    for year in range(1, years):
        weight = weight + increase
        moonweight = weight * 0.165
        print('Year %s is %s' % (year, moonweight))
moonweight()
print(time.asctime())        