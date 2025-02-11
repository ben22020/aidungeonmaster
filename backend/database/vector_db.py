import chromadb
import uuid
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chromadb")
model = SentenceTransformer("all-MiniLM-L6-v2")

npc_memory_collection = client.get_or_create_collection("npc_memory")
world_memory_collection = client.get_or_create_collection("quests")


def store_npc_memory(npc_id, user_input, npc_reply):
    vector = model.encode(f"Player: {user_input} | NPC: {npc_reply}").tolist()
    npc_memory_collection.add(ids=[npc_id], embeddings=[vector], metadatas=[{"memory": user_input + " | " + npc_reply}])

def store_world_memory(events: list):
    """Store a world event in the vector database"""
    ids = [str(uuid.uuid4()) for _ in events]
    vectors = model.encode([events])
    world_memory_collection.add(
        ids=ids,
        embeddings=[vec.tolist() for vec in vectors],  # Convert vectors to lists
        metadatas=[{"event": event} for event in events]
    )

def retrieve_relevant_world_events(query: str, top_k=3):
    """Retrieve relevant world events from ChromaDB based on query."""
    query_vector = model.encode(query).tolist()
    
    results = world_memory_collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    # Extract metadata (event descriptions)
    return [item["event"] for item in results["metadatas"][0]] if results["metadatas"] else []