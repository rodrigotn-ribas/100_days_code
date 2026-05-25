import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list=data["temp"].to_list()
# print(temp_list)

# TODO 0 : Average temp
#
# temp_list = data["temp"].to_list()
# temp_average = sum(temp_list) / len(temp_list)
# print(temp_average)
#
# average = data["temp"].mean()
# print(average)
#
# TODO 1: Max temp
#
# #Get data in Columns
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

#Get Data in Row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#


# TODO 2: Monday temperature, Celsius to Fahrenheit
# monday = data[data.day == "Monday"]
# celsius = monday.temp[0]
# fahrenheit = (celsius * 9/5) + 32
# print(fahrenheit)
#
# #Create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# primary fur color how many

# TODO 3: print the number of colors
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260525.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

color_data = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray, cinnamon, black]
}

color_data_frame = pandas.DataFrame(color_data)
color_data_frame.to_csv("color_data_frame.csv")