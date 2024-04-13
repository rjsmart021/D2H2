#Lesson2: Nested IF
#Task1: Code Correction 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
#Task 2:Setting the Scene
if place == "cave":
    action = input("light a tourch? or proceed in the dark")
if action == "light a tourch?":
    print("Your in the big leages kid")
else:
    print("Just keep swimming")
#Task 3: Default Path 
if place != "cave" and place !="forest":
    print("Neither!")
# 2. Quick Decisions: The Event Planner
#task1:Code Correction
attendees = int(input("Enter number of attendees: "))
 
if attendees > 100: 
    print("large hall!")
else:
    print('small')

#Task 2: Catering Choices
food = input("Choose eating style: Veg or meat? ")
if food == "Veg":
    print ("We recomend Veggie Delight Caterers")
else:
    print("We recomend Gourmet Meals Caterers" )
