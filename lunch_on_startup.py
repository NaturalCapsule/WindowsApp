import keyboard
import subprocess

key = ['ctrl', 'alt', 'p']

while True:
    if keyboard.is_pressed(key):
        subprocess.Popen(['python', 'C:/Users/sxxve/Music/WindowsApp/monitor.py'])
