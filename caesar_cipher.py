
from caesar_tool import check_key
from caesar_tool import identify_key
from caesar_tool import negative_encrypt
from caesar_tool import positive_encrypt
from caesar_tool import key_complement 


def caesar_encoder(input_message,key_num):
    """
    Encoding the input message using the caesar cipher.
    
    Parameters
    ----------
    input_message: str
        The original message that is needed to be encoded.
    key_num: int
        The key value that indicates the number of shifts. 
        The range of shifted value is from positive infinity to negative infinity. 
        The positive shifted value indicates counting to the right (ascendingly); 
        the negative shifted value indicates counting to the left (descendingly). 
        
    Returns
    -------
    out_mes: str
        The encoded message of input message after encypting with caesar cipher using the given key value.
    str
        The specific error occuring during encoding process.
    """
    
    # Check whether the key number is eligible for encoding (Whether it is 0 or multiples of 26 or a float or a string).
    if check_key(key_num):

        out_mes = ''
        
        # Loop through each character in the message and encrypt the letters.
        for char in input_message:
            if char.isalpha() == True:
                
                key = identify_key(key_num)  # Turn the input key value into the equivalent number within the range of -25 to 25 inclusive.
                code_char = ord(char) + key  # Encode the character by adding the shifted value.
                
                # Check if the unicode of encoded character is encoded followed the rules that 
                # uppercase letter remains uppercase; lowercase letter remains lowercase.
                # If not, transform the unicode into the unicode that follows the rules.
                if key > 0:
                    code_char = positive_encrypt(char,code_char)
                elif key < 0:
                    code_char = negative_encrypt(char,code_char)
                
                # Turn the encoded unicode back into character
                encoded = chr(code_char)
                out_mes = out_mes + encoded
                
            else:
                out_mes = out_mes + char 
                
        return out_mes
    
    else:
        return "The value should be an integer that is not equal to 0 or any multiples of 26. "

    
def caesar_decoder(encoded_message,key_num):
    """
    Decoding the encrypted message using caesar cipher.
    
    Parameters
    ----------
    encoded_message: str
        The encoded message that is needed to be decoded.
    key_num: int
        The corresponding key value of the given encoded message, which indicates the number of shifts.
        
    Returns
    -------
    out_mes: str
        The decoded message of the encoded message after decrypting with caesar cipher using the given key value.
    str
        The specific error occuring during decoding process.
    """
    
    # Check if the key is eligible for decoded. (Whether it is 0 or multiples of 26 or a float or a string).
    if check_key(key_num):
        
        out_mes = ''
        
        # Loop through each character in the message and decrypt the letters only.
        for char in encoded_message:
            if char.isalpha() == True:
                
                key = identify_key(key_num)      # Turn the input key value into the equivalent number within the range of -25 to 25 
                decoded_char = ord(char) - key   # Decode the character by subtracting the key from the unicode of encoded character.
                
                # Check whether the unicode of decoded character follows the rule that: 
                # uppercase letter remains uppercase; lowercase letter remains lowercase.
                # If not, transform the unicode into the unicode that follows the rules.
                if key > 0:
                    decoded_char = negative_encrypt(char,decoded_char)  # Because decoding is the reversed process of encoding, the positive key used in the encoding is decrypted by becoming negative here.
                elif key < 0:
                    decoded_char = positive_encrypt(char,decoded_char)  # Due to the same reason, the negative key used in the encoding becomes positive here.
                
                decoded = chr(decoded_char)       
                out_mes = out_mes + decoded
                
            else:
                out_mes = out_mes + char
                
        return out_mes

    elif isinstance(key_num, float) or isinstance(key_num, str):
        return "Please enter an integer."
    
    else:
        return "This message has not been encoded."
                
            
def caesar_key_finder(encoded_mes,decoded_mes):
    """
    Finding the simplified key value (the key value within the range of -26 to 26) with given encoded message and decoded message.
    
    Parameters
    ----------
    encoded_mes: str
        The encoded message that is used to find the key value.
    decoded_mes: str
        The corresponding decoded message of the given encoded message that is used to find the key value.
        
    Returns
    -------
    key: int
        The cooresponding simplified key values of the given encoded message and decoded message. 
        The simplified shifted values occur as pairs, one positive and one negative.
    str
        The specific error occuring in the way of finding the corresponding key value.
    """
    
    # Check if two messages are eligible for finding the key. (If two messages do not have the same length, the message might not be encrypted using classic caesar cipher.)
    if len(encoded_mes) == len(decoded_mes):
        
        # Set the first identified key as the reference key.
        for num in range(len(encoded_mes)):
        
            en_char1 = encoded_mes[num]
            de_char1 = decoded_mes[num]
               
            if en_char1.isalpha and de_char1.isalpha:
                key = ord(en_char1) - ord(de_char1)
                complement_key = key_complement(key)
                break
            
        
        # Test if the shifted value is consistent throughout the message by calculating the shifted value for every letters pair and comparing it to the reference key.
        # If the test fails, the message might be encrypted using at least two different shifted values on different parts of the message;
        for num in range(len(encoded_mes)):
            
            en_char = encoded_mes[num]
            de_char = decoded_mes[num]
            
            if en_char.isalpha() and de_char.isalpha():
                test_key = ord(en_char) - ord(de_char)
                
            if test_key != key and test_key != complement_key:
                return "Sorry, we failed to find the key. Are you sure that they are encrypted via classical caesar ciper?"
            
        # Check the value of key to see if the message is been encryted.
        if not check_key(key):
            return "Your message is not encrypted. "
        
        # If successfully pass all the tests above, output the key and the complement key.
        return key, complement_key
    
    else: 
        return "Two messages do not match. Check your input:)"
        

            