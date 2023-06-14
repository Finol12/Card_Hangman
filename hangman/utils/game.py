import random
class hangman:
    # List of possible words
    possible_words= ['becode', 'learning', 'mathematics', 'sessions']

    # initializing the class
    def __init__(self):
        self.word_to_find=list(random.choice(self.possible_words))
        self.lives=5
        self.correctly_guessed_letters=['_']*len(self.word_to_find)
        self.wrongly_guessed_letters=[]
        self.turn_count=0
        self.error_count=0

    def play(self):
        #Ask the user to enter a letter
        letter=input("Enter aletter: ").lower()
        if letter in self.word_to_find:
            # Iterate over the word to find if the letter matches
            for i,j in enumerate(self.word_to_find):
                if letter==j:
                    self.correctly_guessed_letters[i]=letter
        else: 
            self.wrongly_guessed_letters.append(letter)
            self.error_count+=1 
            self.lives-=1
        self.turn_count+=1 
        print(f"correctly_guessed_letters:{self.correctly_guessed_letters} ,wrongly_guessed_letter:{self.wrongly_guessed_letters} , live:{self.lives} , error_count:{self.error_count} , turn_count:{self.turn_count}")
        

    

    def start_game(self):     
        while self.lives>0:
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                return
            else:
                self.play()   
                
        # If lives run out, call game_over method 
        self.game_over()


    def game_over(self):
        print("game over...")

    def well_played(self):
        print(f"You found the word:  {self.word_to_find}  in  {self.turn_count}  turns with  {self.error_count}  errors!") 
         
         
