from core.interpreter import interpret
from core.executor import execute

while True:
    user_input = input("You: ")
    if user_input == "___":
        break
    actions = interpret(user_input)
    execute(actions)
