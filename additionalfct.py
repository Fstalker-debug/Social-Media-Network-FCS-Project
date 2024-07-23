### here i will be writing standalone functions that could be used in different contexts, 
### i want to make this functions flexible and resuable in the future

from UserClass import user

def sortingUsers(users: list, attribute: str) -> list:

    try:
        users_sorted = sorted(users, key=lambda item: getattr(item[1], attribute))
        
        sorted_names = [name for name, _ in users_sorted]
        return sorted_names

    except AttributeError:
        print(f"Error: Attribute '{attribute}' does not exist in user objects.")
        return []

# Example usage:

# Create user instances
testuser = user("james", "bond", "james_bond", "A1810", "james.bond@gmail.com", "I am the king", ["Barron Tr"])
testuser1 = user("lolipop", "lebron", "lebron_lolipop", "B293", "lebron_lolipop@gmail.com", "HI lolo world", ["smith_kurky"])
testuser2 = user("Brian", "kpop", "brian_kpop", "B285", "brian_kpop@gmail.com", "I am sexy", ["Barron Tr"])
testuser3 = user("Smith", "kurky", "smith_kurky", "B383", "smith_kurky@gmail.com", "Hola world", ["bob_james"])
testuser4 = user("Barron", "Trump", "Barron Tr", "B283", "Barron_trump@hotmail.com", "I am the president of the united states of America", ["brian_kpop"])

# List of users with their names
users_list = [
    ("testuser", testuser),
    ("testuser1", testuser1),
    ("testuser2", testuser2),
    ("testuser3", testuser3),
    ("testuser4", testuser4)
]

# Sort users by 'firstName'
sorted_usernames_by_name = sortingUsers(users_list, 'firstName')
print("Users sorted by firstName:")
print(sorted_usernames_by_name)

# Sort users by 'username'
sorted_usernames_by_username = sortingUsers(users_list, 'username')
print("\nUsers sorted by username:")
print(sorted_usernames_by_username)


##### searching algorithm 
user_ll = [testuser,testuser1,testuser2,testuser3,testuser4]

def search(lst , attribute):

    for i in range(len(user_ll)):
        x = user_ll[i]
        if x.username == attribute:
            return x.displayUser()
        
result = search(user_ll, "smith_kurky")
print(result)