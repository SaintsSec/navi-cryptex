"""
Author: @marvhus
"""
from ..cipher import Cipher


class str2int(Cipher):

    name = 'str2int'
    type = 'cipher'

    def encode(args):
        from ....cryptex import get_argument_value
        text = get_argument_value(args, "text")

        if not text:
            return {'text': "No input text", 'success': False}

        out = 0

        for i, val in enumerate(text):
            char = ord(val)
            adjusted = char << i * 8
            out += adjusted

        return {'text': out, 'success': True}

    def decode(args):
        from ....cryptex import get_argument_value
        text = get_argument_value(args, "text")

        if not text:
            return {'text': "No input text", 'success': False}

        out = ""
        num = int(text)
        str_length = len(hex(num)[2:])//2

        for i in range(str_length):
            mask = 0xFF
            char = (num >> i * 8) & mask
            out += chr(char)

        return {'text': out, 'success': True}

    def print_options(self):
        print('''
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        cryptex str2int -e -t 'hello'
        cryptex str2int -d -t ''
        ''')
