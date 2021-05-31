import os
from os import system




class TicTacToe:
    Boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Box1 = "|1|"
    Box2 = "2"
    Box3 = "|3|"
    Box4 = "|4|"
    Box5 = "5"
    Box6 = "|6|"
    Box7 = "|7|"
    Box8 = "8"
    Box9 = "|9|"

    game_over_draw = False
    game_over_O = False
    game_over_x = False

    choice = 0
    circleOn = True

    def display_no_space(self):
        print(self.Box1 + self.Box2 + self.Box3)
        print(self.Box4 + self.Box5 + self.Box6)
        print(self.Box7 + self.Box8 + self.Box9)

    def display(self):
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(self.Box1 + self.Box2 + self.Box3)
        print(self.Box4 + self.Box5 + self.Box6)
        print(self.Box7 + self.Box8 + self.Box9)

    def next_move(self):
        try:
            self.choice = int(input("Select the box you want to be filled on your turn:"))
        except ValueError:
            print("Invalid input, please try again")
            return

        if self.choice < 0 or self.choice > 9:
            print("Invalid input, please try again")
            return

        if self.circleOn:
            self.Boxes[self.choice - 1] = 1
            if int(self.choice) == 1:
                if self.Box1 == "|1|":
                    self.Box1 = "|O|"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 2:
                if self.Box2 == "2":
                    self.Box2 = "O"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 3:
                if self.Box3 == "|3|":
                    self.Box3 = "|O|"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 4:
                if self.Box4 == "|4|":
                    self.Box4 = "|O|"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 5:
                if self.Box5 == "5":
                    self.Box5 = "O"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 6:
                if self.Box6 == "|6|":
                    self.Box6 = "|O|"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 7:
                if self.Box7 == "|7|":
                    self.Box7 = "|O|"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 8:
                if self.Box8 == "8":
                    self.Box8 = "O"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 9:
                if self.Box9 == "|9|":
                    self.Box9 = "|O|"
                    self.circleOn = False
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
        elif not self.circleOn:
            self.Boxes[self.choice - 1] = 2
            if int(self.choice) == 1:
                if self.Box1 == "|1|":
                    self.Box1 = "|X|"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 2:
                if self.Box2 == "2":
                    self.Box2 = "X"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 3:
                if self.Box3 == "|3|":
                    self.Box3 = "|X|"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 4:
                if self.Box4 == "|4|":
                    self.Box4 = "|X|"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 5:
                if self.Box5 == "5":
                    self.Box5 = "X"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 6:
                if self.Box6 == "|6|":
                    self.Box6 = "|X|"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 7:
                if self.Box7 == "|7|":
                    self.Box7 = "|X|"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 8:
                if self.Box8 == "8":
                    self.Box8 = "X"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)
            elif int(self.choice) == 9:
                if self.Box9 == "|9|":
                    self.Box9 = "|X|"
                    self.circleOn = True
                    self.display(self)
                else:
                    print("Error: Box is already filled!")
                    self.next_move(self)

    def check_for_game_over_0(self):
        if self.Boxes[0] == 1 and self.Boxes[4] == 1 and self.Boxes[8] == 1:
            self.game_over_O = True
        if self.Boxes[2] == 1 and self.Boxes[4] == 1 and self.Boxes[6] == 1:
            self.game_over_O = True
        elif self.Boxes[6] == 1:
            if (self.Boxes[7] == 1 and self.Boxes[8] == 1) or (self.Boxes[0] == 1 and self.Boxes[3] == 1):
                self.game_over_O = True
        elif self.Boxes[4] == 1:
            if (self.Boxes[3] == 1 and self.Boxes[5] == 1) or (self.Boxes[1] == 1 and self.Boxes[7] == 1):
                self.game_over_O = True
        elif self.Boxes[2] == 1:
            if (self.Boxes[5] == 1 and self.Boxes[8] == 1) or (self.Boxes[0] == 1 and self.Boxes[1] == 1):
                self.game_over_O = True

    def check_for_game_over_x(self):
        if self.Boxes[0] == 2 and self.Boxes[4] == 2 and self.Boxes[8] == 2:
            self.game_over_x = True
        if self.Boxes[2] == 2 and self.Boxes[4] == 2 and self.Boxes[6] == 2:
            self.game_over_x = True
        elif self.Boxes[6] == 2:
            if (self.Boxes[7] == 2 and self.Boxes[8] == 2) or (self.Boxes[0] == 2 and self.Boxes[3] == 2):
                self.game_over_x = True
        elif self.Boxes[4] == 2:
            if (self.Boxes[3] == 2 and self.Boxes[5] == 2) or (self.Boxes[1] == 2 and self.Boxes[7] == 2):
                self.game_over_x = True
        elif self.Boxes[2] == 2:
            if (self.Boxes[5] == 2 and self.Boxes[8] == 2) or (self.Boxes[0] == 2 and self.Boxes[1] == 2):
                self.game_over_x = True

    def check_for_game_over_draw(self):
        checker = True
        for index in self.Boxes:
            if index == 0:
                checker = False
        if checker:
            self.game_over_draw = True

    def run_game(self):
        print("Rules: type the number corresponding to your desired box to place a circle or X at the box.")
        print("First to 3 in a row wins and circle has the first move. Good luck! ")
        print(" ")
        self.display_no_space(self)
        while not self.game_over_O and not self.game_over_x and not self.game_over_draw:
            self.next_move(self)
            self.check_for_game_over_0(self)
            self.check_for_game_over_x(self)
            self.check_for_game_over_draw(self)

        self.display(self)
        if self.game_over_O:
            print("Game over, circle wins!")
        elif self.game_over_x:
            print("Game over, X wins!")
        else:
            print("Game over, Draw!")
