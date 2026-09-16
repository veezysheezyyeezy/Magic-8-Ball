import random
name = 'joshiwah'
question = 'am i fat'
answer = ''
random_number = random.randint(1, 11)
#print(random_number)
if name == '':
  print('Name is needed.')
elif question == '':
  print('Question is needed.')
elif random_number == 1:
  answer = 'Yes - Definitely'
elif random_number == 2:
  answer = 'It is decidely so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
elif random_number == 10:
  answer = 'Nah man.'
elif random_number == 11:
  answer = 'Your tripping!'
else:
  answer = 'Error'
print(name + ' asks: ' + question)
print("Magic 8-Ball's answer: " + answer)