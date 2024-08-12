import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd

# Load the trained model
with open('diabetes_model.pkl', 'rb') as handle:
    model = pickle.load(handle)

# Function to verify diabetes
def verificar(Pregnancies, glucose, bloodP, age, insu, bmi):
    datos = [[Pregnancies, glucose, bloodP, insu, bmi, age]]
    df = pd.DataFrame(datos, columns=['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin', 'BMI', 'Age'])
    new_pred = model.predict(df)
    if new_pred == 1:
        return "diabetes detected"
    else:
        return "diabetes not detected"

# Function to handle the button click
def on_submit():
    try:
        Pregnancies = int(entry_pregnancies.get())
        glucose = int(entry_glucose.get())
        bloodP = int(entry_bloodP.get())
        insu = float(entry_insu.get())
        bmi = float(entry_bmi.get())
        age = int(entry_age.get())

        result = verificar(Pregnancies, glucose, bloodP, age, insu, bmi)
        messagebox.showinfo("Resultado", result)
    except ValueError:
        messagebox.showerror("error de entrada", "ingrese valores validos")

# Create the main window
root = tk.Tk()
root.title("Diabetes Prediction")

# Create and place the labels and entries
tk.Label(root, text="Pregnancies").grid(row=0, column=0)
entry_pregnancies = tk.Entry(root)
entry_pregnancies.grid(row=0, column=1)

tk.Label(root, text="Glucose").grid(row=1, column=0)
entry_glucose = tk.Entry(root)
entry_glucose.grid(row=1, column=1)

tk.Label(root, text="Blood Pressure").grid(row=2, column=0)
entry_bloodP = tk.Entry(root)
entry_bloodP.grid(row=2, column=1)

tk.Label(root, text="Insulin").grid(row=3, column=0)
entry_insu = tk.Entry(root)
entry_insu.grid(row=3, column=1)

tk.Label(root, text="BMI").grid(row=4, column=0)
entry_bmi = tk.Entry(root)
entry_bmi.grid(row=4, column=1)

tk.Label(root, text="Age", width=10).grid(row=5, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=5, column=1)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=6, column=1)

# Start the main event loop
root.mainloop()
