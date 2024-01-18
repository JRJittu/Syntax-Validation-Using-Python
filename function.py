import ply.lex as lex
import ply.yacc as yacc

god = True

# List of token names
tokens = (
    'RETURN_TYPE',
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'STAR'
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STAR = r'\*'

def t_RETURN_TYPE(t):
    r'int|byte|short|boolean|long|float|double|char|void'
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule to ignore whitespace and tabs
t_ignore = ' \t\n'

# Define the parser rules


def p_function_declaration(p):
    '''
    function_declaration : RETURN_TYPE star IDENTIFIER LPAREN parameters RPAREN SEMICOLON
                        | RETURN_TYPE star IDENTIFIER LPAREN RPAREN SEMICOLON
    '''
    print("Valid Syntax")

def p_parameters(p):
    '''
    parameters : parameters COMMA parameter
               | parameter
    '''

def p_parameter(p):
    '''
    parameter : RETURN_TYPE star IDENTIFIER 
              | RETURN_TYPE empty
    '''

def p_empty(p):
    'empty :'
    pass
def p_star(p):
    '''
    star : STAR 
         | empty
    '''

# Error rule for syntax errors
def t_error(t):
    global god
    god = False
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Error rule for parsing errors
def p_error(p):
    global god
    god = False
    print(f"Syntax error at line {p.lineno}")

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