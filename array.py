import ply.lex as lex
import ply.yacc as yacc

god = True

tokens = (
    "DATA_TYPE",
    "OPEN_SQUARE",
    "CLOSE_SQUARE",
    "IDENTIFIER",
    'NUMBER',
    "EQUAL",
    "NEW",
    "SEMICOLON"
)

t_EQUAL = r'\='
t_SEMICOLON = r';'
t_CLOSE_SQUARE = r'\]'
t_OPEN_SQUARE = r"\["
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_DATA_TYPE(t):
    r'int|byte|short|boolean|long|float|double|char'
    return t


def t_NUMBER(t):
    r'\d+(\s*\d+)*'
    t.value = int(t.value)
    return t



def t_NEW(t):
    r'new'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    global god
    god = False
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


t_ignore = ' \t\n'


def p_arrdeclear(p):
    '''
    arrdeclear : DATA_TYPE IDENTIFIER OPEN_SQUARE CLOSE_SQUARE SEMICOLON
               | DATA_TYPE OPEN_SQUARE CLOSE_SQUARE IDENTIFIER SEMICOLON
               | DATA_TYPE IDENTIFIER OPEN_SQUARE CLOSE_SQUARE EQUAL NEW DATA_TYPE OPEN_SQUARE NUMBER CLOSE_SQUARE SEMICOLON
               | DATA_TYPE OPEN_SQUARE CLOSE_SQUARE IDENTIFIER EQUAL NEW DATA_TYPE OPEN_SQUARE NUMBER CLOSE_SQUARE SEMICOLON
    '''
    print('Valid Syntax')


def p_error(p):
    global god
    god = False

    print(f"Invalid Syntax")
    print(f'error due to "{p.value}" in the line "{p.lineno}"')


# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Example input
while True:
    god = True
    decotee = True
    try:
        user_input = input(">> ")
        if not user_input:
            break  # Exit the loop if the input is empty
        if user_input[-1] == "{" or user_input[-1] == ')':
            lines = []
            while decotee:
                if user_input == '}':
                    break
                else:
                    lines.append(user_input + '\n')
                user_input = input(".. ")
            s = "".join(lines)
        else:
            s = user_input
    except EOFError:
        break
    parser.parse(s)