import ply.lex as lex


reserved_words = {
    'connect': 'CONNECT',
    'open': 'OPEN',
    'send': 'SEND',
}

# TOKENS
tokens = [
    'NUMBER',
    'LB',
    'RB',
    'EXCLAMATION',
    'ID',
    'SEMICOLON',
] + list(reserved_words.values())


# REGULAR EXPRESSIONS FOR TOKENS
t_LB = r'\['
t_RB = r'\]'
t_EXCLAMATION = r'!'
t_SEMICOLON = r';'

t_ignore = '\n \t'


def t_error(t):
    print('Error Illegal character')
    t.lexer.skip(1)


# Match numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Match an identifier
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t


lexer = lex.lex()
lexer.input('connect[1;2]!')

if __name__ == '__main__':

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
