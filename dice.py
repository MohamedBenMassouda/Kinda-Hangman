from words import words_list

choose = input("Do you want to pick the word? ")

while choose.upper() == "NO":
    choose = False

numm = int(input("Pick a number between 0 and 2465: "))
while numm > len(words_list):
    numm = int(input("Pick a number between 0 and 2465: "))