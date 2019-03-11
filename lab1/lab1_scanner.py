import ply.lex as lex

literals = "()[]{}:;,;'"

t_ADD    = r'\+'
t_SUB   = r'\-'
t_MUL   = r'\*'
t_DIV  = r'\/'
t_DOTADD = r'\.\+'
t_DOTSUB   = r'\.\-'
t_DOTMUL   = r'\.\*'
t_DOTDIV  = r'\.\/'

t_EQ = r'\=\='
t_GT = r'\>'
t_LT = r'\<'
t_GE = r'\>\='
t_LE = r'\<\='
t_NE = r'\!\='

t_ASSIGN = r'\='
t_ADDASSIGN = r'\+\='
t_SUBASSIGN = r'\-\='
t_MULASSIGN = r'\*\='
t_DIVASSIGN = r'\/\='

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT'
}

tokens = [ 'COMMENT', 'INTNUM', 'FLOATNUM', 'STRING',
'ID', 'EQ', 'GT', 'LT', 'GE', 'LE', 'NE', 'IS',
'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
'ADD', 'SUB', 'MUL', 'DIV', 'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 
 ] + list(reserved.values())

def t_COMMENT(t):
     r'\#.*'
     pass
     # No return value. Token discarded

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_FLOATNUM(t):
    r'(([0-9]+\.[0-9]+|[0-9]+\.|\.[0-9]+)E[0-9]+)|([0-9]+\.[0-9]+|[0-9]+\.|\.[0-9]+)'
    t.value = float(t.value)
    return t

def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t) :
    print ("Illegal character '{}' in line {}".format(t.value[0], t.lineno))
    t.lexer.skip(1)


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

t_ignore = '  \t'

lexer = lex.lex()
