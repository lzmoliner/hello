def hello(name):
    print(f"Hello, {name}! Nice to meet you.")

def greeting():
    name = input('Sorry, what is your name? ')
    hello(name)

def main():
    greeting()
   
if __name__ == "__main__":
    main()
