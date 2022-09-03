from colorama import Fore,Style
import random

questions={1:'1. Which one of the following river flows between Vindhyan and Satpura ranges?', 2: '2. Which among the following headstreams meets the Ganges in last?', 3: '3. The metal whose salts are sensitive to light is?', 4: "4. 'OS' computer abbreviation usually means ?", 5: "5. '.MOV' extension refers usually to what kind of file?", 6: "6. Who is the author of the book 'Nineteen Eighty Four'?", 7: "7. Brown Waterfalls are situated in: ", 8: "8. Which of the following is tropical grassland?", 9: "9. Which of the following is indicated by the colour of a star?", 10: '10. Who is the father of Geometry?', 11: '11. Dr. M. S. Swaminathan has distinguished himself in which of the following fields?', 12: "12. Ordinary table salt is sodium chloride. What is baking soda?", 13: "13. The group of minerals chemically containing hydrocarbons is: ", 14: "14. When is the International Workers' Day?", 15: "15. The highest civilian award of India 'Bharat Ratna' has been awarded to only two foreigners so far. One of them is Nelson Mandela. The other is: ", 16: "16. IDA stands for: "}

options={1: ['(a)Narmada', '(b)Mahanadi', '(c)Son', '(d)Netravati'], 2: ['(a)Alaknanda', '(b)Pindar', '(c)Mandakini', '(d)Bhagirathi'], 3: ['(a)Zinc', '(b)Silver', '(c)Copper', '(d)Aluminum'], 4: ['(a)Order of Significance', '(b)Open Software', '(c)Operating System', '(d)Optical Sensor'], 5: ['(a)Image file', '(b)Animation/movie file', '(c)Audio file', '(d)MS Office document'], 6:["(a)Thomas Hardy", '(b)Emile Zola', '(c)George Orwell', '(d)Walter Scott'], 7: ['(a)Australia', '(b)New Zealand', '(c)Canada', '(d)Switzerland'], 8: ['(a)Taiga', '(b)Savannah', '(c)Pampas','(d)Prairies'], 9: ['(a)Weight', '(b)Distance', '(c)Temperature', '(d)Size'], 10: ['(a)Aristotle', '(b)Pythagoras', '(c)Kepler', '(d)Euclid'], 11: ['(a)Agriculture', '(b)Medicine', '(c)Astrophysics', '(d)Physics'], 12: ['(a)Potassium chloride', '(b)Potassium carbonate', '(c)Potassium hydroxide', '(d)Sodium bicarbonate'], 13: ['(a)silicate group', '(b)organic group', '(c)oxide group', '(d)hydride group'], 14: ['(a)15th April', '(b)12th December', '(c)1st May','(d)1st August'], 15: ['(a)Abdul Ghaffar khan', '(b)Mikhail Gorbachev', '(c)Marshal Tito','(d)Abdul Wali Khan'], 16: ['(a)Indian Development Agency', '(b)Industrial Development Analyses', '(c)International Development Agency','(d)None of the above']}

rightA={1: options[1][0], 2: options[2][3], 3: options[3][1], 4: options[4][2], 5: options[5][1], 6: options[6][2], 7: options[7][1], 8: options[8][1], 9: options[9][2], 10: options[10][3], 11: options[11][0], 12: options[12][3], 13: options[13][1], 14: options[14][2], 15: options[15][0], 16: options[16][2]}

lifelines={1: 'Flip the question: New question appears', 2: '50-50: Remove 2 wrong answers', 3: 'Hint', 4: '2 guesses allowed :  The player can make 2 guesses'}

prizes=['1,000', '2,000', '3,000', '5,000', '10,000', '20,000', '40,000', '80,000', '1,60,000', '3,20,000', '6,40,000', '12,50,000','25,00,000', '50,00,000', '1,00,00,000', '7,00,00,000']

print('************************************'.center(25))
print(Fore.LIGHTCYAN_EX+Style.BRIGHT +'Welcome to "Who wants to be a millionaire" Game'.center(35)+Fore.RESET+Style.RESET_ALL)
print('************************************'.center(25))
print(" ")
print(" ")
print(Fore.LIGHTRED_EX+Style.BRIGHT+'Rules for the game: '+Fore.RESET+Style.RESET_ALL)
print("""1. The player has to choose a correct answer.
2. If your answer is correct, you win a specific amount of prize money and moves to the next question.
3. If your answer is incorrect, the game terminates.
4. You may use the given lifelines in case you are unable to answer a question.
""")
print('------------------------------------')
print(Fore.CYAN+Style.BRIGHT+'Lifelines: '+Fore.RESET+Style.RESET_ALL)
for x,y in lifelines.items():
  print(f"{x}. {y}")
print('------------------------------------')
print(" ")
print(Fore.BLUE+Style.BRIGHT+'Here come the questions!!...'+Fore.RESET+Style.RESET_ALL)
print(" ")
print(" ")

def q(questNo):
  print(questions[questNo])
  print(" ")
  for i in range(4):
    print(options[questNo][i])
  print(" ")

def chA(questNo,x):
  correctA=rightA[questNo]
  return correctA

def l1():
  print("Your new question...")
  print("Q. The outermost layer of the atmosphere is called: ")
  print(" ")
  print("""  (a)stratosphere
  (b)exosphere
  (c)mesosphere
  (d)troposphere
  """)
  rightAnswer='(b)'
  print("Enter your answer(a/b/c/d): ")
  x=input(" ")
  return x,rightAnswer

def half(questNo):
  correctA=rightA[questNo]
  options[questNo].remove(correctA)
  w=random.choice(options[questNo])
  list=[w,correctA]
  list.sort()
  print(list[0])
  print(list[1])
  x=input(f"Enter your answer({list[0][1]}/{list[1][1]}): ")
  return correctA,x

def hint(questNo):
  hints={1: "This river is also called 'Reva'.", 2: "The river originates from Gomukh glacier.", 3: "This metal is also the best conductor of electricity.", 4: "Windows is an example of OS.", 5: "Audio file is not the answer.", 6: "This author is also known for his book 'Animal Farm'.", 7: "Australia is not the answer.", 8: "Taiga is not the answer.", 9: "Distance is not the answer.", 10: "This scientist has written the book 'Elements'", 11: "Green revolution is connected with this field.", 12: "The answer is a sodium salt", 13: "Oxide group is not the answer.", 14: "The date is 1st.", 15: "He was very close to Mahatma Gandhi.", 16: "Indian Development Agency is not the answer."}
  print(" ")
  print("Here's your hint...")
  print(hints[questNo])
  print(" ")
  x=input("Enter your answer(a/b/c/d): ")
  return x

def guesses(questNo):
  g1=input("Enter guess 1 (a/b/c/d): ")
  if g1==rightA[questNo][1]:
    print("Your answer is correct!")
    print(" ")
    return g1
  else:
    print("Your answer is wrong..try again")
    print(" ")
    g2=input("Enter guess 2 (a/b/c/d): ")
    return g2
      
question=0
prize=0
noLifeline=[1,2,3,4]
for i in range(1,17):
  q(i)
  question=question+1
  if len(noLifeline)>=1:
    print(f"Enter your answer(a/b/c/d) or if you're unsure enter lifeline number {noLifeline}: ")
  else:
    print("Enter your answer(a/b/c/d) (no lifelines available): ")
  x=input(" ")
  if x in 'abcd':
    h=chA(i,x)
    if x==h[1]:
      prize=prizes[i-1]
      print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
      print(" ")
    else:
      print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect...Game over :(")
      break
  else:
    if x=='1'and int(x) in noLifeline:
      g,h=l1()
      if g==h[1]:
        prize=prizes[i-1]
        print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
        print(" ")
        noLifeline.remove(1)
      else:
        print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect...Game over :(")
        break
    elif x=='2' and int(x) in noLifeline:
      h,g=half(i)
      if g==h[1]:
        prize=prizes[i-1]
        print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
        noLifeline.remove(2)
        print(" ")
      else:
        print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect... Game over :(")
        break
    elif x=='3'and int(x) in noLifeline:
      h=hint(i)
      if h==rightA[i][1]:
        prize=prizes[i-1]
        print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
        noLifeline.remove(3)
        print(" ")
      else:
        print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect... Game over :(")
        break
    elif x=='4'and int(x) in noLifeline:
      h=guesses(i)
      if h==rightA[i][1]:
        prize=prizes[i-1]
        print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
        noLifeline.remove(4)
        print(" ")
      else:
        print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect... Game over :(")
        break
    else:
      print("Please enter valid answer/number...")
      if len(noLifeline)>=1:
        print(f"Enter your answer(a/b/c/d) or if you're unsure enter lifeline number {noLifeline}: ")
      else:
        print("Enter your answer(a/b/c/d) (no lifelines available): ")
      x=input(" ")
      if x in 'abcd':
        h=chA(i,x)
        if x==h[1]:
          prize=prizes[i-1]
          print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
          print(" ")
        else:
          print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect...Game over :(")
          break
      else:
        if x=='1'and int(x) in noLifeline:
          g,h=l1()
          if g==h[1]:
            prize=prizes[i-1]
            print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
            print(" ")
            noLifeline.remove(1)
          else:
            print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect...Game over :(")
            break
        elif x=='2' and int(x) in noLifeline:
          h,g=half(i)
          if g==h[1]:
            prize=prizes[i-1]
            print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
            noLifeline.remove(2)
            print(" ")
          else:
            print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect... Game over :(")
            break
        elif x=='3'and int(x) in noLifeline:
          h=hint(i)
          if h==rightA[i][1]:
            prize=prizes[i-1]
            print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
            noLifeline.remove(3)
            print(" ")
          else:
            print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect... Game over :(")
            break
        elif x=='4'and int(x) in noLifeline:
          h=guesses(i)
          if h==rightA[i][1]:
            prize=prizes[i-1]
            print(Fore.YELLOW+Style.BRIGHT+f"Your answer is correct!! You win {prize} rupees! "+Fore.RESET+Style.RESET_ALL)
            noLifeline.remove(4)
            print(" ")
          else:
            print(Fore.YELLOW+Style.BRIGHT+"Your answer is incorrect... Game over :(")
            break
