# Event Attendant Tracker

A comprehensive Python application for tracking attendants and activities at the **Cloud and AI Event in Melbourne**.

## Overview

The Event Attendant Tracker is designed to help event organizers efficiently manage attendants, activities, and registrations. It provides a simple yet powerful interface for:

- **Registering attendants** with their personal and organizational information
- **Creating activities** (workshops, sessions, networking events)
- **Managing registrations** for activities with capacity controls
- **Generating reports** and statistics about event participation
- **Exporting data** to JSON format for further analysis

## Features

### Attendant Management
- Register attendants with unique IDs
- Store contact information and organization details
- Track which activities each attendant is registered for
- Automatic timestamp of registration time

### Activity Management
- Create activities with detailed information (title, description, time, duration)
- Set capacity limits for each activity
- Track available spots in real-time
- Monitor participant lists

### Registration System
- Register attendants for multiple activities
- Automatic capacity checking (prevents over-booking)
- Duplicate registration prevention
- Easy unregistration process

### Reporting & Analytics
- Generate comprehensive event summaries
- Calculate participation statistics
- Identify most popular activities
- Export all data to JSON format
- Print formatted reports

## Installation

### Prerequisites
- Python 3.8 or higher
- pytest (for running tests)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nolecram/HelpMeCopilot.git
cd HelpMeCopilot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. The application is ready to use!

## Usage

### Running the Demo

The application includes a built-in demonstration:

```bash
python src/event_attendant_tracker.py
```

This will run a complete demo showing:
- Registration of 5 attendants
- Creation of 4 activities
- Multiple activity registrations
- Full event report
- JSON export

### Using the Application in Your Code

```python
from event_attendant_tracker import EventTracker

# Create an event tracker
tracker = EventTracker("Cloud and AI Event - Melbourne 2025")

# Register attendants
tracker.register_attendant("A001", "Sarah Chen", "sarah@techcorp.com", "TechCorp")
tracker.register_attendant("A002", "James Wilson", "james@innovate.au", "Innovate")

# Create activities
tracker.create_activity(
    "ACT001", 
    "AI in the Cloud: Best Practices",
    "Learn how to deploy and scale AI models in cloud environments",
    30,  # capacity
    "2025-11-15 09:00",  # start time
    90  # duration in minutes
)

# Register attendants for activities
tracker.register_for_activity("A001", "ACT001")
tracker.register_for_activity("A002", "ACT001")

# Get information
attendant = tracker.get_attendant("A001")
activity = tracker.get_activity("ACT001")

# Check activity details
print(f"Activity: {activity.title}")
print(f"Capacity: {len(activity.participants)}/{activity.capacity}")
print(f"Available spots: {activity.get_available_spots()}")

# Get attendant's schedule
activities = tracker.get_attendant_activities("A001")
for activity in activities:
    print(f"- {activity.title} at {activity.start_time}")

# Generate and print report
tracker.print_report()

# Export to JSON
tracker.export_to_json("event_data.json")
```

## API Reference

### EventTracker Class

Main class for managing the event.

#### Methods

**`__init__(event_name: str = "Cloud and AI Event - Melbourne")`**
- Initialize a new event tracker
- `event_name`: Name of the event (optional)

**`register_attendant(attendant_id: str, name: str, email: str, organization: str = "") -> Optional[Attendant]`**
- Register a new attendant
- Returns: `Attendant` object if successful, `None` if ID already exists

**`create_activity(activity_id: str, title: str, description: str, capacity: int, start_time: str, duration_minutes: int) -> Optional[Activity]`**
- Create a new activity
- Returns: `Activity` object if successful, `None` if ID already exists

**`register_for_activity(attendant_id: str, activity_id: str) -> bool`**
- Register an attendant for an activity
- Returns: `True` if successful, `False` otherwise (full, already registered, or invalid IDs)

**`unregister_from_activity(attendant_id: str, activity_id: str) -> bool`**
- Unregister an attendant from an activity
- Returns: `True` if successful, `False` otherwise

**`get_attendant(attendant_id: str) -> Optional[Attendant]`**
- Get an attendant by ID
- Returns: `Attendant` object or `None`

**`get_activity(activity_id: str) -> Optional[Activity]`**
- Get an activity by ID
- Returns: `Activity` object or `None`

**`get_all_attendants() -> List[Attendant]`**
- Get all registered attendants
- Returns: List of `Attendant` objects

**`get_all_activities() -> List[Activity]`**
- Get all activities
- Returns: List of `Activity` objects

**`get_attendant_activities(attendant_id: str) -> List[Activity]`**
- Get all activities an attendant is registered for
- Returns: List of `Activity` objects

**`get_activity_participants(activity_id: str) -> List[Attendant]`**
- Get all attendants participating in an activity
- Returns: List of `Attendant` objects

**`generate_summary() -> Dict`**
- Generate event statistics
- Returns: Dictionary with summary information

**`export_to_json(filename: str) -> bool`**
- Export all event data to JSON file
- Returns: `True` if successful, `False` otherwise

**`print_report()`**
- Print a formatted report to console

### Attendant Class

Represents an event attendant.

#### Attributes
- `attendant_id`: Unique identifier
- `name`: Full name
- `email`: Email address
- `organization`: Organization/company name
- `registered_at`: Registration timestamp
- `activities`: List of activity IDs

#### Methods
- `to_dict()`: Convert to dictionary
- `__str__()`: String representation

### Activity Class

Represents an activity or session.

#### Attributes
- `activity_id`: Unique identifier
- `title`: Activity title
- `description`: Detailed description
- `capacity`: Maximum participants
- `start_time`: Start time string
- `duration_minutes`: Duration in minutes
- `participants`: List of attendant IDs

#### Methods
- `is_full()`: Check if at capacity
- `get_available_spots()`: Get available spots
- `to_dict()`: Convert to dictionary
- `__str__()`: String representation

## Testing

The application includes comprehensive tests covering all functionality.

### Running Tests

```bash
# Run all tests
pytest tests/test_event_attendant_tracker.py -v

# Run specific test
pytest tests/test_event_attendant_tracker.py::test_register_attendant -v

# Run tests with coverage
pytest tests/test_event_attendant_tracker.py --cov=src.event_attendant_tracker
```

### Test Coverage

The test suite includes:
- **Attendant class tests**: Creation, data conversion, string representation
- **Activity class tests**: Capacity checks, spot availability, data conversion
- **EventTracker tests**: All CRUD operations, registration logic, reporting
- **Integration tests**: Complete workflow scenarios
- **Edge case tests**: Invalid inputs, duplicate registrations, capacity limits

Total: **40+ test cases**

## Example Output

When running the demo, you'll see output like:

```
Cloud and AI Event - Attendant Tracker Demo
============================================================

Registering attendants...
Registered 5 attendants

Creating activities...
Created 4 activities

Registering attendants for activities...

============================================================
Event Report: Cloud and AI Event - Melbourne 2025
============================================================

Summary Statistics:
  Total Attendants: 5
  Total Activities: 4
  Total Registrations: 12
  Average Activities per Attendant: 2.4
  Most Popular Activity: Networking Lunch
  Activities with Available Spots: 4

============================================================
All Activities:
============================================================

AI in the Cloud: Best Practices
  Time: 2025-11-15 09:00 (90 minutes)
  Capacity: 3/30
  Available Spots: 27
  Participants:
    - Sarah Chen
    - James Wilson
    - Emily Thompson

...
```

## Data Export Format

When exporting to JSON, the data structure is:

```json
{
  "event_name": "Cloud and AI Event - Melbourne 2025",
  "attendants": [
    {
      "attendant_id": "A001",
      "name": "Sarah Chen",
      "email": "sarah.chen@techcorp.com",
      "organization": "TechCorp",
      "registered_at": "2025-11-10T03:17:00.000000",
      "activities": ["ACT001", "ACT002", "ACT004"]
    }
  ],
  "activities": [
    {
      "activity_id": "ACT001",
      "title": "AI in the Cloud: Best Practices",
      "description": "Learn how to deploy and scale AI models",
      "capacity": 30,
      "start_time": "2025-11-15 09:00",
      "duration_minutes": 90,
      "participants": ["A001", "A002", "A005"],
      "available_spots": 27
    }
  ]
}
```

## Use Cases

### Conference Management
- Track attendees across multiple breakout sessions
- Monitor room capacity in real-time
- Generate participation reports

### Workshop Coordination
- Register participants for hands-on workshops
- Ensure workshop sizes stay within limits
- Track which workshops are most popular

### Networking Events
- Register attendees for networking sessions
- Track participation across different networking activities
- Export data for follow-up communications

### Hybrid Events
- Manage both in-person and virtual activities
- Track attendance across all formats
- Generate comprehensive participation analytics

## Best Practices

1. **Unique IDs**: Always use unique IDs for attendants and activities
2. **Capacity Planning**: Set realistic capacity limits for activities
3. **Time Formatting**: Use consistent time format (e.g., "2025-11-15 09:00")
4. **Regular Exports**: Export data regularly for backup purposes
5. **Error Handling**: Check return values to handle registration failures

## Troubleshooting

### Registration Fails
- Check if attendant/activity exists
- Verify activity isn't full
- Ensure attendant isn't already registered

### Export Fails
- Check file path permissions
- Ensure directory exists
- Verify disk space available

## Future Enhancements

Potential features for future versions:
- Email notifications for registrations
- Conflict detection (overlapping activities)
- QR code generation for check-in
- Real-time capacity monitoring dashboard
- Integration with calendar systems
- Waitlist management for full activities

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

This project is part of the HelpMeCopilot repository and is available under the MIT License.

## Contact

For questions or support, please open an issue on GitHub.

---

**Last Updated:** November 10, 2025  
**Version:** 1.0.0  
**Maintainer:** [nolecram](https://github.com/nolecram)
