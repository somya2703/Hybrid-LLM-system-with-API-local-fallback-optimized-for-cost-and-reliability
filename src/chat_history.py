class ChatHistory:

    def __init__(self):
        self.history = []

    def add(self, question, answer):
        self.history.append(
            {"question": question, "answer": answer}
        )

    def get(self):
        return self.history