positive_number = 0
negative_number = 0
sum = 0
average=0
user_input = int(input("Enter an integer, the input ends if it is 0: "))
while user_input != 0:
    user_input = int(input())
    if user_input < 0:
        negative_number+= 1
    if user_input > 0:
        positive_number+=1
    if user_input == 0:
        print("Non-included number ")
    else:
        sum += user_input
total = positive_number+negative_number

average =sum/total
print(f"The number of positive is {positive_number}")
print(f"the number of negative is {negative_number}")
print(f"The total is {sum}")
print(f"The average is {average:.2f}")

