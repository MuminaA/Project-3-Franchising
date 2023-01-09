# imports
import csv

# defined functions
def count_by_state(restaurants, state_abri):
    count = 0
    for i in restaurants.values():
        if i[0] == state_abri.upper() or state_abri.upper() == 'US':
            count += 1
    return count
    #pass

def count_by_style(restaurants, rest_style):
    count = 0
    for i in restaurants.values():
        if i[1] == rest_style or rest_style == 'any':
            count += 1
    return count
    #pass

def avg_by_state(restaurants, state_abri):
    count = 0
    revenue = 0
    for i in restaurants.values():
        if i[0] == state_abri.upper() or state_abri.upper() == 'US':
             revenue += float(i[2])
             count += 1
    if count == 0:
        return 0
    return revenue/count
    
def avg_by_style(restaurants, rest_style):
    count = 0
    revenue = 0
    for i in restaurants.values():
        if i[1] == rest_style.lower() or rest_style.lower() == 'any':
             revenue += float(i[2])
             count += 1
    if count == 0:
        return 0
    return revenue/count
    
def print_lowest_revenue(restaurants):
    lowest_revenue = float(list(restaurants.values())[0][2])
    state = ''
    restuarant = ''
    style = ''
    for i in restaurants:
        if float(restaurants[i][2]) < lowest_revenue:
            lowest_revenue = float(restaurants[i][2])
            state = restaurants[i][0]
            style = restaurants[i][1]
            restaurant = i
    return lowest_revenue, state, restaurant, style

def print_menu():
    print('(1) Get the number of restaurants by state')
    print('(2) Get the number of restaurants by style')
    print('(3) Get the average revenue of restaurants by state')
    print('(4) Get the average revenue of restaurants by restaurant style')
    print('(5) Print restaurant with lowest revenue')
    print('(6) Exit')

###########################################################################################################
# main code
if __name__ == '__main__':
    
    # below is a list containing all of the valid state abbreviations in the United States
    States = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "US"]
              
    Styles = ["dine in", "express", "truck", "any"]
    
    #get file
    file_name = input('Enter the filename of the file containing restaurants data:\n')

    restaurants = {}
    
    #read file
    with open(file_name, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        first_row = True
        for id in csv_reader:
            if first_row:
                first_row = False
                #I got this section from the book and understand how it is being used
                continue
            
            restaurants[id[0]] = [id[1], id[2], id[3]]
            
            #print(id)
    #print menu
    print_menu()
    #get choice
    choice = int(input('Enter a selection 1-6:\n'))
    
    while choice != 6:
        if choice == 1:
            while choice == 1:
                #prompt the user for a state and expects the input to be a two-character state abbreviation.
                state_abri = input("Enter a 2 letter state abbreviation, or 'US' for all restaurants in the U.S.:\n")
                if state_abri.upper() in States:
                    count = count_by_state(restaurants, state_abri)
                    print(f'There are {count} Sparty Burger Restaurants in {state_abri.upper()}')
                    print_menu()
                    choice = 0
                else:
                    print(f'{state_abri} is not a valid state abbreviation')
        elif choice == 2:
            while choice == 2:
            #the program should similarly prompt the user for a restaurant style
                rest_style = input("Enter the restaurant style, or 'any' for all styles:\n").lower()
                if rest_style.lower() in Styles:
                    count = count_by_style(restaurants, rest_style)
                    print(f'There are {count} Sparty Burger {rest_style} style restaurants')
                    print_menu()
                    choice = 0
                else:
                    print(f'{rest_style} is not a valid restaurant style')
        elif choice == 3:
            while choice == 3:
                #prompt the user for a state and expects the input to be a two-character state abbreviation.
                state_abri = input("Enter a 2 letter state abbreviation, or 'US' for all restaurants in the U.S.:\n")
                if state_abri.upper() in States:
                    revenue = avg_by_state(restaurants, state_abri)
                    print(f'The average revenue in {state_abri.upper()} is ${revenue:.2f}')
                    print_menu()
                    choice = 0
                else:
                    print(f'{state_abri} is not a valid state abbreviation')
        elif choice == 4:
            while choice == 4:
                #the program should similarly prompt the user for a restaurant style
                rest_style = input("Enter the restaurant style, or 'any' for all styles:\n")
                if rest_style.lower() in Styles:
                    revenue = avg_by_style(restaurants, rest_style)
                    print(f'The average revenue of {rest_style.lower()} style restaurants is ${revenue:.2f}')
                    print_menu()
                    choice = 0
                else:
                    print(f'{rest_style} is not a valid restaurant style')
        elif choice == 5:
            lowest_revenue, state, restaurant, style = print_lowest_revenue(restaurants)
            print(f'Lowest Revenue: Restaurant {restaurant} in {state}, {style} style, had ${lowest_revenue:.2f}')
            print_menu()
        else:
            print_menu()
            
        choice = int(input('Enter a selection 1-6:\n'))