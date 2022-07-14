import pandas as pd

series = pd.Series(["BMW", "Toyota", "Honda"])
colors = pd.Series(["Red", "Blue", "White"])

car_data = pd.DataFrame({"Car make": series, "Color": colors})

car_sales_csv = pd.read_csv("car-sales.txt")

heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")

car_sales_csv.to_csv("exported_car_sales.csv", index = False)

print(car_sales_csv.dtypes)
print(car_sales_csv.index)

print(car_sales_csv.describe())

print(car_sales_csv.info())

print(car_sales_csv.mean())

print(car_sales_csv.sum())

print(car_sales_csv["Doors"].sum())

print(len(car_sales_csv))

## day5: Viewing and selecting data

print(car_sales_csv.head()) # first 5 rows
print(car_sales_csv.head(7)) # first 7 rows

animals = pd.Series(["Dog", "cat", "panda", "hamster", "snake"], index = [2, 3, 5, 3, 12])
print(animals)

print(animals.loc[3])  # by index
print(animals.iloc[3]) # by position
print(animals.loc[:2])

print(car_sales_csv.Make)
print(car_sales_csv["Make"])

print(car_sales_csv[car_sales_csv.Make == "Toyota"])

print(car_sales_csv[car_sales_csv["Odometer (KM)"] > 100000])

print(pd.crosstab(car_sales_csv["Make"], car_sales_csv["Doors"]))

# Group by
print(car_sales_csv.groupby(["Make"]).mean())

import matplotlib.pyplot as pl

car_sales_csv["Odometer (KM)"].plot()
car_sales_csv["Odometer (KM)"].hist()
pl.plot(car_sales_csv["Odometer (KM)"])


prices = car_sales_csv["Price"].replace('[\$\,\.]', '', regex=True).astype(int)

car_sales_csv.Price = prices
pl.hist(car_sales_csv)
#pl.show()

## Manipulating data

print(car_sales_csv.Make.str.lower())

cars_mis = pd.read_csv("data/car-sales-missing-data.csv")
print(cars_mis)

cars_mis["Odometer"].fillna(cars_mis["Odometer"].mean(), inplace=True)

cars_mis_drop = cars_mis.dropna()

cars_mis_drop.to_csv("cars-sales-missing-dropped.csv")

seats_column = pd.Series([5, 5, 5, 5, 5])
car_sales_csv["Seats"] = seats_column
print(car_sales_csv)

car_sales_csv.Seats.fillna(5, inplace=True)

## Column from Python list
fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 4.7, 3.0, 4.5, 7.8, 5.7]
car_sales_csv["Fuel per 100KM"] = fuel_economy

car_sales_csv["Total fuel used"] = car_sales_csv["Odometer (KM)"]/100 * car_sales_csv["Fuel per 100KM"]

car_sales_csv["Passed safety tests"] = True


shuffled = car_sales_csv.sample(frac=1)

# Only select 20% of data
shuffled.sample(frac=0.2)

# Reset indeces 
print(shuffled.reset_index(drop=True))

#Remove 1 seat from each car
print(car_sales_csv["Seats"].apply(lambda x: x - 1))

