import string 
from random import choice
from colorama import Fore, Back, Style

play = 'yes'
while play == 'yes':
	with open('wordL.txt') as wordlist:
		word_choice = choice([word.upper() for word in wordlist.read().split('\n')])
	with open('allowed.txt') as wordlist:
		wordlist = [word.upper() for word in wordlist.read().split('\n')]
		print('\n'+'\n')
	correct_letters_at_correct_index = ''
	num_guesses = 5
	alphabet = string.ascii_uppercase

	while num_guesses > 0:
		guess = input('    guess a 5 letter word\n').upper()
		if guess == word_choice:
			print("          " + Fore.WHITE + Back.GREEN + guess + Style.RESET_ALL + '\nYou win')
			play = input('          play again?\n')
		elif guess in wordlist:
				print('\n' * 4) 
				print('            ', end='')
				for i in range(5):
					if guess[i] == word_choice[i]:
						alphabet = alphabet.replace(guess[i], str(Fore.WHITE + Back.GREEN + guess[i] + Style.RESET_ALL))
						correct_letters_at_correct_index += guess[i]
						print(Fore.WHITE + Back.GREEN + guess[i] + Style.RESET_ALL, end='')
					elif guess[i] in word_choice and guess[i] not in correct_letters_at_correct_index:
						alphabet = alphabet.replace(guess[i], str(Fore.WHITE + Back.YELLOW + guess[i] + Style.RESET_ALL))
						print(Fore.WHITE + Back.YELLOW + guess[i] + Style.RESET_ALL, end='')
					elif guess[i] in word_choice and guess[i] in correct_letters_at_correct_index:
						print(guess[i], end='')
					else:
						alphabet = alphabet.replace(guess[i], str(Style.DIM + Fore.WHITE + guess[i] + Style.RESET_ALL))
						print(guess[i], end='')
				print('\n' * 4)
				print('  ' + alphabet + '\n')
				num_guesses -= 1
				print('    You have ' + str(num_guesses) + ' guesses left')
		else:
			print('\n' * 2)
			print("Sorry, that's not an accepted word"+ '\n')
			print('  ' + alphabet + '\n') 
	print('           ' + Fore.WHITE + Back.GREEN + word_choice + Style.RESET_ALL + '\nYou lose')
	
	play = input('          play again?\n')
