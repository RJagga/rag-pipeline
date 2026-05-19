from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":
    # docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")

    ## unless there's new data added no need to build vector store again
    # store.build_from_documents(docs)

    store.load()
    # print(store.query("How to play A minor chord?", top_k=3))

    rag_search = RAGSearch()
    query = "How to play A minor chord?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
    