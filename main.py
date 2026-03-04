import math
import string
import hashlib
import urllib.request
import getpass

GREEN = "\033[38;2;76;175;80m"
RED = "\033[91m"
ORANGE = "\033[33m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def calculate_entropy(password):
    lowercase = False
    uppercase = False
    number = False
    symbols = False

    for caracter in password:
        if caracter in string.ascii_lowercase:
            lowercase = True
        if caracter in string.ascii_uppercase:
            uppercase = True
        if caracter in string.digits:
            number = True
        if caracter in string.punctuation:
            symbols = True

    R = 0
    if lowercase:
        R += 26
    if uppercase:
        R += 26
    if number:
        R += 10
    if symbols:
        R += 32

    if R == 0:
        return 0

    entropy = len(password) * math.log2(R)
    return entropy

def strength(entropy):
    if entropy < 28:
        return f"{RED}Very weak (instant pulverization){RESET}"
    elif entropy < 36:
        return f"{ORANGE}Weak (pulverization in hours or days){RESET}"
    elif entropy < 80:
        return f"{YELLOW}Reasonable (pulverization in month/s){RESET}"
    elif entropy < 128:
        return f"{GREEN}Strong (pulverization in year/s){RESET}"
    else:
        return f"{GREEN}Excellent (practically impossible to crack){RESET}"

def checkpassword(password):
    hashed = hashlib.sha1()
    hashed.update(password.encode('utf-8'))
    sha1password = hashed.hexdigest().upper()
    pre = sha1password[0:5]
    suf = sha1password[5:]
    url = "https://api.pwnedpasswords.com/range/"+pre
    
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'ProyectoPythonCiberseguridad')
        response = urllib.request.urlopen(req)
        data = response.read()
        plaintext = data.decode('utf-8')
        lines = plaintext.split('\n')
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(':')
                apisuf = parts[0]
                apicount = parts[1]
                if apisuf == suf:
                    return int(apicount)
        return 0
    except Exception as e:
        print(f"{RED}API ERROR: {e}{RESET}")
        return -1

def show_banner():
    print(f"{GREEN}") 
    banner = r"""
     ___________________________________________________
    |                                                   |
    |            PASSWORD ENTROPY ANALYZER              |
    |___________________________________________________|
    """
    print(banner)
    print(f"{RESET}")

if __name__ == "__main__":
    show_banner()
    print(f"{BOLD}{WHITE}-" * 30)
    print(f"{BOLD}{RED}SECURITY NOTE:{RESET}")
    print(f"{RED}This entropy score is based on pure brute force calculations.{RESET}")
    print(f"{RED}It does not account for targeted OSINT attacks or personal patterns.{RESET}")
    print(f"{RED}Even high-entropy passwords can be cracked if they contain public info.{RESET}")
    print(f"{BOLD}{WHITE}-" * 30)
    
    while True:
        password = getpass.getpass(f"{BOLD}{WHITE}Enter a password to analyze (input hidden): {RESET}")
        if password.strip():
            break
        print(f"{RED}Password cannot be empty or just spaces please try again{RESET}")        
    entropy = calculate_entropy(password)
    print(f"{BOLD}{WHITE}Entropy: {round(entropy, 2)} bits{RESET}")
    print(f"{BOLD}{WHITE}Strength: {strength(entropy)}{RESET}")    
    print(f"\n{ORANGE}Checking database...{RESET}")
    count = checkpassword(password)    
    if count > 0:
        print(f"{BOLD}{RED}This password has been seen {count:,} times in known data breaches!{RESET}")
        print(f"{RED}It is severely vulnerable to dictionary and stuffing attacks regardless of its mathematical entropy.{RESET}")
    elif count == 0:
        print(f"{BOLD}{GREEN}This password was not found in any known public data breaches.{RESET}")
    elif count == -1:
        print(f"{BOLD}{YELLOW}Could not connect to the breaches database.{RESET}")
        print(f"{YELLOW}Make sure you have internet or that the API is still active.{RESET}")