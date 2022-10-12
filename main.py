import random
 
from bke import start, EvaluationAgent, MLAgent, is_winner, opponent, train, save, RandomAgent, load, train_and_plot

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

def anderpersoon():
  start()
  again()

def domtegen():
  my_random_agent = MyRandomAgent()
  start(player_o=my_random_agent)
  again()

def trainen():    
  my_agent = MyAgent()
 
  train(my_agent, 3000)
 
  save(my_agent, 'MyAgent_3000')

def slimtegen():
  my_agent = load('MyAgent_3000')
 
  my_agent.learning = False
 
  start(player_x=my_agent)
  again()

def plot():
  random.seed(1)
 
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
  #
  random_agent = RandomAgent()
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=50,
      trainings=100,
      validations=1000)
  again()

def again():
  print()
  again = input("Wil je opnieuw spelen?")
  if again == "13" or again == "enter":
        print("")

  else:
      print()
      print("Tot ziens!")
      quit()


print("1: Tegen een ander persoon spelen")
print("2: Tegen een domme tegenstander spelen")
print("3: De tegenstander trainen")
print("4: Tegen een slimme tegenstander spelen")
print("5: Je programma kan de validatie grafiek plotten")

#print("1: Tegen een ander persoon spelen")
#print("2: Tegen een domme tegenstander spelen")
#print("3: De tegenstander trainen")
#print("4: Tegen een slimme tegenstander spelen")
#print("5: Je programma kan de validatie grafiek plotten")


i = input()

if i == "1":
  anderpersoon()

if i == "2":
  domtegen()

if i == "3":
  trainen()

if i == "4":
  slimtegen()

if i == "5":
  plot()

if i == "Enter":
  again()