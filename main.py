import yfinance as yf
######IN-PROGRESS#####

#Hub for company info functions | Maybe throw into class for ORGANIZATION -_-
def companyInfo(tic: str, interval: str):
    company = yf.Ticker(tic)
    stockHist = company.history(period=interval)
    
#Looks through firm recommendations and pulls all signals | Future: Catalog all signals for analysis
def firmRecommendations(company):
    buys,  = 0
    firmRec = company.recommendations['To Grade']
    for df in firmRec:
        print(df)
        if 'Buy' in df:
            buys+=1
    print(len(company.recommendations))






#Translates the input into usable strings
def intervalTran(periodT: list) -> list:
    interval = periodT[2]

    if interval.endswith('s') == False:
        interval += 's'
    intervals = {'minutes': 'm', 'hours': 'h', 'days': 'd', 'weeks': 'w', 'months': 'mo', 'years': 'y'}
    return periodT[0], periodT[1] + intervals[interval]




def main():
    print('number interval(minute, hour, day, week, month, year, max) EXAMPLE: 6 months')
    info = input('Enter a company to get data on with the period of the stock data: Example(AAPL 1 minute) ')
    limits = intervalTran(info.split())
    print(companyInfo(limits[0], limits[1]))
    

main()