CafeItemList = [
        {"name": "1. Mia's booleens", "price": 15.99, "description": "A well-made collage of Mia's misspelled data types"},
        {"name": "2. olivia's cat's fuzzy toes", "price": 20.99, "description": "a chance to feel the fuzzy little toes of Olivia Lu's cats, Ollie and Ellie. You have a choice between the chunky one and the skinny one."},
        {"name": "3. Yakult Iced Coffee", "price": 6.99, "description": "a cool, refreshing coffee drink to cool you down on the worst and best of days."},
        {"name": "4. Salted Caramel Hot Chocolate (with peppermint crumbs)", "price": 6.99, "description": "A warm, comforting hot chocolate infused with notes of salted caramel and peppermint undertones"},
        {"name": "5. Strawberry Tiramisu (with a suprise bigback gooner fanfic)", "price": 12.99, "description": "A creamy, light dessert incorporating fresh strawberries, creamy marscapone, soft ladyfingers, and a generous douse of coffee. Comes with a book in collaboration with BigBack Liver's Library."},
        {"name": "6. maura's yaoi notebook", "price": 2.99, "description": "a magical notebook donated by my dear friend, filled with the tales of a faraway land that immediately transport you to a whole new dimension."},
        {"name": "7. Melon Soda Float w/ a Side of Melon Bread"}
        ]


for i in range(0, len(CafeItemList)):
        print(CafeItemList[i]["name"])
Cart = input("what would you like to buy?")
consent = True
list = []

while consent == True:
    for item in CafeItemList:
        if Cart in item["name"]:
            print(f"{item["name"]} has been added to your cart")
            list.append(item["name"])

            consent = input("Would you like to buy another item?")
            if consent == "yes":
                Cart = input("What else you you like to buy?")
                consent = True
            if consent == "no":
                print("good choice. let's check out.")
                
    print(f"The items in your cart include: {list} ")


    



 







""" def language(x):
    t = 0
    s = 0
    for char in x: 
        if char == "s" or char == "S":
            s += 1
        elif char == "T" or char == "t":
            t += 1
    if s >= t:
        print("French")
    else:
        print("English") 

language("unicornunicornunicorn") 

def spaces(n,x,y):
    occupied = 0
    for i in range(n):  
        print(x[i],y[i])
        if x[i] == "C" and y[i] == "C":
            occupied += 1
    return(occupied)
            
print(spaces(5,"CC..C",".CC..")) 

def honiblock(x):
    h_honi = 0
    o_honi = 0
    n_honi = 0
    i_honi = 0
    for i in range(h_honi):
        if i == "H":
            h_honi +=1
        elif i == "O":
            o_honi +=1
        elif i == "N":
            n_honi +=1
        elif i == "I":
            i_honi +=1
        print(h_honi + o_honi + n_honi + i_honi)
            

honiblock("H O N I") """ 