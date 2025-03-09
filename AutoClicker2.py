import time
import threading
from pynput import keyboard, mouse
import tkinter as tk
from tkinter import messagebox

# Global flag to control the loop and hotkey
is_running = False
interval_ms = 1  # Default interval in milliseconds
hotkey = '`'  # Default hotkey (backtick)

# Function to alternate key presses
def alternate_keys():
    global is_running
    interval_sec = interval_ms / 1000  # Convert ms to seconds
    while is_running:
        try:
            # Use keyboard.Controller() to send key presses globally
            mouse.Controller().press(mouse.Button.left)  # Press right arrow key
            mouse.Controller().release(mouse.Button.left)
            time.sleep(interval_sec)
            # keyboard.Controller().press(keyboard.Key.space)  # Press left arrow key
            # keyboard.Controller().release(keyboard.Key.space)
            # time.sleep(interval_sec)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error in alternate_keys: {e}\n")

# Function to toggle the loop on or off
def toggle_loop():
    global is_running
    if is_running:
        is_running = False  # Stop the loop
        start_stop_button.config(text="Start Loop")
    else:
        try:
            global interval_ms
            interval_ms = int(interval_entry.get())  # Get interval from entry box
            if interval_ms <= 0:
                messagebox.showerror("Invalid input", "Please enter a positive integer for the interval.")
                return
            is_running = True  # Start the loop
            start_stop_button.config(text="Stop Loop")
            threading.Thread(target=alternate_keys, daemon=True).start()  # Start key press loop
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer for the interval.")

# Function to handle key press event (start/stop with the custom hotkey)
def on_press(key):
    global is_running, hotkey
    try:
        if key == keyboard.KeyCode.from_char(hotkey):  # Pressing assigned hotkey to start/stop the loop
            toggle_loop()
    except AttributeError:
        pass

# Function to update the hotkey based on user input
def set_hotkey():
    global hotkey
    new_hotkey = hotkey_entry.get().strip().lower()  # Get the hotkey from entry box
    if len(new_hotkey) == 1 or new_hotkey in ['space', 'enter', 'esc', 'tab']:  # Valid hotkey checks
        hotkey = new_hotkey
        messagebox.showinfo("Hotkey Updated", f"Hotkey for start/stop is now: {hotkey}")
    else:
        messagebox.showerror("Invalid Hotkey", "Please enter a valid key (e.g., 'a', 'space', etc.).")

# Set up the Tkinter window
root = tk.Tk()
root.title("Auto Key Presser")

# Set the window size (width x height)
root.geometry("400x300")

# Create and place the label and entry box for the interval input
interval_label = tk.Label(root, text="Interval (ms):")
interval_label.pack(pady=10)

interval_entry = tk.Entry(root)
interval_entry.insert(0, str(interval_ms))  # Default to 1000 ms
interval_entry.pack(pady=5)

# Create and place the start/stop button
start_stop_button = tk.Button(root, text="Start Loop", command=toggle_loop)
start_stop_button.pack(pady=20)

# Create and place the label and entry box for the hotkey input
hotkey_label = tk.Label(root, text="Set Hotkey for Start/Stop:")
hotkey_label.pack(pady=10)

hotkey_entry = tk.Entry(root)
hotkey_entry.insert(0, hotkey)  # Default hotkey is backtick
hotkey_entry.pack(pady=5)

# Create and place the button to update hotkey
set_hotkey_button = tk.Button(root, text="Set Hotkey", command=set_hotkey)
set_hotkey_button.pack(pady=10)

# Set up the listener for the hotkey
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the Tkinter event loop
root.mainloop()

# To prevent the window from closing immediately
print("Application is running. Press Ctrl+C to stop.")
time.sleep(100)  # Keep running for a while to catch errors/logs