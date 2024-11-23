import tkinter as tk
from tkinter import ttk
#This is just a test file for our GUI the official program file is Recipe_Project_Final.py
# Creating main window
root = tk.Tk()
root.title("Your Recipe Book")

# Creating a notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, expand=True)

# Creating frames for the tabs
search_frame = tk.Frame(notebook, padx=20, pady=20)
add_frame = tk.Frame(notebook, padx=20, pady=20)
manage_frame = tk.Frame(notebook, padx=20, pady=20)

# Adding 3 tabs to notebook
notebook.add(search_frame, text="Search Recipe")
notebook.add(add_frame, text="Add Recipe")
notebook.add(manage_frame, text="Manage Recipes")



# The Search Recipe tab 
# Set search label
search_label = tk.Label(search_frame, text="You can search for a Recipe by Title/Ingredients:", font=("Arial", 12))
search_label.pack(pady=5)

# Set search entry
search_entry = tk.Entry(search_frame, width=50)
search_entry.pack(pady=5)

# Set search button
search_button = tk.Button(search_frame, text="Search", font=("Arial", 12)) 
search_button.pack(pady=10)

# Directions for searching recipes
search_info_label = tk.Label(search_frame, text="Enter a recipe name or an ingredient and press 'Search'", font=("Arial", 10))
search_info_label.pack(pady=10)

# The Add Recipe tab
add_label = tk.Label(add_frame, text="Add a New Recipe:", font=("Arial", 14))
add_label.pack(pady=5)

# Entry fields for adding a recipe
# Title entry field
title_entry_label = tk.Label(add_frame, text="Recipe Title:", font=("Arial", 12)) 
title_entry_label.pack(pady=5)
title_entry = tk.Entry(add_frame, width=50)
title_entry.pack(pady=5)
# Ingredients and steps entry fields
ingredients_entry_label = tk.Label(add_frame, text="Ingredients (seperate with comma):", font=("Arial", 12)) 
ingredients_entry_label.pack(pady=5)
ingredients_entry = tk.Entry(add_frame, width=50)
ingredients_entry.pack(pady=5)

# Steps entry field
steps_entry_label = tk.Label(add_frame, text="Steps:", font=("Arial", 12))
steps_entry_label.pack(pady=5)
steps_entry = tk.Text(add_frame, width=50, height=10)  # Text widget for multiple lines
steps_entry.pack(pady=5)

# Add button
add_button = tk.Button(add_frame, text="Add Recipe", font=("Arial", 12))  # No command attached
add_button.pack(pady=10)
 
# Directions for adding a recipe
view_button = tk.Button(manage_frame, text="View All Recipes", font=("Arial", 12))  # No command attached
view_button.pack(pady=5)

# Buttons for managing recipes
edit_button = tk.Button(manage_frame, text="Edit Recipe", font=("Arial", 12))  # No command attached
edit_button.pack(pady=5)

# Delete button
delete_button = tk.Button(manage_frame, text="Delete Recipe", font=("Arial", 12))  # No command attached
delete_button.pack(pady=5)

# Sort button
sort_button = tk.Button(manage_frame, text="Sort Recipes", font=("Arial", 12))  # No command attached
sort_button.pack(pady=5)

# Filter button
filter_button = tk.Button(manage_frame, text="Filter by Ingredient", font=("Arial", 12))  # No command attached
filter_button.pack(pady=5)

# Directions for managing recipes
manage_info_label = tk.Label(manage_frame, text="Use the buttons above to manage your recipes.", font=("Arial", 10))
manage_info_label.pack(pady=10)

# Start the main event loop
root.mainloop()
