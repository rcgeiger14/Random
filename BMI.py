from colorama import Fore as fg



x=input("What is your name: ")
print("Hello"+" "+x)
y=int(input(x+[i] " , What is your weight (lb): " [i/]))
z=int(input(x+" , What about your height (in): "))
b=y*703/(z**2);
if b<18.5:
    print(fg.Red+"Your BMI is:"+str(b)+". "+x+" you are underweight.")
elif 18.5<b<24.9:
    print(fg.Green+"Your BMI is:"+str(b)+". "+x+" you are of normal weight.")
elif 24.9<=b<=29.9:
    print(fg.LIGHTRED_EX+"Your BMI is:"+str(b)+". "+x+" you are overweight.")
else:
    print(fg.Red+"Your BMI is:"+str(b)+". "+x+" you are super fat...")
dic={
    x:b}
