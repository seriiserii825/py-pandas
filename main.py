import pandas
file_path = 'data.csv'
data = pandas.read_csv(file_path)
#print(data['temp'])

data_dict = data.to_dict()
#print(f"data_dict: {data_dict}")

all_temps = data['temp'].to_list()
average_temp = sum(all_temps) / len(all_temps)
#print(f"average_temp: {round(average_temp, 1)}")
max_temp = data['temp'].max()
#print(f"max_temp: {max_temp}")
min_temp = data['temp'].min()
#print(f"min_temp: {min_temp}")

# print(data[data.temp == max_temp])

monday = data[data.day == 'Monday']
#print(f"monday: {monday}")
monday_temp = monday.temp.to_list()[0] * 9/5 + 32
#print(f"monday_temp: {monday_temp}")
