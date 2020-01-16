import sys
def moon_weight():
    print('Please enter your current Earth weight')
    weight = float(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    increase = float(sys.stdin.readline())
    print('Please enter the number of years')
    years = int(sys.stdin.readline())
    years=years+1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s' % (year, moon_weight))
moon_weight()        