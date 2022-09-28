i = 0
error = []
semanerror = []
temp = ''
funcsemancheck = False
funcseman = []
funcsemandatatype = []
paramsemancheck = False
paramseman = [[]]
paramsemandatatype = [[]]
paramdeccount = 0
statesemancheck = False
stateseman = [[]]
statesemandatatype = [[]]
returncheck = False
paramdeccountlist = [[]]
paramdeccounttemp = 0
funccallparam = False
funccalliden = ''
synerror = True
globaldec = False
globalseman = []
globalsemandatatype = []
funccalldatatypes = []

a = 0
x = 0
def SyntaxAnalyzer(tokens, lineno, semantokens, datatypez,idencheck):
    global error
    global i
    global temp
    global semanerror
    global funcsemancheck
    global funcseman
    global funcsemandatatype
    global paramsemancheck
    global paramseman
    global paramsemandatatype
    global paramdeccount
    global statesemancheck
    global stateseman
    global statesemandatatype
    global returncheck
    global a
    global paramdeccountlist
    global paramdeccounttemp
    global funccallparam
    global funccalliden
    global synerror
    global globaldec
    global globalseman
    global globalsemandatatype
    global funccalldatatypes

    linenoseman = lineno
    paramdeccountlist = [[]]
    semanerror = []
    error = []
    funcsemancheck = False
    funcseman = []
    funcsemandatatype = []
    paramsemancheck = False
    paramseman = [[]]
    paramsemandatatype = [[]]
    paramdeccount = 0
    statesemancheck = False
    stateseman = [[]]
    statesemandatatype = [[]]
    returncheck = False
    paramdeccounttemp = 0
    funccallparam = False
    funccalliden = ''
    synerror = True
    globaldec = False
    globalseman = []
    globalsemandatatype = []
    assignment = False
    funccalldatatypes = []
    i = 0
    x = 0
    a = 0
    temp = ''
    temp2 = ''
    
    def semantics():
        global i
        global temp
        global semanerror
        global funcsemancheck
        global funcseman
        global funcsemandatatype
        global paramsemancheck
        global paramseman
        global paramsemandatatype
        global paramdeccount
        global paramdeccountlist
        global statesemancheck
        global stateseman
        global statesemandatatype
        global returncheck
        global a
        global paramdeccounttemp
        global funccallparam
        global globaldec
        global globalseman
        global globalsemandatatype
        global temp2
        global assignment
        global funccalldatatypes
        if tokens[i] == 'num' or tokens[i] == 'decimal' or tokens[i] == 'piece' or tokens[i] == 'set' or tokens[i] == 'option' :
            temp = tokens[i]
        if tokens[i] == ';' or (tokens[i] == '}' and statesemancheck == True) or (tokens[i] == '(' and funcsemancheck == True) or ((tokens[i] == ')' or tokens[i] == ',') and paramsemancheck == True):
            temp = ''
        if temp != '' and idencheck[i] == 'yes':
            if semantokens[i] in semantokens[:i]:
                semanerror.append("\nSemantic Error: Identifier '" + semantokens[i] + "' already declared, line no. " + str(lineno[i]))
            elif ass_optr(tokens[i+1]) == True:
                temp2 = semantokens[i]
            else:
                datatypez[i] = temp
        #if assignment == True:
        #    pass
        if globaldec == True:
            if temp != '' and idencheck[i] == 'yes':
                globalseman.append(semantokens[i])
                globalsemandatatype.append(temp)
        if funcsemancheck == True:
            if temp != '' and idencheck[i] == 'yes':
                funcseman.append(semantokens[i])
                funcsemandatatype.append(temp)
            if tokens[i - 1] == 'void' and idencheck[i] == 'yes':
                funcseman.append(semantokens[i])
                funcsemandatatype.append('void')
        if paramsemancheck == True:
            if temp != '' and idencheck[i] == 'yes':
                paramseman[a].append(semantokens[i])
                paramsemandatatype[a].append(temp)
        if statesemancheck == True:
            if temp != '' and idencheck[i] == 'yes':
                stateseman[a].append(semantokens[i])
                statesemandatatype[a].append(temp)
            if temp == '' and idencheck[i] == 'yes' and returncheck == False:
                if semantokens[i] in stateseman[a]:
                    index = semantokens.index(semantokens[i])
                    datatypez[i] = datatypez[index]
                elif semantokens[i] in funcseman:
                    index = semantokens.index(semantokens[i])
                    datatypez[i] = datatypez[index]
                elif semantokens[i] in paramseman[a]:
                    index = semantokens.index(semantokens[i])
                    datatypez[i] = datatypez[index]
                elif semantokens[i] in globalseman:
                    index = semantokens.index(semantokens[i])
                    datatypez[i] = datatypez[index]
                else:
                    semanerror.append('\nSemantic Error: Identifier \'' + semantokens[i] + "' undeclared, line no. " + str(lineno[i]))
            if temp == '' and idencheck[i] == 'yes':
                if semantokens[i] not in funcseman:
                    if semantokens[i] not in paramseman[a]:
                        if semantokens[i] not in stateseman[a]:
                            if semantokens[i] not in globalseman:
                                semanerror.append(
                                    '\nSemantic Error: Identifier \'' + semantokens[i] + "' undeclared"
                                                                                         ", line no. " + str(lineno[i]))
        if temp == '' and idencheck[i] == 'yes' and returncheck == True:
            if semantokens[i] in paramseman[a]:
                indexparam = paramseman[a].index(semantokens[i])
                datatypez[i] = paramsemandatatype[a][indexparam]
                if datatypez[i] != funcsemandatatype[a]:
                    if datatypez[i] == 'num' and funcsemandatatype[a] == 'decimal':
                        pass
                    else:
                        semanerror.append(
                            '\nSemantic Error: Invalid Return, Datatype mismatch \'' + semantokens[i] + "' , line no. " + str(
                                lineno[i]))
            elif semantokens[i] in stateseman[a]:
                indexstates = stateseman[a].index(semantokens[i])
                datatypez[i] = statesemandatatype[a][indexstates]
                if datatypez[i] != funcsemandatatype[a]:
                    semanerror.append(
                        '\nSemantic Error: Invalid Return, Datatype mismatch \'' + semantokens[
                            i] + "' , line no. " + str(
                            lineno[i]))
            elif semantokens[i] in globalseman:
                indexglobal = globalseman.index(semantokens[i])
                datatypez[i] = globalsemandatatype[indexglobal]
                if datatypez[i] != funcsemandatatype[a]:
                    semanerror.append('\nSemantic Error: Invalid Return, Datatype mismatch \'' + semantokens[
                            i] + "' , line no. " + str(
                            lineno[i]))
            else:
                semanerror.append(
                    '\nSemantic Error: Identifier \'' + semantokens[i] + "' undeclared, line no. " + str(lineno[i]))
        if funccallparam == True:
            if funccalliden in funcseman:
                index = funcseman.index(funccalliden)
                x = paramdeccountlist[index][0]
                if paramdeccounttemp != x:
                    semanerror.append("\nSemantic Error: function '" + funccalliden + "' invalid parameter count, line no. " + str(linenoseman[i]))
                if paramsemandatatype[index] != funccalldatatypes:
                    semanerror.append("\nSemantic Error: function '" + funccalliden + "' invalid parameter datatypes, line no. " + str(linenoseman[i]))
                elif paramsemandatatype[index] == funccalldatatypes:
                    funccalldatatypes = []

    while x != 500:
        tokens.append('')
        lineno.append('')
        x += 1

    def datatype(token):
        if token == 'num' or token == 'decimal' or token == 'piece' or token == 'set' or token == 'option':
            return True
        else:
            return False

    def literals(token):
        if token == 'numlit' or token == 'decimallit' or token == 'piecelit' or token == 'setlit' or token == 'optionlit':
            return True
        else:
            return False

    def math_optr(token):
        if token == '+' or token == '-' or token == '*' or token == '/' or token == '%':
            return True
        else:
            return False

    def arr_lit(token):
        if token == 'numlit' or token == 'decimallit' or token == 'piecelit' or token == 'setlit':
            return True
        else:
            return False

    def incdec_optr(token):
        if token == '++' or token == '--':
            return True
        else:
            return False

    def incdec_rearchecker(token):
        if incdec_optr(token) == True:
            return True
        else:
            return False
    def incdec_rear(tokens):
        global i
        global error
        if incdec_optr(tokens[i]) == True:
            return None

    def ass_optr(token):
        if token == '=' or token == '+=' or token == '-=' or token == '*=' or token == '/=' or token == '%=':
            return True
        else:
            return False

    def not1(token):
        if token == '!':
            return True
        else:
            return False

    def logoptr(token):
        if token == '&&' or token == '##':
            return True
        else:
            return False

    def reloptr(token):
        if token == '==' or token == '!=' or token == '>' or token == '<' or token == '>=' or token == '<=':
            return True
        else:
            return False

    def digit_rtnchecker(token):
        if token == 'numlit' or token == 'decimallit' or token == 'identifier':
            return True
        else:
            return False
    def digit_rtn(tokens):
        global i
        global error
        if tokens[i] == 'numlit' or tokens[i] == 'decimallit':
            if incdec_rearchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                incdec_rear(tokens)
        elif tokens[i] == 'identifier':
            return None

    def program(tokens):
        global semanerror
        global funcsemancheck
        global funcseman
        global funcsemandatatype
        global paramsemancheck
        global paramseman
        global paramsemandatatype
        global paramdeccount
        global statesemancheck
        global stateseman
        global statesemandatatype
        global a
        global i
        global error
        global paramdeccountlist
        global synerror
        if globalzchecker(tokens[i]) == True:
            value = globalz(tokens)
            if tokens[i + 1] == 'TABLE':
                i += 1
                funcsemancheck = True
                semantics()
                if tokens[i + 1] == '(':
                    i += 1
                    paramsemancheck = True
                    semantics()
                    funcsemancheck = False
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        paramsemancheck = False
                        paramdeccountlist[a].append(paramdeccount)
                        paramdeccountlist.append([])
                        paramdeccount = 0
                        paramseman.append([])
                        paramsemandatatype.append([])
                        if tokens[i + 1] == '{':
                            i += 1
                            statesemancheck = True
                            semantics()
                            if statementschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = statements(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    statesemancheck = False
                                    a += 1
                                    stateseman.append([])
                                    statesemandatatype.append([])
                                    error.append("No Syntax Error")
                                    synerror = False
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                            lineno[i]))
                            elif tokens[i + 1] == '}':
                                i += 1
                                semantics()
                                statesemancheck = False
                                a += 1
                                stateseman.append([])
                                statesemandatatype.append([])
                                error.append("No Syntax Error")
                                synerror = False
                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                        lineno[i]))
                        else:
                            error.append(
                                "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected '{', Line no." + str(
                                    lineno[i]))
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'TABLE,locked,datatype,deck,void', Line no."
                             + str(lineno[i]))

        elif tokens[i] == 'TABLE':
            funcsemancheck = True
            if tokens[i + 1] == '(':
                i += 1
                paramsemancheck = True
                semantics()
                funcsemancheck = False
                if tokens[i + 1] == ')':
                    i += 1
                    semantics()
                    paramsemancheck = False
                    paramdeccountlist[a].append(paramdeccount)
                    paramdeccountlist.append([])
                    paramdeccount = 0
                    paramseman.append([])
                    paramsemandatatype.append([])
                    if tokens[i + 1] == '{':
                        i += 1
                        statesemancheck= True
                        semantics()
                        if statementschecker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = statements(tokens)
                            if tokens[i + 1] == '}':
                                i += 1
                                semantics()
                                statesemancheck = False
                                stateseman.append([])
                                statesemandatatype.append([])
                                a += 1
                                error.append("No Syntax Error")
                                synerror = False
                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected '}, num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank', Line no." + str(
                                        lineno[i]))

                        elif tokens[i + 1] == '}':
                            i += 1
                            semantics()
                            statesemancheck = False
                            stateseman.append([])
                            statesemandatatype.append([])
                            a += 1
                            error.append("No Syntax Error")
                            synerror = False
                        else:
                            error.append(
                                "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                    lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

        else:
            error.append("SYNTAX ERROR: Error on start of program, \nExpected 'TABLE, locked, num, decimal, set, piece, option, deck, void', Line no."
                         + str(lineno[i]))

    def globalzchecker(token):
        if const_decchekcer(token) == True or data_idchecker(token) == True or deck_decchecker(token) == True or voidchecker(token) == True:
            return True
        else:
            return False

    def globalz(tokens):
        global i
        global error
        if const_decchekcer(tokens[i]) == True:
            value = const_dec(tokens)
            if globalzchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = globalz(tokens)
        elif data_idchecker(tokens[i]) == True:
            semantics()
            value = data_id(tokens)
            if globalzchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = globalz(tokens)
        elif deck_decchecker(tokens[i]) == True:
            value = deck_dec(tokens)
            if globalzchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = globalz(tokens)
        elif voidchecker(tokens[i]):
            value = void(tokens)
            if globalzchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = globalz(tokens)

    def voidchecker(token):
        if token == 'void':
            return True
        else:
            return False

    def void(tokens):
        global semanerror
        global funcsemancheck
        global funcseman
        global funcsemandatatype
        global paramsemancheck
        global paramseman
        global paramsemandatatype
        global paramdeccount
        global statesemancheck
        global stateseman
        global statesemandatatype
        global a
        global i
        global error
        if tokens[i] == 'void':
            funcsemancheck = True
            if tokens[i+1] == 'identifier':
                i += 1
                semantics()
                if tokens[i+1] == '(':
                    i += 1
                    paramsemancheck = True
                    semantics()
                    funcsemancheck = False
                    if paramchecker(tokens[i+1]) == True:
                        i += 1
                        semantics()
                        value = param(tokens)
                        if tokens[i+1] == ')':
                            i += 1
                            semantics()
                            paramsemancheck = False
                            paramdeccountlist[a].append(paramdeccount)
                            paramdeccountlist.append([])
                            paramdeccount = 0
                            paramseman.append([])
                            paramsemandatatype.append([])
                            if tokens[i+1] == '{':
                                i += 1
                                statesemancheck = True
                                semantics()
                                if statementschecker(tokens[i+1]) == True:
                                    i += 1
                                    semantics()
                                    value = statements(tokens)
                                    if tokens[i + 1] == '}':
                                        i += 1
                                        semantics()
                                        statesemancheck = False
                                        a += 1
                                        stateseman.append([])
                                        statesemandatatype.append([])
                                    else:
                                        error.append(
                                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, 	blank, }', Line no." + str(lineno[i]))
                                elif tokens[i+1] == '}':
                                    i += 1
                                    semantics()
                                    statesemancheck = False
                                    a += 1
                                    stateseman.append([])
                                    statesemandatatype.append([])
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i+1] + "',\nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(lineno[i]))
                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))
                        else:
                            error.append(
                                "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))
                    elif tokens[i+1] == ')':
                        i += 1
                        semantics()
                        paramsemancheck = False
                        paramdeccountlist[a].append(paramdeccount)
                        paramdeccountlist.append([])
                        paramdeccount = 0
                        paramseman.append([])
                        paramsemandatatype.append([])
                        if tokens[i + 1] == '{':
                            i += 1
                            statesemancheck = True
                            semantics()
                            if statementschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = statements(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    statesemancheck = False
                                    a += 1
                                    stateseman.append([])
                                    statesemandatatype.append([])
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, 	blank, }', Line no." + str(lineno[i]))
                            elif tokens[i + 1] == '}':
                                i += 1
                                semantics()
                                statesemancheck = False
                                a += 1
                                stateseman.append([])
                                statesemandatatype.append([])
                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "',\nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                        lineno[i]))
                        else:
                            error.append(
                                "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected 'num, decimal, piece, set, option, )', Line no." + str(lineno[i]))
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))
            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))


    def const_decchekcer(token):
        if token == 'locked':
            return True
        else:
            return False

    def const_dec(tokens):
        global i
        global error
        global globaldec
        if tokens[i] == 'locked':
            if const_dec1checker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = const_dec1(tokens)
                if tokens[i + 1] == ';':
                    i += 1
                    semantics()
                    globaldec = False
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'num,decimal,piece,set,option', Line no." + str(lineno[i]))

    def const_dec1checker(token):
        if datatype(token) == True:
            return True
        else:
            return False

    def const_dec1(tokens):
        global i
        global error
        global globaldec
        globaldec = True
        if datatype(tokens[i]) == True:
            semantics()
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == '=':
                    i += 1
                    semantics()
                    if literals(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        if const_dec2checker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = const_dec2(tokens)
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected 'numlit,decimallit,piecelit,setlit,optionlit', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '=', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def const_dec2checker(token):
        if token == ',':
            return True
        else:
            return False

    def const_dec2(tokens):
        global i
        global error
        if tokens[i] == ',':
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == '=':
                    i += 1
                    semantics()
                    if literals(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        if const_dec2checker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = const_dec2(tokens)
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected 'numlit,decimallit,piecelit,setlit,optionlit', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '=', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def data_idchecker(token):
        if datatype(token) == True:
            return True
        else:
            return False

    def data_id(tokens):
        global i
        global error
        global funcsemancheck
        global globaldec
        if datatype(tokens[i]) == True:
            globaldec = True
            semantics()
            funcsemancheck = True
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if data_contchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = data_cont(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '(,=,[', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def data_contchecker(token):
        if data_altrchecker(token) == True or token == '(' or token ==';' or id_addchecker(token) == True:
            return True
        else:
            return False

    def data_cont(tokens):
        global i
        global semanerror
        global funcsemancheck
        global funcseman
        global funcsemandatatype
        global paramsemancheck
        global paramseman
        global paramsemandatatype
        global paramdeccount
        global statesemancheck
        global stateseman
        global statesemandatatype
        global returncheck
        global a
        global globaldec
        if data_altrchecker(tokens[i]) == True:
            semantics()
            funcsemancheck = False
            del funcseman[a]
            del funcsemandatatype[a]
            value = data_altr(tokens)
            if id_addchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = id_add(tokens)
                if tokens[i+1] == ';':
                    i += 1
                    semantics()
                    globaldec = False
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '[, ,, ;', Line no." + str(lineno[i]))
            elif tokens[i+1] == ';':
                    i += 1
                    semantics()
                    globaldec = False
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '[, ,, ;', Line no." + str(lineno[i]))
        elif tokens[i] == '(':
            globaldec = False
            index = len(globalseman)-1
            del globalseman[index]
            del globalsemandatatype[index]
            semantics()
            if paramchecker(tokens[i+1]) == True:
                i += 1
                paramsemancheck = True
                semantics()
                funcsemancheck = False
                value = param(tokens)
                if tokens[i+1] == ')':
                    i += 1
                    semantics()
                    paramsemancheck = False
                    paramdeccountlist[a].append(paramdeccount)
                    paramdeccountlist.append([])
                    paramdeccount = 0
                    paramseman.append([])
                    paramsemandatatype.append([])
                    if tokens[i+1] == '{':
                        i += 1
                        statesemancheck = True
                        semantics()
                        if func_stmtchecker(tokens[i+1]) == True:
                            i += 1
                            semantics()
                            value = func_stmt(tokens)
                            if return1checker(tokens[i+1]) == True:
                                i += 1
                                returncheck = True
                                semantics()
                                value = return1(tokens)
                                returncheck = False
                                if tokens[i+1] == '}':
                                    i += 1
                                    semantics()
                                    statesemancheck = False
                                    stateseman.append([])
                                    statesemandatatype.append([])
                                else:
                                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))
                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected 'return', Line no." + str(
                                    lineno[i]))
                        elif return1checker(tokens[i+1]) == True:
                            i += 1
                            returncheck = True
                            semantics()
                            value = return1(tokens)
                            returncheck = False
                            if tokens[i+1] == '}':
                                i += 1
                                semantics()
                                statesemancheck = False
                                a += 1
                                stateseman.append([])
                                statesemandatatype.append([])
                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, blank, return', Line no." + str(lineno[i]))
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ',, )', Line no." + str(lineno[i]))
            elif tokens[i+1] == ')':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'num,decimal,piece,set,option,)', Line no." + str(lineno[i]))
        elif tokens[i] == ';':
            semantics()
            funcsemancheck = False
            del funcseman[a]
            del funcsemandatatype[a]
        elif id_addchecker(tokens[i]) == True:
            semantics()
            funcsemancheck = False
            del funcseman[a]
            del funcsemandatatype[a]
            value = id_add(tokens)
            if tokens[i + 1] == ';':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

    def data_altrchecker(token):
        if var_decchecker(token) == True:
            return True
        elif oned_arrchecker(token) == True:
            return True
        else:
            return False

    def data_altr(tokens):
        global i
        global error
        if var_decchecker(tokens[i]) == True:
            value = var_dec(tokens)
        elif oned_arrchecker(tokens[i]) == True:
            value = oned_arr(tokens)

    def id_addchecker(token):
        if token == ',':
            return True
        else:
            return False

    def id_add(tokens):
        global i
        global error
        if tokens[i] == ',':
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if data_altrchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = data_altr(tokens)
                    if id_addchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = id_add(tokens)
                elif id_addchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = id_add(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def var_decchecker(token):
        if token == '=':
            return True
        else:
            return False

    def var_dec(tokens):
        global i
        global error
        if tokens[i] == '=':
            if literals(tokens[i + 1]) == True:
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,decimallit,piecelit,setlit,optionlit', Line no." + str(lineno[i]))

    def oned_arrchecker(token):
        if token == '[':
            return True
        else:
            return False

    def oned_arr(tokens):
        global i
        global error
        if tokens[i] == '[':
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
                if tokens[i + 1] == ']':
                    i += 1
                    semantics()
                    if twod_arrchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = twod_arr(tokens)
                    elif oned_arr_initchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = oned_arr_init(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ']', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,identifier', Line no." + str(lineno[i]))

    def array_altrchecker(token):
        if token == 'numlit' or token == 'identifier':
            return True
        else:
            return False

    def array_altr(tokens):
        global i
        global error
        if tokens[i] == 'numlit' or tokens[i] == 'identifier':
            if array_altr_exprchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr_expr(tokens)

    def twod_arrchecker(token):
        if token == '[' or oned_arr_initchecker(token) == True:
            return True
        else:
            return False

    def twod_arr(tokens):
        global i
        global error
        if oned_arr_initchecker(tokens[i]) == True:
            semantics()
            value = oned_arr_init(tokens)
        elif tokens[i] == '[':
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
                if tokens[i + 1] == ']':
                    i += 1
                    semantics()
                    if twod_arr_initchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = twod_arr_init(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ']', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, identifier', Line no." + str(lineno[i]))

    def oned_arr_initchecker(token):
        if token == '=':
            return True
        else:
            return False

    def oned_arr_init(tokens):
        global i
        global error
        if tokens[i] == '=':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if arr_elemchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = arr_elem(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'numlit,decimallit,piecelit,setlit', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def arr_elemchecker(token):
        if arr_lit(token) == True:
            return True
        else:
            return False

    def arr_elem(tokens):
        global i
        global error
        if arr_lit(tokens[i]) == True:
            if arr_elem1checker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = arr_elem1(tokens)

    def arr_elem1checker(token):
        if token == ',':
            return True
        else:
            return False


    def arr_elem1(tokens):
        global i
        global error
        if tokens[i] == ',':
            if arr_elemchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = arr_elem(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,decimallit,piecelit,setlit', Line no." + str(lineno[i]))

    def twod_arr_initchecker(token):
        if token == '=':
            return True
        else:
            return False

    def twod_arr_init(tokens):
        global i
        global error
        if tokens[i] == '=':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if twod_arr_init1checker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = twod_arr_init1(tokens)
                    if tokens[i+1] == ')':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ',, )', Line no." + str(lineno[i]))
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def twod_arr_init1checker(token):
        if token == '(':
            return True
        else:
            return False

    def twod_arr_init1(tokens):
        global i
        global error
        if tokens[i] == '(':
            if arr_elemchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = arr_elem(tokens)
                if tokens[i + 1] == ')':
                    i += 1
                    semantics()
                    if twod_arr_init2checker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = twod_arr_init2(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ',, )', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, piecelit, setlit', Line no." + str(lineno[i]))

    def twod_arr_init2checker(token):
        if token == ',':
            return True
        else:
            return False

    def twod_arr_init2(tokens):
        global i
        global error
        if tokens[i] == ',':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if arr_elemchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = arr_elem(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if twod_arr_init2checker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            twod_arr_init2(tokens)
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'numlit, decimallit, piecelit, setlit', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def size_arrchecker(token):
        if token == '[':
            return True
        else:
            return False

    def size_arr(tokens):
        global i
        global error
        if tokens[i] == '[':
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
                if tokens[i + 1] == ']':
                    i += 1
                    semantics()
                    if size_arr1checker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = size_arr1(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '], +, -, *, /, %', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,identifier', Line no." + str(lineno[i]))

    def size_arr1checker(token):
        if token == '[':
            return True
        else:
            return False

    def size_arr1(tokens):
        global i
        global error
        if tokens[i] == '[':
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
                if tokens[i + 1] == ']':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ']', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,identifier', Line no." + str(
                    lineno[i]))

    def deck_decchecker(token):
        if token == 'deck':
            return True
        else:
            return False

    def deck_dec(tokens):
        global i
        global error
        if tokens[i] == 'deck':
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == '{':
                    i += 1
                    semantics()
                    if deck_contchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = deck_cont(tokens)
                        if tokens[i + 1] == '}':
                            i += 1
                            semantics()
                            if deck_objchecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                deck_obj(tokens)
                                if tokens[i + 1] == ';':
                                    i += 1
                                    semantics()
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected ',, ;', Line no." + str(
                                            lineno[i]))

                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected 'identifier', Line no." + str(
                                    lineno[i]))

                        else:
                            error.append(
                                "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected 'num, decimal, piece, set, option', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def deck_contchecker(token):
        if datatype(token) == True:
            return True
        else:
            return False

    def deck_cont(tokens):
        global i
        global error
        if datatype(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if size_arrchecker(tokens[i + 1]):
                    i += 1
                    semantics()
                    value = size_arr(tokens)
                    if tokens[i + 1] == ';':
                        i += 1
                        semantics()
                        if deck_elemchecker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = deck_elem(tokens)
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

                elif tokens[i + 1] == ';':
                    i += 1
                    semantics()
                    if deck_elemchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = deck_elem(tokens)
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def deck_elemchecker(token):
        if deck_contchecker(token) == True:
            return True
        else:
            return False

    def deck_elem(tokens):
        global i
        global error
        if deck_contchecker(tokens[i]) == True:
            value = deck_cont(tokens)

    def deck_objchecker(token):
        if token == 'identifier':
            return True
        else:
            return False

    def deck_obj(tokens):
        global i
        global error
        if tokens[i] == 'identifier':
            if size_arrchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = size_arr(tokens)
                if deck_obj1checker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = deck_obj1(tokens)
            elif deck_obj1checker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = deck_obj1(tokens)

    def deck_obj1checker(token):
        if token == ',':
            return True
        else:
            return False

    def deck_obj1(tokens):
        global i
        global error
        if tokens[i] == ',':
            if deck_objchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = deck_obj(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def paramchecker(token):
        if datatype(token) == True:
            return True
        else:
            return False

    def param(tokens):
        global i
        global error
        global paramdeccount
        if datatype(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                paramdeccount += 1
                semantics()
                if param1checker(tokens[i + 1]):
                    i += 1
                    semantics()
                    value = param1(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def param1checker(token):
        if token == ',':
            return True
        else:
            return False

    def param1(tokens):
        global i
        global error
        global paramdeccount
        if tokens[i] == ',':
            if datatype(tokens[i + 1]) == True:
                i += 1
                semantics()
                if tokens[i + 1] == 'identifier':
                    i += 1
                    paramdeccount += 1
                    semantics()
                    if param1checker(tokens[i + 1]):
                        i += 1
                        semantics()
                        value = param1(tokens)
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'num, decimal, piece, set, option', Line no." + str(lineno[i]))

    def statementschecker(token):
        if funcchecker(token) == True:
            return True
        else:
            return False

    def statements(tokens):
        global i
        global error
        if funcchecker(tokens[i]) == True:
            value = func(tokens)
            if statementschecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = statements(tokens)

    def funcchecker(token):
        if datatype(token) == True or token == 'identifier' or incdec_optr(
                token) == True or io_stmtchecker(token) == True or if_stmtchecker(
            token) == True or loopingchecker(token) == True or token == 'blank':
            return True
        else:
            return False

    def func(tokens):
        global i
        global error
        if datatype(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if data_altrchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = data_altr(tokens)
                    if id_addchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = id_add(tokens)
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '=, [, ,, ;', Line no." + str(
                                lineno[i]))
                    elif tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected '=, [, ,, ; ', Line no." + str(
                            lineno[i]))

                elif id_addchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = id_add(tokens)
                    if tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected '=, [, ,, ; ', Line no." + str(
                            lineno[i]))

                elif tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '=, [, ,, ; ', Line no." + str(
                        lineno[i]))

            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

        elif tokens[i] == 'identifier':
            semantics()
            if id_next_funcchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = id_next_func(tokens)
                if tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '+, ;', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '++, --, .,  [,+, -, *, /, %,(', =, +=, -=, *=, /=, %= , Line no." + str(lineno[i]))

        elif incdec_optr(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." +
                             str(lineno[i]))

        elif io_stmtchecker(tokens[i]) == True:
            value = io_stmt(tokens)
        elif if_stmtchecker(tokens[i]) == True:
            value = if_stmt(tokens)
        elif loopingchecker(tokens[i]) == True:
            value = looping(tokens)
        elif tokens[i] == 'blank':
            if tokens[i+1] == ';':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

    def if_stmtchecker(token):
        if token == 'if':
            return True
        else:
            return False

    def if_stmt(tokens):
        global i
        global error
        if tokens[i] == 'if':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if statementschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = statements(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    if elsif_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = elsif_stmt(tokens)
                                        if else_stmtchecker(tokens[i + 1]) == True:
                                            i += 1
                                            semantics()
                                            value = else_stmt(tokens)
                                    elif else_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = else_stmt(tokens)
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "',\nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                            lineno[i]))
                            elif tokens[i + 1] == '}':
                                i += 1
                                semantics()
                                if elsif_stmtchecker(tokens[i + 1]) == True:
                                    i += 1
                                    semantics()
                                    value = elsif_stmt(tokens)
                                    if else_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = else_stmt(tokens)
                                elif else_stmtchecker(tokens[i + 1]) == True:
                                    i += 1
                                    semantics()
                                    value = else_stmt(tokens)
                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "',\nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                        lineno[i]))
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '+, -, *, /, %, ), ==, !=, >, <, >=, <=, &&, ##', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def elsif_stmtchecker(token):
        if token == 'elsif':
            return True
        else:
            return False

    def elsif_stmt(tokens):
        global i
        global error
        if tokens[i] == 'elsif':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if statementschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = statements(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    if elsif_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = elsif_stmt(tokens)
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected '}', Line no." + str(
                                            lineno[i]))

                            elif tokens[i + 1] == '}':
                                i += 1
                                semantics()
                                if elsif_stmtchecker(tokens[i + 1]) == True:
                                    i += 1
                                    semantics()
                                    value = elsif_stmt(tokens)
                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(
                                        lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def else_stmtchecker(token):
        if token == 'else':
            return True
        else:
            return False

    def else_stmt(tokens):
        global i
        global error
        if tokens[i] == 'else':
            if tokens[i + 1] == '{':
                i += 1
                semantics()
                if statementschecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = statements(tokens)
                    if tokens[i + 1] == '}':
                        i += 1
                        semantics()
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))
                elif tokens[i + 1] == '}':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'num, decimal, option, set, piece, identifier, ++, --, tell, check, if, for, do, while, blank, }', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

    def func_stmtchecker(token):
        if func2checker(token) == True:
            return True
        else:
            return False

    def func_stmt(tokens):
        global i
        global error

        if func2checker(tokens[i]) == True:
            value = func2(tokens)
            if func_stmtchecker(tokens[i + 1]):
                i += 1
                semantics()
                value = func_stmt(tokens)

    def func2checker(token):
        if datatype(token) == True or token == 'identifier' or incdec_optr(
                token) == True or io_stmtchecker(token) == True or func_if_stmtchecker(
            token) == True or loopingchecker(token) == True or token == 'blank':
            return True
        else:
            return False

    def func2(tokens):
        global i
        global error
        global funccalliden
        if datatype(tokens[i]) == True:
            if tokens[i+1] == 'identifier':
                i += 1
                semantics()
                if data_altrchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = data_altr(tokens)
                    if id_addchecker(tokens[i+1]) == True:
                        i += 1
                        semantics()
                        value = id_add(tokens)
                        if tokens[i+1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '=, ,, ;', Line no." + str(lineno[i]))
                    elif tokens[i+1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected '=, ,, ;', Line no." + str(lineno[i]))
                elif id_addchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = id_add(tokens)
                    if tokens[i+1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
                elif tokens[i+1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '=,[,,,;', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))
        elif tokens[i] == 'identifier':
            semantics()
            if id_next_funcchecker(tokens[i+1]) == True:
                i += 1
                value = id_next_func(tokens)
                if tokens[i+1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '++, --, .,  [,+, -, *, /, %,(', Line no." + str(lineno[i]))
        elif incdec_optr(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no." +
                             str(lineno[i]))
        elif io_stmtchecker(tokens[i]) == True:
            value = io_stmt(tokens)
        elif func_if_stmtchecker(tokens[i]) == True:
            value = func_if_stmt(tokens)
        elif loopingchecker(tokens[i]) == True:
            value = looping(tokens)
        elif tokens[i] == 'blank':
            if tokens[i+1] == ';':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

    def id_next_funcchecker(token):
        if id_nextchecker(token) == True or token == '(':
            return True
        else:
            return False

    def id_next_func(tokens):
        global i
        global error
        global funccallparam
        global paramdeccounttemp
        global funccalliden
        if id_nextchecker(tokens[i]) == True:
            value = id_next(tokens)
        elif tokens[i] == '(':
            funccalliden = semantokens[i-1]
            if funct_paramchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = funct_param(tokens)
                if tokens[i+1] == ')':
                    i += 1
                    funccallparam = True
                    semantics()
                    funccalliden = ''
                    paramdeccounttemp = 0
                    funccallparam = False
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '+, -, *, /, %, ,, ;, ),&&, ##, ==, !=, >, <, >=, <=', Line no." + str(lineno[i]))
            elif tokens[i+1] == ')':
                i += 1
                funccallparam = True
                semantics()
                funccalliden = ''
                paramdeccounttemp = 0
                funccallparam = False
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, piecelit, optionlit, setlit, identifier, )', Line no." + str(lineno[i]))

    def func_if_stmtchecker(token):
        if token == 'if':
            return True
        else:
            return False

    def func_if_stmt(tokens):
        global i
        global error
        if tokens[i] == 'if':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if func_stateschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = func_states(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    if func_elsif_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = func_elsif_stmt(tokens)
                                        if func_else_stmtchecker(tokens[i + 1]) == True:
                                            i += 1
                                            semantics()
                                            value = func_else_stmt(tokens)
                                    elif func_else_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = func_else_stmt(tokens)
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected '}', Line no." + str(
                                            lineno[i]))
                            elif tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    if func_elsif_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = func_elsif_stmt(tokens)
                                        if func_else_stmtchecker(tokens[i + 1]) == True:
                                            i += 1
                                            semantics()
                                            value = func_else_stmt(tokens)
                                    elif func_else_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = func_else_stmt(tokens)
                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "',\nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, return, for, while, do, blank, }', Line no." + str(
                                    lineno[i]))
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '&&, ##, ), ;', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no."
                        + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def func_elsif_stmtchecker(token):
        if token == 'elsif':
            return True
        else:
            return False

    def func_elsif_stmt(tokens):
        global i
        global error
        if tokens[i] == 'elsif':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if func_stateschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = func_states(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    if func_elsif_stmtchecker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = func_elsif_stmt(tokens)
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected '}', Line no." + str(
                                            lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'condition', Line no." + str(lineno[i]))

            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def func_else_stmtchecker(token):
        if token == 'else':
            return True
        else:
            return False

    def func_else_stmt(tokens):
        global i
        global error
        if tokens[i] == 'else':
            if tokens[i + 1] == '{':
                i += 1
                semantics()
                if func_stateschecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = func_states(tokens)
                    if tokens[i + 1] == '}':
                        i += 1
                        semantics()
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, return, for, do, while, blank', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

    def func_stateschecker(token):
        if func3checker(token) == True:
            return True
        else:
            return False

    def func_states(tokens):
        global i
        global error
        if func3checker(tokens[i]) == True:
            value = func3(tokens)
            if func_states_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = func_states_rear(tokens)

    def func3checker(token):
        if datatype(token) == True or token == 'identifier' or incdec_optr(token) == True or io_stmtchecker(
                token) == True or func_if_stmtchecker(token) == True or loopingchecker(
            token) == True or token == 'blank':
            return True
        else:
            return False

    def func3(tokens):
        global i
        global error
        if datatype(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if data_altrchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = data_altr(tokens)
                    if id_addchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        id_add(tokens)
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ';', Line no." + str(
                                lineno[i]))

                    elif tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(
                            lineno[i]))

                elif id_addchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    id_add(tokens)
                    if tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(
                            lineno[i]))

                elif tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ';', Line no." + str(
                        lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no."
                             + str(lineno[i]))

        elif tokens[i] == 'identifier':
            if id_next_funcchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = id_next_func(tokens)
                if tokens[i+1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '++, --, .,  [,+, -, *, /, %,(', Line no." + str(lineno[i]))

        elif incdec_optr(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no."
                             + str(lineno[i]))

        elif io_stmtchecker(tokens[i]) == True:
            value = io_stmt(tokens)
        elif func_if_stmtchecker(tokens[i]) == True:
            value = func_if_stmt(tokens)
        elif return1checker(tokens[i]) == True:
            value = return1(tokens)
        elif loopingchecker(tokens[i]) == True:
            value = looping(tokens)
        elif tokens[i] == 'blank':
            if tokens[i + 1] == ';':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

    def return_addchecker(token):
        if token == ',':
            return True
        else:
            return False
    def return_add(tokens):
        global i
        global error
        if tokens[i] == ',':
            if return_choiceschecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = return_choices(tokens)
                if return_addchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = return_add(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit ,setlit, optionlit, identifier', Line no." + str(lineno[i]))

    def return1checker(token):
        if token == 'return':
            return True
        else:
            return False

    def return1(tokens):
        global i
        global error
        if tokens[i] == 'return':
            if return_choiceschecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = return_choices(tokens)
                if return_addchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = return_add(tokens)
                    if tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ';, (, +, -, *, /, %', Line no." + str(lineno[i]))
                elif tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';, (, +, -, *, /, %', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, setlit, optionlit, identifier', Line no."
                             + str(lineno[i]))

    def return_choiceschecker(token):
        if token == 'numlit' or token == 'decimallit' or token == 'setlit' or token == 'optionlit' or token == 'identifier':
            return True
        else:
            return False

    def return_choices(tokens):
        global i
        global error
        if tokens[i] == 'numlit' or tokens[i] == 'decimallit':
            if digit_rear_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_rear_rtn(tokens)
        elif tokens[i] == 'setlit' or tokens[i] == 'optionlit':
            return None
        elif tokens[i] == 'identifier':
            if return_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = return_rear(tokens)
                if digit_rear_rtnchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = digit_rear_rtn(tokens)
            elif digit_rear_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_rear_rtn(tokens)

    def return_rearchecker(token):
        if token == '(':
            return True
        else:
            return False

    def return_rear(tokens):
        global i
        global error
        if tokens[i] == '(':
            if funct_param_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = funct_param_rtn(tokens)
                if tokens[i + 1] == ')':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

            if tokens[i + 1] == ')':
                i += 1
                semantics()
            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

    def funct_param_rtnchecker(token):
        if value_rtnchecker(token) == True:
            return True
        else:
            return False

    def funct_param_rtn(tokens):
        global i
        global error
        if value_rtnchecker(tokens[i]) == True:
            value = value_rtn(tokens)
            if digit_rear_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_rear_rtn(tokens)
                if func_param_rear_rtnchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = func_param_rear_rtn(tokens)
            elif func_param_rear_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = func_param_rear_rtn(tokens)

    def value_rtnchecker(token):
        if literals(token) == True or token == 'identifier':
            return True
        else:
            return False

    def value_rtn(tokens):
        global i
        global error
        if literals(tokens[i]) == True or tokens[i] == 'identifier':
            return None

    def func_param_rear_rtnchecker(token):
        if token == ',':
            return True
        else:
            return False

    def func_param_rear_rtn(tokens):
        global i
        global error
        if tokens[i] == ',':
            if funct_param_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = funct_param_rtn(tokens)

    def digit_rear_rtnchecker(token):
        if math_optr(token) == True:
            return True
        else:
            return False

    def digit_rear_rtn(tokens):
        global i
        global error
        if math_optr(tokens[i]) == True:
            if digit_opMath_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_opMath_rtn(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(,numlit, decimallit, identifier', Line no." + str(lineno[i]))

    def digit_opMath_rtnchecker(token):
        if digit1_rtnchecker(token) == True:
            return True
        else:
            return False

    def digit_opMath_rtn(tokens):
        global i
        global error
        if digit1_rtnchecker(tokens[i]) == True:
            value = digit1_rtn(tokens)
            if digit_rear_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_rear_rtn(tokens)

    def digit1_rtnchecker(token):
        if token == '(' or digit_rtnchecker(token) == True:
            return True
        else:
            return False

    def digit1_rtn(tokens):
        global i
        global error
        if tokens[i] == '(':
            if digit_rtnchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                digit_rtn(tokens)
                if digit_rear_rtnchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = digit_rear_rtn(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                elif tokens[i + 1] == ')':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, identifier', Line no." + str(lineno[i]))

        elif digit_rtnchecker(tokens[i]) == True:
            semantics()
            value = digit_rtn(tokens)

    def loopingchecker(token):
        if token == 'for' or token == 'while' or token == 'do':
            return True
        else:
            return False

    def looping(tokens):
        global i
        global error
        if tokens[i] == 'for':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if initchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = init(tokens)
                    if tokens[i + 1] == ';':
                        i += 1
                        semantics()
                        if conditionchecker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = condition(tokens)
                            if tokens[i + 1] == ';':
                                i += 1
                                semantics()
                                if for_unarychecker(tokens[i + 1]) == True:
                                    i += 1
                                    semantics()
                                    value = for_unary(tokens)
                                    if tokens[i + 1] == ')':
                                        i += 1
                                        semantics()
                                        if tokens[i + 1] == '{':
                                            i += 1
                                            semantics()
                                            if stateschecker(tokens[i + 1]) == True:
                                                i += 1
                                                semantics()
                                                value = states(tokens)
                                                if tokens[i + 1] == '}':
                                                    i += 1
                                                    semantics()
                                                else:
                                                    error.append("SYNTAX ERROR: Error on '" + tokens[
                                                        i] + "',Unexpected '" + tokens[
                                                                     i + 1] + "', \nExpected '}', Line no." + str(
                                                        lineno[i]))
                                            else:
                                                error.append("SYNTAX ERROR: Error on '" + tokens[
                                                    i] + "',Unexpected '" + tokens[
                                                                 i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blanks, }', Line no." + str(
                                                    lineno[i]))

                                        else:
                                            error.append("SYNTAX ERROR: Error on '" + tokens[
                                                i] + "',Unexpected '" + tokens[
                                                             i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

                                    else:
                                        error.append("SYNTAX ERROR: Error on '" + tokens[
                                            i] + "',Unexpected '" + tokens[
                                                         i + 1] + "', \nExpected '+, -, *, /, %, )', Line no." + str(lineno[i]))

                                else:
                                    error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                                 "',Unexpected '" + tokens[
                                                     i + 1] + "', \nExpected 'identifier, ++, --', Line no." + str(lineno[i]))

                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                             "',Unexpected '" + tokens[i + 1] + "', \nExpected '&&, ##, ), ;', Line no." + str(
                                    lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                         "',Unexpected '" + tokens[
                                             i + 1] + "', \nExpected 'numlit, decimallit, identifier, numlit, decimallit, piecelit, optionlit, setlit, !', Line no." + str(lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '+, -, *, /, %, ,, ;, ),&&, ##, ==, !=, >, <, >=, <=', Line no." + str(lineno[i]))

                elif tokens[i + 1] == ';':
                    i += 1
                    semantics()
                    if conditionchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = condition(tokens)
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                            if for_unarychecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = for_unary(tokens)
                                if tokens[i + 1] == ')':
                                    i += 1
                                    semantics()
                                    if tokens[i + 1] == '{':
                                        i += 1
                                        semantics()
                                        if stateschecker(tokens[i + 1]) == True:
                                            i += 1
                                            semantics()
                                            value = states(tokens)
                                            if tokens[i + 1] == '}':
                                                i += 1
                                                semantics()
                                            else:
                                                error.append("SYNTAX ERROR: Error on '" + tokens[
                                                    i] + "',Unexpected '" + tokens[
                                                                 i + 1] + "', \nExpected '}', Line no." + str(
                                                    lineno[i]))

                                        elif tokens[i + 1] == '}':
                                            i += 1
                                            semantics()
                                        else:
                                            error.append("SYNTAX ERROR: Error on '" + tokens[
                                                i] + "',Unexpected '" + tokens[
                                                             i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blanks, }', Line no." + str(
                                                lineno[i]))

                                    else:
                                        error.append("SYNTAX ERROR: Error on '" + tokens[
                                            i] + "',Unexpected '" + tokens[
                                                         i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

                                else:
                                    error.append("SYNTAX ERROR: Error on '" + tokens[
                                        i] + "',Unexpected '" + tokens[
                                                     i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                             "',Unexpected '" + tokens[
                                                 i + 1] + "', \nExpected 'identifier, ++, --', Line no." + str(lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                         "',Unexpected '" + tokens[i + 1] + "', \nExpected ';', Line no." + str(
                                lineno[i]))

                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                     "',Unexpected '" + tokens[
                                         i + 1] + "', \nExpected 'numlit, decimallit, identifier, numlit, decimallit, piecelit, optionlit, setlit, !', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'identifier, ;', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

        elif tokens[i] == 'while':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if stateschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = states(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected '}', Line no." + str(
                                            lineno[i]))

                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank', Line no." + str(
                                        lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '+, -, *, /, %, ), ==, !=, >, <, >=, <=, &&, ##', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no."
                                 + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

        elif tokens[i] == 'do':
            if tokens[i + 1] == '{':
                i += 1
                semantics()
                if stateschecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = states(tokens)
                    if tokens[i + 1] == '}':
                        i += 1
                        semantics()
                        if tokens[i + 1] == 'while':
                            i += 1
                            semantics()
                            if tokens[i + 1] == '(':
                                i += 1
                                semantics()
                                if conditionchecker(tokens[i + 1]) == True:
                                    i += 1
                                    semantics()
                                    value = condition(tokens)
                                    if tokens[i + 1] == ')':
                                        i += 1
                                        semantics()
                                        if tokens[i + 1] == ';':
                                            i += 1
                                            semantics()
                                        else:
                                            error.append("SYNTAX ERROR: Error on '" + tokens[
                                                i] + "',Unexpected '" + tokens[
                                                             i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

                                    else:
                                        error.append("SYNTAX ERROR: Error on '" + tokens[
                                            i] + "',Unexpected '" + tokens[
                                                         i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                                else:
                                    error.append("SYNTAX ERROR: Error on '" + tokens[i] +
                                                 "',Unexpected '" + tokens[
                                                     i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no." + str(lineno[i]))

                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected '(', Line no." + str(
                                        lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank, }', Line no."
                                         + str(lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

    def for_unarychecker(token):
        if token == 'identifier' or incdec_optr(token) == True:
            return True
        else:
            return False

    def for_unary(tokens):
        global i
        global error
        if tokens[i] == 'identifier':
            if for_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = for_rear(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '++, --, =, +=, -=, *=, /=, %=, +, -, *, /, %', Line no." + str(lineno[i]))

        elif incdec_optr(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if for_digitopMath_rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = for_digitopMath_rear(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no."
                             + str(lineno[i]))

    def for_rearchecker(token):
        if incdec_optr(token) == True or ass_optr(token) == True or math_optr(token) == True:
            return True
        else:
            return False

    def for_rear(tokens):
        global i
        global error
        if incdec_optr(tokens[i]) == True:
            return None
        elif ass_optr(tokens[i]) == True or math_optr(tokens[i]) == True:
            if ass_opValues1checker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = ass_opValues1(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, identifier', Line no." + str(lineno[i]))

    def ass_opValues1checker(token):
        if for_digitopMathchecker(token) == True:
            return True
        else:
            return False

    def ass_opValues1(tokens):
        global i
        global error
        if for_digitopMathchecker(tokens[i]) == True:
            value = for_digitopMath(tokens)

    def for_digitopMathchecker(token):
        if token == 'numlit' or token == 'identifier':
            return True
        else:
            return False

    def for_digitopMath(tokens):
        global i
        global error
        if tokens[i] == 'numlit' or tokens[i] == 'identifier':
            if for_digitopMath_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = for_digitopMath_rear(tokens)

    def for_digitopMath_rearchecker(token):
        if math_optr(token) == True:
            return True
        else:
            return False

    def for_digitopMath_rear(tokens):
        global i
        global error
        if math_optr(tokens[i]) == True:
            if for_digitopMathchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = for_digitopMath(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,identifier', Line no." + str(lineno[i]))

    def initchecker(token):
        if token == 'identifier':
            return True
        else:
            return False

    def init(tokens):
        global i
        global error
        if tokens[i] == 'identifier':
            if tokens[i + 1] == '=':
                i += 1
                semantics()
                if digit_opMathchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    digit_opMath(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'numlit, identifier', Line no."
                                 + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '=', Line no." + str(lineno[i]))

    def stateschecker(token):
        if func1checker(token) == True:
            return True
        else:
            return False

    def states(tokens):
        global i
        global error
        if func1checker(tokens[i]) == True:
            value = func1(tokens)
            if states_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = states_rear(tokens)

    def func1checker(token):
        if datatype(token) == True or token == 'identifier' or incdec_optr(token) == True or io_stmtchecker(
                token) == True or if_stmt1checker(token) == True or loopingchecker(token) == True or ctrlchecker(
            token) == True or token == 'blank':
            return True
        else:
            return False

    def func1(token):
        global i
        global error
        if datatype(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if data_altrchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = data_altr(tokens)
                    if id_addchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        id_add(tokens)
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ';', Line no." + str(
                                lineno[i]))

                    elif tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(
                            lineno[i]))

                if id_addchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    id_add(tokens)
                    if tokens[i + 1] == ';':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(
                            lineno[i]))

                elif tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ';', Line no." + str(
                        lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no."
                             + str(lineno[i]))

        elif tokens[i] == 'identifier':
            if id_next_funcchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = id_next_func(tokens)
                if tokens[i + 1] == ';':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '++, --, .,  [,+, -, *, /, %,(', Line no." + str(lineno[i]))

        elif incdec_optr(tokens[i]) == True:
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if tokens[i + 1] == ';':
                    return None
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no."
                             + str(lineno[i]))

        elif io_stmtchecker(tokens[i]) == True:
            value = io_stmt(tokens)
        elif if_stmt1checker(tokens[i]) == True:
            value = if_stmt1(tokens)
        elif loopingchecker(tokens[i]) == True:
            value = looping(tokens)
        elif ctrlchecker(tokens[i]) == True:
            value = ctrl(tokens)
        elif tokens[i] == 'blank':
            if tokens[i + 1] == ';':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

    def if_stmt1checker(token):
        if token == 'if':
            return True
        else:
            return False

    def if_stmt1(tokens):
        global i
        global error
        if tokens[i] == 'if':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if stateschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = states(tokens)
                                if tokens[i+1] == '}':
                                    i += 1
                                    semantics()
                                    if elsif_stmt1checker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = elsif_stmt1(tokens)
                                        if else_stmt1checker(tokens[i + 1]) == True:
                                            i += 1
                                            semantics()
                                            value = else_stmt1(tokens)
                                    elif else_stmt1checker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = else_stmt1(tokens)
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected '}', Line no." + str(
                                            lineno[i]))

                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank', Line no." + str(
                                    lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no."
                        + str(lineno[i]))

    def elsif_stmt1checker(token):
        if token == 'elsif':
            return True
        else:
            return False

    def elsif_stmt1(tokens):
        global i
        global error
        if tokens[i] == 'elsif':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditionchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = condition(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == '{':
                            i += 1
                            semantics()
                            if stateschecker(tokens[i + 1]) == True:
                                i += 1
                                semantics()
                                value = states(tokens)
                                if tokens[i + 1] == '}':
                                    i += 1
                                    semantics()
                                    if elsif_stmt1checker(tokens[i + 1]) == True:
                                        i += 1
                                        semantics()
                                        value = elsif_stmt1(tokens)
                                else:
                                    error.append(
                                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                            i + 1] + "', \nExpected '}', Line no." + str(
                                            lineno[i]))

                            else:
                                error.append(
                                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                        i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank', Line no." + str(
                                        lineno[i]))

                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '{', Line no." + str(
                                lineno[i]))

                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def else_stmt1checker(token):
        if token == 'else':
            return True
        else:
            return False

    def else_stmt1(tokens):
        global i
        global error
        if tokens[i] == 'else':
            if tokens[i + 1] == '{':
                i += 1
                semantics()
                if stateschecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = states(tokens)
                    if tokens[i + 1] == '}':
                        i += 1
                        semantics()
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '}', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'num, decimal, piece, set, option, identifier, ++, --, tell, check, if, for, while, do, continue, break, blank', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '{', Line no." + str(lineno[i]))

    def ctrlchecker(token):
        if token == 'continue' or token == 'break':
            return True
        else:
            return False

    def ctrl(tokens):
        global i
        global error
        if tokens[i] == 'continue' or tokens[i] == 'break':
            if tokens[i + 1] == ';':
                i += 1
                semantics()
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))

    def states_rearchecker(token):
        if stateschecker(token) == True:
            return True
        else:
            return False

    def states_rear(tokens):
        global i
        global error
        if stateschecker(tokens[i]) == True:
            value = states(tokens)

    def func_states_rearchecker(token):
        if func_stateschecker(token) == True:
            return True
        else:
            return False

    def func_states_rear(tokens):
        global i
        global error
        if func_stateschecker(tokens[i]) == True:
            value = func_states(tokens)

    def conditionchecker(token):
        if conditional_optrchecker(token) == True or not1(token) == True or token == '(':
            return True
        else:
            return False

    def condition(tokens):
        global i
        global error
        if conditional_optrchecker(tokens[i]) == True:
            value = conditional_optr(tokens)
        elif not1(tokens[i]) == True:
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if conditional_optrchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = conditional_optr(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if rearchecker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = rear(tokens)
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '&&, ##, {==, !=, >, <, >=, <=, ), ;', Line no."
                            + str(lineno[i]))
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'identifier, numlit, decimallit, piecelit, optionlit, setlit,)', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))
        elif tokens[i] == '(':
            if conditional_optrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = conditional_optr(tokens)
                if rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = rear(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if rearchecker(tokens[i + 1]) == True:
                            i += 1
                            semantics()
                            value = rear(tokens)
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no." + str(
                            lineno[i]))

                elif tokens[i + 1] == ')':
                    i += 1
                    semantics()
                    if rearchecker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = rear(tokens)
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected '),++, --, =, +=, -=, *=, /=, %=, +, -, *, /, %', Line no."
                        + str(lineno[i]))

            elif tokens[i + 1] == ')':
                i += 1
                semantics()
                if rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = rear(tokens)
            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'identifier, numlit, decimallit, piecelit, optionlit, setlit,)', Line no." + str(lineno[i]))

    def conditional_optrchecker(token):
        if compare_optrchecker(token) == True:
            return True
        else:
            return False

    def conditional_optr(tokens):
        global i
        global error
        if compare_optrchecker(tokens[i]) == True:
            value = compare_optr(tokens)
            if conditional_optrearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = conditional_optrear(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '==, !=, >, <, >=, <=, &&, ##', Line no." + str(lineno[i]))

    def conditional_optrearchecker(token):
        if reloptr(token) == True or logoptr_rearchecker(token) == True:
            return True
        else:
            return False

    def conditional_optrear(tokens):
        global i
        global error
        if reloptr(tokens[i]) == True:
            if cmprchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = cmpr(tokens)
                if logoptr_rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = logoptr_rear(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier, numlit, decimallit, setlit, optionlit, piecelit,!', Line no." + str(lineno[i]))

        elif logoptr_rearchecker(tokens[i]) == True:
            value = logoptr_rear(tokens)

    def rearchecker(token):
        if logoptr_rearchecker(token) == True or conditional_rearchecker(token) == True:
            return True
        else:
            return False

    def rear(tokens):
        global i
        global error
        if logoptr_rearchecker(tokens[i]) == True:
            value = logoptr_rear(tokens)
        elif conditional_rearchecker(tokens[i]) == True:
            value = conditional_rear(tokens)

    def logoptr_rearchecker(token):
        if logoptr(token) == True:
            return True
        else:
            return False

    def logoptr_rear(tokens):
        global i
        global error
        if logoptr(tokens[i]) == True:
            if logoptr_addchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = logoptr_add(tokens)
                if logoptr_rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = logoptr_rear(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, identifier, setlit, piecelit, optionlit, !', Line no."
                             + str(lineno[i]))

    def logoptr_addchecker(token):
        if conditionchecker(token) == True:
            return True
        else:
            return False

    def logoptr_add(tokens):
        global i
        global error
        if conditionchecker(tokens[i]) == True:
            value = condition(tokens)

    def conditional_rearchecker(token):
        if reloptr(token) == True:
            return True
        else:
            return False

    def conditional_rear(tokens):
        global i
        global error
        if reloptr(tokens[i]) == True:
            if cmprchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = cmpr(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier, numlit, decimallit, piecelit, optionlit, setlit, !', Line no." + str(lineno[i]))

    def cmprchecker(token):
        if comparechecker(token) == True or not1(token) == True:
            return True
        else:
            return False

    def cmpr(tokens):
        global i
        global error
        if comparechecker(tokens[i]) == True:
            value = compare(tokens)
        elif not1(tokens[i]) == True:
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if compare_optrchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = compare_optr(tokens)
                    if tokens[i + 1] == ')':
                        return None
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected 'identifier, numlit, decimallit, setlit, optionlit, piecelit,!', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def compare_optrchecker(token):
        if comparechecker(token) == True:
            return True
        else:
            return False

    def compare_optr(tokens):
        global i
        global error
        if comparechecker(tokens[i]) == True:
            value = compare(tokens)

    def digit_optrCmprchecker(token):
        if math_optr(token) == True:
            return True
        else:
            return False

    def digit_optrCmpr(tokens):
        global i
        global error
        if math_optr(tokens[i]) == True:
            if digit_opMathchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_opMath(tokens)
            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'numlit, decimallit, identifier, ++, --, (', Line no." + str(lineno[i]))

    def comparechecker(token):
        if token == 'identifier' or literals(token) == True:
            return True
        else:
            return False

    def compare(tokens):
        global i
        global error
        if tokens[i] == 'identifier':
            if id_cmprchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = id_cmpr(tokens)
                if digit_optrCmprchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = digit_optrCmpr(tokens)
            elif digit_optrCmprchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit_optrCmpr(tokens)
        elif tokens[i] == 'numlit' or tokens[i] == 'decimallit':
            if digit_optrCmprchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit_optrCmpr(tokens)
        elif tokens[i+1] == 'setlit' or tokens[i+1] == 'optionlit' or tokens[i+1] == 'piecelit':
            return None

    def io_stmtchecker(token):
        if token == 'tell' or token == 'check':
            return True
        else:
            return False

    def io_stmt(tokens):
        global i
        global error
        if tokens[i] == 'tell':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if outputchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = output(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append(
                                "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected ';', Line no." + str(
                                    lineno[i]))
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'identifier, ( ,setlit', Line no." + str(lineno[i]))

            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

        elif tokens[i] == 'check':
            if tokens[i + 1] == '(':
                i += 1
                semantics()
                if tokens[i+1] == 'identifier':
                    i += 1
                    semantics()
                    if id_rearchecker(tokens[i+1]) == True:
                        i += 1
                        semantics()
                        value = id_rear(tokens)
                        if tokens[i+1] == ')':
                            i += 1
                            semantics()
                            if tokens[i+1] == ';':
                                i += 1
                                semantics()
                            else:
                                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                    i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))
                    elif tokens[i+1] == ')':
                        i += 1
                        semantics()
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ';', Line no." + str(lineno[i]))
                    else:
                        if tokens[i + 1] == ';':
                            i += 1
                            semantics()
                        else:
                            error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected '., [, )', Line no." + str(lineno[i]))
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(', Line no." + str(lineno[i]))

    def outputchecker(token):
        if digit_opMath1checker(token) == True or token == 'setlit':
            return True
        else:
            return False

    def output(tokens):
        global i
        global error
        if digit_opMath1checker(tokens[i]) == True:
            value = digit_opMath1(tokens)
            if output_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = output_rear(tokens)
        elif tokens[i] == 'setlit':
            if output_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = output_rear(tokens)

    def output_rearchecker(token):
        if token == ',':
            return True
        else:
            return False

    def output_rear(tokens):
        global i
        global error
        if tokens[i] == ',':
            if outputchecker(tokens[i + 1]):
                i += 1
                semantics()
                value = output(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier,(,setlit', Line no."
                             + str(lineno[i]))

    def digit_opMath1checker(token):
        if digit2checker(token) == True or token == '(':
            return True
        else:
            return False

    def digit_opMath1(tokens):
        global i
        global error
        if digit2checker(tokens[i]) == True:
            value = digit2(tokens)
            if digit_rear1checker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_rear1(tokens)
        elif tokens[i] == '(':
            if digit3checker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit3(tokens)
                if digit_rear1checker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = digit_rear1(tokens)
                    if tokens[i+1] == ')':
                        i += 1
                        semantics()
                        if digit_rear1checker(tokens[i + 1]):
                            i += 1
                            semantics()
                            value = digit_rear(tokens)
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no." + str(
                            lineno[i]))

                elif tokens[i+1] == ')':
                    i += 1
                    semantics()
                    if digit_rear1checker(tokens[i + 1]):
                        i += 1
                        semantics()
                        value = digit_rear1(tokens)
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

    def digit3checker(token):
        if token == '(' or digit2checker(token) == True:
            return True
        else:
            return False

    def digit3(tokens):
        global i
        global error
        if tokens[i] == '(':
            if digit2checker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit2(tokens)
                if digit_rear1(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = digit_rear1(tokens)
                    i += 1
                    semantics()
                    if tokens[i] == ')':
                        return None
                    else:
                        error.append(
                            "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                                i + 1] + "', \nExpected ')', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier', Line no."
                             + str(lineno[i]))

        elif digit2checker(tokens[i]) == True:
            value = digit2(tokens)

    def digit2checker(token):
        if token == 'identifier':
            return True
        else:
            return False

    def digit2(tokens):
        global i
        global error
        if tokens[i] == 'identifier':
            if id_cmprchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = id_cmpr(tokens)

    def digit_rear1checker(token):
        if math_optr(token) == True:
            return True
        else:
            return False

    def digit_rear1(tokens):
        global i
        global error
        if math_optr(tokens[i]) == True:
            if digit_opMath1checker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit_opMath1(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'identifier, (', Line no." + str(lineno[i]))

    def id_nextchecker(token):
        if incdec_optr(token) == True or id_rearchecker(token) == True or digit_rearchecker(token) == True or id_funcrearchecker(token) == True:
            return True
        else:
            return False

    def id_next(tokens):
        global i
        global error
        if incdec_optr(tokens[i]) == True:
            return None
        elif id_rearchecker(tokens[i]) == True:
            value = id_rear(tokens)
            if id_funcrearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = id_funcrear(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '=, +=, -=, *=, /=, %=', Line no." + str(lineno[i]))
        elif id_funcrearchecker(tokens[i]) == True:
            value = id_funcrear(tokens)
        elif digit_rearchecker(tokens[i]) == True:
            value = digit_rear(tokens)


    def id_rearchecker(token):
        if id_choiceschecker(token) == True:
            return True
        else:
            return False

    def id_rear(tokens):
        global i
        global error
        if id_choiceschecker(tokens[i]) == True:
            value = id_choices(tokens)

    def id_choiceschecker(token):
        if elemchecker(token) == True or ins_arrchecker(token) == True:
            return True
        else:
            return False

    def id_choices(tokens):
        global i
        global error
        if elemchecker(tokens[i]) == True:
            value = elem(tokens)
        elif ins_arrchecker(tokens[i]) == True:
            value = ins_arr(tokens)

    def elemchecker(token):
        if token == '.':
            return True
        else:
            return False

    def elem(tokens):
        global i
        global error
        if tokens[i] == '.':
            if tokens[i + 1] == 'identifier':
                i += 1
                semantics()
                if size_arrchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = size_arr(tokens)
            else:
                error.append(
                    "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected 'identifier', Line no." + str(lineno[i]))

    def ins_arrchecker(token):
        if token == '[':
            return True
        else:
            return False

    def ins_arr(tokens):
        global i
        global error
        if tokens[i] == '[':
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
                if tokens[i + 1] == ']':
                    i += 1
                    semantics()
                    if ins_arr2checker(tokens[i + 1]) == True:
                        i += 1
                        semantics()
                        value = ins_arr2(tokens)
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ']', Line no." + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,identifier', Line no."
                             + str(lineno[i]))

    def ins_arr2checker(token):
        if token == '[' or elemchecker(token) == True:
            return True
        else:
            return False

    def ins_arr2(tokens):
        global i
        global error
        if tokens[i] == '[':
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
                if tokens[i + 1] == ']':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ']', Line no."
                                 + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit,identifier', Line no."
                             + str(lineno[i]))

        elif elemchecker(tokens[i]) == True:
            value = elem(tokens)

    def id_funcrearchecker(token):
        if ass_optr(token) == True:
            return True
        else:
            return False

    def id_funcrear(tokens):
        global i
        global error
        if ass_optr(tokens[i]) == True:
            if ass_opValueschecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = ass_opValues(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, identifier, (, ++, --, setlit, optionlit, piecelit', Line no."
                             + str(lineno[i]))

    def ass_opValueschecker(token):
        if digit_opMathchecker(token) == True or token == 'setlit' or token == 'optionlit' or token == 'piecelit':
            return True
        else:
            return False

    def ass_opValues(tokens):
        global i
        global error
        if digit_opMathchecker(tokens[i]) == True:
            value = digit_opMath(tokens)
        elif tokens[i] == 'setlit':
            if str_conchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = str_con(tokens)
        elif tokens[i] == 'optionlit' or tokens[i] == 'piecelit':
            return None

    def str_conchecker(token):
        if token == '+':
            return True
        else:
            return False

    def str_con(tokens):
        global i
        global error
        if tokens[i] == '+':
            if tokens[i + 1] == 'setlit':
                i += 1
                semantics()
                if str_conchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = str_con(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'setlit', Line no." + str(lineno[i]))

    def digit_opMathchecker(token):
        if digitchecker(token) == True or token == '(':
            return True
        else:
            return False

    def digit_opMath(tokens):
        global i
        global error
        if digitchecker(tokens[i]) == True:
            value = digit(tokens)
            if digit_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_rear(tokens)
        elif tokens[i] == '(':
            if digit1checker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit1(tokens)
                if digit_rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = digit_rear(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                        if digit_rearchecker(tokens[i + 1]) == True:
                            value = digit_rear(tokens)
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no."
                                     + str(lineno[i]))

                elif tokens[i + 1] == ')':
                    i += 1
                    semantics()
                    if digit_rearchecker(tokens[i]) == True:
                        value = digit_rear(tokens)
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ')', Line no."
                                 + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected '(, numlit, decimallit, identifier, ++, --', Line no." + str(lineno[i]))

    def digit1checker(token):
        if token == '(' or digitchecker(token) == True:
            return True
        else:
            return False

    def digit1(tokens):
        global i
        global error
        if tokens[i] == '(':
            if digitchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit(tokens)
                if digit_rearchecker(tokens[i + 1]) == True:
                    i += 1
                    semantics()
                    value = digit_rear(tokens)
                    if tokens[i + 1] == ')':
                        i += 1
                        semantics()
                    else:
                        error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no."
                                     + str(lineno[i]))

                elif tokens[i + 1] == ')':
                    i += 1
                    semantics()
                else:
                    error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                        i + 1] + "', \nExpected ')', Line no."
                                 + str(lineno[i]))

            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, identifier, ++, --', Line no." + str(lineno[i]))

        elif digitchecker(tokens[i]) == True:
            value = digit(tokens)

    def digitchecker(token):
        if token == 'numlit' or token == 'decimallit' or token == 'identifier' or incdec_optr(token) == True:
            return True
        else:
            return False

    def digit(tokens):
        global i
        global error
        if tokens[i] == 'numlit' or tokens[i] == 'decimallit':
            if incdec_rearchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                incdec_rear(tokens)
        elif tokens[i] == 'identifier':
            if choice_rearchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = choice_rear(tokens)
        elif incdec_optr(tokens[i]) == True:
            if digit_contchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit_cont(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, identifier', Line no." + str(lineno[i]))

    def digit_contchecker(token):
        if token == 'numlit' or token == 'decimallit' or token == 'identifier':
            return True
        else:
            return False

    def digit_cont(tokens):
        if tokens[i] == 'numlit' or tokens[i] == 'decimallit' or tokens[i] == 'identifier':
            return None

    def choice_rearchecker(token):
        if incdec_optr(token) == True or id_cmprchecker(token) == True:
            return True
        else:
            return False

    def choice_rear(tokens):
        global i
        global error
        if incdec_optr(tokens[i]) == True:
            return None
        elif id_cmprchecker(tokens[i]) == True:
            value = id_cmpr(tokens)

    def id_cmprchecker(token):
        if id_rearchecker(token) == True or token == '(':
            return True
        else:
            return False

    def id_cmpr(tokens):
        global i
        global error
        if id_rearchecker(tokens[i]) == True:
            value = id_rear(tokens)
        elif tokens[i] == '(':
            if funct_paramchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = funct_param(tokens)
                if tokens[i + 1] == ')':
                    i += 1
                    semantics()
                else:
                    error.append(
                        "SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                            i + 1] + "', \nExpected ')', Line no."
                        + str(lineno[i]))
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, piecelit, optionlit, setlit, identifier', Line no."
                             + str(lineno[i]))

    def funct_paramchecker(token):
        if valuezchecker(token) == True:
            return True
        else:
            return False

    def funct_param(tokens):
        global i
        global error
        global paramdeccounttemp
        global funccalldatatypes
        if valuezchecker(tokens[i]) == True:
            semantics()
            paramdeccounttemp += 1
            funccalldatatypes.append(datatypez[i])
            value = valuez(tokens)
            if digit_rearchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = digit_rear(tokens)
                if func_param_rearchecker(tokens[i+1]) == True:
                    i += 1
                    semantics()
                    value = func_param_rear(tokens)
            elif func_param_rearchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = func_param_rear(tokens)

    def digit_rearchecker(token):
        if math_optr(token) == True:
            return True
        else:
            return False

    def digit_rear(tokens):
        global i
        global error
        if math_optr(tokens[i]) == True:
            if digit_opMathchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = digit_opMath(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, identifier, ++, --, (', Line no." + str(lineno[i]))

    def valuezchecker(token):
        if literals(token) == True or elem_rearchecker(token) == True:
            return True
        else:
            return False

    def valuez(tokens):
        global i
        global error
        if literals(tokens[i]) == True:
            semantics()
            return None
        elif elem_rearchecker(tokens[i]) == True:
            value = elem_rear(tokens)

    def elem_rearchecker(token):
        if token == 'identifier':
            return True
        else:
            return False

    def elem_rear(tokens):
        global i
        global error
        if tokens[i] == 'identifier':
            if elemchecker(tokens[i + 1]):
                i += 1
                semantics()
                value = elem(tokens)

    def func_param_rearchecker(token):
        if token == ',':
            return True
        else:
            return False

    def func_param_rear(tokens):
        global i
        global error
        global paramdeccounttemp
        if tokens[i] == ',':
            if funct_paramchecker(tokens[i+1]) == True:
                i += 1
                semantics()
                value = funct_param(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, decimallit, piecelit, optionlit, setlit, identifier', Line no." + str(lineno[i]))

    def array_altr_exprchecker(token):
        if math_optr(token) == True:
            return True
        else:
            return False

    def array_altr_expr(tokens):
        global i
        global error
        if math_optr(tokens[i]) == True:
            if array_altrchecker(tokens[i + 1]) == True:
                i += 1
                semantics()
                value = array_altr(tokens)
            else:
                error.append("SYNTAX ERROR: Error on '" + tokens[i] + "',Unexpected '" + tokens[
                    i + 1] + "', \nExpected 'numlit, identifier', Line no." + str(lineno[i]))

    program(tokens)
    if len(semanerror) != 0:
        return error[0], semanerror[0],synerror
    else:
        return error[0], 0, synerror