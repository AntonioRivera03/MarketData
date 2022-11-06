import yfinance as yf
import pandas as pd

######IN-PROGRESS#####

#Hub for company info functions | Maybe throw into class for ORGANIZATION -_-
def companyInfo(tic: str, interval: str):
    
    company = yf.Ticker(tic)
    companyInfo = company.info
    recommendation = firmRecommendations(company)
    sharesNow = companyInfo['sharesShort']
    sharesPrior = companyInfo['sharesShortPriorMonth']
    sharesNow = f'{sharesNow:,d}'
    sharesPrior = f'{sharesPrior:,d}'
    
    df = pd.DataFrame([companyInfo['shortName'], companyInfo['regularMarketPrice'], companyInfo['dayHigh'], companyInfo['dayLow'], companyInfo['fiftyTwoWeekHigh'], 
                                  companyInfo['fiftyTwoWeekLow'], sharesNow, sharesPrior, companyInfo['shortRatio'], companyInfo['pegRatio']], 
                                  index=['Name', 'Stock Price', 'Day High', 'Day Low', '52 Week High', '52 Week Low', 'Shares Short', 'Shares Short Prior Month', 'Short Ratio', 'PEG Ratio'], 
                                  columns=['Data'], )
    df.style.set_properties(**{'text-align': 'left'})
    
    return(df)

    


    





#Looks through firm recommendations and pulls all signals | Future: Catalog all signals for analysis
def firmRecommendations(company):
    recomF = company.recommendations['Firm']
    recomC = company.recommendations['To Grade']
    buys = 0
    firmList = []
    firmRec = []
    for i in range(len(recomF)):
        if recomF[i] not in firmList:
            firmList.append(recomF[i])
            firmRec.append(recomC)   
    
    return  {'Firm':firmList, 'Recommendation': firmRec}

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