#!/usr/bin/env python3
"""
Test module for event_attendant_tracker.py
Tests the functionality of the Event Attendant Tracker application
"""

import sys
import os
import json
import tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from event_attendant_tracker import Attendant, Activity, EventTracker


# Test Attendant Class
def test_attendant_creation():
    """Test creating an attendant with all fields"""
    attendant = Attendant("A001", "John Doe", "john@example.com", "TechCorp")
    
    assert attendant.attendant_id == "A001"
    assert attendant.name == "John Doe"
    assert attendant.email == "john@example.com"
    assert attendant.organization == "TechCorp"
    assert isinstance(attendant.activities, list)
    assert len(attendant.activities) == 0
    assert attendant.registered_at is not None


def test_attendant_without_organization():
    """Test creating an attendant without organization"""
    attendant = Attendant("A002", "Jane Smith", "jane@example.com")
    
    assert attendant.attendant_id == "A002"
    assert attendant.name == "Jane Smith"
    assert attendant.email == "jane@example.com"
    assert attendant.organization == ""


def test_attendant_to_dict():
    """Test converting attendant to dictionary"""
    attendant = Attendant("A003", "Bob Wilson", "bob@example.com", "CloudCorp")
    attendant.activities = ["ACT001", "ACT002"]
    
    data = attendant.to_dict()
    
    assert data['attendant_id'] == "A003"
    assert data['name'] == "Bob Wilson"
    assert data['email'] == "bob@example.com"
    assert data['organization'] == "CloudCorp"
    assert data['activities'] == ["ACT001", "ACT002"]
    assert 'registered_at' in data


def test_attendant_str():
    """Test string representation of attendant"""
    attendant1 = Attendant("A004", "Alice Brown", "alice@example.com", "DataTech")
    attendant2 = Attendant("A005", "Charlie Davis", "charlie@example.com")
    
    str1 = str(attendant1)
    str2 = str(attendant2)
    
    assert "Alice Brown" in str1
    assert "DataTech" in str1
    assert "alice@example.com" in str1
    
    assert "Charlie Davis" in str2
    assert "charlie@example.com" in str2


# Test Activity Class
def test_activity_creation():
    """Test creating an activity with all fields"""
    activity = Activity("ACT001", "AI Workshop", "Learn about AI", 30, "2025-11-15 09:00", 90)
    
    assert activity.activity_id == "ACT001"
    assert activity.title == "AI Workshop"
    assert activity.description == "Learn about AI"
    assert activity.capacity == 30
    assert activity.start_time == "2025-11-15 09:00"
    assert activity.duration_minutes == 90
    assert isinstance(activity.participants, list)
    assert len(activity.participants) == 0


def test_activity_is_full():
    """Test checking if an activity is full"""
    activity = Activity("ACT002", "Cloud Talk", "Cloud computing", 2, "2025-11-15 10:00", 60)
    
    assert not activity.is_full()
    
    activity.participants = ["A001"]
    assert not activity.is_full()
    
    activity.participants = ["A001", "A002"]
    assert activity.is_full()
    
    activity.participants = ["A001", "A002", "A003"]
    assert activity.is_full()


def test_activity_available_spots():
    """Test getting available spots in an activity"""
    activity = Activity("ACT003", "ML Session", "Machine learning", 5, "2025-11-15 11:00", 120)
    
    assert activity.get_available_spots() == 5
    
    activity.participants = ["A001", "A002"]
    assert activity.get_available_spots() == 3
    
    activity.participants = ["A001", "A002", "A003", "A004", "A005"]
    assert activity.get_available_spots() == 0
    
    activity.participants = ["A001", "A002", "A003", "A004", "A005", "A006"]
    assert activity.get_available_spots() == 0  # Should never be negative


def test_activity_to_dict():
    """Test converting activity to dictionary"""
    activity = Activity("ACT004", "DevOps Workshop", "CI/CD pipelines", 25, "2025-11-15 14:00", 90)
    activity.participants = ["A001", "A002"]
    
    data = activity.to_dict()
    
    assert data['activity_id'] == "ACT004"
    assert data['title'] == "DevOps Workshop"
    assert data['description'] == "CI/CD pipelines"
    assert data['capacity'] == 25
    assert data['start_time'] == "2025-11-15 14:00"
    assert data['duration_minutes'] == 90
    assert data['participants'] == ["A001", "A002"]
    assert data['available_spots'] == 23


def test_activity_str():
    """Test string representation of activity"""
    activity = Activity("ACT005", "Networking Event", "Meet and greet", 50, "2025-11-15 17:00", 60)
    activity.participants = ["A001", "A002", "A003"]
    
    activity_str = str(activity)
    
    assert "Networking Event" in activity_str
    assert "2025-11-15 17:00" in activity_str
    assert "60" in activity_str
    assert "3/50" in activity_str


# Test EventTracker Class
def test_event_tracker_creation():
    """Test creating an event tracker"""
    tracker = EventTracker("Test Event")
    
    assert tracker.event_name == "Test Event"
    assert isinstance(tracker.attendants, dict)
    assert isinstance(tracker.activities, dict)
    assert len(tracker.attendants) == 0
    assert len(tracker.activities) == 0


def test_event_tracker_default_name():
    """Test creating an event tracker with default name"""
    tracker = EventTracker()
    
    assert "Cloud and AI Event" in tracker.event_name
    assert "Melbourne" in tracker.event_name


def test_register_attendant():
    """Test registering an attendant"""
    tracker = EventTracker("Test Event")
    
    attendant = tracker.register_attendant("A001", "Test User", "test@example.com", "TestCorp")
    
    assert attendant is not None
    assert attendant.attendant_id == "A001"
    assert attendant.name == "Test User"
    assert len(tracker.attendants) == 1
    assert "A001" in tracker.attendants


def test_register_duplicate_attendant():
    """Test registering an attendant with duplicate ID"""
    tracker = EventTracker("Test Event")
    
    attendant1 = tracker.register_attendant("A001", "User One", "user1@example.com")
    attendant2 = tracker.register_attendant("A001", "User Two", "user2@example.com")
    
    assert attendant1 is not None
    assert attendant2 is None
    assert len(tracker.attendants) == 1


def test_create_activity():
    """Test creating an activity"""
    tracker = EventTracker("Test Event")
    
    activity = tracker.create_activity("ACT001", "Test Activity", "Description", 20, "2025-11-15 10:00", 60)
    
    assert activity is not None
    assert activity.activity_id == "ACT001"
    assert activity.title == "Test Activity"
    assert len(tracker.activities) == 1
    assert "ACT001" in tracker.activities


def test_create_duplicate_activity():
    """Test creating an activity with duplicate ID"""
    tracker = EventTracker("Test Event")
    
    activity1 = tracker.create_activity("ACT001", "Activity One", "Desc 1", 20, "2025-11-15 10:00", 60)
    activity2 = tracker.create_activity("ACT001", "Activity Two", "Desc 2", 30, "2025-11-15 11:00", 90)
    
    assert activity1 is not None
    assert activity2 is None
    assert len(tracker.activities) == 1


def test_register_for_activity():
    """Test registering an attendant for an activity"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    
    result = tracker.register_for_activity("A001", "ACT001")
    
    assert result is True
    assert "ACT001" in tracker.attendants["A001"].activities
    assert "A001" in tracker.activities["ACT001"].participants


def test_register_for_activity_invalid_attendant():
    """Test registering invalid attendant for activity"""
    tracker = EventTracker("Test Event")
    
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    
    result = tracker.register_for_activity("A999", "ACT001")
    
    assert result is False


def test_register_for_activity_invalid_activity():
    """Test registering attendant for invalid activity"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    
    result = tracker.register_for_activity("A001", "ACT999")
    
    assert result is False


def test_register_for_full_activity():
    """Test registering for an activity that is full"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.register_attendant("A002", "User Two", "user2@example.com")
    tracker.register_attendant("A003", "User Three", "user3@example.com")
    tracker.create_activity("ACT001", "Small Activity", "Description", 2, "2025-11-15 10:00", 60)
    
    result1 = tracker.register_for_activity("A001", "ACT001")
    result2 = tracker.register_for_activity("A002", "ACT001")
    result3 = tracker.register_for_activity("A003", "ACT001")
    
    assert result1 is True
    assert result2 is True
    assert result3 is False
    assert len(tracker.activities["ACT001"].participants) == 2


def test_register_for_activity_duplicate():
    """Test registering attendant for same activity twice"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    
    result1 = tracker.register_for_activity("A001", "ACT001")
    result2 = tracker.register_for_activity("A001", "ACT001")
    
    assert result1 is True
    assert result2 is False
    assert len(tracker.attendants["A001"].activities) == 1
    assert len(tracker.activities["ACT001"].participants) == 1


def test_unregister_from_activity():
    """Test unregistering an attendant from an activity"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    tracker.register_for_activity("A001", "ACT001")
    
    result = tracker.unregister_from_activity("A001", "ACT001")
    
    assert result is True
    assert "ACT001" not in tracker.attendants["A001"].activities
    assert "A001" not in tracker.activities["ACT001"].participants


def test_unregister_from_activity_not_registered():
    """Test unregistering when not registered"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    
    result = tracker.unregister_from_activity("A001", "ACT001")
    
    assert result is False


def test_unregister_from_activity_invalid():
    """Test unregistering with invalid IDs"""
    tracker = EventTracker("Test Event")
    
    result1 = tracker.unregister_from_activity("A999", "ACT001")
    result2 = tracker.unregister_from_activity("A001", "ACT999")
    
    assert result1 is False
    assert result2 is False


def test_get_attendant():
    """Test getting an attendant by ID"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    
    attendant = tracker.get_attendant("A001")
    assert attendant is not None
    assert attendant.name == "User One"
    
    attendant = tracker.get_attendant("A999")
    assert attendant is None


def test_get_activity():
    """Test getting an activity by ID"""
    tracker = EventTracker("Test Event")
    
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    
    activity = tracker.get_activity("ACT001")
    assert activity is not None
    assert activity.title == "Activity One"
    
    activity = tracker.get_activity("ACT999")
    assert activity is None


def test_get_all_attendants():
    """Test getting all attendants"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.register_attendant("A002", "User Two", "user2@example.com")
    tracker.register_attendant("A003", "User Three", "user3@example.com")
    
    attendants = tracker.get_all_attendants()
    
    assert len(attendants) == 3
    assert all(isinstance(a, Attendant) for a in attendants)


def test_get_all_activities():
    """Test getting all activities"""
    tracker = EventTracker("Test Event")
    
    tracker.create_activity("ACT001", "Activity One", "Desc 1", 20, "2025-11-15 10:00", 60)
    tracker.create_activity("ACT002", "Activity Two", "Desc 2", 30, "2025-11-15 11:00", 90)
    
    activities = tracker.get_all_activities()
    
    assert len(activities) == 2
    assert all(isinstance(a, Activity) for a in activities)


def test_get_attendant_activities():
    """Test getting activities for an attendant"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.create_activity("ACT001", "Activity One", "Desc 1", 20, "2025-11-15 10:00", 60)
    tracker.create_activity("ACT002", "Activity Two", "Desc 2", 30, "2025-11-15 11:00", 90)
    tracker.register_for_activity("A001", "ACT001")
    tracker.register_for_activity("A001", "ACT002")
    
    activities = tracker.get_attendant_activities("A001")
    
    assert len(activities) == 2
    assert all(isinstance(a, Activity) for a in activities)


def test_get_attendant_activities_invalid():
    """Test getting activities for invalid attendant"""
    tracker = EventTracker("Test Event")
    
    activities = tracker.get_attendant_activities("A999")
    
    assert len(activities) == 0


def test_get_activity_participants():
    """Test getting participants for an activity"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.register_attendant("A002", "User Two", "user2@example.com")
    tracker.create_activity("ACT001", "Activity One", "Desc", 20, "2025-11-15 10:00", 60)
    tracker.register_for_activity("A001", "ACT001")
    tracker.register_for_activity("A002", "ACT001")
    
    participants = tracker.get_activity_participants("ACT001")
    
    assert len(participants) == 2
    assert all(isinstance(p, Attendant) for p in participants)


def test_get_activity_participants_invalid():
    """Test getting participants for invalid activity"""
    tracker = EventTracker("Test Event")
    
    participants = tracker.get_activity_participants("ACT999")
    
    assert len(participants) == 0


def test_generate_summary():
    """Test generating event summary"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.register_attendant("A002", "User Two", "user2@example.com")
    tracker.create_activity("ACT001", "Activity One", "Desc 1", 20, "2025-11-15 10:00", 60)
    tracker.create_activity("ACT002", "Activity Two", "Desc 2", 2, "2025-11-15 11:00", 90)
    tracker.register_for_activity("A001", "ACT001")
    tracker.register_for_activity("A001", "ACT002")
    tracker.register_for_activity("A002", "ACT001")
    tracker.register_for_activity("A002", "ACT002")
    
    summary = tracker.generate_summary()
    
    assert summary['event_name'] == "Test Event"
    assert summary['total_attendants'] == 2
    assert summary['total_activities'] == 2
    assert summary['total_registrations'] == 4
    assert summary['average_activities_per_attendant'] == 2.0
    assert summary['most_popular_activity'] in ["Activity One", "Activity Two"]
    assert 'activities_with_available_spots' in summary


def test_generate_summary_empty():
    """Test generating summary with no data"""
    tracker = EventTracker("Empty Event")
    
    summary = tracker.generate_summary()
    
    assert summary['total_attendants'] == 0
    assert summary['total_activities'] == 0
    assert summary['total_registrations'] == 0
    assert summary['average_activities_per_attendant'] == 0
    assert summary['most_popular_activity'] is None


def test_export_to_json():
    """Test exporting event data to JSON"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com", "TechCorp")
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    tracker.register_for_activity("A001", "ACT001")
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        filename = f.name
    
    try:
        result = tracker.export_to_json(filename)
        assert result is True
        
        # Verify the file exists and has valid JSON
        assert os.path.exists(filename)
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        assert data['event_name'] == "Test Event"
        assert len(data['attendants']) == 1
        assert len(data['activities']) == 1
        assert data['attendants'][0]['attendant_id'] == "A001"
        assert data['activities'][0]['activity_id'] == "ACT001"
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def test_export_to_json_invalid_path():
    """Test exporting to invalid path"""
    tracker = EventTracker("Test Event")
    
    # Try to write to a non-existent directory
    result = tracker.export_to_json("/nonexistent/directory/file.json")
    
    assert result is False


def test_print_report():
    """Test printing event report (just ensure it doesn't crash)"""
    tracker = EventTracker("Test Event")
    
    tracker.register_attendant("A001", "User One", "user1@example.com")
    tracker.create_activity("ACT001", "Activity One", "Description", 20, "2025-11-15 10:00", 60)
    tracker.register_for_activity("A001", "ACT001")
    
    # Just ensure it runs without error
    try:
        tracker.print_report()
        assert True
    except Exception as e:
        assert False, f"print_report raised exception: {e}"


def test_integration_scenario():
    """Test a complete integration scenario"""
    tracker = EventTracker("Cloud and AI Event - Melbourne")
    
    # Register multiple attendants
    tracker.register_attendant("A001", "Sarah Chen", "sarah@techcorp.com", "TechCorp")
    tracker.register_attendant("A002", "James Wilson", "james@innovate.au", "Innovate")
    tracker.register_attendant("A003", "Maria Garcia", "maria@cloudstart.com", "CloudStart")
    
    # Create multiple activities
    tracker.create_activity("ACT001", "AI Workshop", "AI in the Cloud", 30, "2025-11-15 09:00", 90)
    tracker.create_activity("ACT002", "GitHub Copilot", "Copilot Workshop", 25, "2025-11-15 11:00", 120)
    tracker.create_activity("ACT003", "Networking", "Lunch and networking", 50, "2025-11-15 12:30", 60)
    
    # Register attendants for activities
    tracker.register_for_activity("A001", "ACT001")
    tracker.register_for_activity("A001", "ACT002")
    tracker.register_for_activity("A001", "ACT003")
    tracker.register_for_activity("A002", "ACT001")
    tracker.register_for_activity("A002", "ACT003")
    tracker.register_for_activity("A003", "ACT002")
    tracker.register_for_activity("A003", "ACT003")
    
    # Verify registrations
    assert len(tracker.get_all_attendants()) == 3
    assert len(tracker.get_all_activities()) == 3
    
    sarah_activities = tracker.get_attendant_activities("A001")
    assert len(sarah_activities) == 3
    
    networking_participants = tracker.get_activity_participants("ACT003")
    assert len(networking_participants) == 3
    
    # Generate summary
    summary = tracker.generate_summary()
    assert summary['total_attendants'] == 3
    assert summary['total_activities'] == 3
    assert summary['total_registrations'] == 7


if __name__ == "__main__":
    # Run tests manually if pytest is not available
    import inspect
    
    test_functions = [obj for name, obj in globals().items() 
                     if name.startswith('test_') and callable(obj)]
    
    print(f"Running {len(test_functions)} tests for Event Attendant Tracker...")
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error - {e}")
            failed += 1
    
    print(f"\nTests completed: {passed} passed, {failed} failed")
