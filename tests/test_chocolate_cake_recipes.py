#!/usr/bin/env python3
"""
Test module for chocolate_cake_recipes.py
Tests the functionality of the chocolate cake recipes application
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from chocolate_cake_recipes import (
    CHOCOLATE_CAKE_RECIPES,
    search_recipes_by_keyword,
    get_recipe_by_number
)

def test_recipe_data_structure():
    """Test that all recipes have required fields"""
    required_fields = ['name', 'servings', 'prep_time', 'bake_time', 'ingredients', 'instructions']
    
    assert len(CHOCOLATE_CAKE_RECIPES) > 0, "Should have at least one recipe"
    
    for recipe_key, recipe in CHOCOLATE_CAKE_RECIPES.items():
        for field in required_fields:
            assert field in recipe, f"Recipe {recipe_key} missing field {field}"
        
        # Test data types
        assert isinstance(recipe['name'], str), f"Recipe {recipe_key} name should be string"
        assert isinstance(recipe['servings'], int), f"Recipe {recipe_key} servings should be int"
        assert isinstance(recipe['prep_time'], str), f"Recipe {recipe_key} prep_time should be string"
        assert isinstance(recipe['bake_time'], str), f"Recipe {recipe_key} bake_time should be string"
        assert isinstance(recipe['ingredients'], list), f"Recipe {recipe_key} ingredients should be list"
        assert isinstance(recipe['instructions'], list), f"Recipe {recipe_key} instructions should be list"
        
        # Test that lists are not empty
        assert len(recipe['ingredients']) > 0, f"Recipe {recipe_key} should have ingredients"
        assert len(recipe['instructions']) > 0, f"Recipe {recipe_key} should have instructions"

def test_search_recipes_by_keyword():
    """Test recipe search functionality"""
    # Test search by recipe name
    results = search_recipes_by_keyword("Classic")
    assert len(results) > 0, "Should find Classic Chocolate Cake"
    assert any("Classic" in name for _, name in results), "Should find recipe with 'Classic' in name"
    
    # Test search by ingredient
    results = search_recipes_by_keyword("buttermilk")
    assert len(results) > 0, "Should find recipes with buttermilk"
    
    # Test case insensitive search
    results = search_recipes_by_keyword("CHOCOLATE")
    assert len(results) > 0, "Should find recipes with chocolate (case insensitive)"
    
    # Test search with no results
    results = search_recipes_by_keyword("nonexistent_ingredient")
    assert len(results) == 0, "Should return empty list for non-existent keyword"
    
    # Test empty search
    results = search_recipes_by_keyword("")
    assert len(results) == 0, "Should return empty list for empty keyword"

def test_get_recipe_by_number():
    """Test getting recipe by number"""
    total_recipes = len(CHOCOLATE_CAKE_RECIPES)
    
    # Test valid recipe numbers
    recipe_key = get_recipe_by_number(1)
    assert recipe_key is not None, "Should return valid recipe key for number 1"
    assert recipe_key in CHOCOLATE_CAKE_RECIPES, "Should return existing recipe key"
    
    recipe_key = get_recipe_by_number(total_recipes)
    assert recipe_key is not None, f"Should return valid recipe key for number {total_recipes}"
    
    # Test invalid recipe numbers
    assert get_recipe_by_number(0) is None, "Should return None for recipe number 0"
    assert get_recipe_by_number(total_recipes + 1) is None, "Should return None for number too high"
    assert get_recipe_by_number(-1) is None, "Should return None for negative number"

def test_recipe_content_quality():
    """Test that recipes have reasonable content"""
    for recipe_key, recipe in CHOCOLATE_CAKE_RECIPES.items():
        # Test servings is reasonable
        assert 1 <= recipe['servings'] <= 20, f"Recipe {recipe_key} servings should be between 1 and 20"
        
        # Test ingredients have reasonable content
        for ingredient in recipe['ingredients']:
            assert len(ingredient.strip()) > 0, f"Recipe {recipe_key} has empty ingredient"
            assert len(ingredient) > 3, f"Recipe {recipe_key} has very short ingredient: {ingredient}"
        
        # Test instructions have reasonable content
        for instruction in recipe['instructions']:
            assert len(instruction.strip()) > 0, f"Recipe {recipe_key} has empty instruction"
            assert len(instruction) > 10, f"Recipe {recipe_key} has very short instruction: {instruction}"

def test_specific_recipes_exist():
    """Test that expected recipes exist"""
    expected_recipes = [
        "classic_chocolate",
        "fudgy_chocolate", 
        "german_chocolate",
        "death_by_chocolate",
        "vegan_chocolate"
    ]
    
    for recipe_key in expected_recipes:
        assert recipe_key in CHOCOLATE_CAKE_RECIPES, f"Expected recipe {recipe_key} not found"

def test_recipe_names_are_descriptive():
    """Test that recipe names are descriptive and contain 'Chocolate'"""
    for recipe_key, recipe in CHOCOLATE_CAKE_RECIPES.items():
        name = recipe['name']
        assert "Chocolate" in name or "chocolate" in name, f"Recipe {recipe_key} name should contain 'Chocolate'"
        assert len(name) > 5, f"Recipe {recipe_key} name should be descriptive"
        assert "Cake" in name or "cake" in name, f"Recipe {recipe_key} name should contain 'Cake'"

if __name__ == "__main__":
    # Run tests manually if pytest is not available
    test_functions = [
        test_recipe_data_structure,
        test_search_recipes_by_keyword,
        test_get_recipe_by_number,
        test_recipe_content_quality,
        test_specific_recipes_exist,
        test_recipe_names_are_descriptive
    ]
    
    print("Running chocolate cake recipes tests...")
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error - {e}")
    
    print("Tests completed!")