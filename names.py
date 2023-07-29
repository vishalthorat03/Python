names = []
print("Enter the number of names:")
number = int(input())
if(number<=0):
    print("Invalid Input")
else:
    print("Enter the names:")
    for i in range(number):
        name = input()
        names.append(name)
        names.sort(reverse = True)
        names.sort(reverse=True,key=len)
    print("The sorted name list is:")
    for i in range(number):
        print(names[i])