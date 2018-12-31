'''Edward Yaroslavsky eyarosla 11/12/18
I pledge my honor that I have abided by the Stevens Honor System.

HW 10'''

import sys
from cs115 import *

pref_file = 'musicrecplus.txt'
users = {'Anne Adamant':['50 cent','eminem','lil wayne','snoop dog'],
         'Bacon Bryant$':['Britney Spears','Gotye','Kesha','TMBG'],
         'Caesar Zeppeli':['Fun.','Gotye','Sara Bareilles'],
         'Hidden Powers':['Baby Metal','FLOW','Spyair','Vipera'],
         'Sappho of Lesbos':['Anna Kendrick','Kerkylas of Andros','Sara Bareilles'],
         'Steph Oro':['Fun.','Gotye','Sara Bareilles']}
private = False

def main():
    user = input('Enter your name' +
             '(put a $ symbol after your name' +
             'if you wish your preferences to remain private):').strip()
    if user[-1] == '$':
        private = True
    if user not in users:
        enterPreferences(pref_file, user)
    else:
        menu(pref_file, user)

def read_print_user_prefs(fileName):
    input_file = open(fileName,'r')
    for line in input_file:
        user, artists = line.split(':')
        artistList = artists.split(',')
        for i in range(len(artistList)):
            artistList[i] = artistList[i].strip().lower()
        user = user.strip()
        print(user + ' : ' + str(artistList))
    input_file.close()

def write_prefs(fileName, user, artists):
    output_file = open(fileName,'w')
    allArtists = ''
    for artist in artists:
        if artist == artists[-1]:
            allArtists += artist
        else:
            allArtists += artist + ','
    output_file.write(user + ' : ' + allArtists)
    output_file.close()
        
def menu(fileName, user):
    display = input('Enter a letter to choose an option: \n' +
                    'e - Enter preferences \n' +
                    'r - Get recommendations \n' +
                    'p - Show most popular artists \n' +
                    'h - How popular is the most popular \n' +
                    'm - Which user has the most likes \n' +
                    'q - Save and quit \n').strip()
    if display == 'e':
        enterPreferences(fileName, user)
    elif display == 'r':
        getRecommendations(fileName, user)
    elif display == 'p':
        showPopular()
    elif display == 'h':
        mostPopular()
    elif display == 'm':
        mostLikes()
    elif display == 'q':
        saveAndQuit()
    else:
        menu(fileName, user)

def enterPreferences(fileName, user):
    artists = []
    while True:
        display = input('Enter an artist that you like (Enter to finish):').strip()
        if display != '':
            artists += [str(display)]
        else:
            users[(user)] = artists
            write_prefs(fileName, user, artists)
            break
    menu(fileName, user)

def getRecommendations(fileName, user):
    newUsers = {}
    recommendations = []
    for x in users:
        if users[(x)] != users[(user)]:
            newUsers[(x)] = users[(x)]
    for client in newUsers:
        count = 0
        preferences = client.split('\n')
        for y in preferences:
            if y in users[(user)]:
                count += 1
        if count >= 2:
            for z in preferences:
                if z not in users[(user)] and z not in recommendations:
                    recommendations += [z]
    if private == False:
        recommendations.sort()
    if recommendations == []:
        print('No recommendations available at this time')
    else:
        for rec in recommendations:
            print(rec + '\n')
    menu(fileName, user)
           
read_print_user_prefs(pref_file)
main()  
    
