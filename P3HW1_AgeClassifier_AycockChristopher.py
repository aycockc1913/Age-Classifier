#CTI 110
#P3HW1 Age Classifier
#AycockChristopher
#06/24/2018
age = int(input('Enter a number:'))
if age <= 1:
    print('he or she is an infant')
elif age < 13:
    print('he or she is a child')
elif age < 20:
    print('he or she is a teenager')
else:
    print('he or she is an adult')
