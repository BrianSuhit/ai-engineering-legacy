import os
import chromadb
from google import genai
from dotenv import load_dotenv

# --- 1. Setup & Initialization ---
# Load environment variables (e.g., GOOGLE_API_KEY)
load_dotenv()

# Initialize the Gemini client for generation and ChromaDB for vector storage
client_gemini = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
client_chroma = chromadb.PersistentClient(path=".chromadb")

# --- 2. Database & Ingestion ---
# Create or retrieve the collection where embeddings will be stored
collection = client_chroma.get_or_create_collection(name="my_collection")

# Define the knowledge base (documents) to be indexed
documents_data = [
    "Brian Suhit is studying for the TUDAI technical degree at UNICEN.",
    "Brian's specialty is AI Engineering.",
    "Brian knows how to use Python, HTML, CSS, and Git.",
    "The RAG project is node 10 of Brian's roadmap."
]

ids=["id1", "id2", "id3", "id4"]

# Add documents to the vector database (Embedding happens automatically here)
collection.add(documents=documents_data, ids=ids)

# --- 3. Retrieval (The 'R' in RAG) ---
question = "What is Brian studying and at which university?"
print(f"❓ User asks: {question}")

# Query the database for the most relevant documents
search_results = collection.query(query_texts=[question], n_results=2)
retrieved_context = " ".join(search_results['documents'][0])

print(f"🔍 Information found in DB (Multi-document):")
print(f"{retrieved_context}")

# --- 4. Augmentation (The 'A' in RAG) ---
# Construct a prompt that includes the retrieved context
final_prompt = f"""
Use the following information to answer the user's question.
If the information is not sufficient, say you don't know.

COMPLEMENTARY INFORMATION:
{retrieved_context}

USER QUESTION:
{question}
"""

print("🧠 Gemini is drafting the response...")

# --- 5. Generation (The 'G' in RAG) ---
# Generate the final answer using the LLM
response = client_gemini.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=final_prompt
)

print("\n" + "="*40)
print("🤖 FINAL AI RESPONSE:")
print("="*40)
print(response.text)