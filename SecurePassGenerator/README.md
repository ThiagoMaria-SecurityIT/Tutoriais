# 🔐 Secure Password Generator

![App Screenshot](https://github.com/ThiagoMaria-SecurityIT/Tutoriais/edit/main/SecurePassGenerator/images/securpassimage1)  

A cryptographically secure password generator with GUI, built with Python and tkinter.

## 🌟 Features
- Generates truly random passwords using `secrets` module
- Customizable length (8-32 characters)
- Selectable character sets
- Copy to clipboard functionality
- Cross-platform (Windows/macOS/Linux)
- 🔄 **One-click generation** with customizable length (8-32 chars)  
- 📋 **Auto-copy** (clipboard clears after 30 seconds)  
- 🎲 **True randomness** (powered by your OS’s crypto magic)  
- 🎨 **Clean GUI** (no confusing menus) 

## Security Notes
- Passwords are generated locally and never stored/transmitted
- Uses OS-level cryptographic randomness (`/dev/urandom` or Windows equivalent)
- Guarantees at least one character from each selected set

## 🔒 Security Guarantees

1. **No Telemetry**: The app never connects to the internet.
2. **Memory Protection**: 
   - Passwords are wiped from memory after generation
   - Uses Python's `secrets` module (cryptographically secure)
3. **Clipboard Safety**: 
   - Pyperclip automatically clears clipboard after 30s  
---
## 🌟 Features  
- 🔄 **One-click generation** with customizable length (8-32 chars)  
- 📋 **Auto-copy** (clipboard clears after 30 seconds)  
- 🎲 **True randomness** (powered by your OS’s crypto magic)  
- 🎨 **Clean GUI** (no confusing menus)  

---

## ⚡ Quick Start  
1. **Download**: Click "Code" → "Download ZIP"  
2. **Run**: Double-click `PassGenPython.py` (needs [Python](https://www.python.org/downloads/))  

*"But wait, I don’t know Python!"* → No problem! Just install Python. copy and paste the code and run it like any app.  

---

## 🛠️ Customization  
Edit `PassGenPython.py` to:  
```python
# Change default settings
DEFAULT_LENGTH = 16  # 12 → 16 chars
SPECIAL_CHARS = "!@#$%&*"  # Add/remove symbols
```

---

## 🤔 Why Trust This?  
| Security Feature      | Guarantee                               |  
|-----------------------|-----------------------------------------|  
| **Randomness**        | Uses your OS’s built-in crypto (no DIY math!) |  
| **No Internet**       | Runs 100% offline—no sneaky calls home  |  
| **Clipboard Safety**  | Auto-wipes after 30 seconds (has a countdown)            |  

---
## 🤝 Credits & Disclaimer  

**Development Assistance**:  
This project was created with AI-powered suggestions from [DeepSeek Chat](https://deepseek.com) (like a very smart rubber duck 🦆💡).  

**Important Notes**:  
🔐 **Passwords**: Generated passwords are cryptographically secure and safe to use.  
⚠️ **Code**: Review before production use - as with any open-source project, test thoroughly in your environment.  

---
## 🎩 Hat Tip

Cheers to DeepSeek's AI for not judging my 3AM coding questions.  
While the passwords are **pro-level secure**, treat the code like a beginner skateboarder – **wear a helmet!** 🛹⚠️  

## 📜 License  
MIT © Thiago Maria – *Use it, share it.*  


## ☕ Support the Project
Love this tool? Help me keep it updated!  

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red?logo=GitHub&style=for-the-badge)](https://github.com/sponsors/ThiagoMaria-SecurityIT)
