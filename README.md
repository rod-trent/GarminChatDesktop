# Garmin Chat Desktop

# Garmin Chat Desktop v4.0.3

<div align="center">

![Version](https://img.shields.io/badge/version-4.0.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**AI-Powered Insights for Your Garmin Connect Data**

Garmin Chat Desktop is a local desktop chatbot that lets you interact with your Garmin Connect data using natural language. Ask questions about your workouts, sleep, steps, and activities in plain English and get intelligent AI-powered responses.

[Download Latest](https://github.com/rod-trent/GarminChatDesktop/tree/main/Releases) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage)

![Garmin Chat Desktop](https://github.com/rod-trent/GarminChatDesktop/blob/main/AppImages/GarminChatDesktop.jpg?raw=true "Dark Mode Engaged")

**AI-powered insights for your fitness data**

---

## 🎯 Features

### Core Functionality
- **Natural Language Queries** - Ask questions in plain English
- **Multi-AI Provider Support** - Choose from xAI (Grok), OpenAI (ChatGPT), Google Gemini, Anthropic (Claude), or Azure OpenAI
- **Comprehensive Data Access** - Steps, workouts, sleep, heart rate, stress, body battery, nutrition, and more
- **Chat History** - Save and review past conversations
- **Export Reports** - Export conversations as PDF, DOCX, or TXT

### New in v4.0.3
- ✨ **Customizable Quick Questions** - Create your own frequently-asked questions
- 🎨 **Rounded Hover Effects** - Modern, polished button styling
- 🪟 **Smooth Dialog Animations** - No more flashing windows
- 🔤 **Perfect Text Rendering** - All character encoding issues fixed
- 🚀 **Professional Splash Screen** - Beautiful startup experience
- 🎯 **Enhanced UI** - Fluent Design throughout all dialogs

### Previous Features
- 💾 **Saved Prompts** - Save and reuse your favorite questions
- 🔍 **Search History** - Find past conversations quickly
- 🌓 **Dark Mode** - Easy on the eyes
- 📊 **Markdown Formatting** - Clean, readable responses
- 🔐 **Local & Secure** - All data stays on your computer

---

## 📋 Requirements

### System Requirements
- **OS**: Windows 10 or later (64-bit)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 200MB free space
- **Internet**: Required for AI API calls and Garmin Connect sync

### Account Requirements
- **Garmin Connect Account** - Free account from [Garmin Connect](https://connect.garmin.com)
- **AI API Key** - At least one of:
  - [xAI (Grok)](https://console.x.ai/) - Recommended for cost-effectiveness
  - [OpenAI (ChatGPT)](https://platform.openai.com/)
  - [Google Gemini](https://makersuite.google.com/app/apikey)
  - [Anthropic (Claude)](https://console.anthropic.com/)
  - Azure OpenAI (requires Azure subscription)

---

## 🚀 Installation

### Option 1: Installer (Recommended)
1. Download `GarminChatDesktop_v4.0.3_Setup.exe`
2. Run the installer
3. Follow the setup wizard
4. Launch from Start Menu or Desktop shortcut

### Option 2: Portable Executable
1. Download `GarminChat.exe`
2. Place in any folder
3. Double-click to run
4. No installation required!

---

## 🎮 Getting Started

### First Time Setup

1. **Launch the Application**
   - The app will open and prompt for configuration

2. **Configure Settings**
   - Click the **Settings** button
   - Enter your **Garmin Connect** email and password
   - Choose an **AI Provider** and enter your API key
   - Click **Save**

3. **Connect to Garmin**
   - Click **▶ Connect to Garmin**
   - Wait for authentication (may require MFA if enabled)
   - Once connected, you're ready to chat!

### Basic Usage

**Quick Questions:**
- Click any Quick Question button to instantly ask
- Customize them: Click **⚙️ Customize** to create your own

**Ask Anything:**
- Type your question in the input box
- Press `Ctrl+Enter` to send (or click **Send →**)
- Examples:
  - "How many steps did I take today?"
  - "What was my last workout?"
  - "How did I sleep last night?"
  - "Show me my activities from last week"

**Advanced Queries:**
- "Compare my last 3 runs"
- "How's my body battery trending?"
- "What's my average sleep duration this month?"
- "Show me all strength training from February"

---

## ⚙️ Settings & Configuration

### AI Provider Selection

Choose the AI provider that best fits your needs:

| Provider | Best For | Cost | Model |
|----------|----------|------|-------|
| **xAI (Grok)** | Best value, great quality | Low | grok-3 |
| **OpenAI** | Most popular, reliable | Medium | gpt-4o |
| **Gemini** | Fast responses | Low | gemini-1.5-flash |
| **Anthropic** | Long conversations | Medium | claude-sonnet-4-5 |
| **Azure** | Enterprise users | Variable | Your deployment |

💡 **Tip**: Start with xAI (Grok) for the best cost-to-quality ratio!

### Garmin Credentials

- **Email**: Your Garmin Connect email
- **Password**: Your Garmin Connect password
- **MFA**: If enabled, you'll be prompted for your 6-digit code

🔒 **Security**: Credentials are stored locally in `~/.garmin_chat/config.json`

### Quick Questions Customization

1. Click **⚙️ Customize** next to Quick Questions
2. Edit the questions (one per line, max 8)
3. Click **💾 Save**
4. Questions update instantly!

---

## 🎨 Features Guide

### Chat History
- **Save Chat**: Click **💾 Save Chat** to save the current conversation
- **View History**: Click **📂 History** to browse saved chats
- **Load Chat**: Select a saved chat and click **Load Into Chat**
- **Rename**: Click **✏️ Rename** to give chats custom names
- **Delete**: Remove unwanted conversations

### Saved Prompts
- Click **📝 Prompts** to manage saved questions
- Click **➕ New Prompt** to save a frequently-asked question
- Click **✏️ Use Selected** to insert into chat

### Search
- Click **🔍 Search** to find past conversations
- Search across all saved chat history
- View matching results instantly

### Export Reports
- Click **📄 Export Report** to save conversations
- Choose format: **PDF**, **Word (.docx)**, or **Text (.txt)**
- Include/exclude timestamps and system messages

### Dark Mode
- Click **◐ Theme** to toggle dark/light mode
- Preference is saved automatically
- Easy on the eyes for night use

---

## 📊 Data You Can Query

### Activity Data
- Steps, distance, calories
- Workouts (running, cycling, swimming, etc.)
- Activity summaries and details
- Date range queries

### Health Metrics
- Sleep duration and quality
- Heart rate (resting, max, zones)
- Body Battery energy levels
- Stress levels
- Respiration rate
- SpO2 (blood oxygen)
- HRV (heart rate variability)

### Nutrition & Wellness
- Hydration tracking
- Nutrition/food logs
- Floors climbed
- Intensity minutes
- Training load and status
- VO2 max and fitness age

---

## 💾 File Locations

All data is stored in your user directory:

```
C:\Users\YourName\.garmin_chat\
├── config.json              # Settings and credentials
├── quick_questions.json     # Custom quick questions
├── saved_prompts.json       # Saved prompts
└── chat_history\            # Saved conversations
    ├── chat_20260215_143022.json
    ├── chat_20260214_091533_MyWorkout.json
    └── ...
```

---

## 🐛 Troubleshooting

### Connection Issues

**Problem**: "Failed to connect to Garmin"
- **Solution**: 
  - Verify email/password in Settings
  - Check internet connection
  - Try MFA if enabled
  - Refresh and try again

**Problem**: "MFA code required"
- **Solution**:
  - Enter your 6-digit code from authenticator app
  - Code expires quickly - enter promptly

### API Issues

**Problem**: "AI client initialization failed"
- **Solution**:
  - Verify API key in Settings
  - Check key hasn't expired
  - Ensure provider service is online
  - Try a different provider

**Problem**: "Rate limit exceeded"
- **Solution**:
  - Wait a few minutes
  - Reduce query frequency
  - Check your API quota

### Display Issues

**Problem**: Text showing as boxes (□)
- **Solution**: 
  - Update to v4.0.3 (this is fixed!)
  - All character encoding issues resolved

**Problem**: Dialogs flashing when opening
- **Solution**:
  - Update to v4.0.3 (this is fixed!)
  - Smooth animations implemented

---

## 🔄 Updating

### From v4.0.x
1. Download new installer or executable
2. Run installer (will replace old version)
3. Settings and data are preserved

### From Earlier Versions
1. Export any important chat history
2. Install v4.0.3
3. Reconfigure settings
4. Import saved chats if needed

---

## 💡 Tips & Best Practices

### Optimize AI Costs
- Use xAI (Grok) for best value
- Save frequently-used questions as Quick Questions
- Use chat history instead of re-asking
- Enable auto-login to save re-authentication queries

### Better Queries
- Be specific: "last 7 days" vs "recently"
- Use date ranges for historical data
- Ask follow-up questions in same chat
- Save complex queries as prompts

### Data Management
- Save important conversations with custom names
- Use Search to find old chats quickly
- Export reports for offline reference
- Delete old chats to save space

---

## 📝 Version History

### v4.0.3 (February 15, 2026)
- ✨ Added customizable Quick Questions
- 🎨 Implemented rounded hover effects
- 🪟 Fixed all dialog flashing issues
- 🔤 Resolved all character encoding problems
- 🚀 Added professional splash screen
- 🎯 Enhanced all dialogs with Fluent Design
- 📄 Added Export Report text label
- 🌓 Improved dark mode consistency

### v4.0.1 (February 2026)
- 🐛 Fixed window positioning bugs
- 📚 Enhanced documentation
- 🔧 Improved stability

### v4.0.0 (January 2026)
- 🆕 Initial public release
- 🤖 Multi-AI provider support
- 💾 Chat history and saved prompts
- 🔍 Search functionality
- 📊 Comprehensive Garmin data access

---

## ❓ FAQ

**Q: Is my data secure?**  
A: Yes! All data stays local on your computer. API keys and credentials are stored in `~/.garmin_chat/config.json`.

**Q: Which AI provider should I use?**  
A: We recommend xAI (Grok) for the best cost-to-quality ratio. OpenAI is great if you already have credits.

**Q: Can I use multiple Garmin accounts?**  
A: Change credentials in Settings. Only one account can be active at a time.

**Q: How much does it cost?**  
A: The app is free! You only pay for AI API usage (typically $0.01-0.10 per conversation).

**Q: Does it work offline?**  
A: No, internet is required for Garmin Connect sync and AI API calls.

**Q: Can I see my real-time heart rate?**  
A: The app shows recent synced data from Garmin Connect, not live device data.

**Q: What Garmin devices are supported?**  
A: Any device that syncs with Garmin Connect (watches, bike computers, etc.).

**Q: Can I customize the Quick Questions?**  
A: Yes! Click **⚙️ Customize** next to Quick Questions to create your own.

---

## 🤝 Support

### Getting Help
- **Issues**: Check Troubleshooting section above
- **Questions**: See FAQ
- **Bugs**: Report on GitHub Issues
- **Feature Requests**: Submit on GitHub

### Community
- **GitHub**: [github.com/yourusername/garmin-chat](https://github.com/yourusername/garmin-chat)
- **Discussions**: GitHub Discussions
- **Updates**: Check Releases page

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

---

## 🙏 Acknowledgments

- **Garmin Connect** - For the excellent fitness platform
- **AI Providers** - xAI, OpenAI, Google, Anthropic, Microsoft
- **Python Community** - For amazing libraries
- **Contributors** - Thank you to all who helped improve this project!

---

## 🚀 What's Next?

Future features we're considering:
- 📈 Visual charts and graphs
- 🗣️ Voice input/output
- 📱 Mobile companion app
- ☁️ Cloud sync (optional)
- 🏆 Goal tracking and recommendations
- 📧 Email reports

**Feedback welcome!** Let us know what features you'd like to see.

---

**Garmin Chat Desktop v4.0.3**  
Made with ❤️ for fitness enthusiasts

*Not affiliated with Garmin Ltd. All trademarks belong to their respective owners.*
