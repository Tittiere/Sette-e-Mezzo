from os import system
import numpy as np
import time
import random

deckVal = [1,2,3,4,5,6,7,0.5,0.5,0.5]
deckCards = ["asso di picche","due di picche","tre di picche","quattro di picche","cinque di picche","sei di picche","sette di picche","jack di picche","donna di picche","re di picche","asso di quadri","due di quadri","tre di quadri","quattro di quadri","cinque di quadri","sei di quadri","sette di quadri","jack di quadri","donna di quadri","re di quadri","asso di fiori","due di fiori","tre di fiori","quattro di fiori","cinque di fiori","sei di fiori","sette di fiori","jack di fiori","donna di fiori","re di fiori","asso di cuori","due di cuori","tre di cuori","quattro di cuori","cinque di cuori","sei di cuori","sette di cuori","jack di cuori","donna di cuori","re di cuori"]

def askPlayers():
    nPlayers = input("Quanti giocatori ci sono?\n")
    while True:
        if nPlayers.isdigit() == False:
            nPlayers = input("Il numero inserito non è valido.\nInserisci un numero valido di giocatori:\n")
        else:
            nPlayers = int(nPlayers)
            if nPlayers < 1:
                nPlayers = input("Il numero inserito non è valido.\nInserisci un numero valido di giocatori:\n")
            else:
                break
    nickNames = np.empty(nPlayers, dtype=object)
    if nPlayers > 1:
        for i in range(nPlayers):
            nickNames[i] = input(f"Inserisci il nickname del giocatore {i+1}:\n")
    return nPlayers, nickNames

def fourtyToTen(num):
    if num >= 10 and num < 20:
        num -= 10
    elif num >= 20 and num < 30:
        num -= 20
    elif num >= 30:
        num -= 30
    return num

def getJoker():
    print("Hai pescato la matta!")
    time.sleep(1)
    print("Questa carta speciale puo' assumere un qualsiasi valore tra 1 e 7 oppure 0.5")
    time.sleep(1)
    joker = input("Inserisci il valore che vuoi che assuma\n")
    while True:
        if joker.isdigit() == False and joker != "0.5":
            joker = input("Il valore inserito non è valido.\nInserisci un valore valido per la matta:\n")
        else:
            joker = float(joker)
            if joker != 0.5 and joker != 1 and joker != 2 and joker != 3 and joker != 4 and joker != 5 and joker != 6 and joker != 7:
                joker = input("Il valore inserito non è valido.\nInserisci un valore valido per la matta:\n")
            else:
                break
    return joker

def changeJoker():
    print("Vuoi cambiare il valore della matta?")
    answ = input("(Y/N)\n")
    if answ == 'y' or answ == 'Y':
        joker = input("Inserisci il valore che vuoi che assuma\n")
        while True:
            if joker.isdigit() == False and joker != "0.5":
                joker = input("Il valore inserito non è valido.\nInserisci un valore valido per la matta:\n")
            else:
                joker = float(joker)
                if joker != 0.5 and joker != 1 and joker != 2 and joker != 3 and joker != 4 and joker != 5 and joker != 6 and joker != 7:
                    joker = input("Il valore inserito non è valido.\nInserisci un valore valido per la matta:\n")
                else:
                    break
    else:
        joker = False
    return joker

def computer(verify):
    turn = 0
    compScore = 0
    while True:
        while True:
            card = random.randrange(40)
            if verify[card] != 1:
                break
        num = fourtyToTen(card)
        verify[card] += 1
        if turn > 0:
            print("Il computer chiede un'altra carta")
            time.sleep(1)
        turn += 1
        if card == 8 or card == 18 or card == 28 or card == 38:
            print(f"La carta del computer è una {deckCards[card]}")
        else:
            print(f"La carta del computer è un {deckCards[card]}")
        time.sleep(1)
        if card == 19:
            joker = 7.5 - compScore
            if joker == 0.5 or joker == 1.5 or joker == 2.5 or joker == 3.5 or joker == 4.5 or joker == 5.5 or joker == 6.5 or joker == 7.5:
                joker -= 0.5
                compScore += joker
                print(f"Il computer ha pescato la matta e la fa valere {joker}")
        else:
            compScore += deckVal[num]
        if compScore >= 5.5:
            break
    time.sleep(1)
    print("Il computer si ferma")
    time.sleep(1)
    print(f"Il suo punteggio è {compScore}")
    return compScore, verify

def highestScore(names, data):
    for i in range(nPlayers):
        minPos = i
        j = i+1
        for j in range(nPlayers-1):
            if data[minPos] > data[j]:
                minPos = j
            if minPos != i:
                aux = data[i]
                data[i] = data[minPos]
                data[minPos] = aux
                aux = names[i]
                names[i] = names[minPos]
                names[minPos] = aux
    return names, data

def singleplayer():
    score = 0
    playerPoints = 0
    computerPoints = 0
    draws = 0
    verify = np.zeros(40)
    while True:
        if verify[19] == 1:
            verify = np.zeros(40)
        gotJoker = False
        score = 0
        while True:
            card = random.randrange(40)
            if verify[card] != 1:
                break
        num = fourtyToTen(card)
        verify[card] += 1
        if card == 8 or card ==18 or card == 28 or card == 38:
            print(f"La tua prima carta è una {deckCards[card]}")
        else:
            print(f"La tua prima carta è un {deckCards[card]}")
        time.sleep(1)
        if card == 19:
            while True:
                joker = getJoker()
                if score + joker > 7.5:
                    print(f"Facendo valere la matta {joker} arriveresti a {score+joker}")
                else:
                    break
            score += joker
            gotJoker = True
        else:
            score += deckVal[num]
        print("Vuoi un'altra carta?")
        answ = input("(Y/N)\n")
        time.sleep(1)
        system('cls')
        while answ == 'y' or answ == 'Y':
            while True:
                card = random.randrange(40)
                if verify[card] != 1:
                    break
            num = fourtyToTen(card)
            verify[card] += 1
            if card == 8 or card ==18 or card == 28 or card == 38:
                print(f"La tua carta è una {deckCards[card]}")
            else:
                print(f"La tua carta è un {deckCards[card]}")
            time.sleep(1)
            if card == 19:
                while True:
                    joker = getJoker()
                    if score + joker > 7.5:
                        print(f"Facendo valere la matta {joker} arriveresti a {score+joker}")
                    else:
                        break
                score += joker
                gotJoker = True
            else:
                score += deckVal[num]
            print(f"Sei arrivato a {score}")
            time.sleep(1)
            if card != 19 and gotJoker == True:
                newJoker = changeJoker()
                if newJoker != False:
                    while True:
                        newJoker = changeJoker()
                        if score + newJoker > 7.5:
                            print(f"Facendo valere la matta {newJoker} arriveresti a {score-joker+newJoker}")
                        else:
                            break
                    score -= joker
                    score += newJoker
                    joker = newJoker
            if score > 7.5:
                print("Hai sballato")
                break
            elif score == 7.5:
                print("Hai fatto Sette e Mezzo!")
                break
            else:
                print("Vuoi un'altra carta?")
                answ = input("(Y/N)\n")
                time.sleep(1)
                system('cls')
            if answ != 'y' and answ != 'Y':
                break
        time.sleep(1)
        if score > 7.5:
            print("Vince il computer")
            time.sleep(2)
            system('cls')
            computerPoints += 1
        else:
            print("E' il turno del computer")
            time.sleep(2)
            system('cls')
            tuple1 = computer(verify)
            compScore = tuple1[0]
            verify = tuple1[1]
            if compScore > 7.5 or compScore < score:
                print("Hai vinto!")
                playerPoints += 1
            elif compScore > score:
                print("Vince il computer!")
                computerPoints += 1
            elif compScore == score:
                print("Pareggio!")
                draws += 1
        time.sleep(1)
        print("Vuoi giocare un'altra partita?")
        answ = input("(Y/N)\n")
        time.sleep(1)
        system('cls')
        if answ != 'y' and answ != 'Y':
            break
    return playerPoints, computerPoints, draws

def multiplayer():
    score = np.zeros(nPlayers)
    verify = np.zeros(40)
    points = np.zeros(nPlayers)
    print("Volete leggere le regole riguardo ai punteggi?")
    answ = input("(Y/N)\n")
    if answ == 'y' or answ == 'Y':
        print("Il punteggio è organizzato in questo modo:")
        print("Arrivare a 7.5: +1 punto")
        print("Sballare: -1 punto")
        print("Ogni turno la persona che vince guadagna un punto extra")
        print("Se due giocatori pareggiano la manche il punto extra non viene assegnato")
    while True:
        count = 0
        while True:
            if verify[19] == 1:
                verify = np.zeros(40)
            gotJoker = False
            score[count] = 0
            print(f"E' il turno di {nickNames[count]}")
            while True:
                card = random.randrange(40)
                if verify[card] != 1:
                    break
            num = fourtyToTen(card)
            verify[card] += 1
            if card == 8 or card ==18 or card == 28 or card == 38:
                print(f"La tua prima carta è una {deckCards[card]}")
            else:
                print(f"La tua prima carta è un {deckCards[card]}")
            if card == 19:
                joker = getJoker()
                score[count] += joker
                gotJoker = True
            else:
                score[count] += deckVal[num]
            print("Vuoi un'altra carta?")
            answ = input("(Y/N)\n")
            while answ == 'y' or answ == 'Y':
                while True:
                    card = random.randrange(40)
                    if verify[card] != 1:
                        break
                num = fourtyToTen(card)
                verify[card] += 1
                if card == 8 or card ==18 or card == 28 or card == 38:
                    print(f"La tua carta è una {deckCards[card]}")
                else:
                    print(f"La tua carta è un {deckCards[card]}")
                if card == 19:
                    joker = getJoker()
                    score[count] += joker
                    gotJoker = True
                else:
                    score[count] += deckVal[num]
                print(f"Sei arrivato a {score[count]}")
                if card != 19 and gotJoker == True:
                    newJoker = changeJoker()
                    if newJoker != False:
                        score[count] -= joker
                        score[count] += newJoker
                        joker = newJoker
                if score[count] > 7.5:
                    print("Hai sballato")
                    if points[count] != 0:
                        points[count] -= 1
                    score[count] = -1
                    break
                elif score[count] == 7.5:
                    print("Hai fatto Sette e Mezzo!")
                    points[count] += 1
                    break
                else:
                    print("Vuoi un'altra carta?")
                    answ = input("(Y/N)\n")
                if answ != 'y' and answ != 'Y':
                    break
            count += 1
            if count >= nPlayers:
                break
        names2 = np.empty(nPlayers, dtype=object)
        scores2 = np.zeros(nPlayers)
        for n in range(nPlayers):
            names2[n] = nickNames[n]
            scores2[n] = score[n]
        vect = highestScore(names2, scores2)
        if vect[1][0] == vect[1][1]:
            print("Manche pareggiata!")
        else:
            for i in range(nPlayers):
                if vect[0][0] == nickNames[i]:
                    holder = i
            points[holder] += 1
            print(f"Vince la manche {nickNames[holder]}")
        print("Punteggi:")
        for i in range(nPlayers):
            print(f"{nickNames[i]}:\t\t\t{int(points[i])}")
        print("Volete giocare un'altra partita?")
        answ = input("(Y/N)\n")
        if answ != 'y' and answ != 'Y':
            break
    print("Classifica:")
    vect = highestScore(nickNames, points)
    highestScore(vect[0], vect[1])
    i = 0
    while i < nPlayers:
        if i < nPlayers-1:
            if vect[1][i] == vect[1][i+1]:
                print(f"Al posto n°{i+1} ci sono:")
                j = i
                while j < nPlayers-2 and vect[1][j] == vect[1][j+1]:
                    print(vect[0][j])
                    j += 1
                print(vect[0][j])
                i = j
                if i+1 != nPlayers-1:
                    print(f"con {int(vect[1][i])} punti")
            else:
                print(f"Al posto n°{i+1} con {int(vect[1][i])} punti: {vect[0][i]}")
        elif vect[1][i] == vect[1][i-1]:
            print(vect[0][i])
            print(f"con {int(vect[1][i])} punti")
        else:
            print(f"Al posto n°{i+1} con {int(vect[1][i])} punti: {vect[0][i]}")
        i += 1

#main
system('cls')
#introduzione()
#system("cls")
tupleMain = askPlayers()
time.sleep(1)
system('cls')
nPlayers = tupleMain[0]
nickNames = tupleMain[1]
if nPlayers == 1:
    tupleSing = singleplayer()
    print("Fine del Gioco\n")
    print(f"Partite vinte: {tupleSing[0]}\nPartite perse: {tupleSing[1]}\nPartite pareggiate: {tupleSing[2]}")
else:
    multiplayer()
    print("Fine del Gioco\n")
answ = input("Si vogliono visualizzare i crediti?\nY/N\n")
if answ == 'y' or answ == 'Y':
    #credits()
    placeholder = 0
else:
    print("Grazie per aver giocato\n")