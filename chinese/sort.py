print sorted([36, 5, -12, 9, -21], key=abs)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True) # compare with all lower case, reverse them

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(n):
    return n[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(n):
    return n[1]

L2 = sorted(L, key=by_score)
print(L2)
