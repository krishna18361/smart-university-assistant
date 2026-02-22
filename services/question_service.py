from services.db_service import save_question


def process_question(question: str):

    answer = "This is a dummy response from service layer."

    # Save to database
    save_question(question, answer)

    return {
        "question": question,
        "answer": answer
    }