# Do not use. Prefer to use instance-bound messages
# e.g. UserMessage or AgentMessage
class Message:
    role = ""
    content = ""

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class UserMessage(Message):
    def  __init__(self, content: str):
        super().__init__("user", content)

class AgentMessage(Message):
    def  __init__(self, content: str):
        super().__init__("assistant", content)
