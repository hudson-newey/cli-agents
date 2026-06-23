from src.agent import Agent
from src.commands import Commands


class UI:
    @staticmethod
    def run():
        agent = Agent()

        while True:
            user_input: str = input("> ")

            Commands.handle(user_input)

            agent.send(user_input)
            print("")
