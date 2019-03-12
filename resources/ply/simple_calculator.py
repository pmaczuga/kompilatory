#!/usr/bin/python

import ply.lex as lex;
import ply.yacc as yacc;

symtab = {}

literals = [ '+','-','*','/','(',')','=' ]

tokens = ( "VAR", "NUMBER");

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
#    line = t.value.lstrip()
#    i = line.find("\n")
#    line = line if i == -1 else line[:i]
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

def t_VAR(t):
    r"[a-zA-Z_]\w*"
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

precedence = (
   ("right", '='),
   ("left", '+', '-'),
   ("left", '*', '/'),
)

def p_error(p):
    print("parsing error\n")

def p_start(p):
    """start : EXPRESSION
             | start EXPRESSION"""
    if   len(p)==2: print("p[1]=", p[1])
    else:           print("p[2]=", p[2])


def p_expression_number(p):
    """EXPRESSION : NUMBER"""
    p[0] = p[1]

def p_expression_var(p):
    """EXPRESSION : VAR"""
    val = symtab.get(p[1])
    if val:
        p[0] = val
    else:
        p[0] = 0
        print("%s not used\n" %p[1])

def p_expression_assignment(p):
    """EXPRESSION : VAR '=' EXPRESSION"""
    p[0] = p[3]
    symtab[p[1]] = p[3]

def p_expression_sum(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION"""
    if   p[2]=='+': p[0] = p[1] + p[3];
    elif p[2]=='-': p[0] = p[1] - p[3];


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION"""
    if   p[2]=='*': p[0] = p[1] * p[3];
    elif p[2]=='/': p[0] = p[1] / p[3];


def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ')'"""
    p[0] = p[2]

file = open("plik.ini", "r");

lexer = lex.lex()
parser = yacc.yacc()
text = file.read()
parser.parse(text, lexer=lexer)



