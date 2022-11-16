import pyfiglet 
word = pyfiglet.figlet_format("JARVIS")
print(word)
while True:
  You = str(input("You:"))
  if You=='Hello':
    print("Bot:Hi") 
  elif You=='What is your name':
    print("Bot:Jarvis")
  elif You=='How are you':
    print('Bot:I am fine')
  else:
    print("Bot:Error")
