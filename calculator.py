number1 = input("Write The First Number\n")
OperationSign = input("Write One Of These(+,-,x,/)\n")
number2 = input("Write The Second Number\n")
if OperationSign == ("+") :
    result = int(number1) + int(number2)
    print (number1,"+",number2,"=")
    print (result)
elif OperationSign == ("-") :
    result = int(number1) - int(number2)
    print (number1,"-",number2,"=")
    print (result)
elif OperationSign == ("x") :
    result = int(number1) * int(number2)
    print (number1,"x",number2,"=")
    print (result)
elif OperationSign == ("/") :
    result = int(number1) / int(number2)
    print (number1,"/",number2,"=")
    print (result)
