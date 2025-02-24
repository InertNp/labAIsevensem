# Knowledge Base - Observation 1
knowledge_base = {
    "women": ["Ria", "Sita"],
    "plays": {"Ria": "guitar", "Sita": "guitar"},
    "writes": {"Hari": "letter"}
}

# Queries
def is_woman(name):
    return name in knowledge_base["women"]

def who_plays(instrument):
    return [person for person, item in knowledge_base["plays"].items() if item == instrument]

def who_writes(item):
    return [person for person, written_item in knowledge_base["writes"].items() if written_item == item]

def list_women():
    return knowledge_base["women"]

# Query Solutions
print("Observation 1:")
print("Is Ria a woman?", is_woman("Ria"))  # Output: True
print("Who plays guitar?", who_plays("guitar"))  # Output: ['Ria', 'Sita']
print("Who writes a letter?", who_writes("letter"))  # Output: ['Hari']
print("List of women:", list_women())  # Output: ['Ria', 'Sita']

# Additional Functions
def list_instruments():
    return list(set(knowledge_base["plays"].values()))

print("List of instruments:", list_instruments())  # Output: ['guitar']

print("\n" + "="*30 + "\n")

# Knowledge Base - Observation 2
knowledge_base_2 = {
    "eats": {
        "Bear": ["honey", "salmon"],
        "Rat": ["salmon"],
        "Salmon": ["worm"]
    }
}

# Queries
def what_eats(animal):
    return knowledge_base_2["eats"].get(animal, [])

def who_eats(food):
    return [animal for animal, foods in knowledge_base_2["eats"].items() if food in foods]

# Query Solutions
print("Observation 2:")
print("What does Salmon eat?", what_eats("Salmon"))  # Output: ['worm']
print("Who eats honey?", who_eats("honey"))  # Output: ['Bear']
print("Who eats salmon?", who_eats("salmon"))  # Output: ['Bear', 'Rat']

print("\n" + "="*30 + "\n")

# Knowledge Base - Observation 3
knowledge_base_3 = {
    "male": ["Nilesh", "Ramesh"],
    "female": ["Sita", "Sunita"],
    "married": {
        "Rohan": "Sita",
        "Ram": "Sunita"
    }
}

# Queries
def list_males():
    return knowledge_base_3["male"]

def list_females():
    return knowledge_base_3["female"]

def married_to(person):
    return knowledge_base_3["married"].get(person, "Not married")

def list_married():
    return list(knowledge_base_3["married"].items())

def list_bachelors():
    return [male for male in knowledge_base_3["male"] if male not in knowledge_base_3["married"]]

# Query Solutions
print("Observation 3:")
print("List of males:", list_males())  # Output: ['Nilesh', 'Ramesh']
print("List of females:", list_females())  # Output: ['Sita', 'Sunita']
print("Who is Rohan married to?", married_to("Rohan"))  # Output: 'Sita'
print("List of married people:", list_married())  # Output: [('Rohan', 'Sita'), ('Ram', 'Sunita')]
print("List of bachelors:", list_bachelors())  # Output: ['Nilesh', 'Ramesh']
