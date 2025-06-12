dict1 = {}
def DictionaryAdd():
    name = input("Enter the name of student: ")
    mark = float(input("Enter the marks of student: "))
    dict1[name] = mark

def DictionaryDelete():
    name = input("Enter the name of new student: ")
    del dict1[name]
    print("Dictionary with deleted data: ", dict1)

def DictionaryDisplay():
    print("All data or Elements present in the dictionary: ", dict1)

def DictionarySearch():
    name = input("Enter the name of key: ")
    print("The Marks of the searched name: ",dict1.get(name,"There is no record of this name"))   


while True:    
    print("1 - Adding new element in Dictionary \n2 - Deleting element in Dictionary \n3 - Display the Dictionary \n4 - Search the Key and it's value \n5 - Stop the Program")
    choice = int(input("Enter the Choice: "))
    if choice == 1:
        print("Adding New Element in the Dictionary: ")
        DictionaryAdd()
    elif choice == 2:
        DictionaryDelete()
    elif choice == 3:
        DictionaryDisplay()
    elif choice == 4:
        DictionarySearch()
    elif choice == 5:
        print("Closing the program")
        break
    else:
        print("Invalid Input")