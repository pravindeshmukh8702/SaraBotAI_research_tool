import pandas as pd
import plotly.express as px
from langchain.schema import Document

class Visualizer:
    @staticmethod
    def generate_word_frequency_chart(documents):
        if not documents:
            return None
            
        words = " ".join([doc.page_content for doc in documents]).split()
        word_freq = pd.Series(words).value_counts().reset_index()
        word_freq.columns = ['word', 'count']
        
        # Filter short words and non-alphabetic
        word_freq = word_freq[
            (word_freq['word'].str.len() >= 4) & 
            (word_freq['word'].str.isalpha())
        ].head(10)
        
        if word_freq.empty:
            return None
            
        fig = px.bar(
            word_freq, 
            x='word', 
            y='count', 
            title="Frequent Terms in Articles",
            color='count'
        )
        fig.update_layout(
            xaxis_title="Terms",
            yaxis_title="Frequency",
            plot_bgcolor='rgba(0,0,0,0)'
        )
        return fig