import pickle
import pandas as pd

with open('model.pkl','rb') as file:
    model=pickle.load(file)



while True:
    print("*"*10)
    print("menu")
    print("*"*10)
    print("1. predict insurance charge:")
    print("2. exit")

    choose=(input("enter your choice: "))

    if choose=="1":
        print("*"*50)
        print("      INSURANCE CHARGES PREDICTION SYSTEM")
        print("*"*50)

        age=int(input("enter the age: "))
        sex=input("enter the sex(male/female): ")
        bmi=float(input("enter the bmi : "))
        children=int(input("enter the number of children: "))
        smoker=input("Are you a smoker(yes/no?? : )")
        region=input("Enter Region (northeast/northwest/southeast/southwest): ").strip().lower()

        user_data=pd.DataFrame({
            'age':[age],
            "sex":[sex],
            'bmi':[bmi],
            'children':[children],
            'smoker':[smoker],
            'region':[region]

        })

        prediction=model.predict(user_data)
        print("the predicted charges is",prediction[0])
        
    elif choose=='2':
        print("thank you for choosing us")
        break

    else:
        print("enter the valid number")
