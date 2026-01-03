#!/bin/bash
# Quick Fix Script for SaraBot AI AWS Deployment
# Run this script on your EC2 instance to fix common deployment issues

set -e  # Exit on error

echo "🚀 SaraBot AI - AWS Deployment Fix Script"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "SaraBotAI.py" ]; then
    echo -e "${RED}❌ Error: SaraBotAI.py not found!${NC}"
    echo "Please run this script from the project root directory."
    exit 1
fi

echo -e "${GREEN}✅ Found SaraBotAI.py${NC}"
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo -e "${YELLOW}📦 Activating virtual environment...${NC}"
    source venv/bin/activate
    echo -e "${GREEN}✅ Virtual environment activated${NC}"
else
    echo -e "${YELLOW}⚠️  Virtual environment not found. Creating one...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    echo -e "${GREEN}✅ Virtual environment created and activated${NC}"
fi

echo ""
echo -e "${YELLOW}📥 Installing/upgrading required packages...${NC}"
pip install --upgrade pip setuptools wheel
pip install --upgrade langchain langchain-community langchain-chroma langchain-core
pip install -r requirements.txt --upgrade

echo ""
echo -e "${GREEN}✅ Packages installed${NC}"
echo ""

# Fix imports in SaraBotAI.py
echo -e "${YELLOW}🔧 Fixing imports in SaraBotAI.py...${NC}"

python3 << 'PYTHON_SCRIPT'
import re

file_path = 'SaraBotAI.py'
try:
    with open(file_path, 'r') as f:
        content = f.read()
    
    original_content = content
    
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
    
    # Fix any corrupted import lines
    content = re.sub(
        r'from langchain_community\.document_loaders import U[^n].*',
        'from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader',
        content
    )
    
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print("✅ SaraBotAI.py imports fixed!")
    else:
        print("✅ SaraBotAI.py imports are already correct!")
        
except Exception as e:
    print(f"❌ Error fixing SaraBotAI.py: {e}")
    exit(1)
PYTHON_SCRIPT

# Fix module files if they exist
if [ -d "sarabotai/modules" ]; then
    echo -e "${YELLOW}🔧 Fixing imports in module files...${NC}"
    
    if [ -f "sarabotai/modules/data_processing.py" ]; then
        sed -i 's/from langchain\.document_loaders import/from langchain_community.document_loaders import/g' sarabotai/modules/data_processing.py 2>/dev/null || true
    fi
    
    if [ -f "sarabotai/modules/vector_store.py" ]; then
        sed -i 's/from langchain\.vectorstores import Chroma/from langchain_chroma import Chroma/g' sarabotai/modules/vector_store.py 2>/dev/null || true
        sed -i 's/from langchain\.embeddings import HuggingFaceEmbeddings/from langchain_community.embeddings import HuggingFaceEmbeddings/g' sarabotai/modules/vector_store.py 2>/dev/null || true
    fi
    
    if [ -f "sarabotai/modules/visualization.py" ]; then
        sed -i 's/from langchain\.schema import Document/from langchain_core.documents import Document/g' sarabotai/modules/visualization.py 2>/dev/null || true
    fi
    
    echo -e "${GREEN}✅ Module files fixed${NC}"
fi

echo ""
echo -e "${YELLOW}🧪 Testing imports...${NC}"
python3 << 'PYTHON_TEST'
try:
    from langchain_community.document_loaders import UnstructuredURLLoader, SeleniumURLLoader
    from langchain_chroma import Chroma
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.memory import ConversationBufferMemory
    print("✅ All imports successful!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    exit(1)
PYTHON_TEST

echo ""
echo -e "${GREEN}✅ All fixes applied successfully!${NC}"
echo ""
echo -e "${YELLOW}📋 Next steps:${NC}"
echo "1. Make sure Streamlit config is set up:"
echo "   mkdir -p ~/.streamlit"
echo "   cat > ~/.streamlit/config.toml << 'EOF'"
echo "   [server]"
echo "   headless = true"
echo "   port = 8501"
echo "   enableCORS = false"
echo "   EOF"
echo ""
echo "2. Run your app:"
echo "   streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501"
echo ""
echo "3. Or use screen to run in background:"
echo "   screen -S sarabot"
echo "   streamlit run SaraBotAI.py --server.address 0.0.0.0 --server.port 8501"
echo "   # Press Ctrl+A then D to detach"
echo ""
echo -e "${GREEN}🎉 Done!${NC}"

