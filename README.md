# Ransomware-Style File Encryptor/Decryptor

This project demonstrates how to encrypt and decrypt files in a folder, simulating the behavior of ransomware. It is intended for educational purposes only.

## Features
- Encrypts and decrypts files in a specified directory.
- Uses strong symmetric encryption (Fernet/AES) from the `cryptography` library.
- Simulates a ransomware attack with terminal animations and banners.
- Supports `.txt`, `.exe`, and `.bat` files by default.

## How It Works
- **Encryption**: (Not shown in this repo, but typically, a script would generate a key, encrypt files, and save the key.)
- **Decryption**: The provided `decryptor.py` script loads a saved key from `keyfile.key` and decrypts all supported files in the target directory.
- **Animations**: The script includes terminal-based animations to mimic a hacking/ransomware process.

## Usage
1. **Install dependencies:**
   ```bash
   pip install cryptography
   ```
2. **Prepare your environment:**
   - Place the `keyfile.key` (the Fernet key) in the same directory as the script.
   - Set the `target_dir` variable in `decryptor.py` to the folder you want to decrypt.
3. **Run the decryption script:**
   ```bash
   python decryptor.py
   ```
   The script will display animations and decrypt all `.txt`, `.exe`, and `.bat` files in the target directory.

## Example
```
Initiating decryption sequence...
Connecting to target system...
Bypassing security protocols for decryption...
Accessing files for decryption...
Decryption files...
Decryption complete.
========================================
Files have been decrypted by Mainekdeveloper
========================================
```

## ⚠️ Disclaimer
- **This project is for educational and ethical testing purposes only.**
- Do NOT use this code to attack, encrypt, or decrypt files without explicit permission.
- The author is not responsible for any misuse or damage caused by this code.
