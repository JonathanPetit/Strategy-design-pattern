import random
from abc import ABCMeta, abstractmethod

class Question(object):
    def __init__(self, question):
        self.strategy = None
        self.question = question["question"]
        self.incorrect_answers = question["incorrect_answers"]
        self.correct_answer = question["correct_answer"]
        self.difficuty = question["difficulty"]
        self.category = question["category"]

        self.proposals = []

    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def proposals_choices(self):
        return self.strategy.strategy_answer(self.incorrect_answers, self.correct_answer)
    
    def add_score(self):
        return self.strategy.score()

class QuestionStrategyAbstract(object, metaclass=ABCMeta):
    @abstractmethod
    def strategy_answer(self, incorrect_answers, correct_answer):
        pass

    @abstractmethod
    def score(self):
        pass

class StrategyDuo(QuestionStrategyAbstract):
    def strategy_answer(self, incorrect_answers, correct_answer):
        proposals = []
        choice = random.choice(incorrect_answers)
        proposals.append(choice)
        proposals.append(correct_answer)
        return proposals
    
    def score(self):
        return 1

class StrategySquare(QuestionStrategyAbstract):
    def strategy_answer(self, incorrect_answers, correct_answer):
        proposals = incorrect_answers
        proposals.append(correct_answer)
        return proposals

    def score(self):
        return 3

class StrategyCash(QuestionStrategyAbstract):
    def strategy_answer(self, incorrect_answers, correct_answer):
        proposals = []
        return proposals
    
    def score(self):
        return 5