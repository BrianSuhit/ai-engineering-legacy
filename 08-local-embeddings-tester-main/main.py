from sentence_transformers import SentenceTransformer

# Load the pre-trained sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# List of sentences to be encoded into embeddings
sentences = [
    "Artificial intelligence seeks to replicate human cognitive abilities.",
    "The AI Engineer integrates language models into software applications.",
    "Alignment ensures that AI follows human values and goals.",
    "Sycophancy is when a model lies to please the user.",
    "To make a barbecue, you need wood, meat, and a lot of patience."
]

# Generate embeddings for the sentences
embeddings_array = model.encode(sentences)
print("Embeddings array")

# Define the search query
query = "what is sycophancy?"
print(f"\n🔎 Searching for: '{query}'")

# Encode the query into a vector
query_vector = model.encode([query])

# Calculate similarity scores between the query vector and the sentence embeddings
scores = model.similarity(query_vector, embeddings_array)

print("-" * 50)

# Iterate through the results and print the score for each document
for i in range(len(sentences)):
    score = scores[0][i].item() # Get the raw score from the tensor
    print(f"Score: {score:.4f} | Document: {sentences[i]}")