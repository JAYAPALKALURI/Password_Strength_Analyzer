#  Password Strength Analyzer & Custom Wordlist Generator

This project is a Python-based tool that helps users:
- Analyze the strength of a given password using the `zxcvbn` library.
- Generate custom wordlists based on user-specific inputs like names, birthdates, and pet names using leetspeak and variations.

---

##  Features

- Estimate password strength and crack time.
- Get security suggestions for weak passwords.
- Generate personalized password wordlists with years and leetspeak.
- Simple command-line interface.
- Easy-to-use graphical user interface (GUI) with Tkinter.

---

##  Tools & Libraries

- Python 3.x
- [`zxcvbn`](https://github.com/dropbox/zxcvbn) – Password strength estimator
- `nltk`, `unidecode` – For future enhancements (included in `requirements.txt`)
- `tkinter` – For GUI (built-in with Python)

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### 2.Create and activate a virtual environment(OPTIONAL)
NOTE: It is optional because you can run the program even without virtual environment
by skiping this step and follow the next Steps

CREATE
```bash
python -m venv .venv
```
Activate for Linux
```bash
source .venv/bin/activate    
```
Activate for Windows

```bash
 .venv\Scripts\activate
```


### 3.Install dependencies

```bash
pip install -r requirements.txt
```
### 4.Command-Line Interface (CLI)

```bash
python cli.py --password MySecret123! --inputs name birthdate petname --export
```
### 5.Graphical Interface (GUI)

```bash
python gui.py
```
