import pandas
# file_path = 'data.csv'
# data = pandas.read_csv(file_path)
# #print(data['temp'])
#
# data_dict = data.to_dict()
# # print(f"data_dict: {data_dict}")
#
# all_temps = data['temp'].to_list()
# average_temp = sum(all_temps) / len(all_temps)
# #print(f"average_temp: {round(average_temp, 1)}")
# max_temp = data['temp'].max()
# #print(f"max_temp: {max_temp}")
# min_temp = data['temp'].min()
# #print(f"min_temp: {min_temp}")
#
# # print(data[data.temp == max_temp])
#
# monday = data[data.day == 'Monday']
# # print(f"monday: {monday}")
# monday_temp = monday.temp.to_list()[0] * 9/5 + 32
# #print(f"monday_temp: {monday_temp}")


# (Fur Color,Count
# ,grey, 2473
# 1,red, 392
# 2,black, 103

start_file_path = 'central_park.csv'
end_file_path = 'squirrel_count.csv'

data = pandas.read_csv(start_file_path)
colors = data['Primary Fur Color'].to_list()
unique_colors = set(colors)
result = []
for index, color in enumerate(unique_colors):
   result.append({"index": index, "color": color, "count": colors.count(color)})
with open(end_file_path, mode='w') as file:
    file.write("Index,Fur Color,Count\n")
    for item in result:
        file.write(f"{item['index']},{item['color']},{item['count']}\n")


