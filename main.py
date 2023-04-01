import requests

class CheckInputNumber():
    def __init__(self):
        print('Welcome to Name Generator !')
        userInput = int(input('Enter a Number between 1-100 : '))
        self.userInput = userInput

    def Check(self):
        if self.userInput < 1 or self.userInput > 100:
            print(f'{self.userInput} not between 1-100')
            return False
        else:
            print(f'OK , here is a {self.userInput} names..')
            return True


class PrintName(CheckInputNumber):
    def generate_names(self):
        if not self.Check():
            return

        counter = 0
        while counter < self.userInput:
            res = requests.get('https://randomuser.me/api/')
            nameJson = res.json()
            name = nameJson['results'][0]['name']['first']
            print(name)
            counter += 1


printName = PrintName()
printName.generate_names()
