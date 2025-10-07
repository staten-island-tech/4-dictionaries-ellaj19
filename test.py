""" CafeItemList = [
        {"name": "1. Mia's boleens", "price": 15.99, "description": "A well-made collage of Mia's misspelled data types"},
        {"name": "2. olivia's cat's fuzzy toes", "price": 20.99, "description": "a chance to feel the fuzzy little toes of Olivia Lu's cats, Ollie and Ellie. You have a choice between the chunky one and the skinny one."},
        {"name": "3. Yakult Iced Coffee", "price": 6.99, "description": "a cool, refreshing coffee drink to cool you down on the worst and best of days."},
        {"name": "4. Salted Caramel Hot Chocolate (with peppermint crumbs)", "price": 6.99, "description": "A warm, comforting hot chocolate infused with notes of salted caramel and peppermint undertones"},
        {"name": "5. Strawberry Tiramisu (with a suprise bigback gooner fanfic)", "price": 12.99, "description": "A creamy, light dessert incorporating fresh strawberries, creamy marscapone, soft ladyfingers, and a generous douse of coffee. Comes with a book in collaboration with BigBack Liver's Library."},
        {"name": "6. maura's yaoi notebook", "price": 2.99, "description": "a magical notebook donated by my dear friend, filled with the tales of a faraway land that immediately transport you to a whole new dimension."},
        {"name": "7. Melon Soda Float w/ a Side of Melon Bread"}
        ]



for i in range(0, len(CafeItemList)):
    print(CafeItemList[i]["name"])
    int(input("what would you like to buy?")) """

""" def language(x):
       x = x.lower()
    scount = x.count("s")
    tcount = x.count("t")
    if scount > tcount:
         print("english")
    elif tcount >= scount:
                 print("french")
    else:
                 print("idk") """

""" def parkinglot(x):
    carcount = x.count("C")
    carcount2 = x.count("CC")
    carcount2 = carcount2 * 2
    print(carcount-carcount2)
    
parkinglot("CC..C.CC..")"""
 

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

language("unicornunicornunicorn")  """

def spaces(x,y):
    l = 0
    t = 0
    for char in x:
        if char == "C":
            l += 1
    for char in y:
        if char == "C":
            t += 1
    print(l-t)

spaces("CC..C",".CC..")





    

