# A simple recipe app project using Python
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
class RecipeApp:
    def __init__(self):
        self.recipes = []
    def add_recipe(self, name, ingredients, instructions):
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)
        print(f"Recipe '{name}' added successfully!")
    def delete_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                self.recipes.remove(recipe)
                print(f"Recipe '{name}' deleted successfully!")
                return
        print(f"Recipe '{name}' not found.")
    def display_recipes(self):
        if not self.recipes:
            print("No recipes found.")
            return
        for recipe in self.recipes:
            print(f"Recipe: {recipe.name}")
            print("Ingredients:")
            for ingredient in recipe.ingredients:
                print(f"- {ingredient}")
            print("Instructions:")
            for step, instruction in enumerate(recipe.instructions, start=1):
                print(f"{step}. {instruction}")
            print()
recipe_app = RecipeApp()
while True:
    print("Recipe App")
    print("1. Add Recipe")
    print("2. Delete Recipe")
    print("3. Display Recipes")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma-separated): ").split(',')
        instructions = input("Enter instructions (one step per line, enter 'done' when finished): ").split('\n')
        recipe_app.add_recipe(name, ingredients, instructions)
    elif choice == '2':
        name = input("Enter recipe name to delete: ")
        recipe_app.delete_recipe(name)
    elif choice == '3':
        recipe_app.display_recipes()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")