POUCH_MAX_ITEMS = 10

shouldRun = True
pouch = [] # Påse

def pouch_sort(descending = False):
    pouch.sort(reverse=descending)

def pouch_show():
    itemCount = len(pouch)
    if itemCount == 0:
        print("Påsen är tom.")
        return
    print("-- Innehåll --")
    for i in range(itemCount):
        print(f"{i+1}. {pouch[i]}")

def pouch_removeItem(item) -> bool:
    try:
        pouch.remove(item)
        return False
    except:
        print("Angiven sak finns inte i påsen.")
        return True

# Returns True on failure/error.
def pouch_addItem(item) -> bool:
    if len(pouch) >= POUCH_MAX_ITEMS:
        print("Påsen är full.")
        return True
    pouch.append(item)
    return False

def pouch_hasItem(item) -> bool:
    try:
        return pouch.index(item) != None
    except:
        return False

def makeChoice():
    global shouldRun
    choice = input("Val: ").strip().upper()
    match choice:
        # Visa innehållet i påsen
        case "V":
            pouch_show()
        
        # Spara i påsen
        case "S":
            pouch_addItem(input("Sak att spara: "))

        # Leta (finns) i påsen
        case "F":
            item = input("Sak att hitta: ")
            itemFound = pouch_hasItem(item)
            if itemFound:
                print(f"{item} hittades!")
            else:
                print(f"{item} hittades inte.")

        # Avsluta programmet
        case "Q":
            shouldRun = False
        
        # Ta bort sak från påsen.
        case "D":
            item = input("Sak att ta bort: ")
            pouch_removeItem(item)
        
        # Sortera (organisera) påsen
        case "O":
            pouch_sort()
            print("Sorterade påsen i stigande ordning.")
        
        case _:
            print("Angivna kommandot förstods inte.")

while shouldRun:
    makeChoice()
    if not shouldRun:
        break