from ..cipher import Cipher


class AK(Cipher):
    name = 'Autokey Cipher'
    type = 'cipher'

    def encode(args):
        output = ''
        from ....cryptex import get_argument_value
        text = get_argument_value(args, "text").lower()
        key = get_argument_value(args, "key")
        exclude_options = get_argument_value(args, "exclude")
        exclude = exclude_options if exclude_options else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"
        new_key = ''
        temp = key + text

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No shift key", 'success': False}

        for k in temp:
            if k not in exclude:
                new_key += k

        output = []
        i = 0
        for c in text:
            if c in exclude:
                output.append(c)
            else:
                x = ((ord(c) % 97) + (ord(new_key[i]) % 97)) % 26
                x += ord('a')
                i += 1
                output.append(chr(x))

        return {'text': "".join(output), 'success': True}

    def decode(args):
        output = ''
        from ....cryptex import get_argument_value
        text = get_argument_value(args, "text").lower()
        key = get_argument_value(args, "key")
        exclude_options = get_argument_value(args, "exclude")
        exclude = exclude_options if exclude_options else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"
        new_key = ''

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No shift key", 'success': False}

        for k in key:
            if k not in exclude:
                new_key += k

        output = []
        i = 0
        for c in text:
            if c in exclude:
                output.append(c)
            else:
                x = ((ord(c) % 97) - (ord(new_key[i]) % 97)) % 26
                x += ord('a')
                output.append(chr(x))
                new_key += chr(x)
                i += 1

        return {'text': "".join(output), 'success': True}

    def print_options(self):
        print('''
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text
        -k / --key ------- shift key
        -ex / --exclude -- exclude list

        ### Examples
        cryptex cc -e -t "hello" -k 10
        cryptex cc -d -t "hello" -k 10
        cryptex cc -e -t "hello" -k 10 -ex '123456789'
        cryptex cc -d -t "hello" -k 10 -ex '123456789'
       ''')
