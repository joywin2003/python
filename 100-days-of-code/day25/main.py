# with open("weather_data.csv") as data:
#     weather_list = data.readlines()
#     print(weather_list)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# temp_list = data["temp"].tolist()
# average_temp = round(sum(temp_list)/len(temp_list),2)
# print(average_temp)
# print(data["temp"].min())

# for day in data.da
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# # print(monday)
# print(monday.temp)
#
# print(monday["temp"])

# monday_fah = (int(monday.temp) * 9/5)+32
# print(monday_fah)
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count = 0
data_squirrel_grey = len(data[data["Primary Fur Color"] == "Gray"])
print(data_squirrel_grey)
data_squirrel_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(data_squirrel_cinnamon)
data_squirrel_black = len(data[data["Primary Fur Color"] == "Black"])
print(data_squirrel_black)

data_doct = {
    "fur color": ["gray","cinnamon","black"],
    "count":[data_squirrel_grey,data_squirrel_cinnamon,data_squirrel_black]
}
df = pandas.DataFrame(data_doct)
df.to_csv("squirrel_count.csv")
