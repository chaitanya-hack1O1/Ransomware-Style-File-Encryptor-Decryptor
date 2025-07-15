import os
import time
from cryptography.fernet import Fernet

# Function to simulate hacking animation
def hacking_animation(action):
    print(f"Initiating {action} sequence...")
    time.sleep(1)
    for _ in range(1):
        print("Connecting to target system", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print(f"\nBypassing security protocols for {action}...")
        time.sleep(1)
        print(f"Accessing files for {action}...")
        time.sleep(1)
        print(f"{action.capitalize()} files...")
        time.sleep(1)
        print(f"{action.capitalize()} complete.")
        time.sleep(1)

# Function to display a banner
def display_banner(action):
    print("\n" + "="*40)
    print(f"Files have been {action} by Mainekdeveloper")
    print("="*40)
    time.sleep(1)

# Function to decrypt files
def decrypt_files(target_dir):
    # Load saved key
    with open("keyfile.key", "rb") as key_in:
        key = key_in.read()

    fernet = Fernet(key)

    # Decrypt files
    for file in os.listdir(target_dir):
        if file.endswith((".txt", ".exe", ".bat")):
            path = os.path.join(target_dir, file)
            with open(path, "rb") as f:
                data = f.read()
            
            decrypted_data = fernet.decrypt(data)
            
            with open(path, "wb") as f:
                f.write(decrypted_data)

# Main execution
target_dir = "/to/path/file"  # Change this to your target directory

# Decrypt files with animation
hacking_animation("decryption")
decrypt_files(target_dir)
display_banner("decrypted")
