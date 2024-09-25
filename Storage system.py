
def classify_item(item):
    outdoorfurniture = { "Outdoor Tables", "Umbrellas", "Deck Boxes", "Storage benches", "Outdoor Cuhions"}
    storagefurniture = {"Shelve units", "Bookcases","Storage Cabinets", "Closets","Storage bins"}
    officefurniture = {"Desks", "Office Chairs","Filing Cabinets", "Shelves"}
    kitchenfurniture = {"Dining Tables", "Bar stools", "Pantry Organizers"}
    livingroomfurniture = {"Chairs", "Coffee Tables", "End Tables","Armchairs","Round Tables","Rugs","Throw pillows"}
    Bathroomfurniture = {"Toilet seats", "Medicine Cabinet", "Toiletries organiser"}

    if item in outdoorfurniture:
        return "Outdoor Furniture", "Aisle 1"
    elif item in storagefurniture:
        return "Storage furniture", "Aisle 2"
    elif item in officefurniture:
        return "Office Furniture", "Aisle 3"
    elif item in kitchenfurniture:
        return "Kitchen Furniture", "Aisle 4"
    elif item in livingroomfurniture:
        return "Living Room Furniture", "Aisle 5"
    elif item in Bathroomfurniture:
        return "Bathroom Furniture", "Aisle 6"
    else:
        return "Not found", ""

print ("Welcome to the Home Depot")
user_input = input("What item are you looking for today? ")

classification, aisle = classify_item(user_input)

if classification != "Not found":
    print (f"Your item '{user_input}' was classified under {classification}.")
    print(f"Your item may be found in {aisle}.")
else:
    print(f"Sorry, the item '{user_input}' was not found")



