weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)



# list_comprehension = [new_list for item in list if test]
# dict_comprehention = {new_key:new_value for (key,value) in dict.items() if test}
# df_comprehention = {new_key:new_value for (index, row) in df.iterows()}

