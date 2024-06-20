

input_1 = int(input())
input_2 = int(input())
input_3 = int(input())

if input_1 == input_2 and input_1 == input_3 and input_2 == input_3:
    print(int(input_1 + input_2 + input_3))
    print(int(input_1 + input_2 + input_3))
    print(int(input_1 + input_2 + input_3))
else:
    print(int(input_1 + input_2 + input_3))


grade = int(input())

if(grade>=90):
    print("A")
elif(grade <90 and grade>=80):
    print("B")
elif(grade <80 and grade>=70):
    print("C")
elif(grade <70 and grade>=60):
    print("D")
elif(grade <60):
    print("F")



year = int(input())
is_leap_year = year%4

if(is_leap_year == 0):
    print("Its a leap year")
else:
    print("its not a leap year")