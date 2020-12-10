# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:56:31 2020

@author: eardi
"""
import csv
#filepath = "C:\\Users\\eardi\\OneDrive\\Documents\\Bootcamp\\Python\\Resource\\budget_data.csv"
filepath = '..\\Resources\\budget_data.csv'
 
with open(filepath, 'r') as text:
    reader = csv.reader(text, delimiter=",")    
    next(reader)
    DateCnt = 0
    Net = 0
    Profit = 0
    Loss = 0
    Avg = 0
    max_ = 0
    TL_Difference = 0
    for row in reader:      
      Date_Set = row[0]      
      DateCnt += 1    
      
      Monthly_Tl = float(row[1])
      Net += Monthly_Tl 
      if Monthly_Tl > 0:
          Profit += Monthly_Tl
      if Monthly_Tl < 0:
          Loss += Monthly_Tl
    
    TL_Difference = (Profit / Loss * DateCnt)
    print (TL_Difference)
    Total_Net = '${:,.2f}'.format(Net)
    Mean =  '${:,.2f}'.format((TL_Difference)) 
        
    print("Total Months: ",DateCnt) 
    print("Net Total : ",Total_Net)
    print("Average of Changes: ", Mean)   
    #print("Greatest Increase in Profits: ", max(row) )
    #print("Greatest Decrease in Profits: ", min(row))     
