# 🛡️ Password entropy analyzer

A tool to evaluate password strength (mathematical entropy) and verify if the password has been previously compromised in known public data breaches using the Have I Been Pwned API.

## 🚀 Key features

*   **Mathematical entropy**: Calculates bits of entropy based on character sets (lowercase, uppercase, digits, symbols) and length.
*   **Data breach verification**: Connects to the API to check for known leaks.
*   **Privacy**: Uses hashlib to locally generate a SHA-1 hash of the password. Only the first 5 characters of the hash are sent to the API. The remaining check is performed locally, ensuring your password is never sent over the network.

## ⚙️ Installation and usage

1. Clone the repository
   ```bash

   ```

2. Run the script
   ```bash
   python main.py
   ```

## ⚠️ Note

No software can guarantee absolute security. This script provides an estimate of resistance against brute-force and dictionary attacks. It does not account for targeted OSINT attacks, social engineering, or personal patterns. Always use unique passwords managed by a trusted password manager.

