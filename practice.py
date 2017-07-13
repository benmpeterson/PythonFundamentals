a = [1, 2, 3]
x = []

print(a)

s = [[-1, 1]] * 5
s[2].append(7)

n = [1, 300, 3, 700, 302392, 10]

(n.sort())

print(n)

(n.sort(reverse=True))

print(n)

g = dict(wheat='no', barley='yes')

f = dict(g)

for key, value in f.items():
    print("{0},{1} okh".format(key, value))

print(f)

t = [1, 4, 2, 1, 7, 9, 9]
print(set(t))
# sets cannot contain duplicates

blue_eyes = {'Olivia', 'Harry', "Lily", "Jack", "Amelia"}
blond_hair = {'Harry', 'Jack', "Amelia", "Mia", "Joshua"}
smell_hcn = {"Harry", "Amelia"}
o_blood = {"Mia"}
a_blood = {"Harry"}

print(blue_eyes.union(blond_hair))  # join
print(blond_hair.intersection(blue_eyes))  # both
print(blond_hair.difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes))
print(o_blood.issubset(blond_hair))  # all common
print(a_blood.isdisjoint(o_blood))  # no common




