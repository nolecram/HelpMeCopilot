# Setup & Installation Guide

## Prerequisites

Before setting up HelpMeCopilot, ensure you have the following installed:

### Required
- **Git** 2.30+
- **Python** 3.8+
- **pip** (Python package manager)

### Optional (for specific features)
- **Node.js** 14+ (for JavaScript/TypeScript examples)
- **Terraform** 1.0+ (for infrastructure examples)
- **Docker** (for containerized examples)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/nolecram/HelpMeCopilot.git
cd HelpMeCopilot
```

### 2. Set Up Python Environment (Recommended)

Create a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### 4. Verify Installation

Run a quick test to ensure everything is set up correctly:

```bash
# Run Python tests
pytest tests/ -v

# Or run individual test
python tests/test_chocolate_cake_recipes.py
```

## Optional Setup

### Node.js Setup (for JavaScript examples)

If you want to run JavaScript examples:

```bash
# Install Node.js dependencies (if applicable)
npm install

# Run JavaScript tests
node tests/Test.js
```

### Terraform Setup (for Infrastructure examples)

If you want to use Terraform configurations:

```bash
# Navigate to infrastructure directory
cd src/infrastructure/lamp_stack

# Initialize Terraform
terraform init

# Validate configuration
terraform validate

# Plan deployment
terraform plan

# Apply configuration (be careful!)
terraform apply
```

## Directory Overview

After installation, you'll have this structure:

```
HelpMeCopilot/
├── src/                    # Source code and examples
├── tests/                  # Test files
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
└── venv/                   # Virtual environment (if created)
```

## Running Examples

### Python Examples

```bash
# Chocolate cake recipes
python src/applications/chocolate_cake_recipes.py

# Temperature converter
python src/applications/temperature_converter.py
```

### Web Application (Excuse Generator)

```bash
cd src/applications/excuse_generator
python app.py
# Open http://localhost:5000 in your browser
```

### Hello World Examples

```bash
# Navigate to examples
cd src/examples/hello-world

# Run examples in different languages
python "Hello World.py"
node "Hello World.js"
ruby "Hello World.rb"
go run "Hello World.go"
# ... and many more
```

## Troubleshooting

### Python Version Issues
```bash
# Check Python version
python --version

# If Python 3 is not default
python3 --version
python3 -m venv venv
```

### Virtual Environment Not Activating
```bash
# Ensure you're in the project root directory
pwd

# Try explicit path
source ./venv/bin/activate
```

### Missing Dependencies
```bash
# Reinstall all requirements
pip install --upgrade -r requirements.txt
```

### Terraform Issues
```bash
# Check Terraform version
terraform version

# Reinitialize Terraform
cd src/infrastructure/lamp_stack
rm -rf .terraform
terraform init
```

## Next Steps

1. **Explore Examples** - Check out `src/examples/hello-world/` for language-specific implementations
2. **Read Documentation** - See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed directory information
3. **Run Tests** - Execute `pytest tests/ -v` to see all tests pass
4. **Try Copilot** - Use GitHub Copilot to generate variations of the examples
5. **Contribute** - Follow [CONTRIBUTING.md](../CONTRIBUTING.md) to add your own examples

## Getting Help

- Check existing issues: https://github.com/nolecram/HelpMeCopilot/issues
- Read documentation in `docs/` directory
- Review examples in `src/`
- See CONTRIBUTING.md for contribution guidelines

---

**Last Updated:** October 29, 2025
