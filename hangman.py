#!/usr/bin/env python
# -*-coding:utf-8-*-
# modified from Hangman recipe by Veysel Nantu
import random
import time
from time import sleep

game="HARRY'S HOGWARTS HANGMAN"
by="## quantixed ##"
date="30.11.2019"
line="-"*50
blank=""*5
rules="""            You will earn 50 points if you know a character
            and you will lose 25 points if your answer is wrong.
            If you give 5 wrong answers you will lose."""
print("{:^80}\n{:^80}\n{:^80}\n{:^80}\n{}".format(game,by,date,line,blank))
print(rules)
print("{:^80}\n{:^80}\n{:^80}".format(blank,line,blank))

words = ["accio","aguamenti","alohomora","animagus","apparate",
         "apparition","arithmancy","auror","avada","azkaban",
         "basilisk","beater","bludger","broomstick","bubotuber",
         "butterbeer","canary","cauldron","centaur","charm",
         "charms","chaser","cockroach","cruciatus","dark",
         "deathstick","deluminator","dementor","disapparate",
         "divination","dragon","engorgio","erised","expelliarmus",
         "fiendfyre","firebolt","fizzing","floo","floo","goblin",
         "griffindor","gringotts","hallow","haversacking","headmaster",
         "headmistress","heartstring","herbology","hex","horcrux",
         "howler","hufflepuff","imperio","jinx","keeper","legilimens",
         "mandrake","mead","morsmordre","mudblood","newt","niffler",
         "nimbus","occlumency","occlumens","omniocular","outstanding",
         "owl","parselmouth","parseltongue","patronus","pensieve",
         "phoenix","polyjuice","potions","quaffle","quibbler","quidditch",
         "quill","ravenclaw","remembrall","reparo","revealer","runes",
         "sectumsempra","seeker","shrieking","skrewt","slytherin",
         "sneakoscope","snitch","spellotape","squib","stupefy",
         "toad","transfiguration","triwizard","trunk","unbreakable",
         "unicorn","veritaserum","wand","wingardium","witch","wizard","wronski",]
word = random.choice(words)
blanked=[]
blanked.append("-"*len(word))
reveal=[]
for i in blanked:
    for h in i:
        reveal.append(h)
print("Our word has {} letters.".format(len(word)),' '.join(reveal))
print(""*7)
c="""  _________
  |
  |"""
c1="\n  O"
c2="\n \|/"
c3="\n  |" 
c4="\n / \ "
cstr=""
corrguess=""
wrongguess=""
a=len(corrguess)
lives=5
penalty=0
badchar="+/ 1234567890*-_?.,"
while True:
    if len(corrguess)==len(word):
        print("You won! Word: {} Your score: {}".format(word,penalty))
        print("Please press 'Enter' for quit..")
        break
    if lives==0:
        print("\nYou lose...")
        sleep(0.9)
        print ("Your score: {}".format(penalty))
        sleep(0.9)
        print ("The word that you could not answer: {}".format(word))
        sleep(0.9)
        print("Please press 'Enter' to quit...")
        break

    x=input("\nPlease enter a letter: ")
    if 1<len(x):
        print ("\nYou can enter only 1 letter...")
        continue
    if x in badchar:
        print("\nIt's not even a letter!")
        continue
    if x in corrguess:
        print("You used this letter before!")
        continue
    if x in wrongguess:
        print("You used this letter before!")
        continue
    if x in word and not x in corrguess:
        penalty+=50*word.count(x)
        print("Letter {} is counted {} times.".format(x,word.count(x)))
        sleep(0.7)
        for letter, match in enumerate(word):
            if 2 <=word.count(match) and x==match:
                corrguess+=x
                a+=word.count(match)
                if reveal[letter]=="-": 
                    reveal[letter]=x
                print("In space {}.".format(letter+1))
                sleep(0.7)
            if word.count(match)==1 and x==match:
                corrguess+=x
                a+=word.count(match)
                if reveal[letter]=="-":
                    reveal[letter]=x
                print("In line {} .".format(letter+1))
                sleep(0.7)
        print("\nWord:",' '.join(reveal))
        sleep(0.7)

    else:
        wrongguess+=x
        lives-=1
        penalty-=25
        print("\nLetter {} not in our word! {} health left.".format(x,lives))
        sleep(0.7)
        print("\nWord:",' '.join(reveal))
        sleep(0.7)
        if lives==4:
            cstr+=str(c)
            print(cstr)
        if lives==3:
            cstr+=str(c1)       # WE START THE HANGMAN HERE :-)
            print(cstr)      
        if lives==2:          
            cstr+=str(c2)
            print(cstr)
        if lives==1:
            cstr+=str(c3)
            print(cstr)
        if lives==0:
            cstr+=str(c4)
            print(cstr)


try:
    input()
except SyntaxError:
    pass