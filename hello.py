def hello(name):
    print(f"Hello, {name}! Nice to meet you.")

def greeting():
    name = input('Sorry, what is your name? ')
    hello(name)

def create_person():
    person = {}
    print('Hello, welcome M&L Company interview!')
    print('Please enter the following data about you')
    person.name = input('Your name: ')
    person.age = int(input('Your age: '))
    person.opcupation = input('Your ocupation: ')
    person.other_information = input('Other information about you')
    return person

def main():
    person = create_person()
    hello(person.name)

   
if __name__ == "__main__":
    main()
