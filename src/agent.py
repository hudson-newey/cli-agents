from ollama import chat

class Agent:
    def send(self, message: str):
        stream = chat(
            model="gemma4:e2b",
            messages=[{"role": "user", "content": message}],
            think=False,
            stream=True,
        )

        for chunk in stream:
            if "message" in chunk:
                print(chunk.message.content, end="", flush=True)
