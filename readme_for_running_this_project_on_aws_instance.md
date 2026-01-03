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
