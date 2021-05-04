with open('file.txt', 'r') as file:
  # content = file.read()
  # print(content)

  for line in file.readlines():
    print(line)