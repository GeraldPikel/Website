footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes":
    # Pets consume resources like water, litter, and toys. 
    footprint = footprint + 5
    if input("Does your pet food contain meat?") == "yes":
        footprint = footprint + 10        
    else:
        footprint = footprint + 0
else:
    footprint = footprint + 0


days = int(input("How many days a week do you commute to school or work? "))

if days > 0:
    transport = input("Do you commute by foot, bike, bus, train, or car? ")
    # Different methods of transportation have different environmental impacts.
    if transport == "bus" or transport == "train":
        footprint = footprint + (4* days)
    if transport == "bike" or transport == "foot":
        footprint == footprint + days
    if transport == "car":
        footprint = footprint + (8 * days)

print("Your environmental footprint score is " + str(footprint) + ".")
