sizelimit= 42
length=int(input("Enter the length of zender:"))
if length<sizelimit:
    belowlimit= sizelimit-length
    print("size limit is not enough put the fish back into the lake.")
    print(f"The caught fish was {belowlimit}cm lower than sizelimit.")
elif length>= sizelimit:
    print("Goodjob!You have caught a perfect one")

cabinclass= input("Enter the cabin class(LUX,A,B,C):")
if cabinclass== "LUX":
    print("LUX:upper deck with a balcony")
elif cabinclass=="A":
    print("A:above the car equipped with a window")
elif cabinclass=="B":
    print("B:windowless cabin above the car deck")
elif cabinclass=="C":
    print("C:windowless cabin below the car deck")
else:
     print("invalid cabin class")

gender=input("Enter your gender(M or F):")
hemoglobin=float(input("Enter your hemoglobin:"))
if gender=="F":
    if 117<= hemoglobin<= 155:
     print("normal")
    elif hemoglobin<117:
     print("low")
    else:
     print("high")
if gender=="M":
    if 134<=hemoglobin<=167:
        print("normal")
    elif hemoglobin<134:
        print("low")
    else:
        print("high")

year=int(input("Enter a year:"))
if (year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

