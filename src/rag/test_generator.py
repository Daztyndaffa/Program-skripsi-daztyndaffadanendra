from src.rag.generator import generate_answer

while True:

    question = input("\nTanya AI > ")

    if question.lower() == "exit":
        break

    answer = generate_answer(question)

    print("\nAI Assistant:\n")
    print(answer)