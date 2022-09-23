
import requests
import json
import time


tickers = ["aapl"]#, "adbe", "amd", "crsr", "googl","logi", "msft", "nvda","TM","tsla"]
tickerPrices = {}
results = {}


# API Key  NT4KFTZJUN0QODV
def createData(ticker):

        
        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ ticker + '&outputsize=full&apikey=8NT4KFTZJUN0QODV'
        r = requests.get(url)
        tickerjson = json.loads(r.text)
        key1 = "Time Series (Daily)" # dictionary with all prices by date
        key2 = '4. close'
        
        
        
        writeLines = []
        for date in tickerjson[key1]:
            writeLines.append(date + ", " + tickerjson[key1][date][key2]+ "\n")
        writeLines = writeLines[::-1]
        
        csvFile = open(ticker + ".csv", "w")
        csvFile.writelines(writeLines)
        



def appendData(ticker):
        
         url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ ticker + '&outputsize=full&apikey=8NT4KFTZJUN0QODV'
         r = requests.get(url)
         tickerjson = json.loads(r.text)
         key1 = "Time Series (Daily)" # dictionary with all prices by date
         key2 = '4. close'
        
         csvFile = open(ticker + ".csv", "r")
         lines = csvFile.readlines()
         lastDate = lines[-1].split(",")[0]
        
         newLines = []
         for date in tickerjson[key1]:
            if date == lastDate:
                break
            newLines.append(date + ", " + tickerjson[key1][date][key2] + "\n")
            
         newLines = newLines[::-1]
         csvFile = open(ticker + ".csv", "a")
         csvFile.writelines(newLines)
         
         
         
def meanReversionStrategy(prices):
    
    
    #initialize variables
    canBuy = True
    totalProfit = 0
    buy = 0
    profit = 0
    sell = 0
    avg = 0
    firstBuy = True
    start = 0
    res = []


    for i in range(len(prices)): #Creating loop with range to make indexing easier. 
    
    
        if i >= 5: #Must be at least 5 days for rolling average
            avg = (prices[i - 1] + prices[i - 2] + prices[i - 3] + prices[i - 4] + prices[i - 5]) /5
            price = round(prices[i],2)
       
    
            
            
            if price < avg * .98 and canBuy == True:  # Buy.  canBuy if not holding a stock already. 
                if firstBuy == True:#First time buying to keep track of original price. 
                    start = price
                    
                    buy = price
                    firstBuy = False
                else:
                    buy = price
                    if prices[i] == prices[len(prices)-1]:
                        print("YOU SHOULD BUY THIS TODAY")
                    
                    
            
            if price > (avg * 1.02):  #Sell- can only sell if currently holding a stock 
                sell = price
                profit = sell - buy
                totalProfit +=profit #Track total profit by incrementing by each sale's profit. 
                if prices[i] == prices[len(prices)-1]:
                    print("YOU SHOULD SELL THIS TODAY")
                
                
                
                
    percent = (totalProfit/start) * 100
    
   #print final results
    
    print("-----------------------------\nTotal Profit: " + str(round(totalProfit,2)) + " \n First buy: " + str(round(start,2)) + " \n Percentage return: " + str(round(percent,2))  + "%  \n \n")
    #return values so we can reference in final call
    return round(totalProfit,2), round(percent,2)  
        
        
        
        
        
def bollinger(prices):       
        
        #initialize variables
    canBuy = True
    totalProfit = 0
    profit = 0
    sell = 0
    avg = 0
    firstBuy = True
    start = 0
    res = []
    
    for i in range(len(prices)): #Creating loop with range to make indexing easier. 


        if i >= 5: #Must be at least 5 days for rolling average
            avg = (prices[i - 1] + prices[i - 2] + prices[i - 3] + prices[i - 4] + prices[i - 5]) /5
            price = round(prices[i],2)
       
    
            
            
            if price > avg * 1.05  and canBuy == True:  # Buy.  canBuy if not holding a stock already. 
                if firstBuy == True:#First time buying to keep track of original price. 
                    start = price
                    canBuy = False
                    buy = price
                    firstBuy = False
                else:
                    buy = price
                    canBuy = False
                    
            
            if price < avg * .95 and canBuy == False:  #Sell- can only sell if currently holding a stock 
                sell = price
                profit = sell - buy
                totalProfit +=profit #Track total profit by incrementing by each sale's profit. 
                canBuy = True
                
                
                
    percent = (totalProfit/start) * 100
    
    print("-----------------------------\nTotal Profit: " + str(round(totalProfit,2)) + " \n First buy: " + str(round(start,2)) + " \n Percentage return: " + str(round(percent,2))  + "%  \n \n")
    return round(totalProfit,2), round(percent,2)    
        
        
        
        
        
        
def simpleMovingAverageStrategy(prices):

    #initialize variables
    canBuy = True
    totalProfit = 0
    profit = 0
    sell = 0
    avg = 0
    firstBuy = True
    start = 0
    res = []
    
    for i in range(len(prices)): #Creating loop with range to make indexing easier. 


        if i >= 5: #Must be at least 5 days for rolling average
            avg = (prices[i - 1] + prices[i - 2] + prices[i - 3] + prices[i - 4] + prices[i - 5]) /5
            price = round(prices[i],2)
       
    
            
            
            if price > avg  and canBuy == True:  # Buy.  canBuy if not holding a stock already. 
                if firstBuy == True:#First time buying to keep track of original price. 
                    start = price
                    canBuy = False
                    buy = price
                    firstBuy = False
                else:
                    buy = price
                    canBuy = False
                    
            
            if price < avg and canBuy == False:  #Sell- can only sell if currently holding a stock 
                sell = price
                profit = sell - buy
                totalProfit +=profit #Track total profit by incrementing by each sale's profit. 
                canBuy = True
                
              
                
    percent = (totalProfit/start) * 100
    
    print("-----------------------------\nTotal Profit: " + str(round(totalProfit,2)) + " \n First buy: " + str(round(start,2)) + " \n Percentage return: " + str(round(percent,2))  + "%  \n \n")
    return round(totalProfit,2), round(percent,2)
    
    
    
def saveResults(resdict):
    for i in tickers:
        file = open("/home/ec2-user/environment/" + i + ".csv", "r")
        lines = file.readlines()
        
        prices = [float(line.split(",")[1]) for line in lines]
        tickerPrices[str(i) + "_prices"] = prices
    for ticker in tickerPrices.keys():
        print(str(ticker).split("_")[0].upper() + " " + "Mean Reversion Strategy output:")  # Title returns in output
        data = meanReversionStrategy(tickerPrices[ticker])
        profit = data[0]
        percent = data[1]  # Setting variables for return values to store in dictionary

        results[str(ticker).split("_")[0].upper() + "_mr_profit_with_shorting"] = profit  #Adding names for keys in dictionary
        results[str(ticker).split("_")[0].upper() + "_mr_return_with_shorting"] = percent
    
        
        print(str(ticker).split("_")[0].upper() + " " + "Simple moving average output:")
        data = simpleMovingAverageStrategy(tickerPrices[ticker])
        profitsm = data[0]
        percentsm = data[1]
        
        results[str(ticker).split("_")[0].upper() + "_sma_profit"] = profitsm
        results[str(ticker).split("_")[0].upper() + "_sma_return"] = percentsm
        
        print(str(ticker).split("_")[0].upper() + " " + "Bollinger Bands output:")
        data = bollinger(tickerPrices[ticker])
        profitb = data[0]
        percentb = data[1]
        
        results[str(ticker).split("_")[0].upper() + "_bollinger_profit"] = profitb
        results[str(ticker).split("_")[0].upper() + "_bollinger_return"] = percentb
        if profit > profitsm and profit > profitb:
            results[str(ticker).split("_")[0].upper() + "_Most_Profitable"] = "Mean Reversion"
        elif profitsm > profit and profitsm > profitb:
            results[str(ticker).split("_")[0].upper() + "_Most_Profitable"] = "Simple Moving Average"
        elif profitb > profit and profitb > profitsm:
            results[str(ticker).split("_")[0].upper() + "_Most_Profitable"] = "Bollinger Bands"

    json.dump(results, open("results.json", "w"), indent = 4)

            


for ticker in tickers:
    #createData(ticker)
    appendData(ticker)
    time.sleep(12)
    saveResults(results)