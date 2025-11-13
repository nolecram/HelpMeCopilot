#!/usr/bin/env python3
"""
Test module for event_attendants_tracker.py
Tests the functionality of the event attendants tracking application
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from event_attendants_tracker import (
    Attendant,
    Event,
    EventTracker
)


class TestAttendant:
    """Test cases for the Attendant class"""
    
    def test_attendant_creation(self):
        """Test creating an attendant"""
        attendant = Attendant("att001", "John Doe", "john@email.com", "555-1234")
        
        assert attendant.attendant_id == "att001"
        assert attendant.name == "John Doe"
        assert attendant.email == "john@email.com"
        assert attendant.phone == "555-1234"
        assert len(attendant.events_registered) == 0
    
    def test_attendant_creation_without_phone(self):
        """Test creating an attendant without phone number"""
        attendant = Attendant("att002", "Jane Smith", "jane@email.com")
        
        assert attendant.attendant_id == "att002"
        assert attendant.name == "Jane Smith"
        assert attendant.phone == ""
    
    def test_attendant_string_representation(self):
        """Test string representation of attendant"""
        attendant = Attendant("att003", "Bob Wilson", "bob@email.com")
        
        str_repr = str(attendant)
        assert "att003" in str_repr
        assert "Bob Wilson" in str_repr
        assert "bob@email.com" in str_repr


class TestEvent:
    """Test cases for the Event class"""
    
    def test_event_creation(self):
        """Test creating an event"""
        event = Event("evt001", "Tech Conference", "2025-03-15", "San Francisco", 100)
        
        assert event.event_id == "evt001"
        assert event.name == "Tech Conference"
        assert event.date == "2025-03-15"
        assert event.location == "San Francisco"
        assert event.max_capacity == 100
        assert len(event.registered_attendants) == 0
        assert len(event.checked_in_attendants) == 0
        assert len(event.checked_out_attendants) == 0
    
    def test_event_creation_without_capacity(self):
        """Test creating an event without max capacity"""
        event = Event("evt002", "Workshop", "2025-04-20", "New York")
        
        assert event.max_capacity is None
    
    def test_register_attendant(self):
        """Test registering an attendant to an event"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        result = event.register_attendant(attendant)
        
        assert result is True
        assert "att001" in event.registered_attendants
        assert "evt001" in attendant.events_registered
    
    def test_register_duplicate_attendant(self):
        """Test registering the same attendant twice"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        result = event.register_attendant(attendant)
        
        assert result is False
        assert len(event.registered_attendants) == 1
    
    def test_register_attendant_exceeds_capacity(self):
        """Test registering attendant when event is at capacity"""
        event = Event("evt001", "Small Event", "2025-03-15", "SF", max_capacity=1)
        attendant1 = Attendant("att001", "John Doe", "john@email.com")
        attendant2 = Attendant("att002", "Jane Smith", "jane@email.com")
        
        result1 = event.register_attendant(attendant1)
        result2 = event.register_attendant(attendant2)
        
        assert result1 is True
        assert result2 is False
        assert len(event.registered_attendants) == 1
    
    def test_unregister_attendant(self):
        """Test unregistering an attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        result = event.unregister_attendant("att001")
        
        assert result is True
        assert "att001" not in event.registered_attendants
        assert "evt001" not in attendant.events_registered
    
    def test_unregister_nonexistent_attendant(self):
        """Test unregistering an attendant that is not registered"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        
        result = event.unregister_attendant("att999")
        
        assert result is False
    
    def test_check_in_attendant(self):
        """Test checking in an attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        result = event.check_in_attendant("att001")
        
        assert result is True
        assert "att001" in event.checked_in_attendants
    
    def test_check_in_unregistered_attendant(self):
        """Test checking in an unregistered attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        
        result = event.check_in_attendant("att999")
        
        assert result is False
    
    def test_check_in_duplicate(self):
        """Test checking in an already checked-in attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        event.check_in_attendant("att001")
        result = event.check_in_attendant("att001")
        
        assert result is False
    
    def test_check_out_attendant(self):
        """Test checking out an attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        event.check_in_attendant("att001")
        result = event.check_out_attendant("att001")
        
        assert result is True
        assert "att001" not in event.checked_in_attendants
        assert "att001" in event.checked_out_attendants
    
    def test_check_out_not_checked_in_attendant(self):
        """Test checking out an attendant who is not checked in"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        result = event.check_out_attendant("att001")
        
        assert result is False
    
    def test_get_attendant_status_registered(self):
        """Test getting status of a registered attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        status = event.get_attendant_status("att001")
        
        assert status == "registered"
    
    def test_get_attendant_status_checked_in(self):
        """Test getting status of a checked-in attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        event.check_in_attendant("att001")
        status = event.get_attendant_status("att001")
        
        assert status == "checked_in"
    
    def test_get_attendant_status_checked_out(self):
        """Test getting status of a checked-out attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        attendant = Attendant("att001", "John Doe", "john@email.com")
        
        event.register_attendant(attendant)
        event.check_in_attendant("att001")
        event.check_out_attendant("att001")
        status = event.get_attendant_status("att001")
        
        assert status == "checked_out"
    
    def test_get_attendant_status_not_registered(self):
        """Test getting status of a non-registered attendant"""
        event = Event("evt001", "Conference", "2025-03-15", "SF")
        
        status = event.get_attendant_status("att999")
        
        assert status is None
    
    def test_get_statistics(self):
        """Test getting event statistics"""
        event = Event("evt001", "Conference", "2025-03-15", "SF", max_capacity=10)
        
        att1 = Attendant("att001", "John Doe", "john@email.com")
        att2 = Attendant("att002", "Jane Smith", "jane@email.com")
        att3 = Attendant("att003", "Bob Wilson", "bob@email.com")
        
        event.register_attendant(att1)
        event.register_attendant(att2)
        event.register_attendant(att3)
        
        event.check_in_attendant("att001")
        event.check_in_attendant("att002")
        event.check_out_attendant("att001")
        
        stats = event.get_statistics()
        
        assert stats['total_registered'] == 3
        assert stats['checked_in'] == 1  # att002 is still checked in
        assert stats['checked_out'] == 1  # att001 checked out
        assert stats['not_checked_in'] == 1  # att003 not checked in yet
        assert stats['capacity_remaining'] == 7


class TestEventTracker:
    """Test cases for the EventTracker class"""
    
    def test_tracker_creation(self):
        """Test creating an event tracker"""
        tracker = EventTracker()
        
        assert len(tracker.events) == 0
        assert len(tracker.attendants) == 0
    
    def test_create_event(self):
        """Test creating an event through tracker"""
        tracker = EventTracker()
        
        result = tracker.create_event("evt001", "Conference", "2025-03-15", "SF", 100)
        
        assert result is True
        assert "evt001" in tracker.events
        assert tracker.events["evt001"].name == "Conference"
    
    def test_create_duplicate_event(self):
        """Test creating an event with duplicate ID"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        result = tracker.create_event("evt001", "Another Event", "2025-04-20", "NY")
        
        assert result is False
        assert len(tracker.events) == 1
    
    def test_create_attendant(self):
        """Test creating an attendant through tracker"""
        tracker = EventTracker()
        
        result = tracker.create_attendant("att001", "John Doe", "john@email.com", "555-1234")
        
        assert result is True
        assert "att001" in tracker.attendants
        assert tracker.attendants["att001"].name == "John Doe"
    
    def test_create_duplicate_attendant(self):
        """Test creating an attendant with duplicate ID"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        result = tracker.create_attendant("att001", "Jane Smith", "jane@email.com")
        
        assert result is False
        assert len(tracker.attendants) == 1
    
    def test_register_attendant_to_event(self):
        """Test registering an attendant to an event through tracker"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        
        result = tracker.register_attendant_to_event("att001", "evt001")
        
        assert result is True
        assert "att001" in tracker.events["evt001"].registered_attendants
    
    def test_register_nonexistent_attendant_to_event(self):
        """Test registering a non-existent attendant"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        
        result = tracker.register_attendant_to_event("att999", "evt001")
        
        assert result is False
    
    def test_register_attendant_to_nonexistent_event(self):
        """Test registering an attendant to a non-existent event"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        
        result = tracker.register_attendant_to_event("att001", "evt999")
        
        assert result is False
    
    def test_get_attendant_events(self):
        """Test getting all events for an attendant"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        tracker.create_event("evt002", "Workshop", "2025-04-20", "NY")
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        
        tracker.register_attendant_to_event("att001", "evt001")
        tracker.register_attendant_to_event("att001", "evt002")
        
        events = tracker.get_attendant_events("att001")
        
        assert len(events) == 2
        assert any(e.event_id == "evt001" for e in events)
        assert any(e.event_id == "evt002" for e in events)
    
    def test_get_attendant_events_nonexistent(self):
        """Test getting events for a non-existent attendant"""
        tracker = EventTracker()
        
        events = tracker.get_attendant_events("att999")
        
        assert len(events) == 0
    
    def test_get_event_attendants(self):
        """Test getting all attendants for an event"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        tracker.create_attendant("att002", "Jane Smith", "jane@email.com")
        
        tracker.register_attendant_to_event("att001", "evt001")
        tracker.register_attendant_to_event("att002", "evt001")
        
        attendants = tracker.get_event_attendants("evt001")
        
        assert len(attendants) == 2
        assert any(a.attendant_id == "att001" for a in attendants)
        assert any(a.attendant_id == "att002" for a in attendants)
    
    def test_get_event_attendants_nonexistent(self):
        """Test getting attendants for a non-existent event"""
        tracker = EventTracker()
        
        attendants = tracker.get_event_attendants("evt999")
        
        assert len(attendants) == 0
    
    def test_search_attendants_by_name(self):
        """Test searching attendants by name"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        tracker.create_attendant("att002", "Jane Doe", "jane@email.com")
        tracker.create_attendant("att003", "Bob Smith", "bob@email.com")
        
        results = tracker.search_attendants("Doe")
        
        assert len(results) == 2
        assert any(a.attendant_id == "att001" for a in results)
        assert any(a.attendant_id == "att002" for a in results)
    
    def test_search_attendants_by_email(self):
        """Test searching attendants by email"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        tracker.create_attendant("att002", "Jane Smith", "jane@example.com")
        
        results = tracker.search_attendants("example")
        
        assert len(results) == 1
        assert results[0].attendant_id == "att002"
    
    def test_search_attendants_case_insensitive(self):
        """Test that attendant search is case insensitive"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        
        results = tracker.search_attendants("JOHN")
        
        assert len(results) == 1
        assert results[0].attendant_id == "att001"
    
    def test_search_attendants_empty_query(self):
        """Test searching attendants with empty query"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        
        results = tracker.search_attendants("")
        
        assert len(results) == 0
    
    def test_search_events_by_name(self):
        """Test searching events by name"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Python Conference", "2025-03-15", "SF")
        tracker.create_event("evt002", "Python Workshop", "2025-04-20", "NY")
        tracker.create_event("evt003", "Java Meetup", "2025-05-10", "LA")
        
        results = tracker.search_events("Python")
        
        assert len(results) == 2
        assert any(e.event_id == "evt001" for e in results)
        assert any(e.event_id == "evt002" for e in results)
    
    def test_search_events_by_location(self):
        """Test searching events by location"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "San Francisco")
        tracker.create_event("evt002", "Workshop", "2025-04-20", "New York")
        
        results = tracker.search_events("Francisco")
        
        assert len(results) == 1
        assert results[0].event_id == "evt001"
    
    def test_search_events_case_insensitive(self):
        """Test that event search is case insensitive"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        
        results = tracker.search_events("CONFERENCE")
        
        assert len(results) == 1
        assert results[0].event_id == "evt001"
    
    def test_search_events_empty_query(self):
        """Test searching events with empty query"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        
        results = tracker.search_events("")
        
        assert len(results) == 0
    
    def test_get_all_events(self):
        """Test getting all events"""
        tracker = EventTracker()
        
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        tracker.create_event("evt002", "Workshop", "2025-04-20", "NY")
        
        events = tracker.get_all_events()
        
        assert len(events) == 2
    
    def test_get_all_attendants(self):
        """Test getting all attendants"""
        tracker = EventTracker()
        
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        tracker.create_attendant("att002", "Jane Smith", "jane@email.com")
        
        attendants = tracker.get_all_attendants()
        
        assert len(attendants) == 2


class TestIntegration:
    """Integration tests for complete workflows"""
    
    def test_complete_event_workflow(self):
        """Test a complete event workflow from creation to check-out"""
        tracker = EventTracker()
        
        # Create event
        tracker.create_event("evt001", "Tech Conference", "2025-03-15", "SF", 100)
        
        # Create attendants
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        tracker.create_attendant("att002", "Jane Smith", "jane@email.com")
        
        # Register attendants
        tracker.register_attendant_to_event("att001", "evt001")
        tracker.register_attendant_to_event("att002", "evt001")
        
        # Check in attendants
        tracker.events["evt001"].check_in_attendant("att001")
        tracker.events["evt001"].check_in_attendant("att002")
        
        # Check out one attendant
        tracker.events["evt001"].check_out_attendant("att001")
        
        # Verify final state
        stats = tracker.events["evt001"].get_statistics()
        assert stats['total_registered'] == 2
        assert stats['checked_in'] == 1
        assert stats['checked_out'] == 1
        
        assert tracker.events["evt001"].get_attendant_status("att001") == "checked_out"
        assert tracker.events["evt001"].get_attendant_status("att002") == "checked_in"
    
    def test_multi_event_attendant_workflow(self):
        """Test an attendant registered for multiple events"""
        tracker = EventTracker()
        
        # Create events
        tracker.create_event("evt001", "Conference", "2025-03-15", "SF")
        tracker.create_event("evt002", "Workshop", "2025-04-20", "NY")
        tracker.create_event("evt003", "Meetup", "2025-05-10", "LA")
        
        # Create attendant
        tracker.create_attendant("att001", "John Doe", "john@email.com")
        
        # Register for multiple events
        tracker.register_attendant_to_event("att001", "evt001")
        tracker.register_attendant_to_event("att001", "evt002")
        tracker.register_attendant_to_event("att001", "evt003")
        
        # Verify registration
        events = tracker.get_attendant_events("att001")
        assert len(events) == 3
        
        # Check in to one event
        tracker.events["evt001"].check_in_attendant("att001")
        
        # Verify status differs across events
        assert tracker.events["evt001"].get_attendant_status("att001") == "checked_in"
        assert tracker.events["evt002"].get_attendant_status("att001") == "registered"
        assert tracker.events["evt003"].get_attendant_status("att001") == "registered"


if __name__ == "__main__":
    # Run tests manually if pytest is not available
    import inspect
    
    print("Running event attendants tracker tests...")
    
    test_classes = [TestAttendant, TestEvent, TestEventTracker, TestIntegration]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for test_class in test_classes:
        print(f"\n{test_class.__name__}:")
        instance = test_class()
        
        for name, method in inspect.getmembers(instance, predicate=inspect.ismethod):
            if name.startswith("test_"):
                total_tests += 1
                try:
                    method()
                    print(f"  ✓ {name}")
                    passed_tests += 1
                except AssertionError as e:
                    print(f"  ✗ {name}: {e}")
                    failed_tests += 1
                except Exception as e:
                    print(f"  ✗ {name}: Unexpected error - {e}")
                    failed_tests += 1
    
    print(f"\n{'='*60}")
    print(f"Tests completed: {total_tests} total, {passed_tests} passed, {failed_tests} failed")
    print(f"{'='*60}")
