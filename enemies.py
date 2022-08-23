import random
from main import item_upper
from words import words_list
from dice import numm, choose

player_health = 100
print("The enemy is challenging you to a fight.")
print("Note if you deny the fight you will lose 40hp")
answer = input("Do you accept it: ")
answer_upper = answer.upper()

if item_upper == "POTION":
    from main import num

    potion = num


def gues(x):
    a = False
    for i in range(1, word_len):
        if x in list(word):
            guessin.replace("_", guess)
            a = True

        else:
            a = False

    return a, guessin


if answer_upper == "NO":
    print("You denied the challenge.")
    if player_health > 40:
        if item_upper == "SHIELD":
            print("The shield secret ability is activated")
            player_health -= 20

        elif item_upper == "DAGGER":
            print("You hold the dagger.")
            print("Damage is going to be reduced.")
            player_health -= random.randint(0, 35)
        else:
            player_health -= 40
        print("You have", player_health, "hp remaining.")

    else:
        print("You died.")

else:
    print("You agreed to fight.")
    print("There's no coming back.")
    if choose:
        word = words_list[numm]

    else:
        word = random.choice(words_list)
        while not (word.isalpha()):
            word = random.choice(words_list)

    word_len = len(word)
    guessed_letters = [word[0]]
    enemy_health = word_len * 10 - 10
    print("You need to guess the word correctly.")
    print("You have", player_health, "hp.")
    print("Your hint: The first letter of the word is", word[0])
    guess = ""
    guessin = "_" * word_len
    print(guessin)
    
    while guess != word:
        guess = input("Guess a letter from the word : ")

        if guess in guessed_letters:
            print("You already guessed the letter", guess)
            print("This is what you guessed so far", guessed_letters)


        elif gues(guess):
            if item_upper == "SWORD":
                enemy_health -= 20

            elif item_upper == "DAGGER":
                enemy_health -= 15

            else:
                enemy_health -= 10
            print("Good job you guessed it correctly.")
            print("You damaged the enemy. The enemy has", enemy_health, "hp left")

            indices = [i for i, letter in enumerate(word) if letter == guess]  # the correct word replace _ in guessin
            word_as_list = list(guessin)  
            for index in indices:  
                word_as_list[index] = guess  

            guessin = "".join(word_as_list)

        elif len(guess) == len(word):
            print(guessin)
            guessed_letters.append(guess)

        else:
            if item_upper == "SHIELD":
                player_health -= 5

            elif item_upper == "DAGGER":
                player_health -= random.randint(0, 8)

            else:
                player_health -= 10
            print("You guessed incorrectly. Try again")
            print("You have", player_health, "hp remaining.")
            guessed_letters.append(guess)

        if player_health <= 20 and item_upper == "POTION" and potion:
            print("The potion was used automatically.")
            player_health += 20
            print(player_health)
            potion -= 1

        if player_health <= 0:
            print("You died.")
            exit()

        else:
            pass

        if enemy_health <= 0 or guess == word:
            print("You killed the enemy")
            print("Your word was ", guessin)
            exit()

