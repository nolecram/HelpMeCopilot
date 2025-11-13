# Event Attendants Tracking Application

A comprehensive Python application for tracking attendants across multiple events with check-in/check-out functionality.

## Overview

The Event Attendants Tracking Application provides a complete solution for managing events, attendants, and their participation status. It features a user-friendly command-line interface with real-time tracking of registrations, check-ins, and check-outs.

## Features

### Core Functionality

- **Event Management**
  - Create and manage multiple events
  - Set maximum capacity limits
  - View detailed event statistics
  - Search events by name or location

- **Attendant Management**
  - Create attendant profiles with contact information
  - Track attendants across multiple events
  - Search attendants by name or email
  - View attendant participation history

- **Registration System**
  - Register attendants to events
  - Automatic capacity management
  - Prevent duplicate registrations
  - Unregister attendants when needed

- **Check-in/Check-out Tracking**
  - Real-time check-in status
  - Track check-outs
  - View attendant status (registered, checked in, checked out)
  - Generate attendance statistics

### Interactive Menu

The application provides 12 interactive options:

1. View all events
2. View event details
3. View all attendants
4. View attendant details
5. Create new event
6. Create new attendant
7. Register attendant to event
8. Check in attendant
9. Check out attendant
10. Search events
11. Search attendants
12. Exit

## Installation

1. Ensure you have Python 3.8+ installed
2. Clone the repository:
   ```bash
   git clone https://github.com/nolecram/HelpMeCopilot.git
   cd HelpMeCopilot
   ```
3. Install dependencies (for testing):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

```bash
python src/event_attendants_tracker.py
```

### Sample Data

The application comes pre-loaded with sample data for demonstration:

- **Events:**
  - Python Conference 2025 (March 15, San Francisco, 100 capacity)
  - Tech Meetup (April 20, New York, 50 capacity)
  - DevOps Workshop (May 10, Austin, unlimited capacity)

- **Attendants:**
  - Alice Johnson (alice@email.com)
  - Bob Smith (bob@email.com)
  - Carol Williams (carol@email.com)
  - David Brown (david@email.com)

### Example Workflow

1. **View all events** to see what's available
2. **Create a new attendant** with their information
3. **Register the attendant** to an event
4. **Check in the attendant** when they arrive
5. **View event details** to see real-time statistics
6. **Check out the attendant** when they leave

## Code Structure

### Classes

#### `Attendant`
Represents an event attendant with their personal information.

**Attributes:**
- `attendant_id`: Unique identifier
- `name`: Full name
- `email`: Email address
- `phone`: Phone number (optional)
- `events_registered`: Set of event IDs the attendant is registered for

#### `Event`
Represents an event with attendant tracking capabilities.

**Attributes:**
- `event_id`: Unique identifier
- `name`: Event name
- `date`: Event date (YYYY-MM-DD format)
- `location`: Event location
- `max_capacity`: Maximum attendants (optional)
- `registered_attendants`: Dictionary of registered attendants
- `checked_in_attendants`: Set of checked-in attendant IDs
- `checked_out_attendants`: Set of checked-out attendant IDs

**Key Methods:**
- `register_attendant()`: Register an attendant
- `check_in_attendant()`: Check in an attendant
- `check_out_attendant()`: Check out an attendant
- `get_attendant_status()`: Get attendant status
- `get_statistics()`: Get event statistics

#### `EventTracker`
Main class for tracking attendants across multiple events.

**Key Methods:**
- `create_event()`: Create a new event
- `create_attendant()`: Create a new attendant
- `register_attendant_to_event()`: Register attendant to event
- `get_attendant_events()`: Get all events for an attendant
- `get_event_attendants()`: Get all attendants for an event
- `search_attendants()`: Search attendants
- `search_events()`: Search events

## Testing

The application includes comprehensive test coverage with 44 test cases.

### Running Tests

```bash
# Run all tests
pytest tests/test_event_attendants_tracker.py -v

# Run specific test class
pytest tests/test_event_attendants_tracker.py::TestEvent -v

# Run specific test
pytest tests/test_event_attendants_tracker.py::TestEvent::test_check_in_attendant -v
```

### Test Coverage

- **TestAttendant**: Tests for Attendant class (3 tests)
- **TestEvent**: Tests for Event class (17 tests)
- **TestEventTracker**: Tests for EventTracker class (22 tests)
- **TestIntegration**: Integration tests for complete workflows (2 tests)

All tests pass ✅

## API Reference

### Event Statistics

The `get_statistics()` method returns:
```python
{
    'total_registered': int,      # Total registered attendants
    'checked_in': int,            # Currently checked in
    'checked_out': int,           # Already checked out
    'not_checked_in': int,        # Registered but not checked in
    'capacity_remaining': int|None # Spots remaining (if capacity set)
}
```

### Attendant Status

Possible status values:
- `'registered'`: Attendant is registered but not checked in
- `'checked_in'`: Attendant is currently checked in
- `'checked_out'`: Attendant has checked out
- `None`: Attendant is not registered

## Display Features

The application uses emoji indicators for better visual feedback:

- 📅 Events
- 👥 Attendants
- 📊 Statistics
- 📝 Registered
- ✅ Checked In
- 👋 Checked Out
- 🔍 Search Results
- ✅ Success
- ❌ Error

## Examples

### Creating a New Event

```
Enter your choice (1-12): 5

--- Create New Event ---
Event ID: evt004
Event Name: AI Summit 2025
Date (YYYY-MM-DD): 2025-06-15
Location: Seattle
Max Capacity (press Enter for unlimited): 200

✅ Event 'AI Summit 2025' created successfully!
```

### Viewing Event Details

```
Enter event ID: evt001

======================================================================
📅 EVENT: Python Conference 2025
======================================================================
Event ID: evt001
Date: 2025-03-15
Location: San Francisco
Capacity: 3/100

📊 STATISTICS:
  Total Registered: 3
  Checked In: 1
  Checked Out: 1
  Not Yet Checked In: 1
  Capacity Remaining: 97

👥 ATTENDANTS:
----------------------------------------------------------------------
  👋 Alice Johnson (alice@email.com) - CHECKED_OUT
  ✅ Bob Smith (bob@email.com) - CHECKED_IN
  📝 Carol Williams (carol@email.com) - REGISTERED
======================================================================
```

### Searching for Events

```
Enter search query (name or location): Python

🔍 Found 1 event(s):
------------------------------------------------------------
  evt001: Python Conference 2025 - 2025-03-15 (San Francisco)
```

## Contributing

This application is part of the HelpMeCopilot repository. See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

This project is part of the HelpMeCopilot repository and is available under the MIT License.

## Author

Created as a coding example for the HelpMeCopilot repository.

---

**Last Updated:** November 13, 2025  
**Version:** 1.0.0
