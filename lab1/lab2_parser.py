import ply.yacc as yacc

from lab1_scanner import tokens

def p_expression_plus(p):
	'expression : expression PLUS term'
	p[0] = p[1] + p[3]

parser = yacc.yacc()