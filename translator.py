from googletrans import Translator

# Initialize the Translator object
translator = Translator()

# Function to translate text
def translate_text(input_text, target_language):
    try:
        # Automatically detect the source language
        detected_language = translator.detect(input_text).lang
        # Perform the translation
        translation = translator.translate(input_text, src=detected_language, dest=target_language)
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"
