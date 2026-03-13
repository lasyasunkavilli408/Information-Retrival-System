# Program: Ranked Retrieval of Documents using PageRank Algorithm

import networkx as nx

# Create a directed graph representing documents and hyperlinks
G = nx.DiGraph()

# Add hyperlinks between documents
# Example: Doc1 links to Doc2 and Doc3
G.add_edges_from([
    ("Doc1", "Doc2"),
    ("Doc1", "Doc3"),
    ("Doc2", "Doc3"),
    ("Doc3", "Doc1"),
    ("Doc4", "Doc3"),
    ("Doc4", "Doc2")
])

# Compute PageRank scores
pagerank_scores = nx.pagerank(G)

# Display ranking of documents
print("Document Ranking based on PageRank:\n")

for doc, score in pagerank_scores.items():
    print(f"{doc} : {score:.4f}")

# Sort documents by rank
print("\nDocuments sorted by importance:")

sorted_docs = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)

for doc, score in sorted_docs:
    print(doc, "->", score)
