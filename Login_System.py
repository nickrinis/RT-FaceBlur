"""LOGIN SYSTEM"""

import sys
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def login(user_data):
    
    # User ID and clearance.
    logged_in = 0
    clearance = 0
    
    # Flags.
    correct_username = 0
    correct_password = 0
    pw_check = 0
    error = 0
   
    while correct_username == 0:
        
        # Tkinter window.
        window = tk.Tk()
        # Hide the root windows.
        window.withdraw()
        # Get the username through a GUI.
        username = simpledialog.askstring(title="Login system", prompt="Username:\t\t\t\t")
       
        for ID, name, pword, clrnc in user_data.itertuples(index=False):
            # Check the username and password.
            if username == name:
                correct_username = 1
                while pw_check == 0:
                    
                    # Tkinter window.
                    window = tk.Tk()
                    # Hide the root windows.
                    window.withdraw()
                    # Get the username through a GUI censored.
                    password = simpledialog.askstring(title="Login system", prompt="Password:\t\t\t\t", show='*')
                    
                    if password == pword:
                        correct_password = 1
                        pw_check = 1
                    # If the password is incorrect print the appropriate message and exit after 3 attempts.
                    else:
                        messagebox.showwarning("Error", "Incorrect password!")
                        error += 1
                        if error == 3:
                            messagebox.showerror("Error", "You've reached the maximum login attempts, exiting...")
                            sys.exit()
                            
            # If password and username are correct change flags and save ID.
            if correct_username and correct_password == 1:
                logged_in = ID
                clearance = clrnc
            # Reset password flag.
            correct_password = 0
        
        if correct_username == 0:
            messagebox.showwarning("Error", "Incorrect username!")
   
    if not logged_in == 0:
        
        messagebox.showinfo("Successful Login", "Welcome to the monitoring platform, "+username+".")
   
    # Return the ID of the logged-in user.
    return logged_in, clearance
