import ply.yacc as yacc

import lab1_scanner

tokens = lab1_scanner.tokens

precedence = (
   ('nonassoc', 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
   ('nonassoc', 'EQ', 'GT', 'LT', 'GE', 'LE', 'NE'),
   ('left', 'ADD', 'SUB', 'DOTADD', 'DOTSUB'),
   ('left', 'MUL', 'DIV', 'DOTMUL', 'DOTDIV'),
   ('right', 'NEGATION'),
   ('left', 'TRANSPOSE')
)

def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, scanner.find_tok_column(p), p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    '''program : instructions_opt'''
    p[0] = p[1]

def p_instructions_opt_some(p):
    '''instructions_opt : instructions'''
    p[0] = p[1]

def p_instructions_opt_none(p):
    '''instructions_opt : '''
    p[0] = []

def p_instructions_multiple(p):
    '''instructions : instructions instruction'''
    p[0] = p[1] + [p[2]] 

def p_instructions_single(p):
    '''instructions : instruction'''
    p[0] = [p[1]]

def p_instruction_statement(p):
    '''instruction : statement ';' '''
    p[0] = p[1]

def p_instruction_if(p):
    '''instruction : IF '(' condition ')' instruction ELSE instruction
                   | IF '(' condition ')' instruction'''
    if len(p) == 8:
        p[0] = ('IF', p[3], p[5], 'ELSE', p[7])
    elif len(p) == 6:
        p[0] = ('IF', p[3], p[5])

def p_instruction_for(p):
    '''instruction : FOR ID ASSIGN expression ':' expression instruction'''
    p[0] = ('FOR', p[2], p[4], p[6], p[7])

def p_instruction_while(p):
    '''instruction : WHILE '(' condition ')' instruction'''
    p[0] = ('WHILE', p[3], [5])

def p_instruction_comlex(p):
    '''instruction : '{' instructions '}' '''
    p[0] = p[2]

def p_statement_print(p):
    '''statement : PRINT expression'''
    p[0] = ('PRINT', p[2])

def p_statement_return(p):
    '''statement : RETURN expression
                 | RETURN'''

    if len(p) == 3:
        p[0] = ('RETURN', p[2])
    elif len(p) == 2:
        p[0] = ('RETURN', )

def p_statement_continue(p):
    '''statement : CONTINUE'''
    p[0] = ('CONTINUE', )

def p_statement_break(p):
    '''statement : BREAK'''
    p[0] = ('BREAK', )

def p_statement_assign(p):
    '''statement : variable ASSIGN expression
                 | variable ADDASSIGN expression
                 | variable SUBASSIGN expression
                 | variable MULASSIGN expression
                 | variable DIVASSIGN expression'''
    p[0] = (p[2], p[1], p[3])

def p_condtion(p):
    '''condition : expression EQ expression
                 | expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression NE expression'''
    p[0] = ('CONDITION', p[2], p[1], p[3])

def p_expression_binary_simple(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MUL expression
                  | expression DIV expression'''
    p[0] = ('BINOP', p[2], p[1], p[3])

def p_expression_binary_dot(p):
    '''expression : expression DOTADD expression
                  | expression DOTSUB expression
                  | expression DOTMUL expression
                  | expression DOTDIV expression'''
    p[0] = ('BINDOT', p[2], p[1], p[3])

def p_expression_negation(p):
    '''expression : SUB expression %prec NEGATION'''
    p[0] = ('-', p[1])

def p_expression_transposition(p):
    '''expression : expression TRANSPOSE '''
    p[0] = ('TRANSPOSE', p[1])

def p_expression_number(p):
    '''expression : INTNUM
              | FLOATNUM'''
    p[0] = ('NUMBER', p[1])

def p_expression_variable(p):
    '''expression : variable'''
    p[0] = p[1]

def p_variable(p):
    '''variable : ID
                | ID '[' expression ']' 
                | ID '[' expression ',' expression ']' '''
    if len(p) == 2:
        p[0] = ('VAR', p[1])
    elif len(p) == 5:
        p[0] = ('VAR', p[1], p[2])
    elif len(p) == 7:
        p[0] = ('VAR', p[1], p[2], p[3])

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('STRING', p[1])

def p_expression_matrix(p):
    '''expression : matrix'''
    p[0] = p[1]

def p_expression_vector(p):
    '''expression : vector'''
    p[0] = p[1]

def p_matrix_ones(p):
    '''matrix : ONES '(' expression ')'
              | ONES '(' expression ',' expression ')' '''
    if len(p) == 5:
        p[0] = ('ONES', p[3], p[3])
    elif len(p) == 7:
        p[0] = ('ONES', p[3], p[5])

def p_matrix_zeros(p):
    '''matrix : ZEROS '(' expression ')'
              | ZEROS '(' expression ',' expression ')' '''
    if len(p) == 5:
        p[0] = ('ZEROS', p[3], p[3])
    elif len(p) == 7:
        p[0] = ('ZEROS', p[3], p[5])

def p_matrix_EYE(p):
    '''matrix : EYE '(' expression ')'
              | EYE '(' expression ',' expression ')' '''
    if len(p) == 5:
        p[0] = ('EYE', p[3], p[3])
    elif len(p) == 7:
        p[0] = ('EYE', p[3], p[5])

def p_matrix_vectors(p):
    '''matrix : '[' ']'
              | '[' vector ']' 
              | '[' vectors ']' '''
    if 
    p[0] = ('MATRIX', p[2])

def p_vectors_two(p):
    '''vectors : vector ',' vector '''
    p[0] = [p[1], p[3]]

def p_vectors_more(p):
    '''vectors : vectors ',' vector '''
    p[0] = p[1] + [p[3]]

def p_vector(p):
    '''vector : '[' ']'
              | '[' element ']'
              | '[' elements ']' '''
    if len(p) == 4:
        p[0] = p[1][1] + [p[3]]
    elif len(p) == 2:
        p[0] = ('VECTOR', [p[1]])

def p_elements(p):
    '''elements : elements ',' element
                | element'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_element(p):
    '''element : expression'''
    p[0] = p[1]


# to finish the grammar
# ....


    


parser = yacc.yacc()
