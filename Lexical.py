import re

###TOKENS###
# Reserved Words#
toklist = [
    '!',
    '!=',
    '+',
    '++',
    '+=',
    '-',
    '--',
    '-=',
    '*',
    '*=',
    '/',
    '/=',
    '&&',
    '##',
    '>',
    '>=',
    '<',
    '<=',
    '=',
    '==',
    ';',
    ',',
    ')',
    '(',
    ']',
    '[',
    '}',
    '{',
    '%',
    '%=',
    '&',
    '#',
    '~',
    '.',
    '\'',
    '\"'
]
t_blank = 'blank'
t_break = 'break'
t_check = 'check'
t_continue = 'continue'
t_decimal = 'decimal'
t_deck = 'deck'
t_do = 'do'
t_else = 'else'
t_elsif = 'elsif'
t_false = 'false'
t_for = 'for'
t_if = 'if'
t_locked = 'locked'
t_num = 'num'
t_option = 'option'
t_piece = 'piece'
t_return = 'return'
t_set = 'set'
t_TABLE = 'TABLE'
t_tell = 'tell'
t_true = 'true'
t_void = 'void'
t_while = 'while'

# Reserved Symbols#
t_not = '!'
t_noteq = '!='
t_plus = '+'
t_plusplus = '++'
t_pluseq = '+='
t_minus = '-'
t_minusminus = '--'
t_minuseq = '-='
t_mult = '*'
t_multeq = '*='
t_div = '/'
t_diveq = '/='
t_and = '&&'
t_or = '##'
t_gthan = '>'
t_gthaneq = '>='
t_lthan = '<'
t_lthaneq = '<='
t_eq = '='
t_eqeq = '=='
t_semicolon = ';'
t_comma = ','
t_cparen = ')'
t_oparen = '('
t_cbrack = ']'
t_obrack = '['
t_cbrace = '}'
t_obrace = '{'
t_modulo = '%'
t_moduloeq = '%='

andhalf = r'\&'
orhalf = r'\#'
negsym = r'\~'
period = r'\.'

# literals
t_comments = r'\|.*'
t_piecelit1 = r'\'([^\^])+\''
t_piecelit2 = r'\'(\^n|\^t|\^\^|\^0\|\^\'|\^\")\''
t_setlit = r'\"([^\^\"\n\t]|\^n|\^t|\^\^|\^0|\^\'|\^\")+\"'
t_numlit = r'~?[0-9]'
t_decimallit = r'~?[0-9]+\.[0-9]+'
t_identifierfirst = r'[a-z]'
t_identifierlast = r'[a-z0-9_]+'
t_idenchecker = r'[a-zA-Z0-9_]'

# DELIMITERS
whitespace = r'[\ \n\t]'
bound1 = r'[\ \n\t\;]'
bound2 = r'[\ \n\t\(]'
bound3 = r'[\ \n\t\{]'
bound4 = r'[\ \n\t\,\;\)\&\#]'
bound5 = r'[\ \n\t\(a-z0-9\~]'
bound6 = r'[\ \n\t\;a-z\)0-9]'
bound7 = r'[\ \n\t\(a-z0-9\~\"\']'
bound8 = r'[\ \n\t\,\;\)\+\-\/\*\%\<\>\=\&\#\{]'
bound9 = r'[\ \n\t\(a-z0-9\~\"\'\!\)]'
bound10 = r'[\ \n\t\,\;\)\+\-\/\*\%\<\>\=\!\[\.\&\#]'
bound11 = r'[\ \n\ta-z0-9\~]'
bound12 = r'[\ \n\ta-z\}]'
bound13 = r'[\ \n\t\(a-z\}]'
bound14 = r'[\ \n\t\,\;\)\!\=\&\#]'
bound15 = r'[\ \n\t\,\;\)\+\-\/\*\%\<\>\=\&\#]'
bound16 = r'[\ \n\t\(a-z0-9\~\"\'\!]'
bound17 = r'[\ \n\t\(a-z0-9\~\"]'

bound_semi = r'[\ \n\t\(a-z0-9\~\"\'\!\§\+\-]'
bound_closebrace = r'[\ \n\ta-z\}\§]'
bound_num = r'[\ \n\t\,\;\)\+\-\/\*\<\>\=\&\#\]\%]'
bound_id = r'[\ \n\t\,\;\)\+\-\/\*\%\<\>\=\&\#\[\]\(\.\{\!]'
bound_set = r'[\ \n\t\,\;\)\!\=\&\#\+]'



def lexical_analyzer(code):
    i = 0
    code = code[:-1]
    code += '§'
    lexeme = ''
    line_pos = 1
    column_pos = 1
    lexres = ""
    lexerror = ""
    tokens = []
    lineno = []
    datatypez = []
    semantokens = []
    idencheck = []
    semanerror = []

    while i != len(code):
        if i != len(code) - 1:
            lexeme += code[i]

            # whitespace, tabs and newline
            if re.match(whitespace, lexeme):
                lexres += ("\nWhitespace")
                lexeme = ''
                if code[i] == '\n':
                    line_pos += 1
                    column_pos = 1

            # blank
            if lexeme == t_blank and re.match(bound1, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tblank\t\t\t" + lexeme)
                tokens.append(t_blank)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_blank and code[i+1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif lexeme == t_blank and re.match(bound1, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i+1]):
                    pass
                elif re.match(t_idenchecker, code[i+1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # break
            if lexeme == t_break and re.match(bound1, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tbreak\t\t\t" + lexeme)
                tokens.append(t_break)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_break and code[i+1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif lexeme == t_break and re.match(bound1, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''

            # check
            if lexeme == t_check and re.match(bound2, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tcheck\t\t\t" + lexeme)
                tokens.append(t_check)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_check and code[i+1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif lexeme == t_check and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # continue
            if lexeme == t_continue and re.match(bound1, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tcontinue\t\t\t" + lexeme)
                tokens.append(t_continue)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_continue and code[i+1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif lexeme == t_continue and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # decimal
            if lexeme == t_decimal and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tdecimal\t\t\t" + lexeme)
                tokens.append(t_decimal)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_decimal and code[i+1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif lexeme == t_decimal and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''

            # deck
            if lexeme == t_deck and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tdeck\t\t\t" + lexeme)
                tokens.append(t_deck)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_deck and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_deck and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # do
            if lexeme == t_do and re.match(bound3, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tdo\t\t\t" + lexeme)
                tokens.append(t_do)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_do and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_do and re.match(bound3, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # else
            if lexeme == t_else and re.match(bound3, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\telse\t\t\t" + lexeme)
                tokens.append(t_else)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_else and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_else and re.match(bound3, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # elsif
            if lexeme == t_elsif and re.match(bound2, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\telsif\t\t\t" + lexeme)
                tokens.append(t_elsif)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_elsif and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif lexeme == t_elsif and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # false
            if lexeme == t_false and re.match(bound4, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tfalse\t\t\t" + lexeme)
                tokens.append('optionlit')
                semantokens.append("false")
                datatypez.append('option')
                idencheck.append('no')
                lineno.append(line_pos)
                lexeme = ''
            elif lexeme == t_false and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_false and re.match(bound4, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # for
            if lexeme == t_for and re.match(bound2, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tfor\t\t\t" + lexeme)
                tokens.append(t_for)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_for and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_for and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # if
            if lexeme == t_if and re.match(bound2, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tif\t\t\t" + lexeme)
                tokens.append(t_if)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_if and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_if and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # locked
            if lexeme == t_locked and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tlocked\t\t\t" + lexeme)
                tokens.append(t_locked)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_locked and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_locked and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # num
            if lexeme == t_num and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tnum\t\t\t" + lexeme)
                tokens.append(t_num)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_num and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_num and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # option
            if lexeme == t_option and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\toption\t\t\t" + lexeme)
                tokens.append(t_option)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_option and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_option and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # piece
            if lexeme == t_piece and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tpiece\t\t\t" + lexeme)
                tokens.append(t_piece)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_piece and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_piece and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # return
            if lexeme == t_return and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\treturn\t\t\t" + lexeme)
                tokens.append(t_return)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_return and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_return and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # set
            if lexeme == t_set and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tset\t\t\t" + lexeme)
                tokens.append(t_set)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_set and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_set and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # TABLE
            #if lexeme == t_TABLE and re.match(bound2, code[i + 1]):
                #tokens.append(t_TABLE)
                #lineno.append(line_pos)
                #idencheck.append('no')
                #semantokens.append('')
                #datatypez.append('')
                #lexres += ("\n" + str(line_pos) + "\t\t\tTABLE\t\t\t" + lexeme)
                #lexeme = ''
            #elif lexeme == t_TABLE and code[i+1] == '§':
                #lexerror += (
                            #"LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                #lexeme = ''
                
            #elif lexeme == t_TABLE and re.match(bound2, code[i + 1]) is None:
                #if re.match(t_idenchecker, code[i + 1]):
                    #pass
                #elif re.match(t_idenchecker, code[i + 1]) is None:
                    #lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    #lexeme = ''

            if lexeme == 'T' and code[i + 1] == 'A' and code[i + 2] == 'B' and code[i + 3] == 'L' and code[i + 4] == 'E' and re.match(bound2, code[i + 5]):
                i += 4
                tokens.append(t_TABLE)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexres += ("\n" + str(line_pos) + "\t\t\tTABLE\t\t\t" + 'TABLE')
                lexeme = ''
            elif code[i] == 'T' and code[i + 1] == 'A' and code[i + 2] == 'B' and code[i + 3] == 'L' and code[i + 4] == 'E' and code[i+5] == '§':
                i += 4
                lexerror += (
                        "LEXICAL ERROR: On \'TABLE\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
            elif code[i] == 'T' and code[i + 1] == 'A' and code[i + 2] == 'B' and code[i + 3] == 'L' and code[i + 4] == 'E' and re.match(bound2, code[i + 5]) is None:
                i += 4
                if re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'TABLE\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''

            if len(lexeme) > 0:
                if lexeme[0].isupper():
                    lexerror += (
                        "LEXICAL ERROR: On \'" + lexeme + "\', at line " + str(line_pos) + "\n")
                    lexeme = ''

            # tell
            if lexeme == t_tell and re.match(bound2, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\ttell\t\t\t" + lexeme)
                tokens.append(t_tell)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_tell and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_tell and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # true
            if lexeme == t_true and re.match(bound4, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\ttrue\t\t\t" + lexeme)
                tokens.append('optionlit')
                semantokens.append('true')
                datatypez.append('option')
                idencheck.append('no')
                lineno.append(line_pos)
                lexeme = ''
            elif lexeme == t_true and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_true and re.match(bound4, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # void
            if lexeme == t_void and re.match(whitespace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tvoid\t\t\t" + lexeme)
                tokens.append(t_void)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_void and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_void and re.match(whitespace, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # while
            if lexeme == t_while and re.match(bound2, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\twhile\t\t\t" + lexeme)
                tokens.append(t_while)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_while and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_while and re.match(bound2, code[i + 1]) is None:
                if re.match(t_idenchecker, code[i + 1]):
                    pass
                elif re.match(t_idenchecker, code[i + 1]) is None:
                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                    lexeme = ''
                    

            # not
            if lexeme == t_not and re.match(bound2, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tnot\t\t\t" + lexeme)
                tokens.append(t_not)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_not and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_not and re.match(bound2, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # not equals
            if lexeme == t_noteq and re.match(bound7, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tnot equals\t\t\t" + lexeme)
                tokens.append(t_noteq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_noteq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_noteq and re.match(bound7, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # plus
            if lexeme == t_plus and re.match(bound17, code[i + 1]) and code[i + 1] != '+' and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tplus\t\t\t" + lexeme)
                tokens.append(t_plus)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_plus and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_plus and re.match(bound17, code[i + 1]) is None and code[i + 1] != '+' and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # plus plus
            if lexeme == t_plusplus and re.match(bound6, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tplus plus\t\t\t" + lexeme)
                tokens.append(t_plusplus)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_plusplus and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_plusplus and re.match(bound6, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # plus equal
            if lexeme == t_pluseq and re.match(bound5, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tplus equal\t\t\t" + lexeme)
                tokens.append(t_pluseq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_pluseq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_pluseq and re.match(bound5, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # minus
            if lexeme == t_minus and re.match(bound5, code[i + 1]) and code[i + 1] != '-' and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tminus\t\t\t" + lexeme)
                tokens.append(t_minus)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_minus and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_minus and re.match(bound5, code[i + 1]) is None and code[i + 1] != '-' and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # minus minus
            if lexeme == t_minusminus and re.match(bound6, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tminus minus\t\t" + lexeme)
                tokens.append(t_minusminus)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_minusminus and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_minusminus and re.match(bound6, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # minus equals
            if lexeme == t_minuseq and re.match(bound5, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tminus equals\t\t\t" + lexeme)
                tokens.append(t_minuseq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_minuseq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_minuseq and re.match(bound5, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # multiply
            if lexeme == t_mult and re.match(bound5, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tmultiply\t\t\t" + lexeme)
                tokens.append(t_mult)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_mult and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_mult and re.match(bound5, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # multiply equal
            if lexeme == t_multeq and re.match(bound5, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tmultiply equals\t\t\t" + lexeme)
                tokens.append(t_multeq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_multeq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_multeq and re.match(bound5, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # divide
            if lexeme == t_div and re.match(bound5, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tdivide\t\t\t" + lexeme)
                tokens.append(t_div)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_div and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_div and re.match(bound5, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # divide equal
            if lexeme == t_diveq and re.match(bound5, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tdevide equals\t\t\t" + lexeme)
                tokens.append(t_diveq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_diveq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_diveq and re.match(bound5, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # and
            if lexeme == t_and and re.match(bound16, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tand\t\t\t" + lexeme)
                tokens.append(t_and)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_and and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_and and re.match(bound16, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # or
            if lexeme == t_or and re.match(bound16, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tor\t\t\t" + lexeme)
                tokens.append(t_or)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_or and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_or and re.match(bound16, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # greaterthan
            if lexeme == t_gthan and re.match(bound5, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tgraterthan\t\t\t" + lexeme)
                tokens.append(t_gthan)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_gthan and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_gthan and re.match(bound5, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # greaterthan equal
            if lexeme == t_gthaneq and re.match(bound5, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tgreaterthan equal\t\t\t" + lexeme)
                tokens.append(t_gthaneq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_gthaneq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_gthaneq and re.match(bound5, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # lessthan
            if lexeme == t_lthan and re.match(bound5, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tlessthan\t\t\t" + lexeme)
                tokens.append(t_lthan)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_lthan and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_lthan and re.match(bound5, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # lessthan equal
            if lexeme == t_lthaneq and re.match(bound5, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tlessthan equal\t\t\t" + lexeme)
                tokens.append(t_lthaneq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_lthaneq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_lthaneq and re.match(bound5, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # equal
            if lexeme == t_eq and re.match(bound7, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tequal\t\t\t" + lexeme)
                tokens.append(t_eq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_eq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_eq and re.match(bound7, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # equal equal
            if lexeme == t_eqeq and re.match(bound7, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tequal equal\t\t\t" + lexeme)
                tokens.append(t_eqeq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_eqeq and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_eqeq and re.match(bound7, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # comma
            if lexeme == t_comma and re.match(bound7, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tcomma\t\t\t" + lexeme)
                tokens.append(t_comma)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_comma and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_comma and re.match(bound7, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # close perenthesis
            if lexeme == t_cparen and re.match(bound8, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tcparen\t\t\t" + lexeme)
                tokens.append(t_cparen)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_cparen and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_cparen and re.match(bound8, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # open perenthesis
            if lexeme == t_oparen and re.match(bound9, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\toparen\t\t\t" + lexeme)
                tokens.append(t_oparen)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_oparen and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_oparen and re.match(bound9, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # close brackets
            if lexeme == t_cbrack and re.match(bound10, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tcbrack\t\t\t" + lexeme)
                tokens.append(t_cbrack)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_cbrack and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_cbrack and re.match(bound10, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # open brackets
            if lexeme == t_obrack and re.match(bound11, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tobrack\t\t\t" + lexeme)
                tokens.append(t_obrack)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_obrack and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_obrack and re.match(bound11, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # close braces
            if lexeme == t_cbrace and re.match(bound_closebrace, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tcbrace\t\t\t" + lexeme)
                tokens.append(t_cbrace)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_cbrace and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_cbrace and re.match(bound_closebrace, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # open braces
            if lexeme == t_obrace and re.match(bound13, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tobrace\t\t\t" + lexeme)
                tokens.append(t_obrace)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_obrace and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_obrace and re.match(bound13, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # modulo
            if lexeme == t_modulo and re.match(bound5, code[i + 1]) and code[i + 1] != '=':
                lexres += ("\n" + str(line_pos) + "\t\t\tmodulo\t\t\t" + lexeme)
                tokens.append(t_modulo)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_modulo and code[i + 1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_modulo and re.match(bound5, code[i + 1]) is None and code[i + 1] != '=':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[
                    i + 1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # modulo equal
            if lexeme == t_moduloeq and re.match(bound7, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tmodulo equal\t\t\t" + lexeme)
                tokens.append(t_moduloeq)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_moduloeq and code[i + 1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif lexeme == t_moduloeq and re.match(bound7, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[
                    i + 1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # comments
            if re.match(t_comments, lexeme) and (code[i + 1] == '\n' or code[i + 1] == '§'):
                lexres += ("\n" + "Comment")
                lexeme = ''

            # if piecelit and setlit is empty error
            if lexeme == "\"\"":
                lexerror += ("LEXICAL ERROR: Empty Setlit on line " + str(line_pos) + "\n")
                lexeme = ''
                
            if lexeme == "\'\'":
                lexerror += ("LEXICAL ERROR: Empty Piecelit on line " + str(line_pos) + "\n")
                lexeme = ''
                

            # piece lit single characters
            if re.match(t_piecelit1, lexeme) and len(lexeme) > 3:
                lexerror += ("LEXICAL ERROR: Invalid Piecelit On \'" + lexeme + "\', at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif re.match(t_piecelit1, lexeme) and re.match(bound14, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tpiecelit\t\t\t" + lexeme)
                print(lexeme)
                tokens.append('piecelit')
                datatypez.append('piece')
                semantokens.append(lexeme)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_piecelit1 and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif re.match(t_piecelit1, lexeme) and re.match(bound14, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # piece lit escaped characters
            if re.match(t_piecelit2, lexeme) and len(lexeme) > 4:
                lexerror += ("LEXICAL ERROR: Invalid Piecelit On \'" + lexeme + "\', at line " + str(line_pos))
                
            elif (re.match(t_piecelit2, lexeme) or lexeme == '\'^\'\'') and re.match(bound14, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tpiecelit\t\t\t" + lexeme)
                tokens.append('piecelit')
                datatypez.append('piece')
                semantokens.append(lexeme)
                lineno.append(line_pos)
                idencheck.append('no')
                lexeme = ''
            elif lexeme == t_piecelit2 and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif re.match(t_piecelit2, lexeme) and re.match(bound14, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[
                    i + 1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # set lit
            if re.match(t_setlit, lexeme) and re.match(bound_set, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tsetlit\t\t\t" + lexeme)
                tokens.append('setlit')
                semantokens.append(lexeme)
                datatypez.append('set')
                lineno.append(line_pos)
                idencheck.append('no')
                lexeme = ''
            elif lexeme == t_setlit and code[i+1] == '§':
                lexerror += (
                            "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(line_pos) + "\n")
                lexeme = ''
                
            elif re.match(t_setlit, lexeme) and re.match(bound_set, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                lexeme = ''
                

            # num lit
            if i != len(code) - 1:
                if not lexeme.__contains__('.'):
                    if re.match(t_numlit, lexeme):
                        if lexeme[0] == '~':
                            if not code[i + 1].isdigit():
                                if len(lexeme) <= 11:
                                    if code[i + 1] == '§':
                                        lexerror += (
                                                    "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                                                line_pos) + "\n")
                                        lexeme = ''
                                        
                                    elif re.match(bound_num, code[i + 1]) is None and code[i+1] != '.':
                                        lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                                        lexeme = ''
                                        
                                    elif re.match(bound_num, code[i + 1]) and code[i+1] != '.':
                                        lexres += ("\n" + str(line_pos) + "\t\t\tnumlit\t\t\t" + lexeme)
                                        tokens.append('numlit')
                                        semantokens.append(lexeme)
                                        datatypez.append('num')
                                        idencheck.append('no')
                                        lineno.append(line_pos)
                                        lexeme = ''
                                elif len(lexeme) > 11 and code[i+1] != '.':
                                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + lexeme[11] + "' at line " + str(line_pos) + "\n")
                                    lexeme = ''
                                    
                        elif lexeme[0] != '~':
                            if code[i + 1].isdigit() == False:
                                if len(lexeme) <= 10:
                                    if code[i + 1] == '§':
                                        lexerror += (
                                                    "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                                                line_pos) + "\n")
                                        lexeme = ''
                                        
                                    elif re.match(bound_num, code[i + 1]) is None and code[i+1] != '.':
                                        lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(line_pos) + "\n")
                                        lexeme = ''
                                        
                                    elif re.match(bound_num, code[i + 1]) and code[i+1] != '.':
                                        lexres += ("\n" + str(line_pos) + "\t\t\tnumlit\t\t\t" + lexeme)
                                        tokens.append('numlit')
                                        semantokens.append(lexeme)
                                        datatypez.append('num')
                                        idencheck.append('no')
                                        lexeme = ''
                                elif len(lexeme) > 10 and code[i+1] != '.':
                                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + lexeme[10] + "' at line " + str(line_pos) + "\n")
                                    lexeme = ''
                                    

            # dec lit
            if i != len(code) - 1:
                if re.match(t_decimallit, lexeme):
                    if lexeme[0] == '~':
                        if not code[i + 1].isdigit():
                            a, b = lexeme.split('.')
                            if len(a) <= 11 and len(b) <= 10:
                                if code[i + 1] == '§':
                                    lexerror += (
                                                "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                                            line_pos) + "\n")
                                    lexeme = ''
                                    
                                elif re.match(bound15, code[i + 1]) is None:
                                    lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i + 1] + "' at line " + str(
                                        line_pos) + "\n")
                                    lexeme = ''
                                    
                                elif re.match(bound_num, code[i + 1]):
                                    lexres += ("\n" + str(line_pos) + "\t\t\tdeclit\t\t\t" + lexeme)
                                    tokens.append('decimallit')
                                    semantokens.append(lexeme)
                                    datatypez.append('decimal')
                                    idencheck.append('no')
                                    lineno.append(line_pos)
                                    lexeme = ''
                            elif len(a) > 11:
                                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + a[11] + "' at line " + str(
                                    line_pos) + "\n")
                                lexeme = ''
                                
                            elif len(b) > 10:
                                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + b[10] + "' at line " + str(
                                    line_pos) + "\n")
                                lexeme = ''
                                
                    elif lexeme[0] != '~':
                        if not code[i + 1].isdigit():
                            a, b = lexeme.split('.')
                            if len(a) <= 11 and len(b) <= 10:
                                if code[i + 1] == '§':
                                    lexerror += (
                                                "LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                                            line_pos) + "\n")
                                    lexeme = ''
                                elif re.match(bound15, code[i + 1]) is None:
                                    lexerror += ("\n" + "LEXICAL ERROR: Invalid Delimiter '" + code[i + 1] + "' at line " + str(
                                        line_pos) + "\n")
                                    lexeme = ''
                                    
                                elif re.match(bound_num, code[i + 1]):
                                    lexres += ("\n" + str(line_pos) + "\t\t\tdeclit\t\t\t" + lexeme)
                                    tokens.append('decimallit')
                                    semantokens.append(lexeme)
                                    datatypez.append('decimal')
                                    idencheck.append('no')
                                    lexeme = ''
                                    
                            elif len(a) > 11:
                                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + a[11] + "' at line " + str(
                                    line_pos) + "\n")
                                lexeme = ''
                                
                            elif len(b) > 10:
                                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + b[10] + "' at line " + str(
                                    line_pos) + "\n")
                                lexeme = ''
                                

            # identifiers
            if i != len(code) - 1 and len(lexeme) != 0:
                if re.match(t_identifierfirst, lexeme[0]):
                    if not re.match(t_identifierlast, code[i+1]):
                        if code[i + 1] == '§':
                            lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                                line_pos) + "\n")
                            lexeme = ''
                            
                        elif not re.match(bound_id, code[i + 1]):
                            lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i+1] + "' at line " + str(
                                line_pos) + "\n")
                            lexeme = ''
                            
                        elif any(x.isupper() for x in lexeme):
                            lexerror += ("LEXICAL ERROR: Invalid identifier \'" + lexeme + "\' at line " + str(line_pos) + "\n")
                            lexeme = ''
                            
                        elif len(lexeme) > 25:
                            lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + lexeme[25] + "' at line " + str(line_pos) + "\n")
                            lexeme = ''
                            
                        else:
                            lexres += ("\n" + str(line_pos) + "\t\t\tidentifier\t\t\t" + lexeme)
                            tokens.append('identifier')
                            semantokens.append(lexeme)
                            datatypez.append('')
                            idencheck.append('yes')
                            lineno.append(line_pos)
                            lexeme = ''

            # semi-colon
            if lexeme == t_semicolon and re.match(bound_semi, code[i + 1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tsemi-colon\t\t\t" + lexeme)
                tokens.append(t_semicolon)
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif lexeme == t_semicolon and re.match(bound_semi, code[i + 1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i + 1] + "' at line " + str(
                    line_pos) + "\n")
                lexeme = ''


            # others
            if re.match(andhalf, lexeme) and re.match(andhalf, code[i + 1]):
                pass
            elif re.match(andhalf, lexeme) and code[i + 1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                    line_pos) + "\n")
                lexeme = ''
                
            elif re.match(andhalf, lexeme) and re.match(andhalf, code[i+1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[
                    i + 1] + "' at line " + str(
                    line_pos) + "\n")
                lexeme = ''



            if re.match(orhalf, lexeme) and re.match(orhalf, code[i+1]):
                pass
            elif re.match(orhalf, lexeme) and code[i + 1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                    line_pos) + "\n")
                lexeme = ''

            elif re.match(orhalf, lexeme) and re.match(orhalf, code[i+1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[
                    i + 1] + "' at line " + str(
                    line_pos) + "\n")
                lexeme = ''


            if re.match(negsym, lexeme) and re.match(r'[0-9]', code[i+1]):
                pass
            elif re.match(negsym, lexeme) and code[i + 1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                    line_pos) + "\n")
                lexeme = ''

            elif re.match(negsym, lexeme) and re.match(r'[0-9.]', code[i+1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + code[i+1] + "\', Invalid Num Literal at line " + str(
                    line_pos) + "\n")
                lexeme = ''
                

            if re.match(period, lexeme) and re.match(r'[a-z]', code[i+1]):
                lexres += ("\n" + str(line_pos) + "\t\t\tperiod\t\t\t" + lexeme)
                tokens.append('.')
                lineno.append(line_pos)
                idencheck.append('no')
                semantokens.append('')
                datatypez.append('')
                lexeme = ''
            elif re.match(period, lexeme) and code[i + 1] == '§':
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Delimiter not found at line " + str(
                    line_pos) + "\n")
                lexeme = ''

            elif re.match(period, lexeme) and re.match(r'[a-z]', code[i+1]) is None:
                lexerror += ("LEXICAL ERROR: On \'" + lexeme + "\', Invalid Delimiter '" + code[i + 1] + "' at line " + str(
                    line_pos) + "\n")
                lexeme = ''

            if len(lexeme) != 0:
                if lexeme[0] not in toklist and re.match(r'[a-z0-9]', lexeme[0]) is None:
                    lexerror += ("LEXICAL ERROR: on '" + lexeme[0] + "', at line "+ str(line_pos) + "\n")
                    print(lexeme)
                    lexeme = ''

            column_pos += 1
            i += 1

        else:
            if len(lexeme) != 0 :
                if lexeme[0] == '\"' and '^\"' not in lexeme:
                    lexerror += ("LEXICAL ERROR: Setlit Missing \'\"\'\n")
                if lexeme[0] == '\'' and lexeme[1] != '^':
                    lexerror += ("LEXICAL ERROR: Piecelit Missing \'\'\'\n")
            if len(lexerror) == 0:
                lexerror += ("No Lexical Error\n")
                return lexres[1:], True, lexerror, tokens, lineno, datatypez, semantokens, idencheck
            else:
                return lexres[1:], False, lexerror, tokens, lineno, datatypez, semantokens, idencheck
