import ply.lex as lex


# Reserved words
from file_reader import read_file

reserved_words = {
    'connect': 'CONNECT',
    'client': 'CLIENT',
    'open': 'OPEN',
    'send': 'SEND',
    'external': 'EXTERNAL',
    'default': 'DEFAULT'
}

# TOKENS
tokens = [
    'MESSAGE',
    'IP',
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


# Comments
def t_COMMENTS(t):
    r'\(.*\)'
    pass


# Match IP addresses
def t_IP(t):
    r'\d+\.\d+\.\d+\.\d+'
    t.value = str(t.value)
    return t


# Match numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Match a message
def t_MESSAGE(t):
    r'\<(.)+\>'
    return t


# Match an identifier
def t_ID(t):
    r'[a-zA-Z-_][a-zA-Z-_0-9]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Characters to ignore
t_ignore = ' \t'


# Error rule
def t_error(t):
    print("ERROR: Illegal character '%s', at position %s, %s." %
          (t.value[0], t.lineno, t.lexpos))
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


if __name__ == '__main__':
    # Read the input
    lexer.input(read_file("tests/test.txt"))

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
