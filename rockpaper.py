from random import randint
l=['ROCK','PAPER','SISSOR']



def comp():
   k=randint(0,2)
   return (l[k])



#comp()
#def scoar():



r1=input('Welcome do you ready for combate y/n::::')
if r1 in 'yY':
   name=input('YOUR GAME NAME ')
   print("")
   print(F"OK! {name} ready for a combat")
   print("")
else:
   print('type c to cancle')
   print("")




def num(y):
  k=""
  if y == 1:
    k ='ROCK'
  elif y == 2:
    k ='PAPER'
  elif y== 3:
    k ='SISSOR'
  return k


while True:
   inp=input('choose 1.rock, 2.paper, 3.sissor ::::')

   pi=''
   if inp in '123':
       print ("")
       pi = num(int(inp))
   elif inp not in '123':
       print ("")
       print ('PLEASE...ENTER A VALID OPTION')
   else:
       print ("")
       print (inp)


   bot = comp()
   if inp in 'nNxXcCeE':
      break
   print (pi)



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
