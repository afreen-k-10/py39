def streetlight_status(light_number):
    if light_number % 2 == 0:
        return "ON"
    else:
        return "OFF"

light_number = int(input("Enter the streetlight number: "))
status = streetlight_status(light_number)
print(f"Streetlight {light_number} should be {status}.")