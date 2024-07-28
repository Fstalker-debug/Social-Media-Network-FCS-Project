from UserClass import user


testuser = user("james", "bond", "james_bond", "A1810", "james.bond@gmail.com", "I am the king", ["Barron Tr"])
testuser1 = user("lolipop", "lebron", "lebron_lolipop", "B293", "lebron_lolipop@gmail.com", "HI lolo world", ["smith_kurky"])
testuser2 = user("Brian", "kpop", "brian_kpop", "B285", "brian_kpop@gmail.com", "I am sexy", ["Barron Tr"])
testuser3 = user("Smith", "kurky", "smith_kurky", "B383", "smith_kurky@gmail.com", "Hola world", ["bob_james"])
testuser4 = user("Barron", "Trump", "Barron Tr", "B283", "Barron_trump@hotmail.com", "I am the president of the united states of America", ["brian_kpop"])

ltl = [testuser1, testuser, testuser2, testuser3, testuser4]
### sort users by their firstName
def firstName_sorting(lst, firstName):
    tnt = []
    for i in range(len(lst)):
        temp = lst[i].firstName
        tnt.append(temp)

    return sorted(tnt)

print(firstName_sorting(ltl, "firstName"))

### sort users by their ID
def ID_sorting(lst, ID):
    tnt = []
    for i in range(len(lst)):
        temp = lst[i].ID
        tnt.append(temp)
    return sorted(tnt)

# print(ID_sorting(ltl, "ID"))
# print(firstName_sorting(ltl,"firstName"))