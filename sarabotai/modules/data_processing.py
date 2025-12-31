from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader, SeleniumURLLoader
from config import Config

class DataProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=Config.DEFAULT_CHUNK_SIZE,
            chunk_overlap=Config.DEFAULT_CHUNK_OVERLAP
        )
    
    def process_urls(self, urls, use_selenium=False):
        try:
            if use_selenium:
                loader = SeleniumURLLoader(urls=urls)
            else:
                loader = UnstructuredURLLoader(urls=urls)
            
            data = loader.load()
            return self.text_splitter.split_documents(data)
        except Exception as e:
            raise Exception(f"Error processing URLs: {str(e)}")
    
    def process_text(self, text):
        try:
            return self.text_splitter.create_documents([text])
        except Exception as e:
            raise Exception(f"Error processing text: {str(e)}")