def decrypt(cryptogram, shift):
    decrypted_text = ""

    for char in cryptogram:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted_text += char

    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted_text = decrypt(cryptogram, shift)
        print(f"Shift Key {shift}: {decrypted_text}")

# Example cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBABR"

# Find the shift key
find_shift_key(cryptogram)