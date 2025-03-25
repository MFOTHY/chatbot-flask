import os
import openai

# Aqui tomas la clave de variable de entorno (o la dejas vacía):
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("Hola Chatbot")

if __name__ == "__main__":
    main()

