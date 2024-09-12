import sys


#English to Braille dictionary
braille_dict={
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO..",
    " ":"......",
    "capital":".....O",
    "number":".O.OOO"
}

#Braille to English dictionary
english_dict={v: k for k,v in braille_dict.items()}

#Check if it is braille
def is_braille(input_string):
    #Check if it contains (contains only O, ., and spaces)
    return all(c in "O. " for c in input_string)

#Translate braille text to english
def translate_to_english(braille_text):
    #Split braille text into chunks of 6 characters
    
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    result=[]
    capitalize_follow=False
    number_follow=False

    for braille_char in braille_chars:
        if braille_char == braille_dict["capital"]:
            capitalize_follow = True
        elif braille_char == braille_dict["number"]:
            number_follow = True
        elif braille_char == braille_dict[" "]: #Handle space
            result.append(" ")
            number_follow = False 

        else:
            if number_follow:
                if braille_char in english_dict and english_dict[braille_char].isdigit():
                    result.append(english_dict[braille_char]) #Append number
                else:
                    number_follow=False
                    result.append(english_dict.get(braille_char, " ")) #Default to space for unknown patterns
            else:
                char = english_dict.get(braille_char, " ")
                if capitalize_follow:
                    char = char.upper()
                    capitalize_follow=False
                result.append(char)
                    

    return "".join(result)

#Translate english to braille text
def translate_to_braille(english_text):
    result=[]
    for char in english_text:
        if char.isupper():
            result.append(braille_dict["capital"])
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            result.append(braille_dict["number"])
            result.append(braille_dict[char])
        else:
           result.append(braille_dict.get(char.lower(), "......")) #Default to "......" for unknown patterns
    return "".join(result)



def main():
    #Get input from command line arguments
    if len(sys.argv)!=2:
        print("Please provide a string to translate.")
        return
    

     # Join all the arguments passed, in case they are split due to spaces
    input_string = " ".join(sys.argv[1:]).strip()
    


    #Determine whether the input is braille or english
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__=="__main__":
    main()
