# 🛡️ Phishing Detector

A command-line phishing detection tool written in Python that analyzes URLs and assigns a risk score based on common phishing indicators.

## ✨ Features

* Detects HTTP and HTTPS protocols
* Identifies IP address-based URLs
* Checks URL length
* Detects suspicious keywords
* Detects `@` symbols
* Detects hyphens (`-`) in URLs
* Detects excessive subdomains
* Calculates a phishing risk score
* Verbose mode for detailed analysis
* Colorized terminal output using Colorama

## 📷 Sample Output

```text
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║
██████╔╝███████║██║███████╗███████║
██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║     ██║  ██║██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝

        PHISHING DETECTOR v2.0

URL: http://192.168.1.100/login/verify/account/update/password

Protocol : http
Hostname : 192.168.1.100
Path     : /login/verify/account/update/password

Score : -75

Status : HIGH RISK
```

## 📦 Requirements

* Python 3.10+
* Colorama

Install dependencies:

```bash
pip install colorama
```

## 🚀 Usage

Basic scan:

```bash
python phishingsec.py -u https://google.com
```

Verbose scan:

```bash
python phishingsec.py -u http://192.168.1.100/login/verify/account/update/password -v
```

## 🧠 Detection Logic

The detector currently evaluates URLs using several heuristic checks, including:

* HTTPS vs HTTP
* URL length
* IP address usage
* Suspicious keywords
* Presence of `@`
* Presence of hyphens
* Number of subdomains

Each check contributes to a risk score that is used to classify the URL.

## 📌 Current Status

This project is under active development. New features and improvements will continue to be added as I learn more about Python and cybersecurity.

### Planned Features

* WHOIS lookup
* DNS lookup
* SSL certificate analysis
* URL redirect detection
* Export results to JSON
* Export results to HTML
* Batch URL scanning
* VirusTotal API integration
* Improved risk scoring
* Better terminal interface

## ⚠️ Disclaimer

This project is intended for educational purposes only.

The phishing score is based on simple heuristic checks and should not be considered a replacement for professional security solutions.

## 👨‍💻 Author

Developed by **THEVIGILANTE**

If you find this project useful, feel free to ⭐ the repository and follow its progress.
