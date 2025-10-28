# Contributing to HelpMeCopilot

Thank you for your interest in contributing to HelpMeCopilot! We welcome contributions of all types.

## Getting Started

### Prerequisites
- Git 2.30+
- Python 3.8+
- GitHub account

### Fork and Clone

1. **Fork the Repository** at https://github.com/nolecram/HelpMeCopilot
2. **Clone your fork:**
```bash
git clone https://github.com/YOUR-USERNAME/HelpMeCopilot.git
cd HelpMeCopilot
```
3. **Add upstream remote:**
```bash
git remote add upstream https://github.com/nolecram/HelpMeCopilot.git
```

## Contribution Workflow

### 1. Create a Feature Branch

```bash
git fetch upstream
git checkout main
git merge upstream/main
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Follow PEP 8 for Python code
- Use descriptive names for variables and functions
- Include docstrings and comments
- Update relevant documentation
- Add or update tests

### 3. Test Your Changes

```bash
pip install -r requirements.txt
pytest tests/ -v
```

### 4. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add new Hello World example in Rust"
```

**Commit Message Format:**
- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
# Then create a Pull Request on GitHub
```

## Contribution Categories

### Adding a New Example
1. Add to `src/examples/hello-world/`
2. Create file: `Hello World.<extension>`
3. Include comments explaining the code
4. Test the file runs without errors
5. Update `CHANGELOG.md`

### Adding a New Application
1. Create directory under `src/applications/`
2. Add source files and subdirectories
3. Create test file in `tests/`
4. Add README.md with instructions
5. Update `CHANGELOG.md`

### Adding Infrastructure Code
1. Create subdirectory under `src/infrastructure/`
2. Add Terraform or cloud configs
3. Include comprehensive README.md
4. Add scripts to `scripts/` subdirectory
5. Update `CHANGELOG.md`

## Code of Conduct

- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on constructive feedback
- Be patient with newcomers

## Getting Help

- Check existing issues: https://github.com/nolecram/HelpMeCopilot/issues
- Read documentation in `docs/`
- Review examples in `src/`

---

**Thank you for contributing to HelpMeCopilot!**

Last Updated: October 29, 2025
