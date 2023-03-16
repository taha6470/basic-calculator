x=int(input("enter first number >"))
y=int(input("enter second number >"))
operator=int(input("select an operator from the following >\n 1.addition \n2.subtraction \n3.multiplication \n4.division \n Enter your choice : "))
if operator ==1 :
    print(x+y)
elif operator ==2:
    print(x-y)
elif operator ==3:
    print(x*y)
elif operator ==4:
    print(x/y)
else:
    print("you selected an unkown operator")