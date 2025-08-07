import random
word_guess = {
    "CRICKET": "The game that Indians love the most",
    "PROTEIN": "The nutrition that gymnasts use",
    "SPECTACLES": "It provides you with clearer vision",
    "PVR": "A place where people go to watch cinema",
    "COLLEGE": "Place where students get educated",
    "AMAZON": "Famous e-commerce company",
    "ADOLF HITLER": "Famous dictator",
    "INTERSTELLAR": "One of the best movie of Christopher Nolan",
    "RAJNIKANTH": "Super Star",
    "VIJAY": "Thalapthy",
    "UFC": "Deadliest sport in the world",
    "KHABIB NURMAGOMEDOV": "Famous UFC undefeated champion aka The Eagle",
    "DUSTIN POIRIER": "Diamond",
    "ISLAM MAKACHEV": "The grappler"
}
word2guess = random.choice(list(word_guess.keys()))
hint = word_guess[word2guess]
guessed = set()
chances = 6
stages = [
    """
     _________
     |     |
     |     
     |    
     |    
     |
    =========
    """,
    """
     _________
     |     |
     |     O
     |    
     |    
     |
    =========
    """,
    """
     _________
     |     |
     |     O
     |     |
     |    
     |
    =========
    """,
    """
     _________
     |     |
     |     O
     |    /|
     |    
     |
    =========
    """,
    """
     _________
     |     |
     |     O
     |    /|\\
     |    
     |
    =========
    """,
    """
     _________
     |     |
     |     O
     |    /|\\
     |    / 
     |
    =========
    """,
    """
     _________
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    =========
    """
]
print("🎮 Welcome to Word Guessing Game !")
print(f'''💡 Hint: {hint} 
(Word has {len(word2guess)} letters)''')
while chances > 0:
    display_word = [letter if letter in guessed or letter == " " else "_" for letter in word2guess]
    print(" ".join(display_word))
    print(stages[6 - chances])
    guess = input("Guess a letter: ").upper()
    if not guess.isalpha() or len(guess) != 1:
        continue
    if guess in guessed:
        continue
    elif guess in word2guess:
        guessed.add(guess)
    else:
        guessed.add(guess)
        chances -= 1
    if all(letter in guessed or letter == " " for letter in word2guess):
        print(" ".join([letter if letter in guessed or letter == " " else "_" for letter in word2guess]))
        print("🎉 You WON! The word was:", word2guess)
        break
else:
    print(stages[6])
    print("💀 You lost. The word was:", word2guess)

