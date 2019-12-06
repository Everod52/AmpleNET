import ply.lex as lex


# Reserved words
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


# REGULAR EXPRESSION RULES
# Left bracket
t_LB = r'\['

# Right bracket
t_RB = r'\]'

# Exclamation point
t_EXCLAMATION = r'!'

# Semicolon
t_SEMICOLON = r';'


# Match numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Match an identifier
def t_ID(t):
    r'[a-zA-Z-_][a-zA-Z-_0-9]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t


# Characters to ignore
t_ignore = '\n \t'


# Error rule
def t_error(t):
    print('Error Illegal character')
    t.lexer.skip(1)


# # Comment
# def t_COMMENTS(t):
#     r'\%.*'
#     pass


# Build the lexer
lexer = lex.lex()

# Read the input
# lexer.input('open[s1;DESKTOP-95KQK54;3567]! open[s2;DESKTOP-95KQK54;3789]! connect[s1;s2]! send[s1;s2;lol]!')
#
# if __name__ == '__main__':
#
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         print(tok)
