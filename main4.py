import tkinter as tk
from tkinter import scrolledtext
import random

# Knowledge base
responses = {
    "hello": ["Hi there!", "Hello! How can I help you?", "Hey! What's up?"],
    "how are you": ["I'm doing great!", "Feeling like a bot should—awesome!", "All good, thanks for asking!"],
    "your name": ["My name is PyBot.", "You can call me PyBot!", "I'm PyBot, your assistant."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
}

def get_response(user_msg):
    user_msg = user_msg.lower()
    for key in responses:
        if key in user_msg:
            return random.choice(responses[key])
    return "Sorry, I don't understand that."

# Tkinter UI
root = tk.Tk()
root.title("Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10)
chat_window.config(state=tk.DISABLED)

# Entry and send button
entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5, pady=5)

def send_message():
    user_msg = entry.get()
    if not user_msg.strip():
        return

    # Show user message
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")

    # Bot response
    bot_msg = get_response(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_msg + "\n\n", "bot")
    chat_window.config(state=tk.DISABLED)

    chat_window.see(tk.END)
    entry.delete(0, tk.END)

send_btn = tk.Button(root, text="Send", command=send_message, width=10, bg="lightblue")
send_btn.pack(side=tk.LEFT, pady=5)

# Text colour tags
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

root.mainloop()