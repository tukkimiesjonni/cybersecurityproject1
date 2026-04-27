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

## Vulnerabilities

### CSRF

Can't really screenshot this

### A02:2021 Cryptographic Failures

Can't really screenshot this

### A03:2021 Injection

User can completely bypass authentication without knowing any real credentials.

![Injection](static/Screenshot%20from%202026-04-27%2016-17-15.png)

![Result](static/Screenshot%20from%202026-04-27%2016-17-35.png)

### A09:2021 Security Loggin and Monitoring Failures

This is just a PoC, but without any logging e.g. sign-ins leave no trace. There is not really any way to know who signs in and from where.

![NoLogging1](static/Screenshot%20from%202026-04-27%2016-34-37.png)

![NoLogging2](static/Screenshot%20from%202026-04-27%2016-34-50.png)

With logging, the results are something like this.

![Logging1](static/Screenshot%20from%202026-04-27%2016-28-18.png)

![Logging2](static/Screenshot%20from%202026-04-27%2016-28-35.png)

### A07:2021 Identification and Authentication Failures

Not having a rate-limiter enables attackers to do bruteforce attacks.

Here are screenshots from a small scale bruteforce attack to the /login endpoint without rate-limiter enabled.

![NoLimiter1](static/Screenshot%20from%202026-04-27%2016-39-22.png)

![NoLimiter2](static/Screenshot%20from%202026-04-27%2016-39-51.png)

Here are some screenshots of the rate-limiter being enabled.

![Limiter1](static/Screenshot%20from%202026-04-27%2016-40-51.png)

![Limiter2](static/Screenshot%20from%202026-04-27%2016-41-02.png)

As we can see, the requests do not go through.