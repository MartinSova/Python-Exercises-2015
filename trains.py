# When my function reads the values for how many people entered/left the train and 
# how many people are waiting at the station, the value for how many people are aboard the
# train after each station is appended to a list "aboardeach" by using
# a cumulative sum "aboardsum". Then, I compare the values in the list "aboardeach"
# to the values in the list "waitingateach" (number of people waiting at each station) for the
# same stations using a for loop with zip, which allows me to determine whether the given
# data is plausible, for which then I return either "possible" or "impossible".

from sys import argv

if len(argv) < 2:
    print("No data file given")
    exit(1)

script, filename = argv

def read_data(filename):
    
    """This function reads data from a file in argv[1]. The capacity (C) and the number of stations (n)
    are read as the first value on the first line, and second value on the first line, respectively (they
    are read as integers). The rest of the information (how many people entered/left the train and waited at
    the station) is appended into the list "data", where each new line of the file (apart from the first line)
    is recognized as new station."""
    
    with open(filename, 'r') as f:
        first = f.readline()
        C, n = first.split()
        C = int(C)
        n = int(n)
        data = []
        for i in range(n):
            line = f.readline()
            data.append([int(i) for i in line.split()])
    return C, n, data

def is_possible(C, n, data):
    
    """This function tests whether data on how many people entered, left and waited when
    a train passed a station is possible or impossible. I append data to lists based on how
    many people are aboard, and how many waited, which allows me to check whether the values
    are possible when compared to the capacity, or when the lists are compared to each other."""
    
    if n < 2 or n > 100:
    # an 'if' statement to check if number of stations is out of range (2<=n<=100)
        
        return("impossible")

    else:
        aboardeach = []
        # values for how many people are aboard train after each station will be appended to 'aboardeach' list
        
        aboardsum = 0
        waitingateach = [] 
        for station in data:
            left = station[0] 
            entered = station[1] 
            waiting = station[2]
            aboardsum += entered-left
            # cumulative sum of people abord for each station is appended to list 'aboardeach'

            aboardeach.append(aboardsum) 
            waitingateach.append(waiting)
            #values for number of people waiting at each station are appended to list 'waitingateach'
        
        if aboardsum!=0:
        # cumulative sum of how many people entered-left must equal '0' after last station
            return("impossible")
        else:
            for i in aboardeach: 
                if i>C or i<0:
                # if statement checks if number of people aboard greater than train's capacity or had a negative value for each station
                    
                    return("impossible")
                else: 
                    for x, y in zip(aboardeach, waitingateach):
                    # 'for' checks values of 'aboardeach' and 'waitingateach' for the same stations

                        if x < C and y > 0:
                        # if train was ever under capacity and people still waited, n is set to True
                            n = True 
                    if n == True:
                        return("impossible")
                    else:
                        return("possible") 

C, n, data = read_data(filename)
print(is_possible(C, n, data))

