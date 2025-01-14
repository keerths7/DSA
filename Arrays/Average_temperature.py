total = 0
temperatures = []
days = int(input("Enter the number of days: "))

for i in range(days):
    day_temperature = int(input(f"Temperature of day {i} is:"))
    temperatures.append(day_temperature)
    total += day_temperature        #  'or'    total += temperature_array[i] 
average = round((total/days),2)
# average = round((sum(temperatures) / len(temperatures)),2)
print(f"The average temperature is {average}")

count = 0
for i in temperatures:
    if i > average:
        count += 1
print(f"{count} days have temperature greater than average temperature.")

# above_list = [i for i in temperatures if i > average]
# print(len(above_list), "days have temperature greater than average temperature.")