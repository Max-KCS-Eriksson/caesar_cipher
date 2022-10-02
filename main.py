import argparse
from datetime import datetime

import caesar_cipher

# Shift factor settings.
#   Working range from -26 to 26.
SHIFT_FACTOR = 25

parser = argparse.ArgumentParser()
# Encrypt a string given as an argument and write to a file.
parser.add_argument("-e", "--encrypt", help="Encrypt given string and write to a file.")
# Decrypt a string given as an argument and write to a file.
parser.add_argument("-d", "--decrypt", help="Decrypt given string and write to a file.")
args = parser.parse_args()

# Create a string to be used as filename to write encrypted or decrypted message to.
if args.encrypt or args.decrypt:
    entry_id = str(datetime.now())
    # Remove special characters.
    entry_id = (
        entry_id.replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
    )

if args.encrypt:
    print("*DEBUG* Input:", args.encrypt)
    encrypted_text = caesar_cipher.encrypt(args.encrypt, SHIFT_FACTOR)

    print("Output:", encrypted_text)
    # Implement this later.
    # with open(f"{entry_id}.txt", "w") as f:
    #     f.write(encrypted_message)

if args.decrypt:
    print("*DEBUG* Output:", args.decrypt)
    decrypted_text = caesar_cipher.decrypt(args.decrypt, SHIFT_FACTOR)

    print("Output:", decrypted_text)
    # Implement this later.
    # with open(f"{entry_id}.txt", "w") as f:
    #     f.write(decrypted_message)
