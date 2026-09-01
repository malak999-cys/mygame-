# password stream checker
from email.utils import specialsre

print('please enter strong password using tokens,small,big letter,%&,*+#! ')

password = input('Enter your password :')
lenght = len(password)
print('the lenght of password is {}'.format(lenght))

if lenght >8:



         if not password.isalnum():#دالة تستخدم لمعرفة ما اذا كان المتغير يحتوي على رموز خاصة او لا مثل #%^&@*
                print("Password contains special characters! (Strong)")
         else:
              print("Password does NOT contain special characters! (Weak)")

else:
       print('your password is too weak you need to use differint tokens ')



