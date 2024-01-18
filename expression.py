import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'INT',
    'FLOAT',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL=r'\='

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_line(p):
    '''
    line : INT
         | FLOAT
         | ID
         | expression
    '''

def p_expression(p):
    '''
    expression : line PLUS line
               | line MINUS line
               | line TIMES line
               | line DIVIDE line
               | line EQUAL line
               | LPAREN line RPAREN
    '''
    print("Expression is validated")

def p_error(p):
    print("Invalid Syntax")
    print(f"Syntax error at line {p.lineno}")

parser = yacc.yacc()

# Function to take user input
def get_user_input():
    lines = []
    print("Enter the Expression. Enter an empty line to finish:")
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return '\n'.join(lines)

# Example input from the user
user_input = get_user_input()

parser.parse(user_input)
