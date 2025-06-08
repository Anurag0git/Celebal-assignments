# number of rows
n = 5  

for i in range(1, n + 1):
    print("* " * i)

print("---------------------------------------------------------")

for j in range(n):
    spaces = "  " * j
    stars = "* " * (n - j)
    print(spaces + stars)

print("---------------------------------------------------------")

for k in range(1, n + 1):
    spaces = " " * (n - k)
    stars = "* " * k
    print(spaces + stars)
