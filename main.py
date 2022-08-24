# Sudi yussuf


import random



#1
  #guessing game
  #generarte uniform random numbers in interval [1,100]
  #prompt enter a num
  #tell user if their guess was too hight/low/correct
  #if incorrect prompt user for another guess, if correct congradulate

def guessing_game():
  rand = random.randint(1,101)
  
  i = 0
  while i<1:
    user_choice = input("Guess a random number between 1 and 100")
    if rand > int(user_choice):
      print("Sorry, your guess is too low. Guess again!")
    elif rand < int(user_choice):
      print("Sorry your guess is too high. Guess again") 
    else:
      print("Congrats! You guessed correctly")
      i = 2
    
#guessing_game()



#2
  # reverse guessing game
  #computer gueses user secret number
  #must guess in 7 steps or fewer
  #after each try, computer prompts user to enter L,H or C

def reversed_guessing_game():
  rand = random.randint(1,101)
 
  i = 0
  max = 101
  min = 1

  while i<7:
    user_answer = input(f'Is {rand} too high, too low, or correct?')
    if user_answer == 'H':
      max = rand
      rand = random.randint(min,max)
    elif user_answer == 'L':
      min = rand -1
      rand = random.randint(min,max)   
    else:
      print("Finally")
      i = 7
    i = i +1;
    
#reversed_guessing_game()




# 3
# copy of 2
# modify and add min and max parameters
# lower/uppercase
# let the user know if they cheated
def reversed_guessing_game(min,max):
  rand = random.randint(min,max)
 
  i = 0

  user_real_answer = input(f'Choose a number between {min} and {max} that you want the computer to guess.')


  while  int(user_real_answer) < min or int(user_real_answer) > max:
      user_real_answer = input(f'Nice try lol! Choose a number that is acually between {min} and {max}')
      

  while i<7:
    user_answer = input(f'Is {rand} too high, too low, or correct?')

    if user_answer.upper() == 'H' and int(user_real_answer) < rand:
      max = rand
      rand = random.randint(min,max)
    elif user_answer.upper() == 'L' and int(user_real_answer) > rand:
      min = rand -1
      rand = random.randint(min,max)   
    elif user_answer.upper() == 'C' and int(user_real_answer) == rand:
      print("Finally")
      i = 7
    else:
      print('Why are you lying to me about your number :(')
      i = i - 1
    
  i = i + 1
    
# reversed_guessing_game(1,100)




#4 take away limits to guessing
def reversed_guessing_game_no_limits(min,max):
  rand = random.randint(min,max)
 
  user_real_answer = input(f'Choose a number between {min} and {max} that you want the computer to guess.')


  while  int(user_real_answer) < min or int(user_real_answer) > max:
      user_real_answer = input(f'Nice try lol! Choose a number that is acually between {min} and {max}')
      
  i = 0

  while i < 1:
    user_answer = input(f'Is {rand} too high, too low, or correct?')
    
    if user_answer.upper() == 'H' and int(user_real_answer) < rand:
      max = rand
      rand = random.randint(min,max)
    elif user_answer.upper() == 'L' and int(user_real_answer) > rand:
      min = rand -1
      rand = random.randint(min,max)   
    elif user_answer.upper() == 'C' and int(user_real_answer) == rand:
      print("Finally")
      i = 1
    else:
      print('Why are you lying to me about your number :(')


# reversed_guessing_game_no_limits(1,100)













