# Rockpaper.py
from random import randint # random to pick random word by bot from list
l=['ROCK','PAPER','SISSOR'] #making list to store options



def comp():   #a function to chooses a random word from list 
   k=randint(0,2)
   return (l[k])




#taking inputs 
r1=input('Welcome do you ready for combate y/n::::')
if r1 in 'yY': #checking if player is willing 
   name=input('YOUR GAME NAME ')
   print("")
   print(F"OK! {name} ready for a combat")
   print("")
else:
   print('type c to cancle') #not willing then giving instruction to type c
   print("")




def num(y): #in case if user inputs int in place of string then assign those int as string 
  k=""
  if y == 1:
    k ='ROCK'
  elif y == 2:
    k ='PAPER'
  elif y== 3:
    k ='SISSOR'
  return k


while True:
   inp=input('choose 1.rock, 2.paper, 3.sissor ::::')# taking option for game from user

   pi=''
   if inp in '123': # if user inputs int then in place of string 
       print ("")
       pi = num(int(inp))
   elif inp not in '123':
       print ("")
       print ('PLEASE...ENTER A VALID OPTION') #if user not inputs options then
   else:
       print ("")
       print (inp)


   bot = comp()
   if inp in 'nNxXcCeE':#options for breaking loop
      break
   print (pi)#when user give int the concerted string will print over here else just a space


#game body it all depends on your logic
   print ("")
   print (f"{name} choose ({inp}{pi})  and   computer choose ({bot}) ")
   print ("")
   if  bot == inp.upper() or bot == pi:
     print ("it's a draw ")
     print ("")
   elif bot == 'ROCK' and inp == 'sissor'or bot == 'ROCK' and inp == 'SISSOR'or bot == 'ROCK' and int(inp) ==  3:
     print ('you lose')
     print ("")
   elif bot == 'SISSOR' and inp == 'paper' or bot == 'SISSOR' and inp == 'PAPER' or bot == 'SISSOR' and int(inp) == 2:
     print ('you lose')
     print ("")
   elif bot == 'PAPER' and inp ==  'rock' or bot == 'PAPER' and inp == 'ROCK' or bot == 'PAPER' and int(inp) == 1:
     print ('you lose')
     print ("")
   else:
     print ('you won')
     print ("")
