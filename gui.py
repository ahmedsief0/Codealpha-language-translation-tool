import tkinter as tk
from tkinter import ttk
from translator import translate_text  # Import translate function from translator.py

# Function to handle translation button click
def on_translate_button_click():
    # Get the input text and target language
    input_text = text_to_translate.get("1.0", "end-1c")
    target_language = target_lang_combo.get()
    
    # Translate the text
    result = translate_text(input_text, target_language)
    
    # Display the result
    translated_text.delete("1.0", "end-1c")
    translated_text.insert("1.0", result)

# Create the main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("500x400")

# Label for the input text area
label = tk.Label(root, text="Enter text to translate:")
label.pack(pady=10)

# Text box for entering the text to translate
text_to_translate = tk.Text(root, height=5, width=40)
text_to_translate.pack(pady=10)

# Label for target language selection
target_lang_label = tk.Label(root, text="Select target language:")
target_lang_label.pack(pady=5)

# ComboBox for selecting target language
target_lang_combo = ttk.Combobox(root, values=['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh'])
target_lang_combo.set('en')  # Default language is English
target_lang_combo.pack(pady=5)

# Button to trigger the translation
translate_button = tk.Button(root, text="Translate", command=on_translate_button_click)
translate_button.pack(pady=10)

# Label for displaying the translated text
translated_label = tk.Label(root, text="Translated text:")
translated_label.pack(pady=5)

# Text box for displaying the translated text
translated_text = tk.Text(root, height=5, width=40)
translated_text.pack(pady=10)



root.mainloop()
