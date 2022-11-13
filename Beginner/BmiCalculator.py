#Write your code below this line 👇

#Get Length method
def get_bmi(weight,height):
    return weight/ (height ** 2)

if __name__ == '__main__':
    #Prompt Questions and get inputs
    weight = float(input("Enter your weight in KG: "))
    height = float(input("Enter your height in m: "))
    bmi = round(get_bmi(weight, height),2)

    if bmi < 17:
        print(f"Your BMI is {bmi}, and You're underweight")
    elif bmi >= 17 and bmi < 24:
        print(f"Your BMI is {bmi}, and You're normal weight")
    elif bmi >= 24 and bmi < 32:
        print(f"Your BMI is {bmi}, and You're Overweight")
    elif bmi >= 32:
        print(f"Your BMI is {bmi}, and You're Obese")

    bol = input("Are you working out - Y/N? ")
    if bol == 'Y':
        print("Good for you")
    else:
        print("Irrespective of BMI - you should aim to get a good workout")