bangla = int(input("Enter Marks for Bangla: "))
english = int(input("Enter Marks for English: "))
math = int(input("Enter Marks for Math: "))
science = int(input("Enter Marks for Science: "))

avg = (bangla + english + math + science) / 4

if(avg >= 91 and avg <= 100):
    print("Grade: A+ \nAverage marks is:", avg)
elif(avg >= 81):
    print("Grade: A \nAverage marks is:", avg)
elif(avg >= 71):
    print("Grade: B \nAverage marks is:", avg)
elif(avg >= 61):
    print("Grade: C \nAverage marks is:", avg)
elif (avg >= 41):
    print("Grade: D \nAverage marks is:", avg)
else:
    print("Grade: F \nAverage marks is:", avg)




