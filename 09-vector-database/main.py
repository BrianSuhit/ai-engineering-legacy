import chromadb

client = chromadb.PersistentClient(path=".chromadb")

my_collection = client.get_or_create_collection(name="my_collection")

# Define the documents to be added to the collection.
# These are the pieces of text we want to search through.
documents = [
    "Artificial intelligence seeks to replicate human cognitive abilities.",
    "The AI Engineer integrates language models into software applications.",
    "Alignment ensures that AI follows human values and goals.",
    "Sycophancy is when a model lies to please the user.",
    "To make a barbecue, you need firewood, meat, and a lot of patience."
]

# Assign a unique ID to each document.
ids=["id1", "id2", "id3", "id4", "id5"]

# Add the documents and their corresponding IDs to the collection.
# This process will convert the text into vector embeddings and store them.
my_collection.add(documents=documents, ids=ids)

# Define the search query.
query = "What is sycophancy?"
print(f"\n🔎 Searching the database for: '{query}'")

# Perform a query on the collection.
# This will find the most similar documents to the query text.
results = my_collection.query(
    query_texts=[query],
    n_results=2  # We want the top 2 most similar results.
)

# Print the results of the query.
print("-" * 50)
for i in range(len(results['documents'][0])):
    document = results['documents'][0][i]
    distance = results['distances'][0][i]
    print(f"Distance: {distance:.4f} | Found: {document}")
print("-" * 50)