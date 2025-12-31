import uuid
import json
from datetime import datetime
from langchain.memory import ConversationBufferMemory

class SessionManager:
    def __init__(self):
        self.session_id = str(uuid.uuid4())[:8]
        self.conversation_history = []
        self.processed_articles = []
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    def new_session(self):
        self.session_id = str(uuid.uuid4())[:8]
        self.conversation_history = []
        self.processed_articles = []
        self.memory.clear()
    
    def add_conversation(self, question, answer, context=None):
        self.conversation_history.append({
            "question": question,
            "answer": answer,
            "context": context,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    def export_chat_history(self):
        return json.dumps(self.conversation_history, indent=2)
    
    def add_processed_article(self, article_metadata):
        self.processed_articles.append(article_metadata)