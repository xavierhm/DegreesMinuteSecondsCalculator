
#initalization
continue_check = True

degrees = 0
minutes = 0
seconds = 0

degrees2 = 0
minutes2 = 0
seconds2 = 0

degree_result = 0
minute_result = 0
second_result = 0

seconds_total = 0

operation = ''
divider = 0

while continue_check == True:
    degrees = int(input("Enter degrees: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    operation = input("Enter operation, a for addition, s for substraction and d for division")

    if operation == 'a':
        print("Angle to add: ")
        degrees2 = int(input("Enter degrees: "))
        minutes2 = int(input("Enter minutes: "))
        seconds2 = int(input("Enter seconds: "))
    elif operation == 's':
        print("Angle to subtract: ")
        degrees2 = int(input("Enter degrees: "))
        minutes2 = int(input("Enter minutes: "))
        seconds2 = int(input("Enter seconds: "))
    elif operation == 'd':
        divider = int(input("Divide by: "))
        seconds_total = degrees * 3600 + minutes * 60 + seconds
        seconds_total = seconds_total // divider
        degree_result = seconds_total // 3600
        seconds_total = seconds_total - degree_result * 3600
        minutes_result = seconds_total // 60
        seconds_total = seconds_total - minutes_result * 60
        seconds_result = seconds_total
    
    print(degree_result, "°", minutes_result, "'", seconds_result, "''")


