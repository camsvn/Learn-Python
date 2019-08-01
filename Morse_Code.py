import winsound
import time

# Dictionary stores Morse Equivalents of Alphabets and Numbers
morse_code_dict={'A':'.-', 'B':'-...', 
                 'C':'-.-.', 'D':'-..', 'E':'.', 
                 'F':'..-.', 'G':'--.', 'H':'....', 
                 'I':'..', 'J':'.---', 'K':'-.-', 
                 'L':'.-..', 'M':'--', 'N':'-.', 
                 'O':'---', 'P':'.--.', 'Q':'--.-', 
                 'R':'.-.', 'S':'...', 'T':'-', 
                 'U':'..-', 'V':'...-', 'W':'.--', 
                 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                 '1':'.----', '2':'..---', '3':'...--', 
                 '4':'....-', '5':'.....', '6':'-....', 
                 '7':'--...', '8':'---..', '9':'----.', 
                 '0':'-----'}


# Function to encrypt the message
def encrypt(message,duration):
    cipher='' # string to store the morse equivalent of the message
    for letter in message:
        if letter != ' ': # ' ' used to differentiate words in message
            cipher+=morse_code_dict[letter]+'/' # '/' to differentiate the letters of the words in cipher string
        else:
            cipher+='|' ## '/' to differentiate the words in cipher string
    morse(cipher,duration)

# Function plays the Morse code using 'winsound.beep()'
def morse(cipher,dot_duration):
    '''
        *******Morse Code Rules*******
        + Dot Length = 1 time unit
        + Dash Length = 3 time units
        + Space b/w Symbols (dots and dashes) of the same letter = 1 time unit
        + Space b/w letters = 3 time units
        + Space b/w words = 7 time units
        ******************************        
    '''    
    dash_duration = dot_duration*3
    space_duration = dot_duration/1000
    letter_space_duartion = space_duration*2
    word_space_duartion = space_duration*4
    
    for i in range(len(cipher)):
        if cipher[i] == '.': 
            winsound.Beep(440,dot_duration) #play sine wave of 440Hz for unit time 
            time.sleep(space_duration) #pause for unit time - space b/w symbols
        
        elif cipher[i] == '-':
            winsound.Beep(440,dash_duration) #play sine wave of 440Hz for 3 unit time 
            time.sleep(space_duration) #pause for unit time - Space b/w symbols
        
        elif cipher[i] == '/':
            time.sleep(letter_space_duartion) #pause for 2 unit time [1unit+2units=3units] - Space b/w letters
        
        else:
            time.sleep(word_space_duartion) #pause for 4 unit time [1unit+2units+4units=7units] - Space b/w words
            
def main():
    message=input("Enter String to Encrypt: ")
    message = message.upper()
    encrypt(message,100) #2nd argument represents the dot duration in micro seconds
    
'''Execute the main funtion'''
main() 