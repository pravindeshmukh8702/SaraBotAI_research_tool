# 🚀 Deployment Troubleshooting Guide

This guide helps you fix common issues when deploying SaraBot AI on AWS EC2.

## Quick Fix Script for AWS

Run this script on your EC2 instance to fix common issues:

```bash
#!/bin/bash
# Quick fix script for SaraBot AI deployment

cd ~/SaraBotAI_research_tool
source venv/bin/activate

echo "🔧 Fixing imports and installing packages..."

# Install/upgrade required packages
pip install --upgrade langchain langchain-community langchain-chroma langchain-core

# Fix imports in SaraBotAI.py
python3 << 'EOF'
import re

file_path = 'SaraBotAI.py'
with open(file_path, 'r') as f:
    content = f.read()

# Fix corrupted imports
content = re.sub(
    r'from langchain\.document_loaders import.*',
    'from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader',
    content
)

content = re.sub(
    r'from langchain\.vectorstores import Chroma',
    'from langchain_chroma import Chroma',
    content
)

content = re.sub(
    r'from langchain\.embeddings import HuggingFaceEmbeddings',
    'from langchain_community.embeddings import HuggingFaceEmbeddings',
    content
)

with open(file_path, 'w') as f:
    f.write(content)

print("✅ File fixed successfully!")
EOF

# Fix module files
cd sarabotai/modules 2>/dev/null || echo "Modules directory not found, skipping..."
if [ -d "sarabotai/modules" ]; then
    sed -i 's/from langchain\.document_loaders import/from langchain_community.document_loaders import/g' sarabotai/modules/data_processing.py 2>/dev/null
    sed -i 's/from langchain\.vectorstores import Chroma/from langchain_chroma import Chroma/g' sarabotai/modules/vector_store.py 2>/dev/null
    sed -i 's/from langchain\.embeddings import HuggingFaceEmbeddings/from langchain_community.embeddings import HuggingFaceEmbeddings/g' sarabotai/modules/vector_store.py 2>/dev/null
    sed -i 's/from langchain\.schema import Document/from langchain_core.documents import Document/g' sarabotai/modules/visualization.py 2>/dev/null
fi

echo "✅ All fixes applied!"
echo "🚀 Restart your Streamlit app now"
```

---

## Common Errors & Solutions

### Error 1: `ModuleNotFoundError: No module named 'langchain.document_loaders'`

**Solution:**
```bash
pip install langchain-community langchain-chroma langchain-core
```

Then update imports in `SaraBotAI.py`:
```python
# Change from:
from langchain.document_loaders import UnstructuredURLLoader, SeleniumURLLoader

# To:
from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader
```

---

### Error 2: `ImportError: cannot import name 'U' from 'langchain_community.document_loaders'`

**Cause:** Corrupted import line in the file.

**Solution:**
```bash
# Edit the file
nano SaraBotAI.py

# Find line 7 and make sure it says:
from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader

# Save and exit (Ctrl+O, Enter, Ctrl+X)
```

Or use sed:
```bash
sed -i 's/from langchain_community\.document_loaders import U.*/from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader/g' SaraBotAI.py
```

---

### Error 3: `ModuleNotFoundError: No module named 'langchain_chroma'`

**Solution:**
```bash
pip install langchain-chroma
```

---

### Error 4: `ModuleNotFoundError: No module named 'langchain_community'`

**Solution:**
```bash
pip install langchain-community
```

---

### Error 5: `AttributeError: 'Chroma' object has no attribute 'persist'`

**Solution:** In newer versions of langchain-chroma, `persist()` is called automatically. Remove the `.persist()` call:

```python
# Change from:
vectorstore_chroma = Chroma.from_documents(...)
vectorstore_chroma.persist()

# To:
vectorstore_chroma = Chroma.from_documents(...)
# persist() is automatic in newer versions
```

---

### Error 6: Port 8501 already in use

**Solution:**
```bash
# Find and kill the process
lsof -ti:8501 | xargs kill -9

# Or use:
pkill -f streamlit

# Then restart
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501
```

---

### Error 7: Can't access app from browser

**Checklist:**
1. ✅ Security Group allows port 8501 from your IP (or 0.0.0.0/0)
2. ✅ Streamlit is running: `ps aux | grep streamlit`
3. ✅ App is bound to 0.0.0.0: `--server.address 0.0.0.0`
4. ✅ Check logs for errors: `tail -f streamlit.log` or check screen session

---

### Error 8: App stops when SSH session ends

**Solution:** Use screen or systemd service:

**Option A: Screen**
```bash
screen -S sarabot
cd ~/SaraBotAI_research_tool
source venv/bin/activate
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501
# Press Ctrl+A then D to detach
# Reattach: screen -r sarabot
```

**Option B: Systemd Service** (see README.md for full setup)

---

### Error 9: Out of memory errors

**Solution:**
- Upgrade to larger instance (t3.medium or t3.large)
- Or add swap space:
```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

### Error 10: ChromaDB file locking errors

**Solution:** This is less common on Linux. If it happens:
```bash
# Stop the app
pkill -f streamlit

# Remove old database
rm -rf chroma_db_*

# Restart
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501
```

---

## Complete Fresh Setup on AWS

If you need to start completely fresh:

```bash
# 1. Connect to EC2
ssh -i your-key.pem ubuntu@YOUR_EC2_IP

# 2. Update system
sudo apt update && sudo apt upgrade -y  # Ubuntu
# OR
sudo dnf update -y  # Amazon Linux

# 3. Install Python 3.11
sudo apt install -y python3.11 python3.11-pip python3.11-venv python3.11-dev build-essential  # Ubuntu
# OR
sudo dnf install -y python3.11 python3.11-pip python3.11-devel gcc gcc-c++ make  # Amazon Linux

# 4. Clone or upload project
cd ~
# Option A: If using git
git clone YOUR_REPO_URL
cd genai-research-tool-fastapi-langchain-main

# Option B: If uploading via SCP (from local machine)
# scp -i your-key.pem -r project-folder ubuntu@EC2_IP:/home/ubuntu/

# 5. Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# 6. Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 7. Configure Streamlit
mkdir -p ~/.streamlit
cat > ~/.streamlit/config.toml << EOF
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false
EOF

# 8. Run the app
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501
```

---

## Quick Commands Reference

```bash
# Check if app is running
ps aux | grep streamlit

# View Streamlit logs
tail -f streamlit.log

# Restart app
pkill -f streamlit
streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501

# Check port usage
netstat -tuln | grep 8501
# OR
lsof -i :8501

# Update code from git
cd ~/SaraBotAI_research_tool
git pull origin main

# Reinstall dependencies
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

---

## Need Help?

If you encounter an error not listed here:

1. **Check the full error message** - Copy the complete traceback
2. **Check Streamlit logs** - Look for detailed error information
3. **Verify package versions** - Run `pip list | grep langchain`
4. **Check Python version** - Should be 3.8+ (preferably 3.11)
5. **Verify file paths** - Make sure you're in the correct directory

---

**Last Updated:** 2024
**Maintained by:** PRAVIN & RUTURAJ

