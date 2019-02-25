import ply.lex as lex
import sys

tokens = (  'PLUS',  'MINUS',  'TIMES',  'DIVIDE',  'LPAREN',  'RPAREN' ,  'NUMBER', 'ID' )

t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_DOTPLUS = r'\.\+'
t_MINUS   = r'\.\-'
t_TIMES   = r'\.\*'
t_DIVIDE  = r'\.\/'


literals = [ '+','-','*','/','(',')' ]

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

t_ignore = '  \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t) :
    print ("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
input = "2 + 4 asdasd"
lexer.input( input )
for token in lexer:
    print("line %d: %s(%s)" %(token.lineno, token.type, token.value))

