import tkinter as tk
import time
import random

class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")

        self.sentences = self.load_sentences_from_file("sentences.txt")
        self.current_sentence_index = 0
        self.typing_start_time = None

        self.label = tk.Label(master, text="", wraplength=400)
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind("<Key>", self.start_typing_test)

        self.typing_speed_label = tk.Label(master, text="Typing speed: 0 WPM")
        self.typing_speed_label.pack()

        self.next_button = tk.Button(master, text="Next Sentence", command=self.next_sentence)
        self.next_button.pack()

        self.display_next_sentence()
        self.update_typing_speed()

    def load_sentences_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            sentences = [line.strip() for line in file]
        return sentences

    def display_next_sentence(self):
        self.label.config(text=self.sentences[self.current_sentence_index])
        self.current_sentence_index = (self.current_sentence_index + 1) % len(self.sentences)

    def start_typing_test(self, event):
        if not self.typing_start_time:
            self.typing_start_time = time.time()

    def update_typing_speed(self):
        if self.typing_start_time:
            typing_time = time.time() - self.typing_start_time
            typed_text = self.entry.get()
            typed_words = typed_text.split()
            if typing_time > 0:
                typing_speed = len(typed_words) / (typing_time / 60)
                self.typing_speed_label.config(text=f"Typing speed: {typing_speed:.2f} WPM")
        self.master.after(100, self.update_typing_speed)

    def stop_typing_test(self, event):
        if self.typing_start_time:
            typing_time = time.time() - self.typing_start_time
            typed_text = self.entry.get()
            typed_words = typed_text.split()
            if typing_time > 0:
                typing_speed = len(typed_words) / (typing_time / 60)
                print(f"Typing speed: {typing_speed:.2f} WPM")
            self.typing_start_time = None

    def next_sentence(self):
        self.display_next_sentence()
        self.entry.delete(0, tk.END)
        self.typing_start_time = None
        self.typing_speed_label.config(text="Typing speed: 0 WPM")

def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.bind("<Return>", app.stop_typing_test)
    root.mainloop()

if __name__ == "__main__":
    main()
