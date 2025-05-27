# Secure Password Generator

![App Screenshot](/appguipy.png) 

A cryptographically secure password generator with GUI, built with Python and tkinter.

## Features
- Generates truly random passwords using `secrets` module
- Customizable length (8-32 characters)
- Selectable character sets
- Copy to clipboard functionality
- Cross-platform (Windows/macOS/Linux)

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
4. Next step:  
 **Reproducible Builds**: SHA-256 checksums provided for releases.

 *Obs.: Created with the help of AI - DeepSeek
        May contain errors, don't use for production. Use it for tutorias, ok?
