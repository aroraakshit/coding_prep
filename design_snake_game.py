def __init__(self, width,height,food): # 224ms, credits - LeetCode
    """
    Initialize your data structure here.
    @param width - screen width
    @param height - screen height 
    @param food - A list of food positions
    E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    :type width: int
    :type height: int
    :type food: List[List[int]]
    """
    self.snake = collections.deque([[0,0]])    # snake head is at the front
    self.width = width
    self.height = height
    self.food = collections.deque(food)
    self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
    
def move(self, direction):
    """
    Moves the snake.
    @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
    @return The game's score after the move. Return -1 if game over. 
    Game over when snake crosses the screen boundary or bites its body.
    :type direction: str
    :rtype: int
    """
    newHead = [self.snake[0][0]+self.direct[direction][0], self.snake[0][1]+self.direct[direction][1]]
    
    # notice that the newHead can be equal to self.snake[-1]
    if (newHead[0] < 0 or newHead[0] >= self.height) or (newHead[1] < 0 or newHead[1] >= self.width)\
    or (newHead in self.snake and newHead != self.snake[-1]): return -1

    if self.food and self.food[0] == newHead:  # eat food
        self.snake.appendleft(newHead)   # just make the food be part of snake
        self.food.popleft()   # delete the food that's already eaten
    else:    # not eating food: append head and delete tail                 
        self.snake.appendleft(newHead)   
        self.snake.pop()   
        
    return len(self.snake)-1

# ----

class SnakeGame: # 172ms, Credits - LeetCode

    def __init__(self, width: 'int', height: 'int', food: 'List[List[int]]'):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.gameover=-1
        self.w=width
        self.h=height
        self.food=food[::-1]
        self.size=0
        self.snake=collections.deque([[0, 0]])
    def move(self, direction: 'str') -> 'int':
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
         1.update head
         2.judge head
         3.eat food,update
         normal move, if head in snake, game over
        """
        head= self.snake[-1][:]#need to add [],o.w, head will change self.snake value
        if direction=='U':
            head[0]-=1
        elif direction=='L':
            head[1]-=1
        elif direction=='R':
            head[1]+=1
        elif direction=='D':
            head[0]+=1
        if not (0<=head[0]<self.h and 0<=head[1]<self.w):
            return self.gameover
        
        if self.food and self.food[-1]==head:
            self.food.pop()
            self.size+=1
        else:
            self.snake.popleft()
            if head in self.snake:
                return self.gameover
        self.snake.append(head)
        return self.size
        