import tkinter as tk
from tkinter import messagebox

# Possible data for recipes
recipes = [
    {"title": "Classic Spaghetti", "ingredients": "spaghetti, beef, tomato sauce"},
    {"title": "Chicken Curry", "ingredients": "chicken, curry powder, coconut milk, rice"},
    {"title": "Beef Stew", "ingredients": "beef, potatoes, carrots, onions"},
    {"title": "Vegetable Combo", "ingredients": "broccoli, carrots, bell peppers, soy sauce"},
    {"title": "Macarons", "ingredients": "almond flour, sugar powder, egg white, granulated sugar"}
]

def search_recipes():
    query = search_entry.get().lower()
    results = [recipe for recipe in recipes if query in recipe['title'].lower() or query in recipe['ingredients'].lower()]

    if results:
        result_text = "\n".join([f"Title: {recipe['title']}\nIngredients: {recipe['ingredients']}\n" for recipe in results])
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("No Results", "No recipes found matching your search criteria.")





# main window
root = tk.Tk()
root.title("Personal Recipe Book")

# frame for cover page
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# title label
title_label = tk.Label(frame, text="Welcome to Your Recipe Book", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# search label
search_label = tk.Label(frame, text="Search for a Recipe by Title or Ingredients:", font=("Arial", 12))
search_label.pack(pady=5)

# searching field
search_entry = tk.Entry(frame, width=50)
search_entry.pack(pady=5)

# search button
search_button = tk.Button(frame, text="Search", command=search_recipes, font=("Arial", 12))
search_button.pack(pady=10)

# Directions
info_label = tk.Label(frame, text="Enter a recipe name or an ingredient and press 'Search'", font=("Arial", 10))
info_label.pack(pady=10)


root.mainloop()




