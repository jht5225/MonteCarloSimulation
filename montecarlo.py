import random
import matplotlib.pyplot as plt
from statistics import mean
class monte_carlo_simulation():

    def __init__(self, num_outcomes, num_successes, balance, bet, iterations):
        self.outcomes = num_outcomes
        self.successes = num_successes
        self.bal = balance
        self.b = bet
        self.it = iterations
        self.final_amounts = []
    def draw_card(self):
        card = random.randint(1, self.outcomes)
        if card <= self.successes:
            return True
        else:
            return False

    def play(self, startmoney, betammount, bets):
        play_index = []
        play_index.append(0)
        currentfunds = []
        currentfunds.append(startmoney)
        for i in range(1,bets):
            play_index.append(i)
            if self.draw_card():
                currentfunds.append(currentfunds[i-1] + betammount)
            else:
                currentfunds.append(currentfunds[i-1] - betammount)

        plt.plot(play_index,currentfunds)
        self.final_amounts.append(currentfunds[-1])

    def simulate(self, num_simulations):
        for i in range(num_simulations):
            self.play(self.bal, self.b, self.it)
        print("simulations complete")

    def graph(self):
        plt.ylabel('Player Money in $')
        plt.xlabel('Number of bets')
        plt.show()
        print(mean(self.final_amounts))
def main():
    mc1 = monte_carlo_simulation(52, 14, 10000, 5, 10001)
    mc1.simulate(100)
    mc1.graph()

main()
