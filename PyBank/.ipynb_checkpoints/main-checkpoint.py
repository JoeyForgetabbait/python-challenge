#import operating system for methods
import os
import csv

#for calculating total profit / profit-loss change between each month 
netprftlossprmth = 0 #sum proft/loss per month
prftlossprevmth = 0 #prior month profit/loss
prftlosscrntmth = 0 #currnt month profit/loss
mnthprftchng = 0 #change in profit loss between each month (need top two variables for that)
mnthprftchngsum = 0 # totals each monthly profit/loss change 
mnthpfrtchngmean = 0 #becomes final value, holding the # for each monthly profit/loss chng)

greatestmnthchng = 0 #holds the greatest increase in monthly profit/loss chng value)
greatestmnthchngdt = ' ' #holds the month of the greatest increase in monthy/profit chng
weakmnthchng = 0 #holds the greatest decrease in monthly profit/loss chng value)
weakmnthchngdt = ' ' #holds the month of the greatest increase in monthy/profit chng

#for calculating total months
summonths = 0 #total number of months 

#set path to data
pydata = os.path.join("Resources", "budget_data.csv")

#open data with csv.reader() / Make sure data is there
with open(pydata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(csvheader) #make sure!!

    for row in csvreader:
        if summonths == 0:
            prftlossprevmth = int(row[1])
        else: 
            prftlosscrntmth = int(row[1])
            mnthprftchng = prftlosscrntmth - prftlossprevmth
            #update object holding each change value 
            mnthpfrtchngmean = mnthpfrtchngmean + 1

            mnthprftchngsum = mnthprftchngsum + mnthprftchng
            mnthchngaverage = round(mnthprftchngsum/mnthpfrtchngmean,2)

            #change previous mnthly profit/loss value 
            prftlossprevmth = prftlosscrntmth

            if mnthprftchng > greatestmnthchng:
                greatestmnthchng = mnthprftchng
                greatestmnthchngdt = row[0]

            if mnthprftchng < weakmnthchng:
                weakmnthchng = mnthprftchng
                weakmnthchngdt = row[0]

        netprftlossprmth = netprftlossprmth + int(row[1])
        summonths = summonths + 1 

#begin printing results 
print("Financial Analysis")
print()
print("----------------------------")
print()
print("Total Months: " + str(summonths))
print()
print("Total: $" + str(netprftlossprmth))
print()
print("Averge Change: " + "$" + str(mnthchngaverage))
print()
print("Greatest Increase in Profits: " + greatestmnthchngdt + " ($" + str(greatestmnthchng) + ")")
print()
print("Greatest Decrease in Profits: " + weakmnthchngdt + " ($" + str(weakmnthchng) + ")")


txtoutput = os.path.join("Analysis", "Pybank.txt")
with open(txtoutput,'w') as pybankanalysis:
    
    pybankanalysis.write("Financial Analysis\n")
    
    pybankanalysis.write("----------------------------\n")
    
    pybankanalysis.write("Total Months: " + str(summonths) + "\n")
    
    pybankanalysis.write("Total: $" + str(netprftlossprmth) + "\n")
    
    pybankanalysis.write("Averge Change: " + "$" + str(mnthchngaverage) + "\n")
    
    pybankanalysis.write("Greatest Increase in Profits: " + greatestmnthchngdt + " ($" + str(greatestmnthchng) + ")" + "\n")
    
    pybankanalysis.write("Greatest Decrease in Profits: " + weakmnthchngdt + " ($" + str(weakmnthchng) + ")" + "\n")


