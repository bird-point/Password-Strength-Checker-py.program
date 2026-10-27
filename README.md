# Password-Strength-Checker-py.program
# Password Strength Checker

A simple, interactive Python command-line application that evaluates password strength based on length, character variety, and basic complexity rules. It also provides suggestions to help users create stronger passwords.

## Features

- **Password Length Validation** — Checks whether the password contains at least 8 characters.
- **Character Variety Checks** — Looks for lowercase letters, uppercase letters, digits, and special characters.
- **Length Bonus** — Awards an additional point for passwords containing 12 or more characters.
- **Strength Classification** — Categorizes passwords as `Weak`, `Medium`, or `Strong`.
- **Improvement Suggestions** — Identifies missing requirements and provides feedback.
- **Interactive CLI** — Allows users to check multiple passwords in one session.

## Technologies Used

- **Python 3**
- **Regular Expressions (`re` module)**

## How It Works

The program evaluates a password using five basic criteria:

| Criterion | Score |
|---|---:|
| At least 8 characters long | +1 |
| Contains a lowercase letter | +1 |
| Contains an uppercase letter | +1 |
| Contains a digit | +1 |
| Contains a supported special character | +1 |
| At least 12 characters long | +1 bonus |

The total score determines the password's classification:

| Score | Strength |
|---|---|
| 0–2 | Weak |
| 3–4 | Medium |
| 5–6 | Strong |

If a password fails any of the five basic criteria, the program generates suggestions explaining what is missing.

**Note:** The score is a rule-based indicator, not a formal measure of password entropy or resistance to real-world attacks.

## Getting Started

### Prerequisites

Install Python 3 on your system.

Check your installation by running:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/bird-point/Password-Strength-Checker-py.program.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Password-Strength-Checker-py.program
   ```

3. Run the Python script:

   ```bash
   python password_strength_checker.py
   ```

   Replace `password_strength_checker.py` with the actual name of your Python file if it differs.

No third-party packages are required because the project uses Python's built-in `re` module.

## Usage

Run the script in your terminal and enter a password when prompted.

Example:

```text
Enter a password to check: hello
Password Strength: Weak
Do you want to continue checking(y/n) :y
Suggestions:
- Password should be at least 8 characters long.
- Include at least one uppercase letter.
- Include at least one digit.
- Include at least one special character (e.g., !@#$%^&*).
```

The program then asks whether you want to check another password. Enter `n` to exit.

## Project Structure

```text
Password-Strength-Checker-py.program/
├── password_strength_checker.py
└── README.md
```

The Python filename shown above is a suggested name. Adjust the structure to match the files in your repository.

## Limitations

- Uses predefined rules rather than an advanced password-strength estimation algorithm.
- Does not check passwords against known compromised-password databases.
- Does not evaluate dictionary words, common password patterns, or predictable sequences.
- A password classified as `Strong` is not necessarily secure against every type of attack.
- Special-character detection is limited to the characters explicitly listed in the code.
- The application does not store passwords, but passwords are entered as ordinary terminal input and may be visible while typing.

**Security recommendation:** Do not test real passwords that you currently use for important accounts. Use sample passwords instead.

## Future Improvements

- Add a graphical user interface (GUI).
- Integrate a password-strength estimator such as Dropbox's zxcvbn.
- Detect common passwords and predictable patterns.
- Add unit tests for password validation and strength classification.
- Improve input handling and feedback presentation.
- Support a broader range of special characters.

## Contributing

Contributions, suggestions, and bug reports are welcome. Fork the repository, create a branch for your changes, and submit a pull request.

## License

No license has been specified yet. If you intend to make this project open source, consider adding a suitable license, such as the MIT License, in a `LICENSE` file.

---

**Author:** [bird-point](https://github.com/bird-point)

**Repository:** [Password-Strength-Checker-py.program](https://github.com/bird-point/Password-Strength-Checker-py.program)

