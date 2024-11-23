import os 
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk # Import modules from the pillow package

# File path for database file
file_path = 'Recipe_Database.txt'


# Ingredient Class
class Ingredient:
    # Constructor to initialize the Ingredient class
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    # Returns the ingredient details as a string to be added to the text file
    def to_text(self): 
        return f"{self.name} ({self.quantity} {self.unit})"

    # Input argument is a string that is divided and each word/element becomes a different attribute of the newly created Ingredient object
    @staticmethod 
    def from_text(text):
        name, qty_unit = text.strip().split(' (')
        qty_unit = qty_unit.strip(')')
        quantity, unit = qty_unit.split()
        return Ingredient(name, quantity, unit)

# Recipe Class
class Recipe:
    # Constructor to initialize the Recipe class
    def __init__(self, title, ingredients, steps):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps

    # Adds an object to the ingredients list with an argument of type Ingredient
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    # Adds an object to the step list with an argument of type String
    def add_step(self, step):
        self.steps.append(step)

    # Returns the recipe as a formatted String
    def to_text_block(self):
        ingredients_text = ', '.join([ingredient.to_text() for ingredient in self.ingredients])
        steps_text = ', '.join(self.steps)
        return f"Title: {self.title}\nIngredients: {ingredients_text}\nSteps: {steps_text}\n---"

    # Create a Recipe object using the information from the formatted String
    @staticmethod
    def from_text_block(text_block):
        lines = text_block.strip().split('\n')
        title = lines[0].replace("Title: ", "").strip()
        ingredients_text = lines[1].replace("Ingredients: ", "").strip()
        steps_text = lines[2].replace("Steps: ", "").strip().split(', ')
        ingredients = [Ingredient.from_text(item) for item in ingredients_text.split(', ')]
        return Recipe(title, ingredients, steps_text)

# Recipe Manager Class
class RecipeManager:
    # Constructor to initialize the RecipeManager class
    def __init__(self, file_path):
        self.file_path = file_path
        self.recipes = self.load_recipes()

    # Reads in entire Recipe_Database.txt file to fill program with previously entered recipes
    def load_recipes(self):
        recipes = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                recipe_data = file.read().strip().split('---\n')
                for recipe_text in recipe_data:
                    if recipe_text.strip():
                        recipes.append(Recipe.from_text_block(recipe_text))
        return recipes

    # Saves new recipes to the Recipe_Database.txt file
    def save_recipes(self):
        with open(self.file_path, 'w') as file:
            for recipe in self.recipes:
                file.write(recipe.to_text_block() + '\n')

     # Adds a recipe to the database by taking in a Recipe object as an argument and saving it to the Recipe_Database.txt file
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.save_recipes()

    # Deletes a recipe from the Recipe_Database.txt file
    def delete_recipe(self, title):
        self.recipes = [recipe for recipe in self.recipes if recipe.title.lower() != title.lower()]
        self.save_recipes()

    # Sorts the recipes in the Recipe_Database.txt file alphabetically by title
    def sort_recipes(self):
        self.recipes.sort(key=lambda recipe: recipe.title.lower())
        self.save_recipes()


# GUI Class
class RecipeApp:
    # Constructor for the RecipeApp class
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.ingredient_entries = []

        # Set up for the GUI
        self.setup_gui()

    # Sets up the main GUI by creating the main frame and the different tabbed sections
    def setup_gui(self):
        self.root.title("Personal Recipe Book")
        notebook = ttk.Notebook(self.root)
        notebook.pack(padx=10, pady=10, expand=True)

        # Creates the frames for the Search, Add, and Manage tabs
        self.search_frame = tk.Frame(notebook, padx=20, pady=20)
        self.add_frame = tk.Frame(notebook, padx=20, pady=20)
        self.manage_frame = tk.Frame(notebook, padx=20, pady=20)

        notebook.add(self.search_frame, text="Search Recipe")
        notebook.add(self.add_frame, text="Add Recipe")
        notebook.add(self.manage_frame, text="Manage Recipes")

        # Setup for the Search, Add, and Manage tabs
        self.setup_search_tab()
        self.setup_add_tab()
        self.setup_manage_tab()

    # Set up function for the Search Recipe tab
    def setup_search_tab(self):
        # Search section label
        tk.Label(self.search_frame, text="Search for a Recipe by Title or Ingredients:", font=("Arial", 12)).pack()

        # Entry and button for searching recipes
        self.search_entry = tk.Entry(self.search_frame, width=50)
        self.search_entry.pack(pady=5)
        tk.Button(self.search_frame, text="Search", command=self.search_recipes, font=("Arial", 12)).pack(pady=5)

        # Add an image below the search button using Pillow
        # Load the image using Pillow
        # Image file must be in the same folder as code file and Recipe_Database.txt
        image_path = "book.png"  
        image = Image.open(image_path)

        # Resizing of the image to fit on the page
        resized_image = image.resize((300, 300))

        # Convert the Pillow image to a PhotoImage that is usable by Tkinter
        self.photo = ImageTk.PhotoImage(resized_image)

        # Label creation to display the image
        image_label = tk.Label(self.search_frame, image=self.photo)
        image_label.pack(pady=10)  # Add padding (space) between button and image

    # Set up function for the Add Recipe tab
    def setup_add_tab(self):
        # Label and frame creation for the Add Recipe tab
        tk.Label(self.add_frame, text="Add a New Recipe:", font=("Arial", 14)).pack()
        tk.Label(self.add_frame, text="Recipe Title:", font=("Arial", 12)).pack()
        self.title_entry = tk.Entry(self.add_frame, width=50)
        self.title_entry.pack()

        # Frame creation to add ingredients to a new recipe
        tk.Button(self.add_frame, text="Add Ingredients", command=self.create_ingredient_fields, font=("Arial", 12)).pack()
        self.ingredient_frame = tk.Frame(self.add_frame)
        self.ingredient_frame.pack()

        # Frame creation to add steps to a new recipe
        tk.Label(self.add_frame, text="Steps:", font=("Arial", 12)).pack()
        self.steps_entry = tk.Text(self.add_frame, width=50, height=10)
        self.steps_entry.pack()

        # Button that adds the recipe to the Recipe_Database.txt file
        tk.Button(self.add_frame, text="Add Recipe", command=self.add_recipe, font=("Arial", 12)).pack()

    # Set up function for the Manage Recipe tab
    def setup_manage_tab(self):
        tk.Button(self.manage_frame, text="View All Recipes", command=self.view_all_recipes, font=("Arial", 12)).pack()
        tk.Button(self.manage_frame, text="Delete Recipe", command=self.delete_recipe, font=("Arial", 12)).pack()
        tk.Button(self.manage_frame, text="Sort Recipes", command=self.sort_recipes, font=("Arial", 12)).pack()
        tk.Button(self.manage_frame, text="Edit Recipe", command=self.edit_recipe, font=("Arial", 12)).pack()

    # Method to edit a recipe
    def edit_recipe(self):
        title = simpledialog.askstring("Edit Recipe", "Enter the recipe title to edit:")
        if not title:
            # User pressed cancel, so do nothing
            return

        # Find the recipe to edit
        for recipe in self.manager.recipes:
            if recipe.title.lower() == title.lower():
                # Ask for new title
                new_title = simpledialog.askstring("Edit Recipe", "Enter new title:", initialvalue=recipe.title)
                if new_title is None:
                    return  # User pressed cancel

                # Edit ingredients
                new_ingredients = []
                for ingredient in recipe.ingredients:
                    ingredient_data = simpledialog.askstring(
                        "Edit Ingredient",
                        f"Edit ingredient '{ingredient.to_text()}':",
                        initialvalue=f"{ingredient.name} ({ingredient.quantity} {ingredient.unit})"
                    )
                    if ingredient_data is None:
                        return  # User pressed cancel
                    
                    # check whether the input is valid
                    try:
                        new_ingredients.append(Ingredient.from_text(ingredient_data))
                    except ValueError:
                        messagebox.showerror("Invalid Input", "Invalid ingredient format.")
                        return

                # Edit steps
                new_steps = simpledialog.askstring(
                    "Edit Recipe Steps",
                    "Enter new steps (comma-separated):",
                    initialvalue=", ".join(recipe.steps)
                )
                if new_steps is None:
                    return  # User pressed cancel

                # Ask for confirmation before saving changes
                confirm = messagebox.askyesno("Confirm Edit", "Are you sure you want to save the changes to this recipe?")
                if not confirm:
                    return  # User chose not to save changes

                # Update the recipe
                # Check whether all 3 fields are filled
                if new_title and new_ingredients and new_steps:
                    recipe.title = new_title
                    recipe.ingredients = []
                    # Add new ingredients to recipe
                    for ing in new_ingredients:
                        recipe.add_ingredient(ing)
                    recipe.steps = []
                    # Add new steps to recipe
                    for step in new_steps.split(', '):
                        recipe.add_step(step)
                    self.manager.save_recipes()
                    messagebox.showinfo("Success", "Recipe updated successfully!")
                return

        # If no matching recipe is found
        messagebox.showwarning("Not Found", f"No recipe found with title '{title}'.")

    # Function to display recipe details in a larger window
    def display_recipe_details(self, recipe):
        # Create a new Toplevel window
        recipe_window = tk.Toplevel(self.root)
        recipe_window.title(f"Recipe: {recipe.title}")

        # Set a larger window size
        recipe_window.geometry("600x400")  # Adjust the size as needed

        # Create a text widget to display the recipe details
        text_widget = tk.Text(recipe_window, wrap="none", font=("Arial", 12))
        text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        # Formatting of the data for each recipe
        ingredients_text = ', '.join([ingredient.to_text() for ingredient in recipe.ingredients])
        steps_text = '\n'.join([f"{step}" for i, step in enumerate(recipe.steps)])
        recipe_text = (
            f"Title: {recipe.title}\n\n"
            f"Ingredients: {ingredients_text}\n\n"
            f"Steps:\n{steps_text}"
        )

        # Insert the recipe details into the text widget
        text_widget.insert("1.0", recipe_text)
        text_widget.config(state="disabled")  # Make it read-only

    # Function to search for recipes
    def search_recipes(self):
        query = self.search_entry.get().strip().lower()  # Get the search query

        # Check if the query is empty
        if not query:
            messagebox.showwarning("Input Error", "Please enter a valid search term.")
            return

        # Search logic
        results = []
        for recipe in self.manager.recipes:
            if query in recipe.title.lower() or any(query in ingredient.name.lower() for ingredient in recipe.ingredients):
                results.append(recipe)

        # Display results
        if results:
            for recipe in results:
                self.display_recipe_details(recipe)
        else:
            messagebox.showinfo("No Results", "No recipes found matching your search criteria.")

    # Function to sort recipes in alphabetical order
    def sort_recipes(self):
        self.manager.sort_recipes()
        messagebox.showinfo("Success", "Recipes sorted alphabetically by title.")

    # Function to determine number of ingredients required and creates the appropriate amount of text boxes to enter that many ingredients
    def create_ingredient_fields(self):
        
        # check whether the input is valid
        try: 
            num_ingredients = int(simpledialog.askstring("Ingredients", "How many ingredients do you want to add?"))
        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        # destroy the previous entry boxes
        for widget in self.ingredient_frame.winfo_children():
            widget.destroy()
        # clear ingredient entries list
        self.ingredient_entries.clear()

        tk.Label(self.ingredient_frame, text="Ingredient", font=("Arial", 10, "bold")).grid(row=0, column=1, pady=2)
        tk.Label(self.ingredient_frame, text="Quantity", font=("Arial", 10, "bold")).grid(row=0, column=2, pady=2)
        tk.Label(self.ingredient_frame, text="Unit", font=("Arial", 10, "bold")).grid(row=0, column=3, pady=2)

        # Creation of the entry boxes and storing of the data
        for i in range(num_ingredients):
            tk.Label(self.ingredient_frame, text=f"Ingredient {i+1}:", font=("Arial", 10)).grid(row=i+1, column=0, pady=2)
            name_entry = tk.Entry(self.ingredient_frame, width=20)
            name_entry.grid(row=i+1, column=1, pady=2, padx=5)
            quantity_entry = tk.Entry(self.ingredient_frame, width=10)
            quantity_entry.grid(row=i+1, column=2, pady=2, padx=5)
            unit_entry = tk.Entry(self.ingredient_frame, width=10)
            unit_entry.grid(row=i+1, column=3, pady=2, padx=5)
            self.ingredient_entries.append((name_entry, quantity_entry, unit_entry))

    # Function to add a new recipe
    def add_recipe(self):
        title = self.title_entry.get().strip()
        steps = self.steps_entry.get("1.0", tk.END).strip().split('\n')

        # Creation and filling of the list of Ingredient objects for the new recipe being added
        ingredients = []
        for name_entry, quantity_entry, unit_entry in self.ingredient_entries:
            name = name_entry.get().strip()
            quantity = quantity_entry.get().strip()
            unit = unit_entry.get().strip()
            if name:
                ingredients.append(Ingredient(name, quantity, unit))

        # Creation of the new Recipe object
        # Check whether all 3 fields are filled
        if title and ingredients and steps:
            new_recipe = Recipe(title, ingredients, steps) # Create a new Recipe object
            self.manager.add_recipe(new_recipe)
            messagebox.showinfo("Success", "Recipe added successfully!") 
            self.title_entry.delete(0, tk.END)
            self.steps_entry.delete("1.0", tk.END)
            # Clear the ingredient entry boxes
            for entry_tuple in self.ingredient_entries:
                for entry in entry_tuple:
                    entry.delete(0, tk.END)
        else: # if found empty fields show a error message
            messagebox.showwarning("Input Error", "Please provide a title, ingredients, and steps.")
    
    # Function to display all recipes to the user
    def view_all_recipes(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("All Recipes")
    
        # Create scrollable frame
        canvas = tk.Canvas(result_window)
        scrollbar = ttk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        # Add scrollable frame to canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        # Add canvas to window
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add recipe titles
        for i, recipe in enumerate(self.manager.recipes):
            tk.Label(scrollable_frame, text=f"{i + 1}. {recipe.title}", font=("Arial", 12)).pack(anchor="w", pady=5)

        # combine the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # Function to delete a recipe
    def delete_recipe(self):
        title = simpledialog.askstring("Delete Recipe", "Enter the recipe title to delete:")
        # If the user presses cancel don't do anything
        if title:
            # Find the recipe to delete
            for recipe in self.manager.recipes:
                # If the recipe title matches with title entered 
                if recipe.title.lower() == title.lower():
                    # Ask users to confirm before deleting
                    confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{title}'?")
                    # delete the recipe when user confirmes
                    if confirm:
                        self.manager.delete_recipe(title)
                        messagebox.showinfo("Success", f"Recipe '{title}' deleted successfully.")
                        return
            # If no matching recipe is found
            messagebox.showwarning("Not Found", f"No recipe found with title '{title}'.")
    
    
# Main function to run the application
def main():
    root = tk.Tk()
    manager = RecipeManager(file_path)
    app = RecipeApp(root, manager)
    root.mainloop()


main()
