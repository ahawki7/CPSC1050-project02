class game_status:
    def __init__(self):
        self.game_over = False

    def status(self, bool):
        if bool:
            self.game_over = True
            print("Congratulations! You've escaped from the museum.")
            quit()

    def is_game_over(self):
        return self.game_over