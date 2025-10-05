# Python DevOps Tools

This repository contains a collection of Python scripts for various DevOps tasks.

## Password Strength Checker

A Python script that checks password strength based on the following criteria:
- Minimum length of 8 characters
- Contains both uppercase and lowercase letters
- Contains at least one digit (0-9)
- Contains at least one special character (!, @, #, $, %, etc.)

### Usage

```bash
python password_strength_checker.py
```

Follow the prompts to enter passwords and check their strength. The script will provide detailed feedback on any failed requirements.

## Development

### Requirements
- Python 3.x

### Setup
1. Clone the repository
```bash
git clone [repository-url]
cd [repository-name]
```

2. (Optional) Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate     # On Windows
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request