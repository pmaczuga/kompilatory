
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocASSIGNADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassocEQGTLTGELENEleftADDSUBDOTADDDOTSUBleftMULDIVDOTMULDOTDIVrightNEGATIONleftTRANSPOSEADD ADDASSIGN ASSIGN BREAK COMMENT CONTINUE DIV DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GE GT ID IF INTNUM LE LT MUL MULASSIGN NE ONES PRINT RETURN STRING SUB SUBASSIGN TRANSPOSE WHILE ZEROSprogram : instructions_optinstructions_opt : instructionsinstructions_opt : instructions : instructions instructioninstructions : instructioninstruction : statement ';' instruction : IF '(' condition ')' instruction ELSE instruction\n                   | IF '(' condition ')' instructioninstruction : FOR ID ASSIGN expression ':' expression instructioninstruction : WHILE '(' condition ')' instructioninstruction : '{' instructions '}' statement : PRINT expressionstatement : RETURN expression\n                 | RETURNstatement : CONTINUEstatement : BREAKstatement : variable ASSIGN expression\n                 | variable ADDASSIGN expression\n                 | variable SUBASSIGN expression\n                 | variable MULASSIGN expression\n                 | variable DIVASSIGN expressioncondition : expression EQ expression\n                 | expression GT expression\n                 | expression LT expression\n                 | expression GE expression\n                 | expression LE expression\n                 | expression NE expressionexpression : expression ADD expression\n                  | expression SUB expression\n                  | expression MUL expression\n                  | expression DIV expressionexpression : expression DOTADD expression\n                  | expression DOTSUB expression\n                  | expression DOTMUL expression\n                  | expression DOTDIV expressionexpression : SUB expression %prec NEGATIONexpression : expression TRANSPOSE expression : INTNUM\n              | FLOATNUMexpression : variablevariable : ID\n                | ID '[' expression ']' \n                | ID '[' expression ',' expression ']' expression : STRINGexpression : matrixexpression : vectormatrix : ONES '(' expression ')'\n              | ONES '(' expression ',' expression ')' matrix : ZEROS '(' expression ')'\n              | ZEROS '(' expression ',' expression ')' matrix : EYE '(' expression ')'\n              | EYE '(' expression ',' expression ')' matrix : '[' vectors ']' vectors : vector ',' vector vectors : vectors ',' vector vector : '[' expression ']' vector : '[' expressions ']' expressions : expression ',' expressionexpressions : expressions ',' expression"
    
_lr_action_items = {'$end':([0,1,2,3,4,16,17,46,100,109,127,128,],[-3,0,-1,-2,-5,-4,-6,-11,-8,-10,-7,-9,]),'IF':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[6,6,-5,-41,6,-4,-6,6,-38,-39,-40,-44,-45,-46,-11,-37,-36,6,-42,6,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,6,6,-43,-7,-9,-48,-50,-52,]),'FOR':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[7,7,-5,-41,7,-4,-6,7,-38,-39,-40,-44,-45,-46,-11,-37,-36,7,-42,7,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,7,7,-43,-7,-9,-48,-50,-52,]),'WHILE':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[9,9,-5,-41,9,-4,-6,9,-38,-39,-40,-44,-45,-46,-11,-37,-36,9,-42,9,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,9,9,-43,-7,-9,-48,-50,-52,]),'{':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[10,10,-5,-41,10,-4,-6,10,-38,-39,-40,-44,-45,-46,-11,-37,-36,10,-42,10,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,10,10,-43,-7,-9,-48,-50,-52,]),'PRINT':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[11,11,-5,-41,11,-4,-6,11,-38,-39,-40,-44,-45,-46,-11,-37,-36,11,-42,11,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,11,11,-43,-7,-9,-48,-50,-52,]),'RETURN':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[12,12,-5,-41,12,-4,-6,12,-38,-39,-40,-44,-45,-46,-11,-37,-36,12,-42,12,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,12,12,-43,-7,-9,-48,-50,-52,]),'CONTINUE':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[13,13,-5,-41,13,-4,-6,13,-38,-39,-40,-44,-45,-46,-11,-37,-36,13,-42,13,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,13,13,-43,-7,-9,-48,-50,-52,]),'BREAK':([0,3,4,8,10,16,17,22,25,26,27,28,29,30,46,55,56,70,78,80,81,82,83,84,85,86,87,88,90,92,94,100,109,115,117,119,121,122,123,127,128,129,130,131,],[14,14,-5,-41,14,-4,-6,14,-38,-39,-40,-44,-45,-46,-11,-37,-36,14,-42,14,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-8,-10,-47,-49,-51,14,14,-43,-7,-9,-48,-50,-52,]),'ID':([0,3,4,7,8,10,11,12,16,17,18,20,21,22,24,25,26,27,28,29,30,31,36,37,38,39,40,43,46,47,48,49,50,51,52,53,54,55,56,57,62,63,64,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,90,92,93,94,95,100,107,109,111,115,116,117,118,119,120,121,122,123,127,128,129,130,131,],[8,8,-5,19,-41,8,8,8,-4,-6,8,8,8,8,8,-38,-39,-40,-44,-45,-46,8,8,8,8,8,8,8,-11,8,8,8,8,8,8,8,8,-37,-36,8,8,8,8,8,8,8,8,8,8,8,-42,8,8,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,8,-57,8,-8,8,-10,8,-47,8,-49,8,-51,8,8,8,-43,-7,-9,-48,-50,-52,]),'}':([4,16,17,22,46,100,109,127,128,],[-5,-4,-6,46,-11,-8,-10,-7,-9,]),';':([5,8,12,13,14,23,25,26,27,28,29,30,35,55,56,65,66,67,68,69,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[17,-41,-14,-15,-16,-12,-38,-39,-40,-44,-45,-46,-13,-37,-36,-17,-18,-19,-20,-21,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),'(':([6,9,32,33,34,],[18,21,62,63,64,]),'ASSIGN':([8,15,19,78,123,],[-41,36,43,-42,-43,]),'ADDASSIGN':([8,15,78,123,],[-41,37,-42,-43,]),'SUBASSIGN':([8,15,78,123,],[-41,38,-42,-43,]),'MULASSIGN':([8,15,78,123,],[-41,39,-42,-43,]),'DIVASSIGN':([8,15,78,123,],[-41,40,-42,-43,]),'ADD':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,47,-38,-39,-40,-44,-45,-46,47,47,47,-37,-36,47,-46,47,47,47,47,47,47,-42,-28,-29,-30,-31,-32,-33,-34,-35,-46,-53,-56,-57,47,47,47,47,47,47,47,47,47,47,47,47,-47,-49,-51,47,-43,47,47,47,-48,-50,-52,]),'SUB':([8,11,12,18,20,21,23,24,25,26,27,28,29,30,31,35,36,37,38,39,40,42,43,44,47,48,49,50,51,52,53,54,55,56,57,59,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,92,93,94,95,97,98,99,101,102,103,104,105,106,107,108,111,112,113,115,116,117,118,119,120,122,123,124,125,126,129,130,131,],[-41,24,24,24,24,24,48,24,-38,-39,-40,-44,-45,-46,24,48,24,24,24,24,24,48,24,48,24,24,24,24,24,24,24,24,-37,-36,24,48,-46,24,24,24,48,48,48,48,48,24,24,24,24,24,24,48,-42,24,-28,-29,-30,-31,-32,-33,-34,-35,-46,-53,-56,24,-57,24,48,48,48,48,48,48,48,48,48,24,48,24,48,48,-47,24,-49,24,-51,24,48,-43,48,48,48,-48,-50,-52,]),'MUL':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,49,-38,-39,-40,-44,-45,-46,49,49,49,-37,-36,49,-46,49,49,49,49,49,49,-42,49,49,-30,-31,49,49,-34,-35,-46,-53,-56,-57,49,49,49,49,49,49,49,49,49,49,49,49,-47,-49,-51,49,-43,49,49,49,-48,-50,-52,]),'DIV':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,50,-38,-39,-40,-44,-45,-46,50,50,50,-37,-36,50,-46,50,50,50,50,50,50,-42,50,50,-30,-31,50,50,-34,-35,-46,-53,-56,-57,50,50,50,50,50,50,50,50,50,50,50,50,-47,-49,-51,50,-43,50,50,50,-48,-50,-52,]),'DOTADD':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,51,-38,-39,-40,-44,-45,-46,51,51,51,-37,-36,51,-46,51,51,51,51,51,51,-42,-28,-29,-30,-31,-32,-33,-34,-35,-46,-53,-56,-57,51,51,51,51,51,51,51,51,51,51,51,51,-47,-49,-51,51,-43,51,51,51,-48,-50,-52,]),'DOTSUB':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,52,-38,-39,-40,-44,-45,-46,52,52,52,-37,-36,52,-46,52,52,52,52,52,52,-42,-28,-29,-30,-31,-32,-33,-34,-35,-46,-53,-56,-57,52,52,52,52,52,52,52,52,52,52,52,52,-47,-49,-51,52,-43,52,52,52,-48,-50,-52,]),'DOTMUL':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,53,-38,-39,-40,-44,-45,-46,53,53,53,-37,-36,53,-46,53,53,53,53,53,53,-42,53,53,-30,-31,53,53,-34,-35,-46,-53,-56,-57,53,53,53,53,53,53,53,53,53,53,53,53,-47,-49,-51,53,-43,53,53,53,-48,-50,-52,]),'DOTDIV':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,54,-38,-39,-40,-44,-45,-46,54,54,54,-37,-36,54,-46,54,54,54,54,54,54,-42,54,54,-30,-31,54,54,-34,-35,-46,-53,-56,-57,54,54,54,54,54,54,54,54,54,54,54,54,-47,-49,-51,54,-43,54,54,54,-48,-50,-52,]),'TRANSPOSE':([8,23,25,26,27,28,29,30,35,42,44,55,56,59,61,65,66,67,68,69,77,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,101,102,103,104,105,106,108,112,113,115,117,119,122,123,124,125,126,129,130,131,],[-41,55,-38,-39,-40,-44,-45,-46,55,55,55,-37,55,55,-46,55,55,55,55,55,55,-42,55,55,55,55,55,55,55,55,-46,-53,-56,-57,55,55,55,55,55,55,55,55,55,55,55,55,-47,-49,-51,55,-43,55,55,55,-48,-50,-52,]),'EQ':([8,25,26,27,28,29,30,42,55,56,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,71,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),'GT':([8,25,26,27,28,29,30,42,55,56,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,72,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),'LT':([8,25,26,27,28,29,30,42,55,56,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,73,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),'GE':([8,25,26,27,28,29,30,42,55,56,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,74,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),'LE':([8,25,26,27,28,29,30,42,55,56,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,75,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),'NE':([8,25,26,27,28,29,30,42,55,56,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,76,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),']':([8,25,26,27,28,29,30,44,55,56,58,59,60,61,78,81,82,83,84,85,86,87,88,89,90,92,94,108,110,112,113,114,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,78,-37,-36,90,92,94,-46,-42,-28,-29,-30,-31,-32,-33,-34,-35,-46,-53,-56,-57,123,-55,-58,-59,-54,-47,-49,-51,-43,-48,-50,-52,]),',':([8,25,26,27,28,29,30,44,55,56,58,59,60,61,78,81,82,83,84,85,86,87,88,89,90,92,94,97,98,99,110,112,113,114,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,79,-37,-36,91,93,95,96,-42,-28,-29,-30,-31,-32,-33,-34,-35,96,-53,-56,-57,116,118,120,-55,-58,-59,-54,-47,-49,-51,-43,-48,-50,-52,]),':':([8,25,26,27,28,29,30,55,56,77,78,81,82,83,84,85,86,87,88,90,92,94,115,117,119,123,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,-37,-36,107,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,-47,-49,-51,-43,-48,-50,-52,]),')':([8,25,26,27,28,29,30,41,45,55,56,78,81,82,83,84,85,86,87,88,90,92,94,97,98,99,101,102,103,104,105,106,115,117,119,123,124,125,126,129,130,131,],[-41,-38,-39,-40,-44,-45,-46,70,80,-37,-36,-42,-28,-29,-30,-31,-32,-33,-34,-35,-53,-56,-57,115,117,119,-22,-23,-24,-25,-26,-27,-47,-49,-51,-43,129,130,131,-48,-50,-52,]),'[':([8,11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,91,93,95,96,107,111,116,118,120,],[20,31,31,31,31,31,31,57,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,111,31,31,111,31,31,31,31,31,]),'INTNUM':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FLOATNUM':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'STRING':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'ONES':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'ZEROS':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'EYE':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'ELSE':([17,46,100,109,127,128,],[-6,-11,121,-10,-7,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,10,],[3,22,]),'instruction':([0,3,10,22,70,80,121,122,],[4,16,4,16,100,109,127,128,]),'statement':([0,3,10,22,70,80,121,122,],[5,5,5,5,5,5,5,5,]),'variable':([0,3,10,11,12,18,20,21,22,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,70,71,72,73,74,75,76,79,80,93,95,107,111,116,118,120,121,122,],[15,15,15,27,27,27,27,27,15,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,15,27,27,27,27,27,27,27,15,27,27,27,27,27,27,27,15,15,]),'expression':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[23,35,42,44,42,56,59,65,66,67,68,69,77,81,82,83,84,85,86,87,88,59,97,98,99,101,102,103,104,105,106,108,112,113,122,59,124,125,126,]),'matrix':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,93,95,107,111,116,118,120,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'vector':([11,12,18,20,21,24,31,36,37,38,39,40,43,47,48,49,50,51,52,53,54,57,62,63,64,71,72,73,74,75,76,79,91,93,95,96,107,111,116,118,120,],[30,30,30,30,30,30,61,30,30,30,30,30,30,30,30,30,30,30,30,30,30,89,30,30,30,30,30,30,30,30,30,30,110,30,30,114,30,30,30,30,30,]),'condition':([18,21,],[41,45,]),'vectors':([31,57,],[58,58,]),'expressions':([31,57,111,],[60,60,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','zad2_parser.py',24),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_some','zad2_parser.py',28),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_none','zad2_parser.py',32),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_multiple','zad2_parser.py',36),
  ('instructions -> instruction','instructions',1,'p_instructions_single','zad2_parser.py',40),
  ('instruction -> statement ;','instruction',2,'p_instruction_statement','zad2_parser.py',44),
  ('instruction -> IF ( condition ) instruction ELSE instruction','instruction',7,'p_instruction_if','zad2_parser.py',48),
  ('instruction -> IF ( condition ) instruction','instruction',5,'p_instruction_if','zad2_parser.py',49),
  ('instruction -> FOR ID ASSIGN expression : expression instruction','instruction',7,'p_instruction_for','zad2_parser.py',56),
  ('instruction -> WHILE ( condition ) instruction','instruction',5,'p_instruction_while','zad2_parser.py',60),
  ('instruction -> { instructions }','instruction',3,'p_instruction_comlex','zad2_parser.py',64),
  ('statement -> PRINT expression','statement',2,'p_statement_print','zad2_parser.py',68),
  ('statement -> RETURN expression','statement',2,'p_statement_return','zad2_parser.py',72),
  ('statement -> RETURN','statement',1,'p_statement_return','zad2_parser.py',73),
  ('statement -> CONTINUE','statement',1,'p_statement_continue','zad2_parser.py',81),
  ('statement -> BREAK','statement',1,'p_statement_break','zad2_parser.py',85),
  ('statement -> variable ASSIGN expression','statement',3,'p_statement_assign','zad2_parser.py',89),
  ('statement -> variable ADDASSIGN expression','statement',3,'p_statement_assign','zad2_parser.py',90),
  ('statement -> variable SUBASSIGN expression','statement',3,'p_statement_assign','zad2_parser.py',91),
  ('statement -> variable MULASSIGN expression','statement',3,'p_statement_assign','zad2_parser.py',92),
  ('statement -> variable DIVASSIGN expression','statement',3,'p_statement_assign','zad2_parser.py',93),
  ('condition -> expression EQ expression','condition',3,'p_condtion','zad2_parser.py',97),
  ('condition -> expression GT expression','condition',3,'p_condtion','zad2_parser.py',98),
  ('condition -> expression LT expression','condition',3,'p_condtion','zad2_parser.py',99),
  ('condition -> expression GE expression','condition',3,'p_condtion','zad2_parser.py',100),
  ('condition -> expression LE expression','condition',3,'p_condtion','zad2_parser.py',101),
  ('condition -> expression NE expression','condition',3,'p_condtion','zad2_parser.py',102),
  ('expression -> expression ADD expression','expression',3,'p_expression_binary_simple','zad2_parser.py',106),
  ('expression -> expression SUB expression','expression',3,'p_expression_binary_simple','zad2_parser.py',107),
  ('expression -> expression MUL expression','expression',3,'p_expression_binary_simple','zad2_parser.py',108),
  ('expression -> expression DIV expression','expression',3,'p_expression_binary_simple','zad2_parser.py',109),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_binary_dot','zad2_parser.py',113),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_binary_dot','zad2_parser.py',114),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_binary_dot','zad2_parser.py',115),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression_binary_dot','zad2_parser.py',116),
  ('expression -> SUB expression','expression',2,'p_expression_negation','zad2_parser.py',120),
  ('expression -> expression TRANSPOSE','expression',2,'p_expression_transposition','zad2_parser.py',124),
  ('expression -> INTNUM','expression',1,'p_expression_number','zad2_parser.py',128),
  ('expression -> FLOATNUM','expression',1,'p_expression_number','zad2_parser.py',129),
  ('expression -> variable','expression',1,'p_expression_variable','zad2_parser.py',133),
  ('variable -> ID','variable',1,'p_variable','zad2_parser.py',137),
  ('variable -> ID [ expression ]','variable',4,'p_variable','zad2_parser.py',138),
  ('variable -> ID [ expression , expression ]','variable',6,'p_variable','zad2_parser.py',139),
  ('expression -> STRING','expression',1,'p_expression_string','zad2_parser.py',148),
  ('expression -> matrix','expression',1,'p_expression_matrix','zad2_parser.py',152),
  ('expression -> vector','expression',1,'p_expression_vector','zad2_parser.py',156),
  ('matrix -> ONES ( expression )','matrix',4,'p_matrix_ones','zad2_parser.py',160),
  ('matrix -> ONES ( expression , expression )','matrix',6,'p_matrix_ones','zad2_parser.py',161),
  ('matrix -> ZEROS ( expression )','matrix',4,'p_matrix_zeros','zad2_parser.py',168),
  ('matrix -> ZEROS ( expression , expression )','matrix',6,'p_matrix_zeros','zad2_parser.py',169),
  ('matrix -> EYE ( expression )','matrix',4,'p_matrix_EYE','zad2_parser.py',176),
  ('matrix -> EYE ( expression , expression )','matrix',6,'p_matrix_EYE','zad2_parser.py',177),
  ('matrix -> [ vectors ]','matrix',3,'p_matrix_vectors','zad2_parser.py',184),
  ('vectors -> vector , vector','vectors',3,'p_vectors_two','zad2_parser.py',188),
  ('vectors -> vectors , vector','vectors',3,'p_vectors_more','zad2_parser.py',192),
  ('vector -> [ expression ]','vector',3,'p_vecotor_one','zad2_parser.py',196),
  ('vector -> [ expressions ]','vector',3,'p_vector_more','zad2_parser.py',200),
  ('expressions -> expression , expression','expressions',3,'p_expressions_two','zad2_parser.py',204),
  ('expressions -> expressions , expression','expressions',3,'p_expressions_more','zad2_parser.py',208),
]
