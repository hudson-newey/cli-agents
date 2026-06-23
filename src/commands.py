import sys

def close_session():
    sys.exit()

INBUILT_COMMANDS = {
    "/exit": close_session,
    "/close": close_session,
    "/bye": close_session,
}

class Commands:
    @staticmethod
    def handle(command: str):
        if command not in INBUILT_COMMANDS:
            return

        INBUILT_COMMANDS[command]()
