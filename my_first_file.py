# r - read (you can only read the file)
# w - write (you can only write to the file)
# a - read and write (you can do the both actions)
# x - exclusive (nobody can use the file unless you save and close it)

file = open('file.txt', 'w')
file.write('hello world!')
file.close()

with open('file.txt', 'a') as file:
  file.write('\nusing with statement, you file will be automatically closed!')