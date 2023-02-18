# This program runs in the Command Line Interface (CLI) or Terminal window.
# It asks the user to input a number and outputs a melody with that number
#  of notes in C, including inflections of major, minor and pentatonic.
#  Each note will be followed by that note's duration.

from random import *

saxophone = """
             "'-.'.
                 \\ \\
                  ; ;
                 .| |.---,
                 :| ||o |
                  \\ o  o|
                   '._.'
"""
print('* * * * * M.J. MELODY MAKER * * * * *')
print(saxophone)
print('* * * * * M.J. MELODY MAKER * * * * *\n')

c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
c_minor = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']
c_pentatonic = ['C', 'Eb', 'F', 'G', 'Bb']
scale = choice([c_major, c_minor, c_pentatonic])

print()
print('Welcome to the M.J. Melody Maker!')
print('This program will output a melody in C Major, C Minor or C Pentatonic.')
print('Each line in the output will consist of a note and its duration.')
print('Pick whatever octaves sound best for each note.')
print("Type 'quit' at any time to exit the program.\n")
print()

run_program = True

while run_program:
    melody_list = []
    print('How many notes are in your melody?')
    length = input('Type an integer from 2 to 20 and hit "Enter": ')
    if length.lower() == "quit":
        print()
        run_program = False

    try:
        length = int(length)
    except ValueError:
        continue

    if length < 2 or length > 20:
        print("Please pick a number between 2 and 20.")
        print()
        continue

    for i in range(length):
        duration = choice(['one beat', 'one beat', 'one beat', 'one beat', 'one beat',
                           'one beat', 'two beats', 'two beats', 'two beats', 'two beats',
                           'three beats', 'four beats'])
        melody_list.append(f'{choice(scale)} for {duration}')
    print()

    print('Here is your melody:')
    print()
    print('♩ ♫ ♪ ♬ 🎝 🎜')
    for i in melody_list:
        print(i)
    print('♩ ♪ ♫ ♩ 🎝 ♩')
    print()

    print('Would you like to create another melody?')
    again = input("Type 'yes' or 'no' and hit 'Enter': ").lower()
    print()
    if not again.startswith('y'):
        run_program = False

print("Thank you for using the M.J. Melody Maker!")
valediction = ['a GREAT', 'a RADICAL', 'an AWESOME', 'a MELODIC', 'a HARMONIC',
               'a STUPENDOUS', 'a TERRIFIC', 'an EPIC', 'a REMARKABLE', 'a FAVORABLE',
               'an EXCELLENT', 'a RIGHTEOUS', 'a SUPERB', 'a MOST EXCELLENT',
               'a WONDERFUL', 'a MARVELOUS', 'a CAPITAL']

print(f"Have {choice(valediction)} day!")
