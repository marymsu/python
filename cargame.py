command= ""
started= True
while True:
    command= input(">:").lower()
    if command == "start":
        if started:
            print("The car started!")
        else:
            started = True
            print("The car is already started!")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
Start- to start the car
Stop to stop the car
Quit to quit the program""")
    elif command == "quit":
        break


