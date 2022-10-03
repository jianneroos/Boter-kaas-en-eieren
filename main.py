import random
 
from bke import start, EvaluationAgent, MLAgent, is_winner, opponent, train, save, RandomAgent, train_and_plot
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    
random.seed(1)
 
my_agent = MyAgent(alpha=1.0, epsilon=0.1)
random_agent = RandomAgent()

def anderpersoon():
  start()

def dom()
  class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

  my_random_agent = MyRandomAgent()
  start(player_o=my_random_agent)

def trainen()
	class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
 
  my_agent = MyAgent()
 
  train(my_agent, 3000)
 
  save(my_agent, 'MyAgent_3000')

def slim()


def train_and_plot(
        agent=my_agent,
        validation_agent=random_agent,
        iterations=50,
        trainings=100,
        validations=1000)

print("1: Tegen een ander persoon spelen")
print("1: Tegen een domme tegenstander spelen")
print("1: De tegenstander trainen")
print("1: Tegen een slimme tegenstander spelen")
print("1: Je programma kan de validatie grafiek plotten

i = input()

if i == "1":
  anderpersoon()

if i == "2":
  dom()

if i == "3":
  trainen()

if i == "4":
  slim()

if i == "5":
  plot()