"""Create an implementation of the Atbash cipher, 
an ancient encryption system created in the Middle East. 
"""

import string

def cipher(input_message: str) -> str:
    """Convert a string back and forth using Atbash cipher.
    
    param input_message: str - the message received
    :return: str - the message returned
    """
    input_message = input_message.lower()
    cipher = str.maketrans(string.ascii_lowercase, 
                           string.ascii_lowercase[::-1], 
                           string.punctuation + " "
                          )
    return input_message.lower().translate(cipher)

    
def encode(plain_text: str) -> str:
    """Encode a message using Atbash cipher.
    
    param plain_text: str - The original message
    :return: str - the encoded message
    """
    plain_text = cipher(plain_text)
    len_text = len(plain_text)
    return "".join(plain_text[index:index + 5] + " " 
                   if index + 5 < len_text - 1 
                   else plain_text[index:index + 5]
                   for index in range(0, len_text, 5)
                   )



def decode(ciphered_text: str) -> str:
    """Decode an encrypted message using Atbash cipher.
        
    param plain_text: str - The ciphered message
    :return: str - the decoded message
    """
    return cipher(ciphered_text)