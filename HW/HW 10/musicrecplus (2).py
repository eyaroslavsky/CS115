'''Edward Yaroslavsky eyarosla 11/14/18
I pledge my honor that I have abided by the Stevens Honor System.

HW 10'''


prefFile = 'musicrecplus.txt'

def main():
    '''Initiates the program by loading the txt file and asking for user info'''
    userDict = loadUsers(prefFile)
    username = input('Enter your name (put a $ symbol after your name' +
                     'if you wish your preferences to remain private): \n')
    if username not in userDict:
        preferences = getPref(username, userDict)
        savePref(username, preferences, userDict, prefFile)
        menu(username, userDict)
    else:
        menu(username, userDict)                 
    
def loadUsers(filename):
    '''Loads and adds users to userDict'''
    try:
        file = open(filename, 'r')
    except:
        file = open(filename, 'w')
        userDict= {}
        file.close()
        return userDict
    userDict = {}                                
    for line in file:
        username, artists = line.strip().split(':')
        artistList = artists.split(',')
        artistList.sort()
        userDict[username] = artistList            
    file.close()
    return userDict

def menu(username, userDict):
    '''The main menu for the user to interact with''' 
    while True:
        response = input('Enter a letter to choose an option: \n' +
                         'e - Enter preferences \n' +
                         'r - Get recommendations \n' +
                         'p - Show most popular artists \n' +
                         'h - How popular is the most popular \n' +
                         'm - Which user has the most likes \n' +
                         'q - Save and quit \n')
        if response == 'e':
              prefs = getPref(username,userDict)
              savePref(username, prefs, userDict, prefFile)
        elif response == 'r':
              recommendations = getRecs(username, userDict[username], userDict)
              printRecs(recommendations, username)
              prefs = userDict[username]
              savePref(username, prefs, userDict, prefFile)
        elif response == 'p':
              bestArtists(userDict)
        elif response == 'h':
              printLikes(userDict)
        elif response == 'm':
              best(userDict)
        elif response == 'q':
              try:
                  savePref(username, prefs, userDict, prefFile)
                  break
              except:
                  break
        else:
            print('Please enter only the appropriate letters')
            menu(username, userDict)
                     
def getPref(username, userDict):
    '''Asks for and sorts the user's artist preferences'''
    prefs = []
    while True:
        userPref = input('Enter an artist that you like (Enter to finish): \n')
        if userPref == '':
            break
        else:
            prefs.append(userPref.strip())
    prefs.sort()
    return prefs

def savePref(username, prefs, userDict, filename):
    '''Saves the user's artist preferences'''
    userDict[username] = prefs
    file = open(filename, 'w')
    for user in userDict:
        save = str(user) + ':' + ','.join(userDict[user]) + '\n'
        file.write(save)
    file.close()

def getRecs(currentUser, prefs, userDict):
    '''Receives the artist recommendations from others that are similar to the user'''
    best = findBest(currentUser, prefs, userDict)
    if best != None:
        fullList = list(prefs)
        for user in best:
            fullList += userDict[user]
        recommendations = loseIntersect(prefs, deleteCommon(fullList))
    else:
        recommendations = []
    return recommendations

def printRecs(recommendations, username):
    '''Prints the user artist recommendations'''
    if len(recommendations) == 0:
        print('No recommendations available at this time')
    else:
        for artist in recommendations:
            print(artist)

def findBest(currentUser, prefs, userDict):
    '''Finds the best users associated with the current user for artist recommendations'''
    users = userDict.keys()
    possibleUsers = []
    for user in users:
        if '$' not in user:
            possibleUsers.append(user)
    best = None
    bestScore = 0 
    for user in possibleUsers:
        score = countIntersect(prefs, userDict[user])
        if score > bestScore and currentUser != user and prefs != userDict[user]:
            bestScore = score
            best = [user]
        elif score == bestScore and currentUser != user and prefs != userDict[user] and best != None:
            bestScore = score
            best.append(user)
    return best

def loseIntersect(L1, L2):
    '''Returns a List that contains elements in L2 that are not in L1'''
    L1.sort()
    L2.sort()
    result = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            result.append(L2[j])
            j += 1
    while i < len(L1):
        result.append(L1[i])
        j += 1
    while j < len(L2):
        result.append(L2[j])
        j += 1
    return result

def deleteCommon(L):
    '''Returns a List that removes duplicates'''
    artistDict = {}
    for artist in L:
        if artist in artistDict:
            artistDict[artist] += 1
        else:
            artistDict[artist] = 1
    return list(artistDict.keys())

def countIntersect(L1, L2):
    '''Counts how many elements match in the 2 lists'''
    count = 0
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            count += 1
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j+= 1
    return count

def bestArtists(userDict):
    '''Prints the artist/artists that has/have the most likes'''
    userList = userDict.keys()
    likes = {} 
    mostPop = []
    maximum = 0
    possibleUsers = []
    for user in userList:
        if '$' not in user:
            possibleUsers.append(user)
    for user in possibleUsers:
        for artist in userDict[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    for artist in likes:
        if likes[artist] > maximum:
            maximum = likes[artist]
    for artist in likes:
        if likes[artist] == maximum:
            mostPop.append(artist)
    if len(mostPop) == 0:
        print('Sorry, no artists found')
    else:
        for x in mostPop:
            print(x)

def printLikes(userDict):
    '''Prints the amount of likes that the most popular artist/artists have'''
    userList = userDict.keys()
    likes = {}
    mostPop = []
    maximum = 0
    possibleUsers = []
    for user in userList:
        if '$' not in user:
            possibleUsers.append(user)
    for user in possibleUsers:
        for artist in userDict[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    for artist in likes:
        if likes[artist] > maximum:
            maximum = likes[artist]
    for artist in likes:
        if likes[artist] == maximum:
            mostPop.append(artist)
    if len(mostPop) == 1:
        print(maximum)
    elif len(mostPop) == 0:
        print('Sorry, no artists found')
    else:
        print(maximum)

def best(userDict):
    '''Prints the user/users has the most likes'''
    users = list(userDict)
    maximum = 0
    best = []
    for x in range(len(users)):
        if len(userDict[users[x]]) > maximum and users[x][-1] != '$':
            maximum = len(userDict[users[x]])
            best = [users[x]]
        if len(userDict[users[x]]) == maximum and users[x][-1] != '$':
            maximum = len(userDict[users[x]])
            best.append(users[x])
    if len(best) == 1:
        print(best[0])
    elif len(best) == 0:
        print('Sorry, no user found')
    elif len(best) > 1:
        for user in best[1:]:
            print(user)

main()        


        



            
                    

    
            
            
        



    
                     
              
                  
              
                     
                     
