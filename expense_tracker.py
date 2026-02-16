import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import os

expenses = 'expenses.csv'


if not os.path.exists(expenses):
    df = pd.DataFrame(columns=['Date', 'Category', 'Amount'])
    df.to_csv(expenses, index=False)


# Function to add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))

    df = pd.read_csv(expenses)
    
    # Append new expense
    new_data = pd.DataFrame([[date, category, amount]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)

    # Save back to CSV
    df.to_csv(expenses, index=False)
    print("\nExpense added successfully!\n")

# Function to view all expenses
def view_expenses():
    df= pd.read_csv(expenses)
    if df.empty:
        print("\nNo expenses recorded yet.\n")
        return
    summary = df.groupby('Category')['Amount'].sum()
    print("\nExpense Summary by Category:")
    print(summary)
    print("\nTotal Spending: Ghc", df['Amount'].sum(), "\n")

#Function to visualize expenses
def visualize_expenses():

    # Read expenses from CSV
    df = pd.read_csv("expenses.csv")

    # Group by category and sum amounts
    summary = df.groupby('Category')['Amount'].sum()

    style.use('ggplot')

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot bar chart
    ax1.bar(summary.index, summary.values, color='steelblue')
    ax1.set_title("Expense Summary by Category")
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Total Spent (Ghc)")
    ax1.tick_params(axis='x', rotation=30)
    ax1.grid(True, alpha=0.3)

    # Plot pie chart
    colors = plt.cm.Set3(np.linspace(0, 1, len(summary)))
    ax2.pie(summary.values, labels=summary.index, autopct='%1.1f%%', 
            colors=colors, startangle=90)
    ax2.set_title("Expense Distribution by Category")

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


# Main menu
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Visualize Expenses")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice =="1":
        add_expense()

    elif choice =="2":
        view_expenses()

    elif choice =="3":
        visualize_expenses()

    elif choice =="4":
        print("\nGoodbye!\n")
        break
    else:
        print("\nInvalid Choice. Try again\n")