import random
print("©2022 roaddevs all rights reserved")
hangman = [
  """
   _________
    |/
    |
    |
    |
    |                          
    |
    |___
    HANGMAN (©2022 roaddevs all rights reserved)""",

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___""",

"""
    _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___ """,

"""
    ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___""",


"""
  _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___""",

  
"""
    _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___ """,


  
"""
  ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___  """,


"""
________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___ """
]
words = 'allowit bait bigman bruh bossman bruv bare clapped  ends fam gassed goofy geezer innit jokes leng man mandem maccies myg nob opps peng peak rahh safe shank sheet shit ting vexed wasteman whip '.split()

def getRandWords(wordLs):
  wordIndex = random.randint(0, len(wordLs) - 1)
  return wordLs[wordIndex]
def display(missed, correct, secretWord):
  print(hangman[len(missed)])
  for letter in missed:
    print("Missed letters:", letter)
  blankToFill = "_" * len(secretWord)
  for i in range(len(secretWord)):
    if secretWord[i] in correct:
      blankToFill = blankToFill[:i] + secretWord[i] +blankToFill[i+1:]
  for letter in blankToFill:
    print(letter)
def guesses(alrGuessed):
  while True:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if len(guess) != 1:
      print("man can only enter one letter still")
    elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
      print("English or latin pls fam")
    elif guess in alrGuessed:
      print("R u dumb you already guessed that (absolute nobhead)")
    else:
      return guess
def playAgain():
  ans = input("would fam like to play again [yes/no]: ")
  return ans.lower().startswith("y")
print("HANGMAN (©2022 roaddevs all rights reserved)")
missed = ""
correct = ""
secretWord = getRandWords(words)
gameover = False
while True:
  display(missed, correct, secretWord)
  guess = guesses(missed + correct)
  if guess in secretWord:
    correct = correct + guess
    foundAll = True
    for i in range(len(secretWord)):
      if secretWord[i] not in correct:
        foundAll = False
        break
    if foundAll:
      print("youve saved the stickman my g the word is: ", secretWord)
      gameover = True
  else:
    missed = missed + guess
    if len(missed) == len(hangman) - 1:
      display(missed, correct, secretWord)
      print("RIP stickfam 2022-2022. The word was: ", secretWord)
      gameover = True
  if gameover:
    if playAgain():
      missed = ""
      correct = ""
      gameover = False
      secretWord = getRandWords(words)
    else:
      break
        