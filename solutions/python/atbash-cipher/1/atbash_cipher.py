import string

def encode(plain_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = str.maketrans(alphabet, alphabet[::-1], string.punctuation)
    plain_text = "".join(plain_text.lower().split()).translate(cipher)
    len_text = len(plain_text)
    return "".join(plain_text[index] + " " 
                   if index % 5 == 4 and index != len_text - 1 
                   else plain_text[index] for index in range(len_text)
                   )






def decode(ciphered_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    uncipher = str.maketrans(alphabet[::-1], alphabet, " ")

    return ciphered_text.translate(uncipher)