import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'IF',
    'ELSE',
    'IDENTIFIER',
    'NUMBER',
    'SEMICOLON',
    'PLUS',
    'MINUS',
    'TIMES',
    'LESSTHAN',
    'GREATERTHAN',
    'ASSIGN',
    'EQUALS',
    'NOT',
    'DATA_TYPE',
    'STRING',
    'PRINT'
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'\>'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NOT = r'!'
t_STRING = r'\"([^\\\"]|(\\.))*?\"'

def t_PRINT(t):
    r'System.out.printIn'
    return t

def t_DATA_TYPE(t):
    r'int|byte|short|boolean|long|float|double|char'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule to ignore whitespace and tabs
t_ignore = ' \t\n'

# Define a rule for tracking errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define the lexer
lexer = lex.lex()

# Define the parser rules
def p_program(p):
    '''
    program : statements
    '''

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''

def p_statement(p):
    '''
    statement : assignment_statement
              | if_else_statement
              | variable_declaration
              | empty
              | print_statement
    '''

# ...

def p_if_else_statement(p):
    '''
    if_else_statement : IF LPAREN condition RPAREN LBRACE nested RBRACE ELSE LBRACE nested RBRACE
                      | IF LPAREN condition RPAREN LBRACE nested RBRACE ELSE LBRACE RBRACE
                      | IF LPAREN condition RPAREN LBRACE RBRACE ELSE LBRACE nested RBRACE
                      | IF LPAREN condition RPAREN LBRACE RBRACE ELSE LBRACE RBRACE
                      | IF LPAREN condition RPAREN LBRACE nested RBRACE
                      | IF LPAREN condition RPAREN LBRACE RBRACE
    '''
    print("Valid If-Else Statement Syntax")

# ...

def p_nested(p):
    '''
    nested  : statements
            | if_else_statement
            | empty
    '''

# ...

def p_variable_declaration(p):
    '''
    variable_declaration : DATA_TYPE IDENTIFIER SEMICOLON
                            | DATA_TYPE assignment_statement
    '''
    print("Valid Variable Declaration Syntax")

def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON
    '''
    print("Valid Assignment Statement Syntax")



def p_condition(p):
    '''
    condition : expression
    '''

def p_expression(p):
    '''
    expression : IDENTIFIER
               | NUMBER
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | LPAREN expression RPAREN
               | expression LESSTHAN expression
               | expression GREATERTHAN expression
               | expression ASSIGN expression
               | expression EQUALS expression
               | NOT expression
    '''

def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN STRING RPAREN SEMICOLON
    '''


# Empty production
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error at line {p.lineno} at the value '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Function to take user input
def get_user_input():
    lines = []
    print("Enter the if-else condition, Enter an empty line to finish:")
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return '\n'.join(lines)

# Example input from the user
user_input = get_user_input()

# Tokenize and parse the user input

parser.parse(user_input)
