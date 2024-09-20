def calculate_angle(hour, minute):
    hour_angle = (hour * 30) + (minute * 0.5) 
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)
hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
angle = calculate_angle(hour, minute)
print(f"The angle between the hands at {hour}:{minute} is {angle} degrees.")
