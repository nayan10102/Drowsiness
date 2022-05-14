import tkinter as tk
from tkinter import ttk

from numpy import imag
from flask import Flask,redirect, url_for,render_template,request
import os


root = tk.Tk()
root.title("Drowsiness Detection System")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("950x450")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))# Create a style
style = ttk.Style(root)



def function1(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

def function2(): 
		os.system("python android_cam.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

    
d = tk.IntVar(value=2)
container = ttk.Frame(root, padding=(40, 0, 0, 10))
container.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
container.columnconfigure(index=0, weight=1)
# Label
text1 = ttk.Label(container,text="Drowsiness Detection System",font="colortube" ,justify="center",foreground="black",padding=20)
text1.grid(row=0, column=0, pady=20, columnspan=2)
button1 = ttk.Button(container,text="Run using web cam",command=function1)
button1.grid(row=10, column=0, padx=300, pady=3, sticky="nsew")
button2 = ttk.Button(container,text="Run using phone cam",command=function2)
button2.grid(row=11, column=0, padx=300, pady=3, sticky="nsew")
button3 = ttk.Button(container,text="exit",command=root.destroy)
button3.grid(row=12, column=0, padx=300, pady=3, sticky="nsew")

root.mainloop()