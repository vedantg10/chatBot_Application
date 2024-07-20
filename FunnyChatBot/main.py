import openai
from dotenv import load_dotenv
from colorama import Fore
import os


# Constants
MODEL_ENGINE = "gpt-4o-mini"
MESSAGE_SYSTEM = "You are a helpful assistant"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]

# Load the environment variables - set up the OpenAI API client
load_dotenv()
client = openai.OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.Completion.create(
        engine=MODEL_ENGINE,
        messages=messages,
        max_tokens=150,
    )
    message = response.choices[0].message
    messages.append(message)
    print(Fore.GREEN + "Bot: " + messages.choices[0].messag.content)


def main():
    while True:
        print("\n")
        print("----------------------------------------\n")
        print(" *** 🤖 WELCOME TO THE AI-CHATBOT *** ")
        print("\n----------------------------------------")
        print("\n================* MENU *================\n")
        print("[1]- Start Chat")
        print("[2]- Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_chat()
        elif choice == "2":
            exit()
        else:
            print("Invalid choice")


def start_chat():
    print("to end chat, type 'x'")
    print("\n")
    print("      NEW CHAT       ")
    print("---------------------")

    while True:
        user_input = input(Fore.WHITE + "You: ")

        if user_input.lower() == "x":
            main()
            break
        else:
            generate_chat_completion(user_input)


if __name__ == "__main__":
    main()
