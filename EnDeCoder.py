# this was one of the learning projects
# i've found useful for starting Tkinter
# and for understanding concept of message encryption in a very very simple version..
# NB-NOTE: THE ORIGINAL PROJECT
# CAN BE FOUND IN THE FOLLOWING ADDRESS:
# https://www.geeksforgeeks.org/python-message-encode-decode-using-tkinter/


# This Project is redesigned and updated in a more understandable way
# by me! (/https://github.com/AmirHosseinRnj1)
# If you have any problem running or understanding this project,
# feel free to make contact with me...




#######################
####Vigenère cipher####
#######################

# Vigenère cipher
import base64

def encode(key,clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)

    return "".join(dec)
