 	Expense Tracker  Systems
 	Code

import tkinter as tk
from tkinter import messagebox
# ---------- Main Window ----------
root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("700x500")

# ---------- Global Data ----------
budgets = {}
expenses = []

# ---------- Clear Frame ----------
def clear_frame():
for widget in root.winfo_children():
widget.destroy()

# ---------- Homepage ----------
def homepage():
clear_frame()

tk.Label(root, text="HOME PAGE", font=("Arial", 20, "bold")).pack(pady=20)

tk.Button(root, text="Dashboard", width=20, command=dashboard).pack(pady=5)
tk.Button(root, text="Budget Page", width=20, command=budget_page).pack(pady=5)
tk.Button(root, text="Expense Page", width=20, command=expense_page).pack(pady=5)

# ---------- Dashboard ----------
def dashboard():
clear_frame()

tk.Label(root, text="DASHBOARD", font=("Arial", 20, "bold")).pack(pady=20)

total_budget = sum(budgets.values())
total_expense = sum(expenses)

tk.Label(root, text=f"Total Budget: ₹{total_budget}").pack()
tk.Label(root, text=f"Total Expense: ₹{total_expense}").pack()

tk.Button(root, text="Back", command=homepage).pack(pady=10)

# ---------- Budget Page ----------
def budget_page():
clear_frame()

tk.Label(root, text="BUDGET PAGE", font=("Arial", 20, "bold")).pack(pady=20)

tk.Button(root, text="Create Budget", command=create_budget).pack(pady=5)
tk.Button(root, text="Edit Budget", command=edit_budget).pack(pady=5)
tk.Button(root, text="Delete Budget", command=delete_budget).pack(pady=5)

tk.Button(root, text="Back", command=homepage).pack(pady=10)

# ---------- Create Budget ----------
def create_budget():
clear_frame()

tk.Label(root, text="CREATE BUDGET", font=("Arial", 20, "bold")).pack(pady=20)

tk.Label(root, text="Category").pack()
category = tk.Entry(root)
category.pack()

tk.Label(root, text="Amount").pack()
amount = tk.Entry(root)
amount.pack()

def save():
try:
budgets[category.get()] = float(amount.get())
messagebox.showinfo("Success", "Budget Added")
budget_page()
except:
messagebox.showerror("Error", "Invalid Input")

tk.Button(root, text="Save", command=save).pack(pady=10)
tk.Button(root, text="Back", command=budget_page).pack()

# ---------- Edit Budget ----------
def edit_budget():
clear_frame()

tk.Label(root, text="EDIT BUDGET", font=("Arial", 20, "bold")).pack(pady=20)

tk.Label(root, text="Category").pack()
category = tk.Entry(root)
category.pack()

tk.Label(root, text="New Amount").pack()
amount = tk.Entry(root)
amount.pack()

def update():
if category.get() in budgets:
budgets[category.get()] = float(amount.get())
messagebox.showinfo("Updated", "Budget Updated")
budget_page()
else:
messagebox.showerror("Error", "Category not found")

tk.Button(root, text="Update", command=update).pack(pady=10)
tk.Button(root, text="Back", command=budget_page).pack()

# ---------- Delete Budget ----------
def delete_budget():
clear_frame()

tk.Label(root, text="DELETE BUDGET", font=("Arial", 20, "bold")).pack(pady=20)

tk.Label(root, text="Category").pack()
category = tk.Entry(root)
category.pack()

def delete():
if category.get() in budgets:
del budgets[category.get()]
messagebox.showinfo("Deleted", "Budget Deleted")
budget_page()
else:
messagebox.showerror("Error", "Category not found")

tk.Button(root, text="Delete", command=delete).pack(pady=10)
tk.Button(root, text="Back", command=budget_page).pack()

# ---------- Expense Page ----------
def expense_page():
clear_frame()

tk.Label(root, text="EXPENSE PAGE", font=("Arial", 20, "bold")).pack(pady=20)

tk.Label(root, text="Expense Amount").pack()
amount = tk.Entry(root)
amount.pack()

def add_expense():
try:
expenses.append(float(amount.get()))
messagebox.showinfo("Added", "Expense Added")
except:
messagebox.showerror("Error", "Invalid Input")

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="Back", command=homepage).pack()

# ---------- Start App ----------
homepage()
root.mainloop(














    
























