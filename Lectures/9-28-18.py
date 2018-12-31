from cs115 import *

memo = {}

def fastLCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    elif S1 == "" or S2 == "":
        memo[(S1, S2)] = 0
        return 0
    elif S1[0] == S2[0]:
        answer = 1 + fastLCS(S1[1:], S2[1:])
        memo[(S1, S2)] = answer
        return answer
    else:
        chopS1 = fastLCS(S1[1:], S2)
        chopS2 = fastLCS(S1, S2[1:])
        answer = max(chopS1, chopS2)
        memo[(S1, S2)] = answer
        return answer


def fastLCSalt(S1, S2):
    memo = {}
    def fLCS(S1, S2):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        elif S1 == "" or S2 == "":
            memo[(S1, S2)] = 0
            return 0
        elif S1[0] == S2[0]:
            answer = 1 + fLCS(S1[1:], S2[1:])
            memo[(S1, S2)] = answer
            return answer
        else:
            chopS1 = fLCS(S1[1:], S2)
            chopS2 = fLCS(S1, S2[1:])
            answer = max(chopS1, chopS2)
            memo[(S1, S2)] = answer
            return answer
        return fLCS(S1, S2)

def LCSTrace(S1, S2):
    #print("LCSTrace(" + S1 + "," + S2 + ")")
    def LCST(S1, S2, amt):
        if S1 == "" or S2 == "":
            return 0
        elif S1[0] == S2[0]:
            print(amt * "   " + "LCSTrace(" + S1 + "," + S2 + ")")
            return 1 + LCST(S1[1:], S2[1:], amt+1)
        else:
            print(amt * "   " + "LCSTrace(" + S1 + "," + S2 + ")")
            chopS1 = LCST(S1[1:], S2, amt+1)
            #print(amt * "   " + "LCSTrace(" + S1 + "," + S2 + ")")
            chopS2 = LCST(S1, S2[1:], amt+1)
            return max(chopS1, chopS2)
    return LCST(S1, S2, 1)
