import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables")
    

client = InferenceClient(token=api_key)
    
    
def consult_model(model_name, query):
    print(f"Consult to model {model_name.split('/')[-1]}...")
    
    try:
        response = client.chat_completion(
            model=model_name,
            messages=[
                {"role": "system", "content": "Answer briefly and technically."},
                {"role": "user", "content": query}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error en {model_name}: {e}"    



def main():
    question = "Explain in one sentence why there are so many capybaras in Nordelta, Argentina."
    
    models = [
        "meta-llama/Llama-3.2-1B-Instruct", 
        "mistralai/Mistral-7B-Instruct-v0.2",        
        "Qwen/Qwen2.5-7B-Instruct"              
    ]

    print("\n" + "="*50)
    print(f"QUESTION: {question}")
    print("="*50 + "\n")

    for mod in models:
        answer = consult_model(mod, question)
        print(f"ANSWER: {answer}")
        print("-" * 30)

if __name__ == "__main__":
    main()