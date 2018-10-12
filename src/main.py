import json
import random
import os

from strategy import *

class TLMVPCP:
    def __init__(self):
        self.question = None
        self.score = 0
        self.new_question()

    def new_question(self):
        with open('data.json') as f:
            data = json.load(f)
            data = data["results"]
            random_question = random.choice(data)
            self.question = Question(random_question)
    
    def setup_question(self):
        print(self.question.question)
        possibility = {1: "DUO", 2: "SQUARRE", 3: "CASH"}
        for key, val in possibility.items():
            print("{}. {}".format(key, val))
        
        i = int(input(">>> "))
        os.system('clear')
        if i == 1:
            strategy = StrategyDuo()
        elif i == 2:
            strategy = StrategySquare()
        else: 
            strategy = StrategyCash()
        self.question.set_strategy(strategy)
        return self.question.proposals_choices()
    
    def setup_proposals(self, proposals):
        print(self.question.question)
        for proposal in proposals:
            print("- {}".format(proposal))
        answer = str(input(">>> "))
        os.system('clear')
        return answer

    def run(self):
        try:
            while True:
                proposals = self.setup_question()
                answer = self.setup_proposals(proposals)
                if answer == self.question.correct_answer:
                    self.score += self.question.add_score()
                    print("Good answer, your score is now: {}".format(self.score))
                else:
                    print("Bad answer, try again! Your score is: {}".format(self.score))
                self.new_question()
        except Exception as e:
            print("Exit with score: {}. Congratulation".format(self.score))

        

        
    

if __name__ == '__main__':
    tlmvpcp = TLMVPCP()
    tlmvpcp.run()