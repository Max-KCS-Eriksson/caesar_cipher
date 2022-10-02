import argparse
from datetime import datetime

import caesar_cipher

# Shift factor settings.
# NOTE: Don't use shift factor 26 as it will output the same as shift factor 0.
#   No real need to use shift factor above 25 as the same all possible outputs
#   are covered within the range of 1 to 25 or -1 to -25.
SHIFT_FACTOR = 25

parser = argparse.ArgumentParser()
# Arg to encrypt a string given as an argument and print to CLI.
parser.add_argument(
    "-e", "--encrypt", help="Encrypt string given as argument and print to CLI."
)
# Arg to decrypt a string given as an argument and print to CLI.
parser.add_argument(
    "-d", "--decrypt", help="Decrypt string given as argument and print to CLI."
)
# Arg to write output from encryption/decryption to .txt file.
parser.add_argument(
    "-w",
    "--write",
    nargs="?",
    const=True,
    help="Write output from encryption/decryption to .txt file.",
)
args = parser.parse_args()

# Create a string to be used as filename to write encrypted or decrypted message to.
if args.encrypt or args.decrypt:
    entry_id = str(datetime.now())
    # Remove special characters.
    entry_id = (
        entry_id.replace("-", "").replace(":", "").replace(".", "").replace(" ", "")
    )

if args.encrypt:
    output = caesar_cipher.encrypt(args.encrypt, SHIFT_FACTOR)

    if args.write:
        with open(f"{entry_id}.txt", "w") as f:
            f.write(output)

if args.decrypt:
    output = caesar_cipher.decrypt(args.decrypt, SHIFT_FACTOR)

    if args.write:
        with open(f"{entry_id}.txt", "w") as f:
            f.write(output)

print("Output:", output)
