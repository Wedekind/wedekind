name= input('What\'s yor name? ')

print('\n So, your Name is ' +  name+ ' right? \n '  'Let\'s begin an Adventure')
import time
time.sleep( 2 )


#Choose a weapon
if name != "Hans":
  print("\n Choose your weapon:\n\n (1) For Axe \n (2) For Bow \n (3) for Sword")
else:
  print("\n Choose your weapon:\n\n (1) For Axe \n (2) For Bow \n (3) for Sword \n (4) for FLAMMENWERFER")

waffe= input()
time.sleep( 1 )
if name == "Hans":
  if waffe == '4':
    time.sleep(1)
    print('You win the Game!\n Your are Hans with a FLAMMENWERFER in a Medival-Adventure-Game. GG ^_^')
else:
  if waffe == '1':
   print("You have chosen the Axe as your weapon")
  elif waffe == '2':
     print("You have chosen the Bow as your weapon")
  elif waffe == '3':
     print("You have chosen the Axe as your weapon")
  else:
    print("For now you can only choose between thoose 3") 
    
    time.sleep(0.5)
  print("So " +name+"!" " Now you are ready for your first day as an adventurer!")
  time.sleep(5)
  print("\n\nYou Lose! YOU are NOT HANS! \nTry again as Hans")
