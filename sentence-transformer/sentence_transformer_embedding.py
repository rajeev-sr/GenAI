from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]

embeddings=model.encode(sentences)

print(embeddings.shape)
print(embeddings)

similarities = model.similarity(embeddings, embeddings)
print(similarities)
