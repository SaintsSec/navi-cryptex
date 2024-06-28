from ..cipher import Cipher


class MA(Cipher):
    name = 'MonoAlphabetic cipher'
    type = 'cipher'

    def encode(args):
        from ....cryptex import get_argument_value
        text = get_argument_value(args, "text")
        key = get_argument_value(args, "key")
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No key", 'success': False}

        output = []
        for char in text:
            lower_case = None
            if char.islower():
                lower_case = True
                char = char.upper()
            if char.upper() not in alphabet:
                output.append(char)
            else:
                index = alphabet.index(char)
                if lower_case:
                    output.append(key[index].lower())
                else:
                    output.append(key[index])

        output = ''.join(output)
        return {'text': output, 'success': True}

    def decode(args):
        from ....cryptex import get_argument_value
        text = get_argument_value(args, "text")
        key = get_argument_value(args, "key")
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No key", 'success': False}

        output = []
        for char in text:
            lower_case = None
            if char.islower():
                lower_case = True
                char = char.upper()
            if char.upper() not in key:
                output.append(char)
            else:
                index = key.index(char)
                if lower_case:
                    output.append(alphabet[index].lower())
                else:
                    output.append(alphabet[index])

        output = ''.join(output)
        return {'text': output, 'success': True}

    def print_options(self):
        print('''
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text
        -k / --key ------- key (26 Characters)

        ### Example
        cryptex ma -t 'hello' -k 'BSDPFRJUGEOZLICNQKATYVWHXM'
        ''')
