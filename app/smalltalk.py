import os
from groq import Groq

groq_client = Groq()

def talk(query):
    prompt = f'''You are a helpful and friendly chatbot designed for small talk. You can answer questions about the weather, your name, your purpose, and more.
    
    QUESTION: {query}
    '''
    completion = groq_client.chat.completions.create(
        model=os.environ['GROQ_MODEL'],
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    return completion.choices[0].message.content