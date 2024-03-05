command = ""
help = ('''
start : to start the car
stop : to stop the car
help : to get help
      ''')
carStartFlag = False
print(help)
while command != "quit":
    command = input(">").lower()
    if command == "help":
        print(help)
    elif command == "start":
        if not(carStartFlag):
            print("Car started")
            carStartFlag = True
        else:
            print("Car is already started")
    elif command == "stop":
        if carStartFlag:
            print("Car Stopped")
            carStartFlag = False
        else:
            print("Car is already Stopped")
    else:
        print("Invalid Input. Try Again")