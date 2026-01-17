# Sentinel CLI 🔐

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[Repository](https://github.com/ismailset/Sentinel)

Sentinel is a lightweight, terminal-first security toolkit for Termux, Linux, and macOS. It helps developers and system administrators quickly inspect web properties, monitor uptime and latency, test local applications for insecure configurations, analyze logs, and evaluate password strength — all from the command line.

Table of contents
- Features
- Quickstart (Termux / Linux / macOS)
- Usage examples
- Output samples
- Configuration
- Development
- Publishing the website (GitHub Pages)
- Contributing
- License
- Contact

Features
- 🔍 Website Security Checker — scan TLS, headers, and Content Security Policy (CSP)
- 🚨 Uptime & Latency Monitor — detect downtime and high latency with clear metrics
- 🧪 Local Vulnerable App Tester — scan local apps for missing protections and insecure settings
- 📊 Log Analyzer — parse and summarize local log files
- 🔐 Password Strength Checker — entropy and actionable suggestions
- Small, dependency-light, and optimized for terminal workflows

Quickstart (Termux / Linux / macOS)
1. Update system packages (Termux example)
```bash
pkg update && pkg upgrade -y
pkg install python git curl -y
```

2. Clone the repository and prepare an environment
```bash
git clone https://github.com/ismailset/Sentinel.git
cd Sentinel
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run a command (examples below).

Usage examples
- Website security scan
```bash
python sentinel/cli.py security https://example.com
```

- Uptime & latency check
```bash
python sentinel/cli.py uptime https://example.com
```

- Password strength check
```bash
python sentinel/cli.py password "MySecureP@ss123"
```

- Log analysis (local file)
```bash
python sentinel/logs.py /path/to/your/logfile.log
```

- Local app scan
```bash
python sentinel/localtest.py /path/to/your/app
```

Output samples
Security Report for https://example.com
```
HTTPS: ✅
Content-Security-Policy: ❌
X-Frame-Options: ✅
Strict-Transport-Security: ❌
X-Content-Type-Options: ✅
Referrer-Policy: ❌
```

Uptime / latency
```
Status: 200
Latency: 132 ms
Warning: Site is slower than usual
```

Password strength
```
Password strength: Very Strong
```

Configuration
- The tool is intentionally simple and CLI-driven. If you add configuration files or environment variables, place documentation and examples under sentinel/config or docs/config.example.yaml (follow the repository conventions).
- If you want monitoring/alerting integration (email, webhook), consider adding a small config file to store endpoints and API keys and keep secrets out of the repository.

Development
- Create a virtual environment and install dev dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Run linters / tests (if present)
```bash
# Example (adjust to repo tooling)
pytest
flake8
```

- Code style
  - Follow idiomatic Python (PEP 8)
  - Keep functions small and testable
  - Prefer standard library solutions when lightweight is a priority

Publishing the website (GitHub Pages)
A lightweight, animated landing page is provided (recommended). You can publish a static site directly from this repository using GitHub Pages.

Quick options:
- Option A — docs/ folder (recommended)
  1. Place static site files in a docs/ directory (e.g., docs/index.html, docs/styles.css, docs/script.js).
  2. Commit and push to main.
  3. In the repository Settings → Pages, select branch: main and folder: /docs, then save.

- Option B — gh-pages branch
  1. Build the static site and push the built files to a gh-pages branch.
  2. In Settings → Pages, select the gh-pages branch and root.

See GitHub Pages documentation for details and advanced configuration:
https://docs.github.com/en/pages

Contributing
Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
```bash
git checkout -b feature/myfeature
```
3. Commit your changes
```bash
git commit -m "Add feature: description"
git push origin feature/myfeature
```
4. Open a Pull Request describing the change, motivation, and test plan.

Please follow the repository's code style and add tests for new behavior where appropriate.

License
MIT License © 2026 ismailset  
See LICENSE for details.

Contact
- GitHub: https://github.com/ismailset
- Email: mdismail.121510@gmail.com

