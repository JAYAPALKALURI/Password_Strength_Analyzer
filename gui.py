# gui.py
import tkinter as tk
from analyzer import analyze_password
from wordlist_generator import generate_wordlist, save_wordlist

def analyze():
    pwd = password_entry.get()
    result = analyze_password(pwd)
    output.delete('1.0', tk.END)
    output.insert(tk.END, f"Score: {result['score']}/4\n")
    output.insert(tk.END, f"Crack Time: {result['crack_time']}\n")
    output.insert(tk.END, "Suggestions:\n")
    for s in result['suggestions']:
        output.insert(tk.END, f" - {s}\n")

def generate():
    inputs = input_entry.get().split()
    wordlist = generate_wordlist(inputs)
    save_wordlist(wordlist)
    output.delete('1.0', tk.END)
    output.insert(tk.END, f"Generated {len(wordlist)} words.\nSaved to file.")

root = tk.Tk()
root.title("Password Analyzer & Wordlist Generator")

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root)
password_entry.pack()

tk.Button(root, text="Analyze Password", command=analyze).pack()

tk.Label(root, text="Custom Inputs (space separated):").pack()
input_entry = tk.Entry(root)
input_entry.pack()

tk.Button(root, text="Generate Wordlist", command=generate).pack()

output = tk.Text(root, height=10)
output.pack()

root.mainloop()
