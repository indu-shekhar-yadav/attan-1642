import serial
import datetime
import json

# Establish serial connection with Arduino
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with the appropriate serial port

attendance_data = []

while True:
    # Read data from Arduino
    data = ser.readline().decode().strip()
    if data:
        fingerprint_id = data.split()[0]
        print(fingerprint_id)
        
        if fingerprint_id == "5":
            fingerprint_id = "Indu"
        elif fingerprint_id == "2":
            fingerprint_id = "soumyajit"
        elif fingerprint_id == "4":
            break
        else:
            fingerprint_id = "chutiya"

        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create a dictionary to store the fingerprint data
        fingerprint = {"id": fingerprint_id, "timestamp": timestamp}

        # Append the fingerprint data to the attendance list
        attendance_data.append(fingerprint)

        # Save the attendance data to a JSON file
        with open("fingerprint_data.json", "w") as json_file:
            json.dump(attendance_data, json_file)
