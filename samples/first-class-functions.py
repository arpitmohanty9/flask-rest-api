from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    
    raise RuntimeError(f"Could not find the element {expected}")


# lets have a sequence
#friends
friends= [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Aku Daku", "age": 33},
    {"name": "Monty Ponty", "age": 33}
]

#finder
def get_friend_name(friend):
    return friend["name"]


try:
    print(search(friends, "Bob Smith", get_friend_name))
    print(search(friends, "Bob Smith", lambda friend: friend["name"]))
    print(search(friends, "Bob Smith", itemgetter("name")))
    
except RuntimeError as e:
    print(e)