class Sentence:
    isSentence = True
    def __init__(self, connective=None, leftarg=None, rightarg=None):

        try:
            (self.leftarg.isSentence or self.rightarg.isSentence)
        except:
            self.connect = connective
            self.leftarg = leftarg
            self.rightarg = rightarg
            if self.leftarg != None and self.rightarg == None:
                self.rightarg = leftarg
        else:
            if self.connect == None:
                return leftarg

class subDerv:
    isDerv = True
    def __init__(self,showLine,lineNumber=1):
        pass

def returnSentence(phi):
    try:
        phi.isSentence
    except:
        if phi == 'INVALID':
            return 'INVALID USE OF RULE'
        else:
            print("not a sentence")
            return "oopsies :3"
    else:
        if phi.connect == 'not':
            return f"~{returnSentence(phi.leftarg)}"
        elif phi.connect== None:
            return f"{phi.leftarg}"
        else:
            if phi.rightarg == None or phi.leftarg == None:
                print("Not well formed sentence")
            else:
                conDict = {"implies":"→","and":"∧","or":"∨","iff":"↔"}
                return f"({returnSentence(phi.leftarg)} {conDict[phi.connect]} {returnSentence(phi.rightarg)})"

    

def MP(phi,psi):
    if phi.connect == 'implies' and phi.leftarg == psi:
        return phi.rightarg
    elif psi.connect == 'implies' and psi.leftarg == phi:
        return psi.rightarg
    else:
        return "INVALID"
    
def MT(phi,psi):
    if phi.connect =='implies' and psi.leftarg == phi.rightarg and psi.connect == 'not':
        return Sentence('not',phi.leftarg,phi.rightarg)
    elif psi.connect =='implies' and phi.leftarg == psi.rightarg and phi.connect == 'not':
        return Sentence('not',psi.leftarg,psi.rightarg)
    else:
        return "INVALID"

def DNE(phi):
    if phi.connect == 'not' and (phi.leftarg).connect == 'not':
        return (phi.leftarg).leftarg
    else:
        return "INVALID"

def DNI(phi):
    return Sentence('not', Sentence('not',phi))

def BCL(phi):
    if phi.connect == 'iff':
        return Sentence('implies',phi.leftarg,phi.rightarg)
def BCR(phi):
    if phi.connect == 'iff':
        return Sentence('implies',phi.rightarg,phi.leftarg)
    
def CBL(phi,psi):
    if phi.connect == 'implies' and psi.connect == 'implies' and phi.leftarg == psi.rightarg and phi.rightarg == psi.leftarg:
        return Sentence('iff',phi.leftarg,phi.rightarg)


def CBR(phi,psi):
    if phi.connect == 'implies' and psi.connect == 'implies' and phi.leftarg == psi.rightarg and phi.rightarg == psi.leftarg:
        return Sentence('iff',phi.rightarg,phi.leftarg)

def SL(phi):
    if phi.connect == 'and':
        return phi.leftarg
    else:
        return "INVALID"
    
def SR(phi):
    if phi.connect == 'and':
        return phi.rightarg
    else:
        return "INVALID"

def AdjL(phi,psi):
    return Sentence('and',phi,psi)
    

def AdjR(phi,psi):
    return Sentence('and',psi,phi)
    
def Rep(phi):
    return phi

def MTP(phi,psi):
    if phi.connect == 'or' and psi.connect == 'not' and phi.leftarg == psi.leftarg:
        return phi.rightarg
    elif phi.connect == 'or' and psi.connect == 'not' and phi.rightarg == psi.leftarg:
        return phi.leftarg
    elif psi.connect == 'or' and phi.connect == 'not' and psi.leftarg == phi.leftarg:
        return psi.rightarg
    elif psi.connect == 'or' and phi.connect == 'not' and psi.rightarg == phi.leftarg:
        return psi.leftarg
    else:
        return "INVALID"

def AddL(phi,psi):
    return Sentence('or',phi,psi)

def AddR(phi,psi):
    return Sentence('or',psi,phi)

 

P= Sentence(None,'P')
Q= Sentence(None,'Q')
R= Sentence(None, 'R')
S= Sentence(None, 'S')
T= Sentence(None, 'T')
U= Sentence(None, 'U')
V= Sentence(None, 'V')

S1 = Sentence('implies',P,Q)
S2 = Sentence('implies',Q,P)


print(returnSentence(BCL(CBL(S1,S2))))