"""A collection of function for doing my project."""

# Preparation

import string    

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
    

# Functions

# check if key is eligible for encoding or decoding
def check_key(key_num):
    """
    Check if the key value is eligible for encoding or decoding.
    
    Parameters
    ----------
    key_num: int
        The key value that indicates the number of shifts.
        
    Returns
    ------
    Boolean
        If the key value is eligible for encoding or decoding (not neither equal to 0 nor the multuples of 26 nor a float nor a string), return True; 
        Otherwise, return False.
        """
    
    if key_num % 26 == 0 or key_num == 0:
        return False
    elif isinstance(key_num, float):
        return False
    elif isinstance(key_num, str):
        return False
    else:
        return True

    

# identify the key that used for encoding
def identify_key(input_key):
    """
    Turning the key value that is out of the range between -26 and 26 into the corresponding value within the range. 
    
    Parameters
    ----------
    input_key: int
        The original key value that indicates the number of shifts.
        
    Returns
    -------
    out_key: int
        The corresponding value of the input key value that is within the range of -26 and 26.
    """
    
    if input_key > 26: 
        out_key = input_key % 26
    elif -26 > input_key:  #negative value means counting backwards: e.g. when key = -1, a becomes z. -25 to 25 inclusive
        out_key = -1*((-1*input_key) % 26)
    else:
        out_key = input_key
    return out_key


def negative_encrypt(input_char,raw_code):
    """
    Transforming the unicode that is proccessed by adding negative key value into the corresponding encrypted unicode of input character.
    
    Parameters
    ----------
    input_char: str
        The alphabet character in the input message.
    raw_code: int
        The unicode of the input character that has already added the shift value
        
    Returns
    -------
    out_code: int
        The ultimate encrypted unicode of input character.
    """
    
    if input_char in alphabet_lower and raw_code < 97: 
        out_code = 122 - (96 - raw_code)
    elif input_char in alphabet_upper and raw_code < 65:
        out_code = 90 - (64 - raw_code)
    else:
        out_code = raw_code
            
    return out_code

 
def positive_encrypt(input_char,raw_code):
    """
    Transforming the unicode that is proccessed by adding positive key value into the corresponding encrypted unicode of input character.
    
    Parameters
    ----------
    input_char: str
        The alphabet character in the input message.
    raw_code: int
        The unicode of the input character that has already added the shift value
        
    Returns
    -------
    out_code: int
        The ultimate encrypted unicode of input character.
    """
    
    if input_char in alphabet_lower and raw_code > 122: 
        out_code = 96 + (raw_code - 122)
    elif input_char in alphabet_upper and raw_code > 90:
        out_code = 64 + (raw_code - 90)
    else:
        out_code = raw_code
        
    return out_code
 
    
def key_complement(key):
    """
    Calculating the simplified complement key that have the same encoded effect as the given key. (e.g. if the given key is 12, the complement key is -14.)
    
    Parameters
    ----------
    key: int
        The given key value that indicates the number of shifts.
        
    Returns
    -------
    key_complement: int
        The simplified complement key that have the same encoded effect as the given key value.
    """
    
    if key > 0:
        key_complement = -1 * (26 - key)
    elif key < 0:
        key_complement = 26 + key
    else:
        key_complement = 26
    return key_complement
