class CaesarCipher:
    def __init__(self):
        self.upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"

    def encode(self, shift, stringCode):
        resultString = []

        for letter in stringCode:
            if letter.isupper():
                shiftedChar = self.upperAlphabet[(self.upperAlphabet.index(letter) + shift) % 26]
                resultString.append(shiftedChar)
            elif letter.islower():
                shiftedChar = self.lowerAlphabet[(self.lowerAlphabet.index(letter) + shift) % 26]
                resultString.append(shiftedChar)
            else:
                resultString.append(letter)

        return "".join(resultString)
    
    def decode(self, shift, stringCode):
        resultString = []

        for letter in stringCode:
            if letter.isupper():
                shiftedChar = self.upperAlphabet[(self.upperAlphabet.index(letter) - shift) % 26]
                resultString.append(shiftedChar)
            elif letter.islower():
                shiftedChar = self.lowerAlphabet[(self.lowerAlphabet.index(letter) - shift) % 26]
                resultString.append(shiftedChar)
            else:
                resultString.append(letter)
        
        return "".join(resultString)
    
caesar_cipher = CaesarCipher()
print("Decrypted Message: " + caesar_cipher.decode(5, "RTAJ TZY FY IFBS"))
print("Original Message: " + caesar_cipher.encode(5, "MOVE OUT AT DAWN"))