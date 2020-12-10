# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:56:31 2020

@author: eardi
"""
import csv
#filepath = "C:\\Users\\eardi\\OneDrive\\Documents\\Bootcamp\\Python\\Resource\\election_data.csv"
filepath = '..\\Resources\\election_data.csv'
 
with open(filepath, 'r') as text:
    reader = csv.reader(text, delimiter=",")    
    next(reader)
    
    Total_Vote = 0
    Khan_Vote = 0
    Khan_Percent = 0
    Correy_Vote = 0
    Correy_Percent = 0
    Li_Vote = 0
    Li_Percent = 0
    Tooley_Vote = 0
    Tooley_Percent = 0    
    
    for row in reader:      
      Vote = (row[0])
      Candidate = (row[2])
      Total_Vote += 1
      if (Candidate == "Khan"):
          Khan_Vote +=1          
      elif (Candidate == "Correy"):
          Correy_Vote +=1
      elif (Candidate == "Li"):
          Li_Vote +=1
      elif (Candidate == "O'Tooley"):
          Tooley_Vote +=1
     
      if Khan_Vote > Correy_Vote and Khan_Vote > Li_Vote and Khan_Vote > Tooley_Vote :
              Winner = "Khan"
      elif Correy_Vote > Khan_Vote and Correy_Vote > Li_Vote and Correy_Vote > Tooley_Vote :
              Winner = "Correy"
      elif Li_Vote > Khan_Vote and Li_Vote > Correy_Vote and Li_Vote > Tooley_Vote :
              Winner = "Li"
      elif Tooley_Vote > Khan_Vote and Tooley_Vote > Correy_Vote and Tooley_Vote > Li_Vote :
              Winner = "O'Tooley"

    Khan_Percent = "{:,.3f}".format((Khan_Vote/Total_Vote)*100)
    Correy_Percent = "{:,.3f}".format((Correy_Vote/Total_Vote)*100)
    Li_Percent = "{:,.3f}".format((Li_Vote/Total_Vote)*100)
    Tooley_Percent = "{:,.3f}".format((Tooley_Vote/Total_Vote)*100)
    print("Election Results")
    print("-------------------------------")
    print("Total Votes: ", Total_Vote)
    print("-------------------------------")
    print("Khan: ", Khan_Percent+"% (",Khan_Vote,")")
    print("Correy: ", str(Correy_Percent) +"% (" , Correy_Vote , ")")
    print("Li: ", str(Li_Percent) +"% (" , Li_Vote , ")")
    print("O'Tooley: ", str(Tooley_Percent) + "% (" , Tooley_Vote , ")")
    print("-------------------------------")
    print("Winner: ", Winner)
    print("-------------------------------")