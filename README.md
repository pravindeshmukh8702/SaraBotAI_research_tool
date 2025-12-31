# SaraBot AI: Advanced Research Tool 🤖

SaraBot AI is an intelligent research assistant powered by Google's Gemini AI that helps you extract, process, and analyze information from web articles and documents. It uses Retrieval-Augmented Generation (RAG) technology to provide accurate, source-cited answers to your questions.

---

## 🚀 Features

- **🔑 Secure API Key Management**: Enter your API key directly in the application interface
- **📚 Multi-URL Processing**: Process up to 3 URLs or upload text files
- **🔍 Semantic Search**: Advanced vector-based search using ChromaDB and HuggingFace embeddings
- **💬 Conversational AI**: Chat with your documents using Gemini 1.5 Pro
- **📊 Summary Reports**: Generate comprehensive analysis reports
- **📈 Topic Visualization**: Visualize frequent terms and topics
- **💾 Session Management**: Manage multiple research sessions
- **📥 Export Options**: Download reports and chat history

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 1.5 Pro
- **Vector Database**: ChromaDB
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **Document Processing**: LangChain
- **Visualization**: Plotly
- **Web Scraping**: BeautifulSoup, Unstructured, Selenium

---

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.8 or higher** installed on your system
2. **Google Gemini API Key** - Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Internet connection** for downloading models and processing URLs

---

## 📦 Installation

### Step 1: Clone or Download the Project

If you have the project URL:
```bash
git clone <your-project-url>
cd genai-research-tool-fastapi-langchain-main
```

Or if you downloaded the ZIP file:
1. Extract the ZIP file to your desired location
2. Open a terminal/command prompt in the extracted folder

### Step 2: Create a Virtual Environment (Recommended)

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- streamlit
- google-generativeai
- langchain
- chromadb
- sentence-transformers
- pandas
- plotly
- beautifulsoup4
- requests
- python-dotenv
- unstructured
- selenium

**Note**: The first time you run the application, it will download the HuggingFace embedding model (~80MB), which may take a few minutes.

---

## 🚀 Running the Application

### Step 1: Start the Application

In your terminal/command prompt (with virtual environment activated), run:

```bash
streamlit run SaraBotAI.py
```

### Step 2: Access the Application

The application will automatically open in your default web browser at:
```
http://localhost:8501
```

If it doesn't open automatically, copy the URL shown in the terminal and paste it into your browser.

---

## 📖 Step-by-Step Usage Guide

### Step 1: Configure Your API Key

1. **Get Your API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key" or "Get API Key"
   - Copy your API key

2. **Enter API Key in the Application**:
   - Look for the **"🔑 API Key Configuration"** panel in the left sidebar
   - Paste your API key in the password field
   - Click **"Save API Key"**
   - You should see a success message: "✅ API key saved successfully!"

**Important**: Your API key is stored only in your browser session and is never saved to disk. You'll need to enter it again if you refresh the page or start a new session.

### Step 2: Add Content to Process

You have two options:

#### Option A: Manual URL Entry
1. In the sidebar, find **"📝 Article URLs"** section
2. Select **"Manual Entry"** as the input method
3. Enter up to 3 URLs (one per field)
4. URLs must start with `http://` or `https://`
5. Click **"Process URLs/Text"** button

#### Option B: File Upload
1. In the sidebar, find **"📝 Article URLs"** section
2. Select **"File Upload"** as the input method
3. Click **"Browse files"** and select a `.txt` file
4. The file can contain:
   - URLs (one per line)
   - Plain text content
5. Click **"Process URLs/Text"** button

### Step 3: Wait for Processing

- The application will:
  - Fetch content from URLs or read your file
  - Split the content into chunks
  - Create embeddings and store them in a vector database
  - Display processed articles in the main area

- Processing time depends on:
  - Number of URLs
  - Size of content
  - Your internet speed

- You'll see a success message when processing is complete: "✅ URLs processed successfully!"

### Step 4: Ask Questions

1. Scroll down to the chat input at the bottom of the page
2. Type your question in the input box (e.g., "What are the main points discussed?")
3. Press Enter or wait for the response
4. The AI will:
   - Search through the processed content
   - Find relevant information
   - Generate an answer with context
   - Show source citations

### Step 5: Explore Additional Features

#### Generate Summary Report
1. Click on the **"📊 Summary Report"** tab
2. Click **"Generate Report"** button
3. View the comprehensive analysis
4. Click **"Download Report as Markdown"** to save it

#### Topic Analysis
1. Click on the **"🔍 Topic Analysis"** tab
2. View the visualization of frequent terms
3. The chart shows the top 10 most common words

#### Quick Actions
1. Click on the **"⚡ Quick Actions"** tab
2. Available actions:
   - **Clear Conversation History**: Remove all chat history
   - **Export Chat History**: Download conversation as JSON
   - **Reset Vector Database**: Clear all processed content
   - **Show API Usage**: View current configuration

---

## ⚙️ Advanced Settings

In the sidebar, expand **"⚙️ Advanced Settings"** to customize:

- **Chunk Size** (500-2000): Size of text chunks for processing (default: 1000)
- **Chunk Overlap** (0-500): Overlap between chunks for better context (default: 100)
- **Model Temperature** (0.0-1.0): Controls randomness in responses (default: 0.7)
  - Lower = more focused, Higher = more creative
- **Max Results** (1-10): Number of relevant chunks to retrieve (default: 3)
- **Use Selenium**: Enable for JavaScript-heavy websites (requires Chrome/Chromium)

---

## 🔧 Session Management

- **New Session**: Click "New Session" to start fresh
  - Clears processed URLs
  - Resets conversation history
  - Creates a new session ID
- **Session ID**: Each session has a unique ID for tracking

---

## 📁 Project Structure

```
genai-research-tool-fastapi-langchain-main/
│
├── SaraBotAI.py              # Main application file (RUN THIS)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
├── sarabotai/                # Modular components (optional)
│   ├── config.py             # Configuration settings
│   ├── main.py               # Alternative entry point (incomplete)
│   ├── modules/              # Feature modules
│   │   ├── gemini_integration.py
│   │   ├── data_processing.py
│   │   ├── vector_store.py
│   │   ├── visualization.py
│   │   └── web_scraper.py
│   └── utils/                # Utility functions
│       └── session_manager.py
│
└── chroma_db_*/              # Vector databases (created automatically)
```

---

## ❓ Troubleshooting

### Issue: "Failed to initialize embeddings"
**Solution**: 
- Ensure you have internet connection (first run downloads models)
- Check if you have enough disk space (~500MB)
- Try restarting the application

### Issue: "Invalid API key"
**Solution**:
- Verify your API key is correct (no extra spaces)
- Check if the API key is active in Google AI Studio
- Try generating a new API key

### Issue: "Error processing URLs"
**Solution**:
- Verify URLs are accessible and start with http:// or https://
- Check your internet connection
- For JavaScript-heavy sites, enable "Use Selenium" in Advanced Settings
- Some sites may block automated access

### Issue: "No relevant information found"
**Solution**:
- Try rephrasing your question
- Ensure content was processed successfully
- Check if your question relates to the processed content
- Increase "Max Results" in Advanced Settings

### Issue: Application won't start
**Solution**:
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)
- Try: `pip install --upgrade streamlit`

### Issue: Port 8501 already in use
**Solution**:
- Close other Streamlit applications
- Or run on a different port: `streamlit run SaraBotAI.py --server.port 8502`

---

## 🔒 Security & Privacy

- **API Keys**: Your API key is stored only in your browser session (session state)
- **Data**: Processed content is stored locally in `chroma_db_*` folders
- **No Cloud Storage**: All data remains on your local machine
- **Session-based**: Data is cleared when you start a new session or close the browser

---

## 📝 Notes

- The application uses **ChromaDB** for vector storage, which creates local database files
- These files are automatically cleaned up when you start a new session
- On Windows, you may see file locking warnings - this is normal and can be ignored
- The first run will download embedding models (~80MB) - ensure you have internet connection

---

## 🎯 Example Use Cases

1. **Research Papers**: Process multiple research paper URLs and ask questions
2. **News Articles**: Analyze news articles and generate summaries
3. **Document Analysis**: Upload text files and extract key information
4. **Content Summarization**: Get quick summaries of long articles
5. **Question Answering**: Ask specific questions about processed content

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developers

Developed by **PRAVIN & RUTURAJ**

---

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review the error messages in the application
3. Ensure all prerequisites are met
4. Verify your API key is valid

---

## 🎉 Getting Started Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Google Gemini API key obtained
- [ ] Application started (`streamlit run SaraBotAI.py`)
- [ ] API key configured in the application
- [ ] First URL processed successfully
- [ ] First question asked and answered

**Happy Researching! 🚀**
