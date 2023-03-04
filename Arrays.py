
#Traverse in python
def traverse():
    #creating and initializing a list(array)
    print("printing array content: ")
    nums =[1,3,5,7,9,11,15]
    print(nums)

    #using a for loop to traverse(print) the elements
    #one by one
    print("\nTraverse function in effect: \n")
    for i in nums:
        print(i)

#Insertion  
def insertion():
    print("Inserting an element at a specific index\n")
    list = ["My","is","Mark."]
    print(list)
    print("\nInserting missing item 'name' at index 1")
    list.insert(1,"name")
    print("\nit now outputs: ",list)

def deletion():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    print("Given an array: ",numbers)
    print("\nDeleting an element from index 4 gives")
    numbers.remove(4)
    print(numbers)

def search():
    #initialize the array
    numbers = [1,2,3,4,5,6,7,8,9,0]
    print(numbers)
    user_input= input("Enter a number from the array to check if it exists: ")
    print("\nChecking if the number exists in the array")
    if user_input.isnumeric:
        check_if_exist = numbers.count(int(user_input))

    # checking if it is more than 0
    if check_if_exist > 0:
        print("Yes, it exists in list")
    else:
        print("No, it does not exists in list")
        
#calling the functions 
traverse()
print("\n")
insertion()
print("\n")
deletion()
print("\n")
search()
print("\n")