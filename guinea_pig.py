class GuineaPig: 
    def __init__(self, name: str, color: str, weight: float): 
        self.name = name 
        self.color = color
        self.weight = weight
        self.price = 20.0

    def squeak(self) -> str: 
        return f'{self.name} the {self.color} guinea pig squeaks!'
    
class Snake:
    def __init__(self, name: str, color: str, weight: float):
        self.name = name
        self.color = color
        self.weight= weight
        self.price = 30
        
    def hiss(self) -> str:
        return f'{self.name} the {self.color} snake hisses!'
    
class Customer:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
    
    

if __name__ == '__main__':
    print('welcome to kaelyn\'s pet shop!')

    name = input('Enter your name: ')
    budget = input('What is your current budget? (float format, ex: 10.0) ')

    customer = Customer(name, budget)

    print(f'Welcome {customer.name}! You have a budget of ${customer.budget}.')
    
    potato = GuineaPig('Potato', 'calico', 1.2)
    print(f'You can adopt {potato.name} for ${potato.price}!')

    print(potato.squeak())

    bun = GuineaPig('Bun', 'black', 1.7) 

    print(bun.squeak()) 

    pea = GuineaPig('Pea', 'white', 2.0) 

    print(pea.squeak())

    dragon = Snake('Dragon', 'green', 5.0)
        
    print(dragon.hiss())
