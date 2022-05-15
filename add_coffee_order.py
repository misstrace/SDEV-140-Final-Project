# This a module program that adds coffee orders to
# the coffee.txt file.
# Variables:
    # cType: the users coffee type (str)
    # flavoring: the users coffee flavoring (str)
    # temp: the users coffee temperature (int)
    # espresso: the users coffee strength (int)
    # size: the users coffee size (int)
    # creamer: the users creamer choice (int)


def getSize(done):
    size = int(input('What coffee size? Enter: 1 - for Small, 2 - for Med and 3 - for Large: '))
    # Validation
    while not done:
        if size != 1 and size != 2 and size != 3:
           size = int(input("You can only enter 1, 2 or 3. Please enter 1 - for Small, 2 - for Med and 3 - for Large: "))
        else:
            done = True
    return size

def getTemp(done):
    temp = int(input('Would you like it hot or cold? Please enter 1 - for Hot and 2 - for Cold: '))
    # Validation
    while not done:
        if temp != 1 and temp != 2:
           temp = int(input("You can only enter 1 or 2. Please enter 1 - for Hot and 2 - for Cold: "))
        else:
            done = True
    return temp

def getEspresso(done):
    espresso = int(input('How many extra shots of expresso would you like to add? (Enter 0 - for None): '))
    # Validation
    while not done:
        if espresso < 0: 
           espresso = int(input("Expresso shots cannot be negative. How many extra shots of expresso would you like to add? (Enter 0 - for None): "))
        else:
            done= True
    return espresso

def getCreamer(done):
    creamer = int(input('Would you like room for creamer? Please enter 1 - for Yes and 2 - for None: '))
    # Validation
    while not done:
        if creamer != 1 and creamer != 2:
           creamer = int(input("You can only enter 1 or 2. Please enter 1 - for Yes and 2 - for None: "))
        else:
            done = True
    return creamer

def add():
    # Get the coffee record data.
    done = False
    print('Enter the following coffee data: ')
    cType = input('Enter the coffee type (User enters the name of Coffee): ')
    flavoring = input('Enter the coffee flavoring (Enter None - for No Flavor): ')
    temp = getTemp(done)
    espresso = getEspresso(done)
    size = getSize(done)
    creamer = getCreamer(done)
    

#Forming string for file
    description = "\n\nType: " + cType + "\nFlavoring: " + flavoring + "\nTemperature: "

    if temp == 1:
        description += "Hot"
    else :
        description += "Cold"

    description += "\nExtra Expresso Shots: " + str(espresso) + "\nSize: "

    if size == 1:
        description += "Small"
    elif size == 2:
        description += "Medium"
    else:
        description += "Large"

    description += "\nRoom for creamer: "

    if creamer == 1:
        description += "Yes"
    else:
        description += "No"

    # Writing to file.
    coffee_file = open('coffee.txt', 'a')
    coffee_file.write(description)
    coffee_file.close()



