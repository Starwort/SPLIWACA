from Token import Token, tts
from Error import IllegalCharError, Error
import typing as ty
import consts

#LEXER CLASS
class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
        return
        
    def advance(self):
        #Advance the scanning pos through the program
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        
        #Loop through until we find a non-space/tab, then create a token for it
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in consts.DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(tts["TT_PLUS"]))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(tts["TT_MINUS"]))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(tts["TT_MUL"]))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(tts["TT_DIV"]))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(tts["TT_LPAREN"]))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(tts["TT_RPAREN"]))
                self.advance()
            else:
                #No valid character found and current character exists, so return an error
                return IllegalCharError(f"{self.current_char}")
            
        return tokens
    
    def make_number(self) -> ty.Tuple[Token, Error]:
        num_str = ''
        dot_count = 0
        num_str += self.current_char
        self.advance()
        #Loop through characters until we either reach the end of the number or too many decimal places
        while self.current_char != None and self.current_char in consts.DIGITS + '.':
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    return None, IllegalCharError('Invalid number - too many decimal points. Did you mean to make self a string?')
            num_str += self.current_char
            self.advance()
        #If there is a decimal place, return as float, otherwise return as int
        if dot_count == 1:
            return Token(tts['TT_FLOAT'], float(num_str)), None
        else:
            return Token(tts['TT_INT'], int(num_str)), None
        raise RuntimeError("We shouldn't have been able to get here."+
    "There is more than one dod but the function has not returned!")
        
