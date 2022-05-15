# Program Name: Huckins_Tracey_Final-Project
# Author: Tracey Huckins
# Date:
# Program Summary: Displays the users coffee order or orders into a seperate text file. 
# Variables:
    # choice: The users choice to put another coffee order in
    # coffe_file: the variable for the coffee.txt file
    # done: bool loop control 

import add_coffee_order

def getChoice(done):
    choice = int(input("Would you like to place another coffee order? Enter: 1 - for Yes or 2 No: "))
    # Validation
    while not done:
        if choice != 1 and choice != 2:
           choice = int(input("You can only enter 1 or 2. Please enter: 1 - for Yes or 2 - for No."))
        else:
            done= True
    return choice

def main():
    #Adding coffee order title
    coffee_file = open('coffee.txt', 'w')
    coffee_file.write("Coffee order: ")
    coffee_file.close()
    # Initialize the loop control
    choice = 1
    done = False
    
    # Loop that shows the coffee orders
    # Open the coffee.txt file in append mode.
    while choice == 1:
        done = False
        # Append the data to the file.
        add_coffee_order.add()
        choice = getChoice(done)
        
    print("End of program.")
    
main()



        



