from ollama import chat
from src.context import Context
from src.message import AgentMessage, UserMessage

class Agent:
    context = Context()

    def send(self, message: str):
        user_message = UserMessage(message)
        self.context.add(user_message)

        chat_context = self.context.to_ollama__messages()
        stream = chat(
            model="gemma4:e2b",
            messages=chat_context,
            think=False,
            stream=True,
        )

        agent_response = ""
        for chunk in stream:
            if "message" in chunk:
                content = chunk.message.content
                print(content, end="", flush=True)
                agent_response = agent_response + content

        agent_message = AgentMessage(agent_response)
        self.context.add(agent_message)

        # terminate single line output with a newline
        print("")
