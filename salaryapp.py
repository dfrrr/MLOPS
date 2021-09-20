import pandas as pd

data = pd.read_csv("SalaryData.csv")
x = data["YearsExperience"].values
x = x.reshape(-1,1)
y = data["Salary"]
from sklearn.linear_model import LinearRegression
mind = LinearRegression()
model = mind.fit(x,y)

print("""
     ------------------------------------------------------------------------------------------------------------------------------------------------
     
                                                  WELCOME TO THE WORLD OF PREDICTION
                                
     -------------------------------------------------------------------------------------------------------------------------------------------------
     
""")

while(True):
    exp = input("Enter Your Relative Experience In ML: ")
    exp = float(exp)
    if exp < 0 :
        exit()
