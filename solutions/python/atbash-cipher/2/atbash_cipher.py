"""Create an implementation of the Atbash cipher, 
an ancient encryption system created in the Middle East. 
"""

import string


def encode(plain_text: str) -> str:
    """Encode a message using Atbash cipher.
    
    param plain_text: str - The original message
    :return: str - the encoded message
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = str.maketrans(alphabet, alphabet[::-1], string.punctuation)
    plain_text = "".join(plain_text.lower().split()).translate(cipher)
    len_text = len(plain_text)
    return "".join(plain_text[index] + " " 
                   if index % 5 == 4 and index != len_text - 1 
                   else plain_text[index] for index in range(len_text)
                   )



def decode(ciphered_text: str) -> str:
    """Decode an encrypted message using Atbash cipher.
        
    param plain_text: str - The ciphered message
    :return: str - the decoded message
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    uncipher = str.maketrans(alphabet[::-1], alphabet, " ")

    return ciphered_text.translate(uncipher)