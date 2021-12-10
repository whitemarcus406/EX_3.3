try:
    grade = float(input("Enter your score: "))
    if score >= 0.9 and score <= 1.0:
        print("A")
    elif score>= 0.8 and score <= 0.89:
        print ("B")
    elif score>= 0.7 and score <= 0.79:
        print ("C")
    elif score>= 0.6 and score <= 0.69:
        print ("D")
    elif score >= 0.0 and score <= 0.59:
        print ("F")
    else:
        print("Bad Score")
except :
    print ("Invalid Entry")
