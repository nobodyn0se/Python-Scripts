def getdata():
    data = input("Enter your message to be translated to morse\n")
    return data


def pass_morse():
    morse_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-'}
    return morse_dict


def translate(morse_dict, message):
    out = ""
    for letter in message.upper():
        if letter != " ":
            out += morse_dict[letter]
        else:
            out += " "
    return out


def main():
    message = getdata()
    morse_code = pass_morse()
    morse_output = translate(morse_code, message)
    print(morse_output)


if __name__ == "__main__":
    main()