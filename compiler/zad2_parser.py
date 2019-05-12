import ply.yacc as yacc

import zad1_scanner
from zad3_ast import *

tokens = zad1_scanner.tokens

precedence = (
    ("nonassoc", 'IFX'),
    ("nonassoc", 'ELSE'),

    ('nonassoc', 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('nonassoc', 'EQ', 'GT', 'LT', 'GE', 'LE', 'NE'),
    ('left', 'ADD', 'SUB', 'DOTADD', 'DOTSUB'),
    ('left', 'MUL', 'DIV', 'DOTMUL', 'DOTDIV'),
    ('right', 'NEGATION'),
    ('left', 'TRANSPOSE')
)

def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, zad1_scanner.find_tok_column(p), p.type, p.value))
    else:
        print("Unexpected end of input")
    raise ValueError("Error")

def p_program(p):
    '''program : instructions_opt'''
    p[0] = Program(p[1])
    p[0].line = zad1_scanner.lexer.lineno

def p_instructions_opt_some(p):
    '''instructions_opt : instructions'''
    p[0] = p[1]

def p_instructions_opt_none(p):
    '''instructions_opt : '''
    p[0] = Instructions()
    p[0].line = zad1_scanner.lexer.lineno

def p_instructions_multiple(p):
    '''instructions : instructions instruction'''
    p[0] = Instructions(p[1].instructions + [p[2]])
    p[0].line = zad1_scanner.lexer.lineno

def p_instructions_single(p):
    '''instructions : instruction'''
    p[0] = Instructions([p[1]])
    p[0].line = zad1_scanner.lexer.lineno

def p_instruction_statement(p):
    '''instruction : statement ';' '''
    p[0] = p[1]

def p_instruction_if(p):
    '''instruction : IF '(' condition ')' instruction ELSE instruction
                   | IF '(' condition ')' instruction %prec IFX'''
    if len(p) == 8:
        p[0] = If(p[3], p[5], p[7])
    elif len(p) == 6:
        p[0] = If(p[3], p[5])
    p[0].line = zad1_scanner.lexer.lineno

def p_instruction_for(p):
    '''instruction : FOR variable ASSIGN expression ':' expression instruction'''
    p[0] = For(p[2], Range(p[4], p[6]), p[7])
    p[0].line = zad1_scanner.lexer.lineno

def p_instruction_while(p):
    '''instruction : WHILE '(' condition ')' instruction'''
    p[0] = While(p[3], p[5])
    p[0].line = zad1_scanner.lexer.lineno

def p_instruction_comlex(p):
    '''instruction : '{' instructions '}' '''
    p[0] = p[2]

def p_statement_print_one(p):
    '''statement : PRINT expression'''
    p[0] = Print([p[2]])
    p[0].line = zad1_scanner.lexer.lineno

def p_statement_print_more(p):
    '''statement : PRINT multiple_expressions'''
    p[0] = Print(p[2])
    p[0].line = zad1_scanner.lexer.lineno

def p_statement_return(p):
    '''statement : RETURN expression
                 | RETURN'''
    if len(p) == 3:
        p[0] = Return(p[2])
    elif len(p) == 2:
        p[0] = Return()
    p[0].line = zad1_scanner.lexer.lineno

def p_statement_continue(p):
    '''statement : CONTINUE'''
    p[0] = Continue()
    p[0].line = zad1_scanner.lexer.lineno

def p_statement_break(p):
    '''statement : BREAK'''
    p[0] = Break()
    p[0].line = zad1_scanner.lexer.lineno

def p_statement_assign(p):
    '''statement : assignable ASSIGN expression'''
    p[0] = Assignment(p[1], p[3])
    p[0].line = zad1_scanner.lexer.lineno

def p_statement_assign_and_expr(p):
    '''statement : assignable ADDASSIGN expression
                 | assignable SUBASSIGN expression
                 | assignable MULASSIGN expression
                 | assignable DIVASSIGN expression'''
    p[0] = AssignmentAndExpr(p[2], p[1], p[3])
    p[0].line = zad1_scanner.lexer.lineno

def p_condtion(p):
    '''condition : expression EQ expression
                 | expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression NE expression'''
    p[0] = Condition(p[2], p[1], p[3])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_binary_simple(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MUL expression
                  | expression DIV expression'''
    p[0] = BinExpr(p[2], p[1], p[3])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_binary_dot(p):
    '''expression : expression DOTADD expression
                  | expression DOTSUB expression
                  | expression DOTMUL expression
                  | expression DOTDIV expression'''
    p[0] = BinExpr(p[2], p[1], p[3])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_negation(p):
    '''expression : SUB expression %prec NEGATION'''
    p[0] = UnaryExpr('NEGATE', p[2])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_transposition(p):
    '''expression : expression TRANSPOSE '''
    p[0] = UnaryExpr('TRANSPOSE', p[1])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_int_numver(p):
    '''expression : INTNUM'''
    p[0] = IntNum(p[1])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_float_numver(p):
    '''expression : FLOATNUM'''
    p[0] = FloatNum(p[1])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_assignable(p):
    '''expression : assignable'''
    p[0] = p[1]

def p_assiganble(p):
    '''assignable : variable
                  | reference'''
    p[0] = p[1]

def p_reference_one(p):
    '''reference : variable '[' expression ']' '''
    p[0] = Reference(p[1], [p[3]])
    p[0].line = zad1_scanner.lexer.lineno

def p_reference_more(p):
    '''reference : variable '[' multiple_expressions ']' '''
    p[0] = Reference(p[1], p[3])
    p[0].line = zad1_scanner.lexer.lineno

def p_variable(p):
    '''variable : ID'''
    p[0] = Variable(p[1])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = String(p[1])
    p[0].line = zad1_scanner.lexer.lineno

def p_expression_paren(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]

def p_expression_vector(p):
    '''expression : vector'''
    p[0] = p[1]

def p_expression_matrix(p):
    '''expression : matrix'''
    p[0] = p[1]

def p_matrix_ones(p):
    '''matrix : ONES '(' expression ')'
              | ONES '(' expression ',' expression ')' '''
    if len(p) == 5:
        p[0] = Ones(p[3])
    elif len(p) == 7:
        p[0] = Ones(p[3], p[5])
    p[0].line = zad1_scanner.lexer.lineno

def p_matrix_zeros(p):
    '''matrix : ZEROS '(' expression ')'
              | ZEROS '(' expression ',' expression ')' '''
    if len(p) == 5:
        p[0] = Zeros(p[3])
    elif len(p) == 7:
        p[0] = Zeros(p[3], p[5])
    p[0].line = zad1_scanner.lexer.lineno

def p_matrix_eye(p):
    '''matrix : EYE '(' expression ')'
              | EYE '(' expression ',' expression ')' '''
    if len(p) == 5:
        p[0] = Eye(p[3])
    elif len(p) == 7:
        p[0] = Eye(p[3], p[5])
    p[0].line = zad1_scanner.lexer.lineno

def p_vector_one(p):
    '''vector : '[' expression ']' '''
    p[0] = Vector([p[2]])
    p[0].line = zad1_scanner.lexer.lineno

def p_vector_more(p):
    '''vector : '[' multiple_expressions ']' '''
    p[0] = Vector(p[2])
    p[0].line = zad1_scanner.lexer.lineno

def p_multiple_expressions_two(p):
    '''multiple_expressions : expression ',' expression'''
    p[0] = [p[1], p[3]]

def p_multiple_expressions_more(p):
    '''multiple_expressions : multiple_expressions ',' expression'''
    p[0] = p[1] + [p[3]]


parser = yacc.yacc()
