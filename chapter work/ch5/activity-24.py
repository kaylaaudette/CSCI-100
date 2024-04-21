# Kayla Audette

# DATA INDEX VALUES
# Use to access certain data fields in the list
GAME_TITLE = 0
PUBLISHER = 1
REVIEW_SCORE = 2
USED_PRICE = 3
CONSOLE_NAME = 4
ESRB_RATING = 5
RELEASE_YEAR = 6


# return game data as a list of records
# where each record is a list of string fields
def get_data():
    data_records = []
    game_data = open('video_games.tsv', 'r')
    
    # dispose of TSV header
    game_data.readline()
        
    # collect all records
    for line in game_data:
        allFields = line.split('\t')   # separated by tabs
        allFields[-1] = allFields[-1].replace("\n","") # get rid of newline
        data_records.append(allFields) # each record contains list of all fields
    
    game_data.close()
    return data_records


# return the average price of a Nintendo game
def avg_nintendo_game_price():
    count = 0          # count of games
    running_total = 0  # running total of prices used to calculate average

    # Go through each record from the file.
    # Each record is a list of fields.
    for record in get_data():

        # Use the PUBLISHER index to get the name of the publisher
        if record[PUBLISHER] == 'Nintendo':
            # Use the USED_PRICE index to get the used cost of the game
            running_total += float(record[USED_PRICE])
            count += 1
    
    # Use the count and the sum of all prices to compute an average
    # Then, round to nearest 2 decimal places
    avg = running_total / count
    return round(avg, 2)

# TODO: Define your functions here (all function definitions MUST
#    return data and NOT use the print function)

# What is the lowest rated
def worst_game():
    game_data = get_data()
    worstSofar = int(game_data[0][2])
    title = game_data[0][GAME_TITLE]
    for record in get_data():
        if int(record[REVIEW_SCORE]) < worstSofar:
            worstSofar = int(record[REVIEW_SCORE])
            title = record[GAME_TITLE]
    return title

def best_game():
    game_data = get_data()
    bestSofar = int(game_data[0][2])
    title = game_data[0][GAME_TITLE]
    for record in get_data():
        if int(record[REVIEW_SCORE]) > bestSofar:
            bestSofar = int(record[REVIEW_SCORE])
            title = record[GAME_TITLE]
    return title

def most_expensive():
    game_data = get_data()
    moneySofar = float(game_data[0][3]) #index the price is
    title = game_data[0][GAME_TITLE]
    for record in get_data():
        if float(record[USED_PRICE]) > moneySofar:
            moneySofar = float(record[USED_PRICE]) #float price with decimals
            title = record[GAME_TITLE]
    return title

def least_expensive():
    game_data = get_data()
    moneySofar = float(game_data[0][3]) #index the price is
    title = game_data[0][GAME_TITLE]
    for record in get_data():
        if float(record[USED_PRICE]) < moneySofar:
            moneySofar = float(record[USED_PRICE]) #float price with decimals
            title = record[GAME_TITLE]
    return title

# TODO: Call the functions you defined here and print the data they return neatly
# For example, this prints the result of the function call to find the average nintendo price
print("Average price of Nintendo Games: $ %s" % (avg_nintendo_game_price()) )
print("Lowest Rated Game: %s" % (worst_game()) )
print("Highest Rated Game: %s" % (best_game()) )
print("Most Expensive Used Game: %s" % (most_expensive()) )
print("Least Expensive Used Game: %s" % (least_expensive()) )
