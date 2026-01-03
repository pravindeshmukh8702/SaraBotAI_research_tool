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

---

## ☁️ AWS EC2 Deployment Guide

Yes, you can absolutely run this project on a new AWS EC2 instance! Follow these steps to deploy SaraBot AI on AWS.

### Prerequisites for AWS Deployment

- AWS account with EC2 access
- Basic knowledge of SSH and Linux commands
- Google Gemini API Key (same as local setup)

---

### Step 1: Launch an EC2 Instance

1. **Log in to AWS Console** and navigate to EC2
2. **Click "Launch Instance"**
3. **Configure Instance:**
   - **Name**: `sarabot-ai` (or your preferred name)
   - **AMI**: Choose **Amazon Linux 2023** or **Ubuntu 22.04 LTS** (recommended)
   - **Instance Type**: 
     - Minimum: `t2.micro` (free tier eligible)
     - Recommended: `t3.small` or `t3.medium` (better performance)
   - **Key Pair**: Create new or select existing key pair (`.pem` file)
   - **Network Settings**: 
     - Allow SSH (port 22) from your IP
     - **Add Security Group Rule**: 
       - Type: Custom TCP
       - Port: 8501
       - Source: 0.0.0.0/0 (or your IP for security)
       - Description: Streamlit App
   - **Storage**: 20 GB minimum (recommended: 30 GB for models and data)
4. **Launch Instance**

---

### Step 2: Connect to Your EC2 Instance

**For Windows (PowerShell):**
```bash
# Navigate to folder containing your .pem key file
cd path\to\your\key\folder

# Set permissions (if needed)
icacls your-key.pem /inheritance:r

# Connect via SSH
ssh -i your-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
# For Ubuntu, use: ssh -i your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

**For macOS/Linux:**
```bash
# Set correct permissions
chmod 400 your-key.pem

# Connect via SSH
ssh -i your-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
# For Ubuntu, use: ssh -i your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

**Note**: Replace `YOUR_EC2_PUBLIC_IP` with your instance's public IPv4 address (found in EC2 console).

---

### Step 3: Update System and Install Python

**For Amazon Linux 2023:**
```bash
# Update system packages
sudo dnf update -y

# Install Python 3.11 and pip
sudo dnf install -y python3.11 python3.11-pip python3.11-devel

# Install build tools
sudo dnf install -y gcc gcc-c++ make git

# Verify Python installation
python3.11 --version
```

**For Ubuntu 22.04:**
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3.11 and pip
sudo apt install -y python3.11 python3.11-pip python3.11-venv python3.11-dev

# Install build tools
sudo apt install -y build-essential gcc g++ make git

# Verify Python installation
python3.11 --version
```

---

### Step 4: Install Additional Dependencies

**For Amazon Linux:**
```bash
# Install additional libraries needed for some packages
sudo dnf install -y libffi-devel openssl-devel
```

**For Ubuntu:**
```bash
# Install additional libraries
sudo apt install -y libffi-dev libssl-dev
```

---

### Step 5: Upload Project to EC2 Instance

**Option A: Using SCP (from your local machine)**

```bash
# From your local machine (Windows PowerShell)
scp -i your-key.pem -r "C:\path\to\genai-research-tool-fastapi-langchain-main" ec2-user@YOUR_EC2_PUBLIC_IP:/home/ec2-user/

# For Ubuntu, replace ec2-user with ubuntu
scp -i your-key.pem -r "C:\path\to\genai-research-tool-fastapi-langchain-main" ubuntu@YOUR_EC2_PUBLIC_IP:/home/ubuntu/
```

**Option B: Using Git (if your project is on GitHub)**

```bash
# On EC2 instance
cd ~
git clone YOUR_GITHUB_REPO_URL
cd genai-research-tool-fastapi-langchain-main
```

**Option C: Using ZIP file upload**

1. Zip your project folder locally
2. Upload via SCP:
```bash
scp -i your-key.pem your-project.zip ec2-user@YOUR_EC2_PUBLIC_IP:/home/ec2-user/
```
3. On EC2 instance:
```bash
cd ~
unzip your-project.zip
cd genai-research-tool-fastapi-langchain-main
```

---

### Step 6: Set Up Python Virtual Environment

```bash
# Navigate to project directory
cd ~/genai-research-tool-fastapi-langchain-main

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip setuptools wheel
```

---

### Step 7: Install Project Dependencies

```bash
# Make sure virtual environment is activated (you should see (venv) in prompt)
pip install -r requirements.txt

# Note: This will take several minutes as it downloads:
# - HuggingFace embedding models (~80MB)
# - ChromaDB dependencies
# - All other required packages
```

**If you encounter errors:**
- For `chromadb` issues: `pip install chromadb --no-cache-dir`
- For `sentence-transformers` issues: `pip install sentence-transformers --no-cache-dir`
- For `unstructured` issues: `pip install unstructured --no-cache-dir`

---

### Step 8: Configure Streamlit for External Access

```bash
# Create Streamlit config directory
mkdir -p ~/.streamlit

# Create config file
cat > ~/.streamlit/config.toml << EOF
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FFFFFF"
EOF
```

---

### Step 9: Run the Application

**Option A: Run in Foreground (for testing)**

```bash
# Make sure you're in project directory and venv is activated
cd ~/genai-research-tool-fastapi-langchain-main
source venv/bin/activate

# Run Streamlit
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501
```

**Option B: Run in Background with Screen (Recommended)**

```bash
# Install screen if not available
sudo dnf install -y screen  # For Amazon Linux
# OR
sudo apt install -y screen  # For Ubuntu

# Start a screen session
screen -S sarabot

# Navigate to project and activate venv
cd ~/genai-research-tool-fastapi-langchain-main
source venv/bin/activate

# Run Streamlit
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501

# Detach from screen: Press Ctrl+A, then D
# Reattach later: screen -r sarabot
```

**Option C: Run with nohup (Alternative)**

```bash
cd ~/genai-research-tool-fastapi-langchain-main
source venv/bin/activate

# Run in background
nohup streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501 > streamlit.log 2>&1 &

# Check logs
tail -f streamlit.log

# Find and kill process if needed
ps aux | grep streamlit
kill <PID>
```

---

### Step 10: Access Your Application

1. **Get your EC2 Public IP** from AWS Console
2. **Open browser** and navigate to:
   ```
   http://YOUR_EC2_PUBLIC_IP:8501
   ```
3. **Configure API Key** in the application sidebar (same as local setup)

---

### Step 11: Set Up as System Service (Optional - For Auto-Start)

Create a systemd service for automatic startup:

```bash
# Create service file
sudo nano /etc/systemd/system/sarabot.service
```

**Add this content:**

```ini
[Unit]
Description=SaraBot AI Streamlit Application
After=network.target

[Service]
Type=simple
User=ec2-user
WorkingDirectory=/home/ec2-user/genai-research-tool-fastapi-langchain-main
Environment="PATH=/home/ec2-user/genai-research-tool-fastapi-langchain-main/venv/bin"
ExecStart=/home/ec2-user/genai-research-tool-fastapi-langchain-main/venv/bin/streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Note**: Replace `ec2-user` with `ubuntu` if using Ubuntu AMI, and adjust paths accordingly.

**Enable and start service:**

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (starts on boot)
sudo systemctl enable sarabot

# Start service
sudo systemctl start sarabot

# Check status
sudo systemctl status sarabot

# View logs
sudo journalctl -u sarabot -f
```

---

### 🔒 Security Recommendations

1. **Restrict Security Group**: Instead of `0.0.0.0/0`, allow port 8501 only from your IP:
   - In EC2 Console → Security Groups → Edit Inbound Rules
   - Change Source to: `YOUR_IP/32`

2. **Use Environment Variables for API Key** (Optional):
   ```bash
   # Create .env file
   nano ~/genai-research-tool-fastapi-langchain-main/.env
   # Add: GEMINI_API_KEY=your_api_key_here
   ```

3. **Set up HTTPS** (Advanced):
   - Use Nginx as reverse proxy
   - Configure SSL certificate with Let's Encrypt

---

### 🐛 Troubleshooting AWS Deployment

**Issue: Can't access application on port 8501**
- Check Security Group rules (port 8501 must be open)
- Verify Streamlit is running: `ps aux | grep streamlit`
- Check if port is listening: `netstat -tuln | grep 8501`
- Review Streamlit logs

**Issue: Application stops when SSH session ends**
- Use `screen`, `tmux`, or systemd service (see Step 11)
- Don't run directly in SSH session

**Issue: Out of memory errors**
- Upgrade to larger instance type (t3.medium or higher)
- The embedding model requires ~500MB RAM minimum

**Issue: Slow performance**
- Use larger instance type (t3.medium or t3.large)
- Ensure instance has enough CPU credits (for t2/t3 instances)

**Issue: Dependencies fail to install**
- Ensure build tools are installed: `gcc`, `g++`, `make`
- Try installing packages one by one to identify issue
- Check Python version: `python3.11 --version`

**Issue: ChromaDB file locking errors**
- This is normal on Linux, less common than Windows
- If persistent, restart the application

---

### 📊 Resource Requirements

- **Minimum**: t2.micro (1 vCPU, 1 GB RAM) - may be slow
- **Recommended**: t3.small (2 vCPU, 2 GB RAM)
- **Optimal**: t3.medium (2 vCPU, 4 GB RAM)
- **Storage**: 20-30 GB recommended
- **Network**: Standard (for downloading models)

---

### 💰 Cost Estimation

- **t2.micro**: Free tier eligible (750 hours/month)
- **t3.small**: ~$0.0208/hour (~$15/month if running 24/7)
- **t3.medium**: ~$0.0416/hour (~$30/month if running 24/7)

**Note**: Stop your instance when not in use to save costs!

---

### ✅ AWS Deployment Checklist

- [ ] EC2 instance launched with appropriate instance type
- [ ] Security Group configured (SSH + port 8501)
- [ ] Connected to instance via SSH
- [ ] Python 3.11 installed
- [ ] Project files uploaded to EC2
- [ ] Virtual environment created and activated
- [ ] Dependencies installed successfully
- [ ] Streamlit configured for external access
- [ ] Application running and accessible via public IP
- [ ] API key configured in application
- [ ] (Optional) Systemd service configured for auto-start

---

**Your SaraBot AI is now running on AWS! 🎉**

Access it at: `http://YOUR_EC2_PUBLIC_IP:8501`

---

## 🛠️ Quick Fix Script for Common Issues

If you encounter import errors or other deployment issues, run this script on your AWS instance:

```bash
# Download and run the fix script
cd ~/SaraBotAI_research_tool
wget https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/fix_aws_deployment.sh
chmod +x fix_aws_deployment.sh
./fix_aws_deployment.sh
```

Or copy the `fix_aws_deployment.sh` file to your server and run it.

**For detailed troubleshooting, see:** [DEPLOYMENT_TROUBLESHOOTING.md](DEPLOYMENT_TROUBLESHOOTING.md)
