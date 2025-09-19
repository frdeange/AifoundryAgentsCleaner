# 🧹 Azure AI Foundry Cleaner

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Azure](https://img.shields.io/badge/azure-ai%20foundry-0078d4.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

*A powerful console application for bulk deletion of Azure AI Foundry resources*

</div>

---

## 📋 Overview

This Python console application connects to your Azure AI Foundry environment and performs a **complete and irreversible cleanup** of all Agents and Threads in your project. Perfect for development environments, testing scenarios, or when you need a fresh start.

### ✨ Features

- 🔍 **Smart Discovery**: Automatically lists all agents and threads in your project
- 🗑️ **Bulk Deletion**: Removes all resources without manual intervention
- 🔐 **Secure Authentication**: Uses Azure Default Credentials for seamless integration
- 📊 **Progress Tracking**: Real-time console output showing deletion progress
- 🐳 **Dev Container Ready**: Includes a pre-configured development environment

## ⚠️ Important Disclaimer

> **⚡ DANGER ZONE ⚡**
> 
> **This script will permanently delete ALL agents and threads in your Azure AI Foundry project.** 
> 
> - ❌ **No recovery possible** - Deleted resources cannot be restored
> - ❌ **No confirmation prompts** - Deletion starts immediately upon execution
> - ❌ **No selective deletion** - ALL resources will be removed
> 
> Use with extreme caution and ensure you're targeting the correct environment!

## 🚀 Quick Start

### Option 1: Using Dev Container (Recommended)

This repository includes a pre-configured development container with all necessary tools and dependencies.

1. **Open in Dev Container:**
   - Open the repository in VS Code
   - When prompted, click "Reopen in Container"
   - Or use Command Palette: `Dev Containers: Reopen in Container`

2. **Configure your environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Azure AI Foundry endpoint
   ```

3. **Authenticate and run:**
   ```bash
   az login
   python main.py
   ```

### Option 2: Local Setup

If you prefer to set up the environment locally:

## 📋 Prerequisites

- 🐍 Python 3.8 or higher
- ☁️ Azure account with an active subscription
- 🔑 Access to an Azure AI Foundry project with agent/thread management permissions
- 🛠️ [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured

## 🛠️ Installation & Setup

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd AifoundryAgentsCleaner
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory:

```env
# .env
AI_FOUNDRY_ENDPOINT="https://<your-foundry-name>.services.ai.azure.com/api/projects/<your-project-name>"
```

> 💡 **Tip**: You can find your endpoint in the Azure AI Foundry portal under your project settings.

### 5️⃣ Authenticate with Azure
```bash
az login
```

## 🎯 Usage

## 🎯 Usage

Execute the cleaning script:

```bash
python main.py
```

### 📤 Expected Output

```
Listing agents...
Deleting agent: agent_12345 (My Test Agent)
Deleting agent: agent_67890 (Another Agent)
No agents found.

Listing threads...
Deleting thread: thread_abc123 (Conversation 1)
Deleting thread: thread_def456
No threads found.

Process finished.
```

### 🔄 What the Script Does

1. 🔍 **Discovery Phase**: Lists all agents in your AI Foundry project
2. 🗑️ **Agent Cleanup**: Deletes each agent individually with progress logging
3. 🔍 **Thread Discovery**: Lists all conversation threads
4. 🗑️ **Thread Cleanup**: Removes each thread with detailed logging
5. ✅ **Completion**: Confirms the cleanup process is finished

---

## 🐳 Development Container

This repository includes a fully configured development container that provides:

- ✅ **Pre-installed Python 3.12** with all required packages
- ✅ **Azure CLI** ready to use
- ✅ **VS Code extensions** for Python development
- ✅ **Automatic environment setup** - no manual configuration needed

### Using the Dev Container

1. **Prerequisites**: Ensure you have [Docker](https://www.docker.com/get-started) and [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.

2. **Open**: Clone the repository and open it in VS Code.

3. **Container**: When prompted, select "Reopen in Container" or use `Ctrl+Shift+P` → "Dev Containers: Reopen in Container".

4. **Ready**: Everything is pre-configured! Just add your `.env` file and run `az login`.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⚡ Use responsibly - Your data's safety is in your hands! ⚡**

</div>
