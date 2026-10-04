import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Connect to OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Store conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are an AI Study Assistant for students. "
            "Explain concepts clearly and simply. "
            "Give examples when useful. "
            "Help students understand topics rather than just giving "
            "short answers. Be friendly, accurate and concise."
        )
    }
]


def ask_ai(user_question):
    """Send a question to the AI and return its response."""

    messages.append({
        "role": "user",
        "content": user_question
    })

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    answer = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": answer
    })

    return answer


def show_menu():
    print("\n" + "=" * 55)
    print("              AI STUDY ASSISTANT")
    print("=" * 55)
    print("1. Ask a Question")
    print("2. Explain a Topic Simply")
    print("3. Summarize Text")
    print("4. Generate a Quiz")
    print("5. Give Examples")
    print("6. Exit")
    print("=" * 55)


while True:

    show_menu()

    choice = input("Choose an option (1-6): ").strip()

    # Ask a general question
    if choice == "1":
        question = input("\nEnter your question: ")

        if question.strip():
            print("\nAI:", ask_ai(question))

    # Explain a topic
    elif choice == "2":
        topic = input("\nEnter the topic: ")

        if topic.strip():
            question = (
                f"Explain {topic} in very simple language "
                "with a clear example."
            )
            print("\nAI:", ask_ai(question))

    # Summarize text
    elif choice == "3":
        text = input("\nEnter the text you want to summarize: ")

        if text.strip():
            question = (
                "Summarize the following text in simple bullet points:\n\n"
                + text
            )
            print("\nAI:", ask_ai(question))

    # Generate quiz
    elif choice == "4":
        topic = input("\nEnter the topic for the quiz: ")

        if topic.strip():
            question = (
                f"Create 5 multiple-choice questions about {topic}. "
                "Give four options for each question and provide "
                "the correct answer after each question."
            )
            print("\nAI:", ask_ai(question))

    # Give examples
    elif choice == "5":
        topic = input("\nEnter the topic: ")

        if topic.strip():
            question = (
                f"Give 3 easy and practical examples to explain {topic}."
            )
            print("\nAI:", ask_ai(question))

    # Exit
    elif choice == "6":
        print("\nThank you for using AI Study Assistant!")
        print("Keep learning! 👋")
        break

    else:
        print("\nInvalid option. Please choose between 1 and 6.")

    input("\nPress Enter to continue...")