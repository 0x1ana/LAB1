

def secret_message(letter):
   message = ""
   counter = 1

   for i in range(1, len(letter)):
      if letter[i] == letter[i - 1]:
         counter  += 1
      else:
         message = message + letter[i - 1]
         if counter > 1:
            message += str(counter)
         counter = 1
   message = message + letter[-1]
   if counter > 1:
      message += str(counter)
   return message


letter = str(input('Please enter the secret message: '))
print(secret_message(letter))