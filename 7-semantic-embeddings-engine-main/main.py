import os
from google import genai
from dotenv import load_dotenv
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

documents = [
    "Artificial intelligence seeks to replicate human cognitive abilities",
    "The AI Engineer integrates language models into software applications",
    "Alignment ensures that AI follows human values and goals",
    "Sycophancy is when a model lies to please the user",
    "To make a barbecue you need firewood, meat and a lot of patience"
]

def get_embeddings(texts):
    """Generates embedding vectors for a list of texts.

    Args:
        texts: A list of strings.

    Returns:
        A numpy array where each row is the embedding vector for the
        corresponding text.
    """
    print(f"🛰️ Requesting vectors for {len(texts)} sentences...")

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts
    )
    return np.array([item.values for item in response.embeddings])

    
def search(query, documents, vector_matrix):
    """Searches for a query within a list of documents by comparing vectors.

    Args:
        query: The search query string.
        documents: The list of documents to search within.
        vector_matrix: The numpy matrix with the document vectors.
    """
    print(f"\n🔎 Searching for: '{query}'")
    
    query_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    query_vector = np.array(query_response.embeddings[0].values)


    scores = np.dot(vector_matrix, query_vector)

    print("-" * 50)
    for i in range(len(documents)):
        print(f"Score: {scores[i]:.4f} | {documents[i]}")

if __name__ == "__main__":
    vector_matrix = get_embeddings(documents)
    
    print("\n✅ Vectors received successfully!")
    print(f"Matrix shape: {vector_matrix.shape}")
    
    search("What is sycophancy?", documents, vector_matrix)
    search("How to make a barbecue?", documents, vector_matrix)