# main.py
import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(
    page_title="SaraBotAI: News Research Tool",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Now import other modules
from modules import gemini_integration, data_processing, vector_store, web_scraper
from utils import session_manager
import os

# Apply dark theme with red/white scheme
def apply_dark_theme():
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: #0E1117;
            color: white;
        }}
        .stTextInput>div>div>input {{
            color: white;
            background-color: #262730;
        }}
        .stButton>button {{
            background-color: #FF4B4B;
            color: white;
            border: none;
        }}
        .stButton>button:hover {{
            background-color: #FF3030;
        }}
        .stSelectbox>div>div {{
            background-color: #262730;
            color: white;
        }}
        [data-testid="stSidebar"] {{
            background-color: #1A1A1A !important;
        }}
        .stExpander {{
            background-color: #262730;
            border-color: #FF4B4B;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #FF4B4B;
            color: white !important;
        }}
    </style>
    """, unsafe_allow_html=True)

# Initialize components after theme
apply_dark_theme()
gemini = gemini_integration.GeminiIntegration()
data_processor = data_processing.DataProcessor()
vector_db = vector_store.VectorStore()
scraper = web_scraper.WebScraper()
session = session_manager.SessionManager()

# Rest of your code remains the same...

# Apply dark theme with red/white scheme
def apply_dark_theme():
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: #0E1117;
            color: white;
        }}
        .stTextInput>div>div>input {{
            color: white;
            background-color: #262730;
        }}
        .stButton>button {{
            background-color: #FF4B4B;
            color: white;
            border: none;
        }}
        .stButton>button:hover {{
            background-color: #FF3030;
        }}
        .stSelectbox>div>div {{
            background-color: #262730;
            color: white;
        }}
        [data-testid="stSidebar"] {{
            background-color: #1A1A1A !important;
        }}
        .stExpander {{
            background-color: #262730;
            border-color: #FF4B4B;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #FF4B4B;
            color: white !important;
        }}
    </style>
    """, unsafe_allow_html=True)

apply_dark_theme()

# UI Layout - Matching your screenshot exactly
st.set_page_config(
    page_title="SaraBotAI: News Research Tool",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Configuration - Reordered to match your screenshot
with st.sidebar:
    st.title("Configuration")
    
    # URL Input Section at Top
    with st.expander("📝 Article URLs", expanded=True):
        url_input_method = st.radio(
            "URL Input Method",
            ["Manual Entry", "File Upload"],
            horizontal=True
        )
        
        urls = []
        if url_input_method == "Manual Entry":
            for i in range(3):
                url = st.text_input(f"URL {i+1}", key=f"url_{i}")
                if url:
                    urls.append(url)
        else:
            uploaded_file = st.file_uploader("Upload text file", type=["txt"])
    
    # Process Button below URL inputs
    if st.button("Process URLs/Text", type="primary"):
        # Processing logic here
        pass
    
    # Advanced Settings at Bottom
    with st.expander("⚙️ Advanced Settings", expanded=False):
        use_selenium = st.checkbox("Use Selenium", value=False)
        temperature = st.slider("Model Temperature", 0.0, 1.0, 0.7, 0.1)
    
    # Session Management moved below Process button
    st.markdown("---")
    st.header("Session Management")
    if st.button("New Session"):
        session.new_session()
        st.rerun()
    st.info(f"Session ID: {session.session_id}")

# Main Content Area
st.title("SaraBotAI: Advanced News Research Tool")

# Tabs Layout - Exactly matching your screenshot
tab1, tab2, tab3 = st.tabs(["📊 Summary Report", "🔍 Topic Analysis", "⚡ Quick Actions"])

with tab1:
    st.header("Comprehensive Summary Report")
    if st.button("Generate Report"):
        # Report generation logic
        pass

with tab2:
    st.header("Topic Analysis")
    # Analysis logic here

with tab3:
    st.header("Quick Actions")
    # Quick actions logic here

# Question Input at Bottom - Matching your screenshot
st.text_input("Ask a Question About the Articles", 
             placeholder="What are the key points from these articles?")