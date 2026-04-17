from src.rag.generator import generate_answer


def main():

    print("\n=== AI Assistant Universitas Islam Riau ===")

    while True:

        question = input("\nMahasiswa > ")

        if question.lower() in ["exit", "quit"]:
            print("Terima kasih.")
            break

        answer = generate_answer(question)

        print("\nAI Assistant >")
        print(answer)


if __name__ == "__main__":
    main()