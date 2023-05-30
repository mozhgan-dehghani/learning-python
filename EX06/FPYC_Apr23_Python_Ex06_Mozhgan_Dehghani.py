names = [] # string
prices = [] # float
# add, remove, edit, search
while True:
    user = input("product manager>> Select one option(add/edit/delete/search/detail) :")
    if user == "add":
        name = input("enter name:")
        price = float(input("enter price:"))
        if name not in names:
            names.append(name)
            prices.append(price)
            print("adding susses")
        else:
            print("name exit")
    elif user == "detail":
        for i , t in enumerate(names):
            print(f"name_{i+1}: {t} ----> {prices[i]}")
        l = len (prices)
        print(f"total number of products = {l}")
        sum1 = sum(prices)
        ave = sum1/l+1
        print (f"average price = {ave}")
        cheapest = min(prices)
        expensive = max(prices)
        for i , t in enumerate(prices):
            if t == cheapest:
                print(f"cheapest: {names[i]}")
        for i , t in enumerate(prices):
            if t == expensive:
                print(f"expensive: {names[i]}") 
    elif user == "edit":
        index = input ("index of name: ")
        list1 = [int(i)-1 for i in index.split()]
        for i in list1:
            new_name = input("new_name: ")
            if new_name not in names:
                names[i] = new_name
            else:
                print(f"{new_name}: exist")
    elif user == "search":
        word = input("name to search: ")
        for i , t in enumerate(names):
            if word in t:
                print(f"{t} ----> {price}")
    elif user == "delete":
        index = int (input("index of name:"))
        names.pop(index-1)
        prices.pop(index-1)
    elif user == "":
        pass
    elif user == "exit":
        break
    else:
        print(f"{user}: command not found!")
    
   

        
  
			