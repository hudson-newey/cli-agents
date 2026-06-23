from src.message import Message


class Context:
    messages = []

    def add(self, *messages: Message):
        for m in messages:
            self.messages.append(m)

    def to_ollama__messages(self):
        return [{ "role": m.role, "content": m.content } for m in self.messages]
