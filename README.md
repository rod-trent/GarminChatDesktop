# Garmin Chat Desktop

**Garmin Chat Desktop v4.0.4**

<div align="center">

![Version](https://img.shields.io/badge/version-4.0.4-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

</div>


**AI-Powered Insights for Your Garmin Connect Fitness Data**

Garmin Chat Desktop is a Windows application that lets you interact with your Garmin Connect fitness data through natural language conversations. Ask questions, analyze trends, and get personalized insights using the power of AI.

[Garmin Chat Desktop 4.0.4](https://github.com/rod-trent/GarminChatDesktop/blob/main/AppImages/gchatdesktop404.jpg)

## What's New in v4.0.4

### Ollama Support - Free, Local AI!
Run AI models completely free on your own computer with Ollama integration. No API costs, complete privacy, works offline!

- **$0 Cost** - Unlimited usage with no subscription fees
- **100% Private** - Your fitness data never leaves your computer
- **Works Offline** - No internet connection needed after setup
- **Multiple Models** - Choose from Llama, Mistral, Phi, and more
- **Easy Setup** - Simple installation from ollama.com

See [OLLAMA_SETUP_GUIDE.md](https://github.com/rod-trent/GarminChatDesktop/blob/main/Code/OLLAMA_SETUP_GUIDE.md) for installation instructions.

### Latest Anthropic Claude Models
Updated to include the newest Claude models for improved response quality and reasoning.

### Richer Garmin Data (50 Activities)
The app now pulls your 50 most recent activities from Garmin Connect (previously limited to 10), giving the AI much more context for trend analysis and training insights.

> **Note:** Because more data is being retrieved, the initial Garmin Connect login and subsequent AI responses may take slightly longer than in previous versions. This is expected behavior.

## Features

### 💬 Natural Language Queries
Ask questions about your fitness data in plain English:
- "What was my last workout?"
- "Show me my running pace trend over the last month"
- "How many calories did I burn this week?"
- "What's my average heart rate during runs?"

### 🤖 Multiple AI Providers
Choose from six AI providers to suit your needs and budget:
- **Ollama (Local)** - NEW! Free, private, offline
- **xAI (Grok)** - Fast, advanced reasoning
- **OpenAI (ChatGPT)** - Industry-leading performance
- **Google Gemini** - Excellent for data analysis
- **Anthropic (Claude)** - Superior context understanding
- **Azure OpenAI** - Enterprise-grade deployment

### 📊 Rich Data Analysis
- Activity summaries and detailed metrics
- Training load and recovery insights
- Sleep analysis and trends
- Heart rate zones and patterns
- Step counts and daily activity
- Weight and body composition tracking

### 🎨 Modern Interface
- Clean, intuitive Fluent Design UI
- Dark mode support
- Conversation history with search
- Save and organize chat sessions
- Export conversations as PDF, DOCX, or TXT

### 🔒 Privacy & Security
- All data processing happens locally on your machine
- API keys stored securely on your device
- With Ollama, data never leaves your computer at all
- No third-party tracking or analytics

## System Requirements

- **OS**: Windows 10 or Windows 11
- **RAM**: 4GB minimum (8GB+ recommended for Ollama)
- **Storage**: 200MB for application + 2-40GB for Ollama models (optional)
- **Internet**: Required for cloud AI providers, optional with Ollama

## Installation

### Quick Install
1. Download `GarminChatSetup.exe` from the [Releases](../../releases) page
2. Run the installer
3. Follow the setup wizard
4. Launch Garmin Chat Desktop from your Start menu

### First-Time Setup
1. Enter your Garmin Connect credentials
2. Choose your AI provider:
   - **For Free/Offline**: Select Ollama (requires separate installation)
   - **For Cloud AI**: Select a provider and enter your API key
3. Click "Connect to Garmin"
4. Start chatting with your fitness data!

## Ollama Setup (Optional but Recommended)

For free, unlimited AI with complete privacy:

1. **Install Ollama** from https://ollama.com/download
2. **Pull a model**:
   ```bash
   ollama pull llama2
   ```
3. **Configure Garmin Chat**:
   - Open Settings
   - Select "Ollama (Local)" as your AI provider
   - Click "Test Connection"
   - Choose your model
   - Save

See the complete [Ollama Setup Guide](https://github.com/rod-trent/GarminChatDesktop/blob/main/Code/OLLAMA_SETUP_GUIDE.md) for detailed instructions.

## Cost Comparison

### Traditional AI Subscriptions
- ChatGPT Plus: **$20/month**
- Claude Pro: **$20/month**
- Gemini Advanced: **$20/month**

### Garmin Chat Desktop
- **With Ollama**: **$0** (free forever)
- **With pay-per-use APIs**: Typically **$1-5/month** for casual use
- **Savings**: Up to **$240/year** compared to subscriptions!

## Usage Examples

### Basic Queries
```
You: What was my last workout?
Garmin Chat: Your last workout was a Treadmill Running session on 
February 16, 2026 at 6:20 PM. You ran 3.25 km in 19 minutes, burning 
202 calories at an average pace of 5:51 min/km.
```

### Trend Analysis
```
You: How has my average running pace changed over the last 3 months?
Garmin Chat: Your running pace has improved significantly! In November, 
your average pace was 6:15 min/km. By January, it improved to 5:45 min/km, 
and this month you're averaging 5:30 min/km - that's a 12% improvement!
```

### Training Insights
```
You: Am I overtraining?
Garmin Chat: Based on your recent activity, you're managing your training 
load well. Your 7-day training load is 245, which is in the optimal range. 
However, your recovery time shows you need 48 hours rest after yesterday's 
long run. Consider a rest day or light activity tomorrow.
```

## Supported AI Providers

| Provider | Speed | Quality | Cost | Best For |
|----------|-------|---------|------|----------|
| **Ollama** | Medium | Good | **Free** | Privacy, offline use, unlimited queries |
| **xAI (Grok)** | Very Fast | Excellent | Pay-per-use | Quick responses, latest data |
| **OpenAI** | Fast | Excellent | Pay-per-use | Balanced performance |
| **Gemini** | Fast | Very Good | Pay-per-use | Data analysis |
| **Claude** | Medium | Excellent | Pay-per-use | Detailed explanations |
| **Azure** | Fast | Excellent | Enterprise | Business deployments |

## Features Guide

### Conversation Management
- **Save Chats**: Name and save important conversations
- **History**: Browse and search past chats
- **Export**: Download conversations as PDF, Word, or text files

### Data Refresh
- Click "Refresh" to get the latest data from Garmin Connect
- Automatic connection on startup (can be disabled)
- Real-time sync with your Garmin account

### Quick Questions
Customize quick question buttons for one-tap access to your most common queries.

### Dark Mode
Toggle between light and dark themes for comfortable viewing any time of day.

## Troubleshooting

### "Cannot connect to Garmin"
- Verify your email and password are correct
- Check your internet connection
- If using 2FA, enter the code when prompted

### "AI Provider Error"
- **Cloud providers**: Verify your API key is valid
- **Ollama**: Make sure Ollama is running (`ollama serve`)
- Check Settings to ensure the correct provider is selected

### "No data available"
- Click "Refresh" to sync latest data from Garmin
- Ensure you have activities recorded in Garmin Connect
- Check that your Garmin device has synced recently

### Ollama Issues
See the detailed [Ollama Setup Guide](https://github.com/rod-trent/GarminChatDesktop/blob/main/Code/OLLAMA_SETUP_GUIDE.md) for troubleshooting.

## Privacy & Data Security

- **Local Storage**: All data is stored locally on your computer
- **Encrypted Credentials**: Garmin passwords stored securely
- **No Telemetry**: We don't collect usage data or analytics
- **Ollama Option**: Keep everything 100% on your machine

## Building from Source

Requirements:
- Python 3.11+
- Required packages: `pip install -r requirements.txt`

Build executable:
```bash
pyinstaller GarminChatDesktop.spec
```

Create installer:
```bash
iscc installer_script.iss
```

## API Key Setup

### xAI (Grok)
1. Visit https://console.x.ai/
2. Create an account
3. Generate an API key
4. Paste into Garmin Chat settings

### OpenAI
1. Visit https://platform.openai.com/api-keys
2. Sign in or create an account
3. Create a new API key
4. Paste into Garmin Chat settings

### Google Gemini
1. Visit https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create an API key
4. Paste into Garmin Chat settings

### Anthropic (Claude)
1. Visit https://console.anthropic.com/
2. Create an account
3. Generate an API key
4. Paste into Garmin Chat settings

### Ollama (No API Key Needed!)
1. Install from https://ollama.com/download
2. Run `ollama pull llama2`
3. Select "Ollama" in Settings
4. Click "Test Connection"

## Support

- **Issues**: Report bugs on [GitHub Issues](../../issues)
- **Discussions**: Ask questions in [GitHub Discussions](../../discussions)
- **Email**: [Your contact email]

## License

[Your chosen license]

## Acknowledgments

- Garmin Connect for fitness data API
- OpenAI, xAI, Google, Anthropic, and Ollama for AI capabilities
- The open-source community for tools and libraries

## Version History

### v4.0.4 (Current)
- Added Ollama support for free, local AI
- Added latest Anthropic Claude models
- Expanded Garmin activity fetch from 10 to 50 activities for richer AI context
- Fixed emoji encoding issues throughout UI
- Improved error handling

### v4.0.3
- Updated for Google Gemini API changes
- Bug fixes and stability improvements

### v4.0.0
- 🎨 Modern Fluent Design UI
- 🤖 Multi-provider AI support
- 📊 Enhanced data visualization
- 💾 Conversation history and export

---

**Made with ❤️ for the Garmin fitness community**

*Garmin Chat Desktop is not affiliated with or endorsed by Garmin Ltd.*
