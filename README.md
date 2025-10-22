# Cyber Security Base Project 1

This repository is made for Cyber Security Base MOOC course. I try to recreate 5 flaws from the OWASP Top 10 list.

List of example vulnerabilities in this project:
- A03:2021 Injection
- A02:2021 Cryptographic Failures
- CSRF
- A07:2021 Identification and Authentication Failures
- A09:2021 Security Loggin and Monitoring Failures

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

### Clone the repository
```bash
git clone https://github.com/tukkimiesjonni/cybersecurityproject1.git

cd cybersecurityproject1
```

### Create and activate a virtual environment

For macOS / linux:

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have the requirements.txt file, you can create one with:

```bash
pip freeze > requirements.txt
```

### Initialize the database

```bash
python init_db.py
```

## Usage

### Run the application

```bash
flask run
```
