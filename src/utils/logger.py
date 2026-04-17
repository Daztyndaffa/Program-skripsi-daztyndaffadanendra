import csv
import os
from datetime import datetime


LOG_FILE = "logs/chat_history.csv"


def save_chat(question, answer):

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "question", "answer"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            answer
        ])