def process_question(question: str):

    # This is where business logic lives
    # Later this will connect to database and LLM

    answer = "This is a dummy response from service layer."

    return {
        "question": question,
        "answer": answer
    }
