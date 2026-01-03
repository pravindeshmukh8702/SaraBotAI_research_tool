import os
import shutil
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import Config

class VectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        self.db_path = Config.CHROMA_PERSIST_DIR
        self.collection_name = Config.CHROMA_COLLECTION_NAME
    
    def create_store(self, documents):
        try:
            # Clear existing database
            if os.path.exists(self.db_path):
                shutil.rmtree(self.db_path)
                
            return Chroma.from_documents(
                documents,
                self.embeddings,
                persist_directory=self.db_path,
                collection_name=self.collection_name
            )
        except Exception as e:
            raise Exception(f"Error creating vector store: {str(e)}")
    
    def get_store(self):
        try:
            if os.path.exists(self.db_path):
                return Chroma(
                    persist_directory=self.db_path,
                    embedding_function=self.embeddings,
                    collection_name=self.collection_name
                )
            return None
        except Exception as e:
            raise Exception(f"Error loading vector store: {str(e)}")
    
    def search(self, query, k=Config.MAX_RESULTS):
        store = self.get_store()
        if store:
            return store.similarity_search(query, k=k)
        return []