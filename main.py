rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 

#input 0 for stone 1 for paper and 2 for sciccor
user_input= int(input("enter '0'for stone, '1'for paper or '2'for scissor "))
if user_input==0:
  user=rock
elif user_input==1:
  user=paper  
elif user_input==2:
  user=scissors 

comp_input= random.randint(0,2)
if comp_input==0:
  comp= rock
elif comp_input==1:
  comp= paper  
elif comp_input==2:
  comp= scissors 


#conditions for the gameeeeeeee
if user==rock and comp==rock:
  print("user"+ user)
  print("comp"+ comp)
  print("It is dreww!!!!!")
if user==paper and comp==paper:
  print("user"+ user)
  print("comp"+ comp)
  print("It is dreww!!!!!")
if user==scissors and comp==scissors:
  print("user"+user)
  print("comp"+comp)
  print("It is dreww!!!!!")  

if user==rock and comp==paper:
  print("user"+user)
  print("comp"+comp)
  print("comp win !!!!!!!!!!!!!") 
elif user==paper and comp==rock:
  print("user"+user)
  print("comp"+comp)
  print("user win  !!!!!!!!!!!!!!!!")   

if user==paper and comp==scissors:
  print("user"+user)
  print("comp"+comp)
  print("comp win !!!!!!!!!!!!!")  
elif user==scissors and comp==paper:
  print("user"+user)
  print("comp"+comp)
  print("user winn !!!!!!!!!!!!!!!!!!")

if user==scissors and comp==rock:
  print("user"+user)
  print("comp"+comp)
  print("comp win !!!!!!!!!!!!!!!!")    
elif user==rock and comp==scissors:
  print("user"+user)
  print("comp"+comp)
  print("user wiinn !!!!!!!!!!!!!!!!!!!!!!")  






