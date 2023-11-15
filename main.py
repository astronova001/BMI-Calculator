import tkinter as tk
from tkinter import messagebox, ttk
import csv
import matplotlib.pyplot as plt
from collections import Counter

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height/100)**2
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        messagebox.showinfo("BMI", f"Your BMI is {bmi:.2f}, which is considered {category}.")
        
        # Store the data in a CSV file
        with open('bmi_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, weight, height, bmi, category])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height")

def view_data():
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("BMI Data")

    # Create a treeview widget
    treeview = ttk.Treeview(new_window, columns=("Name", "Weight", "Height", "BMI", "Category"), show="headings")
    treeview.heading("Name", text="Name")
    treeview.heading("Weight", text="Weight")
    treeview.heading("Height", text="Height")
    treeview.heading("BMI", text="BMI")
    treeview.heading("Category", text="Category")
    treeview.pack()

    # Load the data from the CSV file and insert it into the treeview
    categories = []
    with open('bmi_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            treeview.insert('', 'end', values=row)
            categories.append(row[4])

    # Count the number of occurrences of each category
    counter = Counter(categories)

    # Create a bar chart
    plt.bar(counter.keys(), counter.values())
    plt.xlabel('BMI Category')
    plt.ylabel('Number of People')
    plt.title('BMI Distribution')
    plt.show()

root = tk.Tk()
root.title("BMI Calculator")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

weight_label = tk.Label(root, text="Weight (in kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (in cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

view_button = tk.Button(root, text="View Data", command=view_data)
view_button.pack()

root.mainloop()
