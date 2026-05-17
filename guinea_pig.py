class GuineaPig: 
    def __init__(self, name: str, color: str, weight: float): 
        self.name = name 
        self.color = color
        self.weight = weight

    def squeak(self) -> str: 
        return f'{self.name} the {self.color} guinea pig squeaks!'
    

if __name__ == '__main__':
    print('welcome to kaelyn\'s pet shop!')
    
    potato = GuineaPig('Potato', 'calico', 1.2)

    print(potato.squeak())

    bun = GuineaPig('Bun', 'black', 1.7) 

    print(bun.squeak()) 

    pea = GuineaPig('Pea', 'white', 2.0) 

    print(pea.squeak())
