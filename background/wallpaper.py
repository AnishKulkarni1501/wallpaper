import random
import os
import time
import keyboard
import ctypes
import sys
import shutil
import tkinter as tk
from tkinter import simpledialog

sec = 10
bgimages = []
path = os.getcwd()
actual = os.path.join(path, "images")


def images(path):
    for i in os.scandir(path):
        if i.is_file() and i.name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            bgimages.append(i.path)


def generate():
    images(actual)
    a = random.randrange(0, len(bgimages))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, bgimages[a], 0)


def startup():
    startup_dir = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")
    source_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(startup_dir, "images")

    try:
        if not os.path.exists(target_dir):
            shutil.copytree(source_dir, target_dir)
    except Exception as e:
        exit()


def change():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.attributes("-topmost", True)  # Ensure the dialog is on top
    try:
        wait = simpledialog.askstring("Delay", "Enter the delay in seconds:", parent=root)
        if wait is not None:  # If user provides input
            wait = int(wait)
        else:
            wait = 10  # Default value if no input
        root.destroy()  # Destroy the root window after getting the input
        return wait
    except:
        root.destroy()  # If there's an error, still destroy the window
        return 10  # Default delay in case of an error


def on_hotkey_pressed():
    global sec
    sec = change()


def main():
    startup()
    
    # Listen for the hotkey (Ctrl + Shift + U) to change delay
    keyboard.add_hotkey('ctrl+shift+u', on_hotkey_pressed)

    try:
        while True:
            generate()
            time.sleep(sec)  # Sleep for the defined delay
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
