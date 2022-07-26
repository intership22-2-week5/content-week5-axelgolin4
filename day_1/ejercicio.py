DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    # 1. obtener todos los desarrolladores de python
    list = [x for x in DATA if x["language"] == "python"]
    print(list)
    print("--------------------------------------")
    
    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    list = [x for x in DATA if x["language"] == "python" and x["age"] > 20]
    print(list)
    print("--------------------------------------")
    
    # 3. obtener todos los trabajadores de ciancoders organization
    list = [x for x in DATA if x["organization"] == "Ciancoders" ]
    print(list)
    print("--------------------------------------")
    
    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    list = [x for x in DATA if x["organization"] == "Ciancoders" and x["age"] > 30]
    print(list)
    print("--------------------------------------")
    
    # 5. obtener todos los trabajadores de mayores de 18 años
    print("5. obtener todos los trabajadores de mayores de 18 años")
    list = [x for x in DATA if x["age"] > 18]
    print(list)
    print("--------------------------------------")
    
    # 6. obtener todos los trabajadores de mayores a 70 años
    list = [x for x in DATA if  x["age"] > 70]
    print(list)
    print("--------------------------------------")
if __name__ == '__main__':
    run()