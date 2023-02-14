lower = int(input("Enter lower limit"))
upper = int(input("Enter upper limit"))
for i in range(lower, upper) :
    if(i%3==0) & (i%5==0) :
        print("Fizzbuzz")
    elif (i%3==0) :
        print("fizz")
    elif (i%5==0) :
        print("buzz")
    else :
        print("not in range")