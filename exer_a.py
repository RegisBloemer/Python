import json

FILE_PATH = 'exer.json'

class People: 
    def __init__(self, name, hight, weight, cpf):
        self.name = name
        self.hight = hight
        self.weight = weight
        self.cpf = cpf
    
p1 = People('João', 1.70, '80', 38928989283)  
p2 = People('Régis', 1.90, '79', 45645645645)  
p3 = People('Luan', 1.50, '69', 34534534534)  
bd = [vars(p1), p2.__dict__, vars(p3)]

def make_dump(): 
    with open(FILE_PATH, 'w') as file:
        print('Making DUMP')
        json.dump(bd, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('He is the main')
    make_dump()