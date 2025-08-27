import time
import pyotp

# This script generates a Time Based One-Time Password using a given key, to authenticate users, for
# better security in applications.


# generate the key to be send to the user via email
def generate_totp(key):
    totp = pyotp.TOTP(key, interval=600)  # 10-minute interval
    print( totp.now())
    return totp.now()

