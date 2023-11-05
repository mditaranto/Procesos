import random
import string


chars = string.ascii_letters
password = ""
    
for a in range(10):
    password += random.choice(chars)
      
print(password)