"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from caesar_cipher import caesar_encoder
from caesar_cipher import caesar_decoder
from caesar_cipher import caesar_key_finder

# Test (without the key_finder)

def test_caesar_encoder():
    
    callable(caesar_encoder)
    
    # Test key_num is positive number within 0 and 26
    assert caesar_encoder("Hello World!", 18) == "Zwddg Ogjdv!"
    
    # Test key_num is negative number within 0 and -26
    assert caesar_encoder("How are you?", -5) == "Cjr vmz tjp?"
    
    # Test key_num is 0 or the multiple of 26
    assert caesar_encoder("abcdEFG", 0) == "The value should be an integer that is not equal to 0 or any multiples of 26. "
    assert caesar_encoder("abcdEFG", 26) == "The value should be an integer that is not equal to 0 or any multiples of 26. "
    assert caesar_encoder("abcdEFG", -26) == "The value should be an integer that is not equal to 0 or any multiples of 26. "
    assert caesar_encoder("abcdEFG", -156) == "The value should be an integer that is not equal to 0 or any multiples of 26. "
    assert caesar_encoder("abcdEFG", 156) == "The value should be an integer that is not equal to 0 or any multiples of 26. "  
 
    # Test key_num is more than 26 or less than -26 but within the range of -100 to 100 
    assert caesar_encoder("abcdefghijklmnopqrstuvwxyz", 90) == "mnopqrstuvwxyzabcdefghijkl"
    assert caesar_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 90) == "MNOPQRSTUVWXYZABCDEFGHIJKL"
    assert caesar_encoder("abcdefghijklmnopqrstuvwxyz", -90) == "opqrstuvwxyzabcdefghijklmn"
    assert caesar_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -90) == "OPQRSTUVWXYZABCDEFGHIJKLMN"
    
    # Test key_num is out of the range and it is larger than 100 or smaller than -100
    assert caesar_encoder("abcdefghijklmnopqrstuvwxyz", 122) == "stuvwxyzabcdefghijklmnopqr"
    assert caesar_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 122) == "STUVWXYZABCDEFGHIJKLMNOPQR"
    assert caesar_encoder("abcdefghijklmnopqrstuvwxyz", -122) == "ijklmnopqrstuvwxyzabcdefgh"
    assert caesar_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -122) == "IJKLMNOPQRSTUVWXYZABCDEFGH"
    
    # Test key_num is float 
    assert caesar_encoder("Hello World!", 18.0) == "The value should be an integer that is not equal to 0 or any multiples of 26. "
    assert caesar_encoder("Hello World!", 12.5) == "The value should be an integer that is not equal to 0 or any multiples of 26. "
    
    # Test input_message without alphabet
    assert caesar_encoder("!$#$%&'()*+,-./:;<=>?@[\\]^_`{|}~#" + '""', 12) == "!$#$%&'()*+,-./:;<=>?@[\\]^_`{|}~#" + '""'
    assert caesar_encoder(" ", 12) == " "
    assert caesar_encoder("1234567890", 12) == "1234567890"
    
        
def test_caesar_decoder():
    
    callable(caesar_decoder)
    
    # Test key_num is positive number within 0 and 26
    assert caesar_decoder("Zwddg Ogjdv!", 18) == "Hello World!"
    
    # Test key_num is negative number within 0 and -26
    assert caesar_decoder("Cjr vmz tjp?", -5) == "How are you?"
    
    # Test key_num is 0 or the multiple of 26
    assert caesar_decoder("abcdEFG", 0) == "This message has not been encoded."
    assert caesar_decoder("abcdEFG", 26) == "This message has not been encoded."
    assert caesar_decoder("abcdEFG", 260) == "This message has not been encoded."  
    assert caesar_decoder("abcdEFG", -26) == "This message has not been encoded."
    assert caesar_decoder("abcdEFG", -260) == "This message has not been encoded."
    
    # Test key_num is more than 26 or less than -26 but within the range of -100 to 100 
    assert caesar_decoder("mnopqrstuvwxyzabcdefghijkl", 90) == "abcdefghijklmnopqrstuvwxyz"
    assert caesar_decoder("MNOPQRSTUVWXYZABCDEFGHIJKL", 90) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert caesar_decoder("opqrstuvwxyzabcdefghijklmn", -90) == "abcdefghijklmnopqrstuvwxyz"
    assert caesar_decoder("OPQRSTUVWXYZABCDEFGHIJKLMN", -90) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Test key_num is out of the range and it is larger than 100 or smaller than -100
    assert caesar_decoder("stuvwxyzabcdefghijklmnopqr", 122) == "abcdefghijklmnopqrstuvwxyz"
    assert caesar_decoder("STUVWXYZABCDEFGHIJKLMNOPQR", 122) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert caesar_decoder("ijklmnopqrstuvwxyzabcdefgh", -122) == "abcdefghijklmnopqrstuvwxyz"
    assert caesar_decoder("IJKLMNOPQRSTUVWXYZABCDEFGH", -122) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Test key_num is float 
    assert caesar_decoder("asgawef!", 18.0) == "Please enter an integer."
    assert caesar_decoder("asgawef!", 12.5) == "Please enter an integer." 
    
    # Test decoded_message without alphabet
    assert caesar_decoder("!$#$%&'()*+,-./:;<=>?@[\\]^_`{|}~#" + '""', 12) == "!$#$%&'()*+,-./:;<=>?@[\\]^_`{|}~#" + '""'
    assert caesar_decoder(" ", 12) == " "
    assert caesar_decoder("1234567890", 12) == "1234567890"

    

def test_caesar_key_finder():
    
    callable(caesar_key_finder)
    
    # Test when the encoded message has different length from the decoded message
    assert caesar_key_finder("Vszzawe Kzrkeas!", "Hello World!") == "Two messages do not match. Check your input:)"
    
    # Test when the resulted key value is 0 or the multiple of 26
    assert caesar_key_finder("Vszzc Kcfzr!", "Vszzc Kcfzr!") == "Your message is not encrypted. "
    
    # Test when the key value of each character used the encoded message is different
    assert caesar_key_finder("Vsawe Klreu!", "Hello World!") == "Sorry, we failed to find the key. Are you sure that they are encrypted via classical caesar ciper?"
    
    # Test when the encoded message and the decoded message have the matched key value
    assert caesar_key_finder("Vszzc Kcfzr!", "Hello World!") == (14, -12)



                 
    