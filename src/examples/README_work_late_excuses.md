# Work Late Excuse Generator

A Python program that generates random excuses for being late to work. This tool provides various categories of believable excuses for different workplace situations.

## Features

- **7 Excuse Categories**: Traffic, Transport, Personal, Technical, Weather, Family, and Health
- **56+ Unique Excuses**: Each category contains 8 different excuses
- **Command-line Interface**: Easy to use from terminal or command prompt
- **Error Handling**: Graceful handling of invalid inputs
- **Help System**: Built-in help documentation

## Usage

### Basic Usage (Random Excuse)
```bash
python work_late_excuses.py
```

### Specific Category
```bash
python work_late_excuses.py traffic
python work_late_excuses.py weather
python work_late_excuses.py family
```

### Get Help
```bash
python work_late_excuses.py --help
```

## Available Categories

1. **traffic** - Traffic and transportation related excuses
   - Example: "There was a major accident on the highway that caused a 30-minute delay."

2. **transport** - Public transportation excuses
   - Example: "My train was delayed by 25 minutes due to signal problems."

3. **personal** - Personal emergencies and situations
   - Example: "I had to take my pet to the emergency vet - they ate something they shouldn't have."

4. **technical** - Technology-related issues
   - Example: "My phone died overnight and my alarm didn't go off."

5. **weather** - Weather-related excuses
   - Example: "The roads were extremely icy and I had to drive very slowly for safety."

6. **family** - Family emergency excuses
   - Example: "My child woke up sick and I had to arrange last-minute childcare."

7. **health** - Health-related excuses
   - Example: "I had a severe migraine this morning and needed time for medication to take effect."

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Download the `work_late_excuses.py` file
2. Make it executable (optional): `chmod +x work_late_excuses.py`
3. Run directly: `python work_late_excuses.py` or `./work_late_excuses.py`

## Example Output

```
💼 Work Late Excuse Generator 💼
========================================
Category: Traffic
Excuse: Construction work blocked my usual route and GPS rerouted me through heavy traffic.
========================================
💡 Pro tip: Use responsibly and sparingly!
```

## Testing

Run the test suite to verify functionality:

```bash
python -m pytest tests/test_work_late_excuses.py -v
```

## Disclaimer

This tool is intended for educational and entertainment purposes. Use the generated excuses responsibly and sparingly. The authors are not responsible for any workplace consequences resulting from the use of these excuses.

## Contributing

Feel free to add more excuses or categories by modifying the `WORK_LATE_EXCUSES` dictionary in the script. Ensure new excuses are:
- Realistic and believable
- Professional and appropriate for workplace use
- At least 5 words long
- Properly capitalized and punctuated