name = input("Enter Your Name: ")
age = input("Enter Your Age: ")


subjects = {"Maths": "", "English": "", "Urdu": ""}
subjects["Maths"] = int(input("Enter marks for maths: "))
subjects["English"] = int(input("Enter marks for english: "))
subjects["Urdu"] = int(input("Enter marks for urdu: "))

apply_bonus = str(input("Add 5 bonus marks to all subjects? (yes/no): "))

if apply_bonus == "yes":
    subjects = dict(map(lambda item: (item[0], item[1] + 5), subjects.items()))

def average(subjects):
    score = sum(subjects.values())/len(subjects)
    return score
    
def gradechecker(score):    
    if score >= 80:
        Grade = "A"
    elif score >= 60 and score <= 79:
        Grade = "B"
    elif score >= 40 and score <= 59:
        Grade = "C"
    else:
        Grade = "F"
    return Grade

averagescore = average(subjects)
grade = gradechecker(averagescore)


with open("file.txt", "w") as file:
    file.write(f"Name : {name}\n")
    file.write(f"Age : {age}\n")
    for i, j in subjects.items():
        file.write(f"{i} : {j}\n")
    file.write(f"Average : {averagescore}\n")
    file.write(f"Grade : {grade}\n")

with open("file.txt","r") as file:
    print(file.read())







