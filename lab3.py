# Define the knowledge base
knowledge_base = {
    "in_room": ["bananas", "chair", "monkey"],
    "dexterous": ["monkey"],
    "tall": ["chair"],
    "can_move": [("monkey", "chair", "bananas")],
    "can_climb": [("monkey", "chair")]
}

# Define the rules
def can_reach(X, Y):
    return X in knowledge_base["dexterous"] and close(X, Y)

def close(X, Z):
    for Y in knowledge_base["tall"]:
        if get_on(X, Y) and under(Y, Z):
            return True
    return False

def get_on(X, Y):
    return (X, Y) in knowledge_base["can_climb"]

def under(Y, Z):
    for X in knowledge_base["in_room"]:
        if (X, Y, Z) in knowledge_base["can_move"]:
            return True
    return False

# Test the goal
print("Can the monkey reach the bananas?", can_reach("monkey", "bananas"))


# Define the knowledge base
knowledge_base = {
    "american": ["George"],
    "sells_missiles": [("George", "Iraq")],
    "hostile": ["Iraq"],
    "enemy_of_america": ["Iraq"],
    "has_missile": ["Iraq"],
    "country": ["Iraq"]
}

# Define the rules
def criminal(X):
    return X in knowledge_base["american"] and \
           any((X, Y) in knowledge_base["sells_missiles"] and Y in knowledge_base["hostile"] for Y in knowledge_base["hostile"])

# Test the goal
print("Is George a criminal?", criminal("George"))


# Define the knowledge base
knowledge_base = {
    "horse": ["bluebeard"],
    "offspring": [("charlie", "bluebeard")],
    "parent": [("bluebeard", "charlie")]
}

# Define the rules
def mammal(X):
    return X in knowledge_base["horse"]

def horse(X):
    return X in knowledge_base["horse"] or \
           any((X, Y) in knowledge_base["offspring"] and horse(Y) for Y in knowledge_base["horse"])

# Test the goal
print("Is Charlie a horse?", horse("charlie"))
