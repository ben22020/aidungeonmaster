import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chromadb")
model = SentenceTransformer("all-MiniLM-L6-v2")

npc_memory_collection = client.get_or_create_collection("npc_memory")
world_memory_collection = client.get_or_create_collection("quests")


def store_npc_memory(npc_id, user_input, npc_reply):
    vector = model.encode(f"Player: {user_input} | NPC: {npc_reply}").tolist()
    npc_memory_collection.add(ids=[npc_id], embeddings=[vector], metadatas=[{"memory": user_input + " | " + npc_reply}])

def store_world_memory(event):
    vector = model.encode(f"Event: {event}").tolist()
    world_memory_collection.add(emeddings=[vector], metadatas = [{"event": event}])