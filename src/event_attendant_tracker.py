#!/usr/bin/env python3
"""
Event Attendant Tracker
A Python application for tracking attendants and activities at the Cloud and AI Event in Melbourne.

This application allows event organizers to:
- Register attendants with their details
- Create and manage activities
- Track which attendants are participating in which activities
- Generate reports and statistics

Usage:
    python event_attendant_tracker.py
"""

from datetime import datetime
from typing import List, Dict, Optional
import json


class Attendant:
    """Represents an event attendant with their personal information."""
    
    def __init__(self, attendant_id: str, name: str, email: str, organization: str = ""):
        """
        Initialize an Attendant.
        
        Args:
            attendant_id: Unique identifier for the attendant
            name: Full name of the attendant
            email: Email address of the attendant
            organization: Organization/company the attendant represents (optional)
        """
        self.attendant_id = attendant_id
        self.name = name
        self.email = email
        self.organization = organization
        self.registered_at = datetime.now()
        self.activities = []  # List of activity IDs the attendant is participating in
    
    def to_dict(self) -> Dict:
        """Convert attendant to dictionary format."""
        return {
            'attendant_id': self.attendant_id,
            'name': self.name,
            'email': self.email,
            'organization': self.organization,
            'registered_at': self.registered_at.isoformat(),
            'activities': self.activities
        }
    
    def __str__(self) -> str:
        """String representation of the attendant."""
        org = f" ({self.organization})" if self.organization else ""
        return f"{self.name}{org} - {self.email}"


class Activity:
    """Represents an activity or session at the event."""
    
    def __init__(self, activity_id: str, title: str, description: str, 
                 capacity: int, start_time: str, duration_minutes: int):
        """
        Initialize an Activity.
        
        Args:
            activity_id: Unique identifier for the activity
            title: Title of the activity
            description: Detailed description of the activity
            capacity: Maximum number of attendants for this activity
            start_time: Start time (e.g., "2025-11-10 10:00")
            duration_minutes: Duration of the activity in minutes
        """
        self.activity_id = activity_id
        self.title = title
        self.description = description
        self.capacity = capacity
        self.start_time = start_time
        self.duration_minutes = duration_minutes
        self.participants = []  # List of attendant IDs
    
    def is_full(self) -> bool:
        """Check if the activity has reached capacity."""
        return len(self.participants) >= self.capacity
    
    def get_available_spots(self) -> int:
        """Get the number of available spots remaining."""
        return max(0, self.capacity - len(self.participants))
    
    def to_dict(self) -> Dict:
        """Convert activity to dictionary format."""
        return {
            'activity_id': self.activity_id,
            'title': self.title,
            'description': self.description,
            'capacity': self.capacity,
            'start_time': self.start_time,
            'duration_minutes': self.duration_minutes,
            'participants': self.participants,
            'available_spots': self.get_available_spots()
        }
    
    def __str__(self) -> str:
        """String representation of the activity."""
        return f"{self.title} - {self.start_time} ({self.duration_minutes} min) [{len(self.participants)}/{self.capacity}]"


class EventTracker:
    """Main event tracker that manages attendants and activities."""
    
    def __init__(self, event_name: str = "Cloud and AI Event - Melbourne"):
        """
        Initialize the Event Tracker.
        
        Args:
            event_name: Name of the event
        """
        self.event_name = event_name
        self.attendants: Dict[str, Attendant] = {}
        self.activities: Dict[str, Activity] = {}
    
    def register_attendant(self, attendant_id: str, name: str, email: str, 
                          organization: str = "") -> Optional[Attendant]:
        """
        Register a new attendant.
        
        Args:
            attendant_id: Unique identifier for the attendant
            name: Full name of the attendant
            email: Email address of the attendant
            organization: Organization/company name (optional)
            
        Returns:
            The newly created Attendant object, or None if attendant_id already exists
        """
        if attendant_id in self.attendants:
            return None
        
        attendant = Attendant(attendant_id, name, email, organization)
        self.attendants[attendant_id] = attendant
        return attendant
    
    def create_activity(self, activity_id: str, title: str, description: str,
                       capacity: int, start_time: str, duration_minutes: int) -> Optional[Activity]:
        """
        Create a new activity.
        
        Args:
            activity_id: Unique identifier for the activity
            title: Title of the activity
            description: Detailed description
            capacity: Maximum number of participants
            start_time: Start time string
            duration_minutes: Duration in minutes
            
        Returns:
            The newly created Activity object, or None if activity_id already exists
        """
        if activity_id in self.activities:
            return None
        
        activity = Activity(activity_id, title, description, capacity, start_time, duration_minutes)
        self.activities[activity_id] = activity
        return activity
    
    def register_for_activity(self, attendant_id: str, activity_id: str) -> bool:
        """
        Register an attendant for an activity.
        
        Args:
            attendant_id: ID of the attendant
            activity_id: ID of the activity
            
        Returns:
            True if registration successful, False otherwise
        """
        if attendant_id not in self.attendants or activity_id not in self.activities:
            return False
        
        attendant = self.attendants[attendant_id]
        activity = self.activities[activity_id]
        
        # Check if activity is full
        if activity.is_full():
            return False
        
        # Check if already registered
        if activity_id in attendant.activities:
            return False
        
        # Register the attendant for the activity
        attendant.activities.append(activity_id)
        activity.participants.append(attendant_id)
        return True
    
    def unregister_from_activity(self, attendant_id: str, activity_id: str) -> bool:
        """
        Unregister an attendant from an activity.
        
        Args:
            attendant_id: ID of the attendant
            activity_id: ID of the activity
            
        Returns:
            True if unregistration successful, False otherwise
        """
        if attendant_id not in self.attendants or activity_id not in self.activities:
            return False
        
        attendant = self.attendants[attendant_id]
        activity = self.activities[activity_id]
        
        if activity_id not in attendant.activities:
            return False
        
        attendant.activities.remove(activity_id)
        activity.participants.remove(attendant_id)
        return True
    
    def get_attendant(self, attendant_id: str) -> Optional[Attendant]:
        """Get an attendant by ID."""
        return self.attendants.get(attendant_id)
    
    def get_activity(self, activity_id: str) -> Optional[Activity]:
        """Get an activity by ID."""
        return self.activities.get(activity_id)
    
    def get_all_attendants(self) -> List[Attendant]:
        """Get all registered attendants."""
        return list(self.attendants.values())
    
    def get_all_activities(self) -> List[Activity]:
        """Get all activities."""
        return list(self.activities.values())
    
    def get_attendant_activities(self, attendant_id: str) -> List[Activity]:
        """
        Get all activities an attendant is registered for.
        
        Args:
            attendant_id: ID of the attendant
            
        Returns:
            List of Activity objects
        """
        if attendant_id not in self.attendants:
            return []
        
        attendant = self.attendants[attendant_id]
        return [self.activities[aid] for aid in attendant.activities if aid in self.activities]
    
    def get_activity_participants(self, activity_id: str) -> List[Attendant]:
        """
        Get all attendants participating in an activity.
        
        Args:
            activity_id: ID of the activity
            
        Returns:
            List of Attendant objects
        """
        if activity_id not in self.activities:
            return []
        
        activity = self.activities[activity_id]
        return [self.attendants[aid] for aid in activity.participants if aid in self.attendants]
    
    def generate_summary(self) -> Dict:
        """
        Generate a summary report of the event.
        
        Returns:
            Dictionary containing event statistics
        """
        total_attendants = len(self.attendants)
        total_activities = len(self.activities)
        
        # Calculate activity statistics
        total_registrations = sum(len(a.activities) for a in self.attendants.values())
        avg_activities_per_attendant = total_registrations / total_attendants if total_attendants > 0 else 0
        
        # Find most popular activity
        most_popular_activity = None
        max_participants = 0
        for activity in self.activities.values():
            if len(activity.participants) > max_participants:
                max_participants = len(activity.participants)
                most_popular_activity = activity.title
        
        # Find activities with available spots
        activities_with_spots = sum(1 for a in self.activities.values() if not a.is_full())
        
        return {
            'event_name': self.event_name,
            'total_attendants': total_attendants,
            'total_activities': total_activities,
            'total_registrations': total_registrations,
            'average_activities_per_attendant': round(avg_activities_per_attendant, 2),
            'most_popular_activity': most_popular_activity,
            'activities_with_available_spots': activities_with_spots
        }
    
    def export_to_json(self, filename: str) -> bool:
        """
        Export event data to JSON file.
        
        Args:
            filename: Path to the output JSON file
            
        Returns:
            True if export successful, False otherwise
        """
        try:
            data = {
                'event_name': self.event_name,
                'attendants': [a.to_dict() for a in self.attendants.values()],
                'activities': [a.to_dict() for a in self.activities.values()]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False
    
    def print_report(self):
        """Print a formatted report of the event."""
        print(f"\n{'='*60}")
        print(f"Event Report: {self.event_name}")
        print(f"{'='*60}\n")
        
        summary = self.generate_summary()
        print("Summary Statistics:")
        print(f"  Total Attendants: {summary['total_attendants']}")
        print(f"  Total Activities: {summary['total_activities']}")
        print(f"  Total Registrations: {summary['total_registrations']}")
        print(f"  Average Activities per Attendant: {summary['average_activities_per_attendant']}")
        if summary['most_popular_activity']:
            print(f"  Most Popular Activity: {summary['most_popular_activity']}")
        print(f"  Activities with Available Spots: {summary['activities_with_available_spots']}")
        
        print(f"\n{'='*60}")
        print("All Activities:")
        print(f"{'='*60}")
        for activity in self.activities.values():
            print(f"\n{activity.title}")
            print(f"  Time: {activity.start_time} ({activity.duration_minutes} minutes)")
            print(f"  Capacity: {len(activity.participants)}/{activity.capacity}")
            print(f"  Available Spots: {activity.get_available_spots()}")
            if activity.participants:
                print(f"  Participants:")
                for aid in activity.participants[:5]:  # Show first 5
                    if aid in self.attendants:
                        print(f"    - {self.attendants[aid].name}")
                if len(activity.participants) > 5:
                    print(f"    ... and {len(activity.participants) - 5} more")


def demo():
    """Run a demonstration of the Event Attendant Tracker."""
    print("Cloud and AI Event - Attendant Tracker Demo")
    print("=" * 60)
    
    # Create event tracker
    tracker = EventTracker("Cloud and AI Event - Melbourne 2025")
    
    # Register attendants
    print("\nRegistering attendants...")
    tracker.register_attendant("A001", "Sarah Chen", "sarah.chen@techcorp.com", "TechCorp")
    tracker.register_attendant("A002", "James Wilson", "james.w@innovate.au", "Innovate Australia")
    tracker.register_attendant("A003", "Maria Garcia", "maria.g@cloudstart.com", "CloudStart")
    tracker.register_attendant("A004", "Ahmed Hassan", "ahmed.h@ailab.edu", "AI Research Lab")
    tracker.register_attendant("A005", "Emily Thompson", "e.thompson@datatech.io", "DataTech Solutions")
    print(f"Registered {len(tracker.get_all_attendants())} attendants")
    
    # Create activities
    print("\nCreating activities...")
    tracker.create_activity("ACT001", "AI in the Cloud: Best Practices", 
                          "Learn how to deploy and scale AI models in cloud environments",
                          30, "2025-11-15 09:00", 90)
    tracker.create_activity("ACT002", "GitHub Copilot Workshop",
                          "Hands-on workshop exploring GitHub Copilot for productivity",
                          25, "2025-11-15 11:00", 120)
    tracker.create_activity("ACT003", "Azure AI Services Deep Dive",
                          "Explore Azure's AI and ML services with practical examples",
                          20, "2025-11-15 14:00", 90)
    tracker.create_activity("ACT004", "Networking Lunch",
                          "Connect with fellow attendants and speakers",
                          50, "2025-11-15 12:30", 60)
    print(f"Created {len(tracker.get_all_activities())} activities")
    
    # Register attendants for activities
    print("\nRegistering attendants for activities...")
    tracker.register_for_activity("A001", "ACT001")
    tracker.register_for_activity("A001", "ACT002")
    tracker.register_for_activity("A001", "ACT004")
    tracker.register_for_activity("A002", "ACT001")
    tracker.register_for_activity("A002", "ACT003")
    tracker.register_for_activity("A003", "ACT002")
    tracker.register_for_activity("A003", "ACT004")
    tracker.register_for_activity("A004", "ACT003")
    tracker.register_for_activity("A004", "ACT004")
    tracker.register_for_activity("A005", "ACT001")
    tracker.register_for_activity("A005", "ACT002")
    tracker.register_for_activity("A005", "ACT003")
    
    # Print full report
    tracker.print_report()
    
    # Show individual attendant schedule
    print(f"\n{'='*60}")
    print("Individual Attendant Schedule Example:")
    print(f"{'='*60}")
    attendant = tracker.get_attendant("A001")
    if attendant:
        print(f"\nSchedule for: {attendant.name}")
        activities = tracker.get_attendant_activities("A001")
        for activity in activities:
            print(f"  - {activity.title} at {activity.start_time}")
    
    # Export to JSON
    print(f"\n{'='*60}")
    print("Exporting event data...")
    if tracker.export_to_json("/tmp/event_data.json"):
        print("Event data exported to /tmp/event_data.json")
    
    print(f"\n{'='*60}")
    print("Demo completed!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    demo()
