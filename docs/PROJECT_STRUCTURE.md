# Project Structure Reference

## Root Directory

```
HelpMeCopilot/
├── README.md                      # Main project documentation
├── CHANGELOG.md                   # Version history and updates
├── CONTRIBUTING.md                # Contribution guidelines
├── requirements.txt               # Python package dependencies
├── .gitignore                     # Git ignore rules
├── .github/                       # GitHub configuration
├── docs/                          # Documentation directory
├── src/                           # Source code and examples
├── tests/                         # Test suite
└── assets/                        # Static assets and images
```

## Source Code Structure (`/src`)

### Applications (`src/applications/`)
- **chocolate_cake_recipes.py** - Recipe management and display
- **temperature_converter.py** - Unit conversion utilities
- **excuse_generator/** - Flask web application

### Examples (`src/examples/`)
- **hello-world/** - Hello World in 25+ programming languages
- Language-specific implementations

### Infrastructure (`src/infrastructure/`)
- **lamp_stack/** - Terraform LAMP stack configuration
- **azure_aws/** - Azure and AWS examples

### Machine Learning (`src/ml_experiments/`)
- Jupyter notebooks for ML experiments
- Sample ML functions

### Legacy (`src/legacy/`)
- Assembly, COBOL, C examples
- Sybase database examples
- Ruby examples
- Chat and experimental scripts

## Test Structure (`/tests`)
- test_chocolate_cake_recipes.py
- test_TestA.py
- TestB.py
- TestC.py
- Test.js (JavaScript tests)

## Configuration Files

### .gitignore
Comprehensive git ignore rules for:
- Python cache files
- Jupyter notebooks
- Node.js modules
- Terraform state files
- macOS files
- Environment variables
- IDE files

### requirements.txt
- pytest>=7.0.0

### CHANGELOG.md
Version history in Keep a Changelog format

### CONTRIBUTING.md
Contribution guidelines and workflow

---

**Last Updated:** October 29, 2025
