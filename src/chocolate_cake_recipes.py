#!/usr/bin/env python3
"""
Chocolate Cake Recipes Application
Display different recipes for chocolate cakes
"""

# Recipe database with different chocolate cake recipes
CHOCOLATE_CAKE_RECIPES = {
    "classic_chocolate": {
        "name": "Classic Chocolate Cake",
        "servings": 8,
        "prep_time": "20 minutes",
        "bake_time": "30-35 minutes",
        "ingredients": [
            "2 cups all-purpose flour",
            "2 cups granulated sugar",
            "3/4 cup unsweetened cocoa powder",
            "2 teaspoons baking soda",
            "1 teaspoon baking powder",
            "1 teaspoon salt",
            "2 large eggs",
            "1 cup buttermilk",
            "1 cup strong black coffee (cooled)",
            "1/2 cup vegetable oil",
            "1 teaspoon vanilla extract"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease and flour two 9-inch round pans.",
            "In a large bowl, whisk together flour, sugar, cocoa, baking soda, baking powder, and salt.",
            "In another bowl, beat eggs, then mix in buttermilk, coffee, oil, and vanilla.",
            "Gradually add wet ingredients to dry ingredients, mixing until smooth.",
            "Divide batter between prepared pans.",
            "Bake for 30-35 minutes or until toothpick inserted in center comes out clean.",
            "Cool in pans for 10 minutes, then turn out onto wire racks."
        ]
    },
    "fudgy_chocolate": {
        "name": "Fudgy Chocolate Cake",
        "servings": 10,
        "prep_time": "15 minutes",
        "bake_time": "25-30 minutes",
        "ingredients": [
            "1 3/4 cups all-purpose flour",
            "2 cups sugar",
            "3/4 cup cocoa powder",
            "2 teaspoons baking soda",
            "1 teaspoon baking powder",
            "1 teaspoon salt",
            "2 eggs",
            "1 cup sour cream",
            "1 cup hot coffee",
            "1/2 cup melted butter",
            "2 teaspoons vanilla extract",
            "1 cup dark chocolate chips"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease a 9x13 inch pan.",
            "Combine flour, sugar, cocoa, baking soda, baking powder, and salt in large bowl.",
            "In separate bowl, whisk eggs, sour cream, coffee, melted butter, and vanilla.",
            "Add wet ingredients to dry ingredients and mix until combined.",
            "Fold in chocolate chips.",
            "Pour into prepared pan and bake 25-30 minutes.",
            "Cool completely before frosting."
        ]
    },
    "german_chocolate": {
        "name": "German Chocolate Cake",
        "servings": 12,
        "prep_time": "30 minutes",
        "bake_time": "30 minutes",
        "ingredients": [
            "1 package (4 oz) sweet baking chocolate",
            "1/2 cup boiling water",
            "1 cup butter, softened",
            "2 cups sugar",
            "4 egg yolks",
            "1 teaspoon vanilla",
            "2 1/2 cups cake flour",
            "1 teaspoon baking soda",
            "1/2 teaspoon salt",
            "1 cup buttermilk",
            "4 egg whites"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease three 9-inch round pans.",
            "Melt chocolate in boiling water. Cool.",
            "Cream butter and sugar until fluffy. Beat in egg yolks and vanilla.",
            "Add melted chocolate mixture.",
            "Combine flour, baking soda, and salt. Add alternately with buttermilk.",
            "Beat egg whites until stiff peaks form. Fold into batter.",
            "Divide among pans. Bake 30 minutes.",
            "Cool and frost with coconut-pecan frosting."
        ]
    },
    "death_by_chocolate": {
        "name": "Death by Chocolate Cake",
        "servings": 10,
        "prep_time": "25 minutes",
        "bake_time": "35-40 minutes",
        "ingredients": [
            "2 cups all-purpose flour",
            "2 cups sugar",
            "1 cup cocoa powder",
            "2 teaspoons baking soda",
            "1 teaspoon baking powder",
            "1 teaspoon salt",
            "3 large eggs",
            "1 1/2 cups strong coffee",
            "3/4 cup vegetable oil",
            "1/2 cup chocolate syrup",
            "1 cup mini chocolate chips",
            "1/2 cup dark chocolate chunks"
        ],
        "instructions": [
            "Preheat oven to 325°F (165°C). Grease a bundt pan thoroughly.",
            "Whisk together flour, sugar, cocoa, baking soda, baking powder, and salt.",
            "In large bowl, beat eggs, then add coffee, oil, and chocolate syrup.",
            "Gradually mix in dry ingredients until smooth.",
            "Fold in chocolate chips and chunks.",
            "Pour into bundt pan and bake 35-40 minutes.",
            "Cool completely before removing from pan."
        ]
    },
    "vegan_chocolate": {
        "name": "Vegan Chocolate Cake",
        "servings": 8,
        "prep_time": "15 minutes",
        "bake_time": "28-32 minutes",
        "ingredients": [
            "1 1/2 cups all-purpose flour",
            "1 cup sugar",
            "1/4 cup cocoa powder",
            "1 teaspoon baking soda",
            "1/2 teaspoon salt",
            "1 cup water",
            "1/3 cup vegetable oil",
            "1 tablespoon white vinegar",
            "1 teaspoon vanilla extract",
            "1/2 cup dairy-free chocolate chips"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease an 8-inch round pan.",
            "In large bowl, whisk together flour, sugar, cocoa, baking soda, and salt.",
            "In separate bowl, mix water, oil, vinegar, and vanilla.",
            "Pour wet ingredients into dry ingredients and stir until just combined.",
            "Fold in chocolate chips.",
            "Pour into prepared pan and bake 28-32 minutes.",
            "Cool completely before serving."
        ]
    }
}

def display_recipe(recipe_key):
    """Display a complete recipe with formatting"""
    if recipe_key not in CHOCOLATE_CAKE_RECIPES:
        print("Recipe not found!")
        return
    
    recipe = CHOCOLATE_CAKE_RECIPES[recipe_key]
    
    print(f"\n{'='*60}")
    print(f"🍰 {recipe['name']} 🍰")
    print(f"{'='*60}")
    print(f"Servings: {recipe['servings']}")
    print(f"Prep Time: {recipe['prep_time']}")
    print(f"Bake Time: {recipe['bake_time']}")
    
    print(f"\n📋 INGREDIENTS:")
    print("-" * 30)
    for ingredient in recipe['ingredients']:
        print(f"• {ingredient}")
    
    print(f"\n👩‍🍳 INSTRUCTIONS:")
    print("-" * 30)
    for i, instruction in enumerate(recipe['instructions'], 1):
        print(f"{i}. {instruction}")
    print("=" * 60)

def search_recipes_by_keyword(keyword):
    """Search recipes by keyword in name or ingredients"""
    if not keyword or not keyword.strip():
        return []
    
    matching_recipes = []
    keyword_lower = keyword.lower()
    
    for key, recipe in CHOCOLATE_CAKE_RECIPES.items():
        # Search in recipe name
        if keyword_lower in recipe['name'].lower():
            matching_recipes.append((key, recipe['name']))
            continue
        
        # Search in ingredients
        for ingredient in recipe['ingredients']:
            if keyword_lower in ingredient.lower():
                matching_recipes.append((key, recipe['name']))
                break
    
    return matching_recipes

def list_all_recipes():
    """Display a list of all available recipes"""
    print("\n🍫 Available Chocolate Cake Recipes:")
    print("=" * 50)
    for i, (key, recipe) in enumerate(CHOCOLATE_CAKE_RECIPES.items(), 1):
        print(f"{i}. {recipe['name']}")
        print(f"   Servings: {recipe['servings']} | Prep: {recipe['prep_time']} | Bake: {recipe['bake_time']}")
    print("=" * 50)

def get_recipe_by_number(recipe_number):
    """Get recipe key by its display number"""
    recipe_keys = list(CHOCOLATE_CAKE_RECIPES.keys())
    if 1 <= recipe_number <= len(recipe_keys):
        return recipe_keys[recipe_number - 1]
    return None

def main():
    """Main function to run the chocolate cake recipes application"""
    print("🍰 Chocolate Cake Recipes Collection 🍰")
    print("=" * 45)
    
    # Initialize counter for recipe views
    recipes_viewed = 0
    
    while True:
        print("\nSelect an option:")
        print("1. View all available recipes")
        print("2. Display a specific recipe")
        print("3. Search recipes by keyword")
        print("4. View recipes viewed count")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                list_all_recipes()
            
            elif choice == 2:
                list_all_recipes()
                try:
                    recipe_num = int(input(f"\nEnter recipe number (1-{len(CHOCOLATE_CAKE_RECIPES)}): "))
                    recipe_key = get_recipe_by_number(recipe_num)
                    if recipe_key:
                        display_recipe(recipe_key)
                        recipes_viewed += 1
                    else:
                        print("Invalid recipe number!")
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == 3:
                keyword = input("Enter search keyword: ").strip()
                if keyword:
                    matches = search_recipes_by_keyword(keyword)
                    if matches:
                        print(f"\n🔍 Found {len(matches)} recipe(s) matching '{keyword}':")
                        print("-" * 40)
                        for i, (key, name) in enumerate(matches, 1):
                            print(f"{i}. {name}")
                        
                        try:
                            choice_num = int(input(f"\nSelect recipe to view (1-{len(matches)}): "))
                            if 1 <= choice_num <= len(matches):
                                selected_key = matches[choice_num - 1][0]
                                display_recipe(selected_key)
                                recipes_viewed += 1
                            else:
                                print("Invalid selection!")
                        except ValueError:
                            print("Please enter a valid number.")
                    else:
                        print(f"No recipes found matching '{keyword}'.")
                else:
                    print("Please enter a search keyword.")
            
            elif choice == 4:
                print(f"Number of recipes viewed: {recipes_viewed}")
            
            elif choice == 5:
                print(f"Total recipes viewed: {recipes_viewed}")
                print("Thank you for using the Chocolate Cake Recipes Collection! 🍰")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()