import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = [
    'TRY', 'CATCH', 'FINALLY', 'IDENTIFIER', 'COLON', 'SEMICOLON', 'PRINT',
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'NUMBER', 'DOUBLETICKS', 'SINGLETICKS', 'DATA_TYPE', 'COMMA',
    'PLUS', 'MINUS', 'TIMES', 'ASSIGN', 'NOT', 'EQUALS', 'GREATERTHAN', 'LESSTHAN',
]

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COLON = r':'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOUBLETICKS = r'\"([^\\"]|\\.)*\"'
t_SINGLETICKS = r'\'([^\\\']|\\.)*\''
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_ASSIGN = r'\='
t_EQUALS = r'\=='
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_NOT = r'\!'

t_ignore = ' \t'
def t_TRY(t):
    r'try'
    return t
def t_CATCH(t):
    r'catch'
    return t
def t_FINALLY(t):
    r'finally'
    return t

def t_DATA_TYPE(t):
    r'int|byte|short|boolean|long|float|double|char'
    return t

def t_PRINT(t):
    r'System\.out\.println'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parser
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES'),
    ('nonassoc', 'LESSTHAN', 'GREATERTHAN', 'EQUALS'),
    ('right', 'NOT'),
)

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
              | print_statement
              | variable_declaration
              | exception
              | empty
    '''

def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN data RPAREN SEMICOLON
    '''

def p_data(p):
    '''
    data : string
         | NUMBER
         | IDENTIFIER
         | data COMMA data
    '''

def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON
                        | IDENTIFIER PLUS PLUS
                        | MINUS MINUS IDENTIFIER
                        | PLUS PLUS IDENTIFIER
                        | IDENTIFIER MINUS MINUS
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

def p_string(p):
    '''
    string : DOUBLETICKS 
           | SINGLETICKS
           
    '''



def p_variable_declaration(p):
    '''
    variable_declaration : DATA_TYPE IDENTIFIER SEMICOLON
                         | DATA_TYPE IDENTIFIER ASSIGN expression SEMICOLON
    '''

def p_exception(p):
    '''
    exception : TRY LBRACE statements RBRACE CATCH LPAREN IDENTIFIER IDENTIFIER RPAREN LBRACE statements RBRACE finally
              | TRY LBRACE statements RBRACE CATCH LPAREN IDENTIFIER IDENTIFIER RPAREN LBRACE statements RBRACE
              | TRY LBRACE statements RBRACE finally
              | TRY LBRACE statements RBRACE
    '''

def p_finally(p):
    '''
    finally : FINALLY LBRACE statements RBRACE
            | FINALLY LBRACE statements RBRACE finally
            | empty
    '''

def p_empty(p):
    '''
    empty :
    '''

def p_error(p):
    print(f"Syntax error at line '{p.lineno}', at the value '{p.value}' ")

lexer = lex.lex()
parser = yacc.yacc()

# Example Java code
java_code = """
try {
    System.out.println("Try block");
} catch (Exception e) {
    System.out.println("Catch block");
} finally {
    System.out.println("Finally block");
}
"""

lexer.input(java_code)
for token in lexer:
    print(token)

result = parser.parse(java_code)