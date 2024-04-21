# let's ask the user to enter the ticker name of a stock
ticker = 'ntf'

#url = 'http://csweb.wooster.edu/hguarnera/cs100/assignments/in-class-25.html'
url = 'https://finviz.com/quote.ashx?t=' + ticker

# To get access to this particular website, we will need to define a header.
headers = {}
headers['User-Agent'] = "Chrome/24.0.1312.27 Safari/537.17"

# requesting access to the website
req = urllib.request.Request(url, headers = headers)

#the response of our request
resp = urllib.request.urlopen(req)

# print the http code, 200 is okey
#print(resp.code)

#Reading the response
respData = resp.readlines()

# Putting info into a file
infile = open("stock_data.txt", "w")
for line in respData:
    #print(line) # gives back as a byte string
    i = line.decode("UTF-8")
    #print(i)
    infile.write(i)
infile.close()

file = open("stock_data.txt", "r")
file.readline()
info = {}

for line in file:
    if 'Price' in line:
#      print(line)
        Financial_Ratio = line.split('body')[2].split('] ')[0].split('=[')[1]
#         print(Financial_Ratio)
        Value = line.split('<b>')[1].split('</b>')[0]
        # print(Value)
        info[Financial_Ratio] = Value
# print(info)
Value_listing = list(info.values())
# print(Value_listing)
Financial_Ratio_listing = list(info.keys())

j = -1
for i in Value_listing:
    j +=1
    if '<span class' in i:
        i = i.split('>')[1].split('<')[0]
        Value_listing[j] = i
        
stock_info = {} 
for x in Financial_Ratio_listing: 
    for y in Value_listing: 
        stock_info[x] = y 
print(stock_info)
        
    
file.close()


