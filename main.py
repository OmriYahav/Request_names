import requests

# Define a class to check user input.
class CheckInputNumber():
    def __init__(self):
        # Prompt the user to enter a number between 1-100.
        print('Welcome to Name Generator !')
        userInput = int(input('Enter a Number between 1-100 : '))
        self.userInput = userInput

    # Define a method to validate user input.
    def InputValidation(self):
        # Check if user input is between 1-100.
        if self.userInput < 1 or self.userInput > 100:
            print(f'{self.userInput} not between 1-100')
            return False
        else:
            print(f'OK , here is a {self.userInput} names..')
            return True


# Define a class to print random names.
class PrintName(CheckInputNumber):
    # Define a method to generate random names.
    def generate_names(self):
        # Call the InputValidation method to validate user input.
        if not self.InputValidation():
            return

        # Generate the specified number of names using the Random User API.
        counter = 0
        while counter < self.userInput:
            # Make a request to the Random User API using the requests library.
            res = requests.get('https://randomuser.me/api/')
            # Convert the JSON response into a Python dictionary
            nameJson = res.json()
            # Retrieve the first name from the dictionary.
            name = nameJson['results'][0]['name']['first']
            # Print the name to the console.
            print(name)
            # Increment the counter.
            counter += 1


# Create an instance of the PrintName class and call the generate_names method.
printName = PrintName()
printName.generate_names()
