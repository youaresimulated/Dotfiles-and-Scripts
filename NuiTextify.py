import tkinter as tk
from tkinter import scrolledtext

def replace_apostrophes(content):
    content = content.replace('’', '\'') 
    content = content.replace('‘', '\'')  
    content = content.replace('′', '\'')  
    content = content.replace('ʼ', '\'')  
    return content

def process_text():
    input_text = text_box.get("1.0", tk.END)
    processed_text = input_text.replace('\r\n', '\n').replace('\r', '\n')
    processed_text = replace_apostrophes(processed_text)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, processed_text)

root = tk.Tk()
root.title("somebsdiscordname's Text-to-NUI Replacer")
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
text_box.pack(padx=10, pady=10)
process_button = tk.Button(root, text="Process and Replace Text", command=process_text)
process_button.pack(pady=10)
root.mainloop()