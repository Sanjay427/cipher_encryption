# !/usr/bin/env python3
import string


# encryption and decryption using ceasar cipher
class EncryptionWithSingleKey:
    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key
        self.upper_letter = string.ascii_uppercase
        self.encrypt_text = ''
        self.decrypt_text = ''
        # calling encryption
        self.encrypt()
        # calling decryption
        self.decrypt(self.encrypt_text)

    # encrypting the given text
    def encrypt(self):
        for text in self.text:
            if text in self.upper_letter:
                index = self.upper_letter.index(text)
                self.encrypt_text += ''.join(self.upper_letter[((index + self.key) % 26)])
        print(f'The encryption of {self.text} is {self.encrypt_text}')

    # decrypting the given encryption
    def decrypt(self, encrypt_text):
        for text in encrypt_text:
            if text in self.upper_letter:
                index = self.upper_letter.index(text)
                self.decrypt_text += ''.join(self.upper_letter[((index - self.key) % 26)])
        print(f'The decryption of {encrypt_text} is {self.decrypt_text}')


class EncryptionAndDecryptionWithMultipleKey:
    def __init__(self, encrypt_text, decrypt_text):
        self.encrypt_text = encrypt_text.upper()
        self.decrypt_text = decrypt_text.upper()
        self.letter = string.ascii_uppercase
        # encryption
        self.encrypt(self.encrypt_text)
        # decrypting
        self.decrypt(self.decrypt_text)

    def encrypt(self, sentence):
        for key in range(1, len(self.letter)):
            translate = ''
            for word in sentence:
                if word in self.letter:
                    index = self.letter.index(word)
                    # increasing the index by key
                    index = index + key

                    # if index is greater that 26
                    if index > 25:
                        index = index - len(self.letter)
                    translate += self.letter[index]
                else:
                    translate += word
            print(f'key {key} encryption is {translate}')

    def decrypt(self, sentence):
        for key in range(1, len(self.letter)):
            translate = ''
            for symbol in sentence:
                if symbol in self.letter:
                    index = self.letter.index(symbol)
                    # subtrating the index
                    index = index - key
                    # if index is less than 0
                    if index < 0:
                        index = index + len(self.letter)
                    translate += self.letter[index]
                else:
                    translate += symbol
            print(f'key {key} : decryption is {translate}')
