# data from https://datahub.io/core/co2-fossil-by-nation#data
file = open("co2-by-nation.csv", "r")
   
# column number corresponding to different data fields
IDX_YEAR = 0          # Year
IDX_COUNTRY = 1       # string - Nation
IDX_TOTAL_FUELS = 2   # Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)
IDX_SOLID_FUEL = 3    # Carbon emissions from solid fuel consumption
IDX_LIQUID_FUEL = 4   # Carbon emissions from liquid fuel consumption
IDX_GAS_FUEL = 5      # Carbon emissions from gas fuel consumption
IDX_CEMENT = 6        # Carbon emissions from cement production
IDX_GAS_FLARING = 7   # Carbon emissions from gas flaring
IDX_PER_CAPITY = 8    # Per capita carbon emissions (metric tons of carbon; after 1949 only)
IDX_BUNKER_FUELS = 9  # Carbon emissions from bunker fuels (not included in total)
   
perYear = {} # "2014": 5200000 each year dictionary

perCountry = {} # "United States" : 0398464893... using to eventually find top 5 countries with the most carbon emissions. 
   
file.readline() # reading in that first line that just contains header columns
for line in file:
    lst = line.split(",") # we are going to split on the comma because we know the data is seperated by a comma
       
    year = lst[IDX_YEAR] # were taking the year for the particluar record for a string. 
    total = int(lst[IDX_TOTAL_FUELS])
    country = lst[IDX_COUNTRY]
       
    if year in perYear:
        perYear[year] += total # if we already have an entry from another contry so we just want to increase the vaule 
    else:
        perYear[year] = total # if we have not already encountered an entry 
    
    if country in perCountry:
        perCountry[country] = perCountry[country] + total
    else:
        perCountry[country] = total
   
for yr in range(2000, 2015): # for the last __ years what have the carbon emssions been
    #print("year: ", yr)
    #print("million metric tons of carbon: ", perYear[str(yr)] )
    print("%u: %s million metric tons of C" % (yr, perYear[str(yr)])) # telling python what vaules we want to put in
   
allTotals = list(perCountry.values()) # convert into a list
allTotals.sort()       # ascending order 
allTotals.reverse()    # so we change to descending order
topFive = allTotals[4] # the 5th largest number

for country in perCountry:
    val = perCountry[country]
    if (val >= topFive):
        print("%s : %u million metric tons of C" % (country, perCountry[country]) )
    
# %u and %s placeholders it tells python what type of infomartion to expect.
file.close() # we tell the computer we are done with the file closing it 