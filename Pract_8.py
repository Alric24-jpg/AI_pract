import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

chatbot = Chat([
    [r"hi|hello|hey", ["Hello! How can I assist you?", "Hi there! How can I help?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing fine!", "I'm always good!"]],
    [r"(.*) your name?", ["I'm a chatbot, here to assist you."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]],
    [r"(.*)", ["I'm not sure how to respond. Could you rephrase?"]]
], reflections)

def send():
    msg = entry.get()
    history.insert(tk.END, f"You: {msg}\nBot: {chatbot.respond(msg)}\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Chatbot")

history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
history.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

tk.Button(root, text="Send", command=send).pack(pady=5)

root.mainloop()