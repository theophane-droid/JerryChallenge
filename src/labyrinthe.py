from random import randint

from exceptions import WinException, InvalidMoveException

WALL = '#'
JERRY = '£'
CHEESE = '^'
SPACE = ' '

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


class Labyrinthe(list):
    already_expored = []
    def __init__(self, size, nb_break=2):
        if size%2 == 0:
            raise Exception('size sould be an odd number !')
        self.size = size
        while not self.is_complicated_enough():
            super().__init__(
                self.create_labyrithe()
            )
            self.jerry = [size - 2, size//2]
            self.cheese = [1, size//2]
            while not self.can_jerry_reach_cheese(list(self.jerry)):
                self.already_expored = []
                self.break_wall()

    def break_wall(self):
        i, j = 1, 1
        while ((i + j) %2 == 0) or\
            self[i][j] == SPACE:
            i = randint(1, (self.size - 2))
            j = randint(1, (self.size - 2))
        self[i][j] = SPACE

    def create_labyrithe(self) -> list:
        lab = [[SPACE if i%2==1 and j%2==1 else WALL 
            for i in range (self.size)] for j in range (self.size)]
        return lab

    def can_go_to(self, direction) -> bool:
        if direction == LEFT:
            return self.jerry[1] > 1 and self[self.jerry[0]][self.jerry[1] - 1] != WALL
        elif direction == RIGHT:
            return self.jerry[1] < self.size - 2 and self[self.jerry[0]][self.jerry[1] + 1] != WALL
        elif direction == UP:
            return self.jerry[0] > 1 and self[self.jerry[0] - 1][self.jerry[1]] != WALL
        elif direction == DOWN:
            return self.jerry[0] < self.size - 2 and self[self.jerry[0] + 1][self.jerry[1]] != WALL
        else:
            raise Exception('direction not valid')

    def moove(self, direction, jerry) -> list:
        if self.can_go_to(direction):
            if direction == LEFT:
                jerry[1] -= 1
            elif direction == RIGHT:
                jerry[1] += 1
            elif direction == UP:
                jerry[0] -= 1
            elif direction == DOWN:
                jerry[0] += 1
            if jerry == self.cheese:
                raise WinException('You win !')
        else:
            raise InvalidMoveException('Invalid move')
        return jerry

    def is_complicated_enough(self) -> bool:
        if len(self) == 0:
            return False
        mil_n = self.size//2
        mil = [line[mil_n] for line in self[1:-1]]
        return WALL in mil

    def can_jerry_reach_cheese(self, jerry, max_depth=100) -> bool:
        if max_depth <= 0:
            return False
        i = jerry[0]
        j = jerry[1]
        if (i, j) in self.already_expored:
            return False
        self.already_expored.append((i, j))
        if self[i][j] == WALL:
            return False
        if self[i][j] == CHEESE:
            return True
        for dir in [UP, DOWN, LEFT, RIGHT]:
            try:
                ni, nj = self.moove(dir, [i,j])
                if self.can_jerry_reach_cheese([ni, nj], max_depth - 1):
                    return True
            except WinException:
                return True
            except InvalidMoveException:
                pass
        return False


    def __str__(self) -> str:
        tab = [list(e) for e in self]
        tab[self.jerry[0]][self.jerry[1]] = JERRY
        tab[self.cheese[0]][self.cheese[1]] = CHEESE
        result = ''
        for line in tab:
            result += ' '.join(line) + '\n'
        return result