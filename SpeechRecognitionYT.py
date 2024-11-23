import serial
import sounddevice
import speech_recognition as sr
import time

r = sr.Recognizer()
m = sr.Microphone()
# For Linux or macOS, it might be something like '/dev/ttyUSB0' or '/dev/ttyACM0'
ser = serial.Serial('COM15', 115200)  # Set baud rate to match Micro:bit settings
# Give time to establish the connection
time.sleep(2)
try:
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        with m as source: 
            audio = r.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            ser.write(value.encode(encoding="utf-8"))
            print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass