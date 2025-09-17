"""
Test module for work_late_excuses.py

This module tests the functionality of the work late excuse generator.
"""

import sys
import os
import pytest

# Add the src/examples directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'examples'))

from work_late_excuses import (
    get_available_categories, 
    get_random_excuse, 
    WORK_LATE_EXCUSES
)


def test_available_categories():
    """Test that all expected categories are available."""
    categories = get_available_categories()
    expected_categories = ['traffic', 'transport', 'personal', 'technical', 'weather', 'family', 'health']
    
    assert len(categories) == len(expected_categories)
    for category in expected_categories:
        assert category in categories


def test_excuse_data_structure():
    """Test that the excuse data structure is properly formatted."""
    assert isinstance(WORK_LATE_EXCUSES, dict)
    
    for category, excuses in WORK_LATE_EXCUSES.items():
        assert isinstance(category, str)
        assert isinstance(excuses, list)
        assert len(excuses) > 0
        
        for excuse in excuses:
            assert isinstance(excuse, str)
            assert len(excuse.strip()) > 0


def test_get_random_excuse_with_valid_category():
    """Test getting a random excuse from a valid category."""
    for category in get_available_categories():
        cat, excuse = get_random_excuse(category)
        assert cat == category
        assert excuse in WORK_LATE_EXCUSES[category]
        assert isinstance(excuse, str)
        assert len(excuse.strip()) > 0


def test_get_random_excuse_without_category():
    """Test getting a random excuse without specifying a category."""
    cat, excuse = get_random_excuse()
    assert cat in get_available_categories()
    assert excuse in WORK_LATE_EXCUSES[cat]
    assert isinstance(excuse, str)
    assert len(excuse.strip()) > 0


def test_get_random_excuse_with_invalid_category():
    """Test getting an excuse with an invalid category."""
    cat, excuse = get_random_excuse('invalid_category')
    assert cat is None
    assert 'not found' in excuse
    assert 'Available categories' in excuse


def test_excuse_quality():
    """Test that excuses are realistic and appropriate for work situations."""
    for category, excuses in WORK_LATE_EXCUSES.items():
        for excuse in excuses:
            # Excuses should be reasonably long (not just one word)
            assert len(excuse.split()) >= 5, f"Excuse too short: {excuse}"
            
            # Excuses should start with capital letter and end with period
            assert excuse[0].isupper(), f"Excuse should start with capital: {excuse}"
            assert excuse.endswith('.'), f"Excuse should end with period: {excuse}"
            
            # Excuses should not contain inappropriate language
            inappropriate_words = ['damn', 'hell', 'crap', 'stupid']
            excuse_lower = excuse.lower()
            for word in inappropriate_words:
                assert word not in excuse_lower, f"Inappropriate word '{word}' in excuse: {excuse}"


def test_category_coverage():
    """Test that each category has a reasonable number of excuses."""
    for category, excuses in WORK_LATE_EXCUSES.items():
        # Each category should have at least 5 excuses for variety
        assert len(excuses) >= 5, f"Category '{category}' should have at least 5 excuses, has {len(excuses)}"


def test_excuse_uniqueness():
    """Test that excuses are unique within each category."""
    for category, excuses in WORK_LATE_EXCUSES.items():
        # Check for duplicate excuses within each category
        assert len(excuses) == len(set(excuses)), f"Duplicate excuses found in category '{category}'"


if __name__ == '__main__':
    pytest.main([__file__])