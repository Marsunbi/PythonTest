name = 234
name2 = 'hej'
my_list = [1, 2, 'hej', [2, "hej2"]]

print("hej")
print("this is {} and {}".format(name, name2))

def my_function(var1, var2):
    sum = var1 + var2
    if sum is 42:
        print("the answer")
    else:
        print("no")

my_function(40,2)

def return_something():
    return 5, True, 5/6, "bacon", [1, 2, 3]

a, b, c, d, e = return_something()

print(a, d)
print(return_something())

a = [123, 456, 789]
i = 0
while i < 3:
    print(a[i])
    i = i + 1

for x in a:
    print(x)
