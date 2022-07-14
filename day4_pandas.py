import pandas as pd

series = pd.Series(["BMW", "Toyota", "Honda"])
colors = pd.Series(["Red", "Blue", "White"])

car_data = pd.DataFrame({"Car make": series, "Color": colors})

car_sales_csv = pd.read_csv("car-sales.txt")

heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")

car_sales_csv.to_csv("exported_car_sales.csv", index = False)
