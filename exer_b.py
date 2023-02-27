import json
from exer_a import People, make_dump,FILE_PATH

with open(FILE_PATH, 'r') as file:
    people = json.load(file)
    p1 = People(**people[0])
    p2 = People(**people[1])
    p3 = People(**people[2])

    print(p1.name, p1.hight)
    print(p2.name, p2.hight)
    print(p3.name, p3.hight)
