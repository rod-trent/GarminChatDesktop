# Garmin Chat Desktop

Chat with your Garmin fitness data using AI! Ask questions about your workouts, sleep, steps, and more in natural language.

![Version](https://img.shields.io/badge/version-4.0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

---
![Garmin Chat Desktop](https://github.com/rod-trent/GarminChatDesktop/blob/main/AppImages/DarkMode.jpg?raw=true "Dark Mode Engaged")

# Garmin Chat Desktop

<div align="center">

![Version](https://img.shields.io/badge/version-4.0.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**AI-Powered Insights for Your Garmin Connect Data**

Chat with your fitness data using natural language and get instant AI-powered analysis of your workouts, sleep, health metrics, and performance trends.

[Download Latest](https://github.com/rod-trent/GarminChatDesktop/releases/latest) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Build Guide](BUILD_GUIDE.md)

</div>

---

## 🌟 What's New in v4.0.2

### Custom Session Naming
Save your conversations with meaningful names! When you click "Save Session", you can now provide a custom name like "Morning Run Analysis" or "Weekly Sleep Review" instead of just seeing timestamps.

### Rename Saved Chats
Added a **Rename** button in the Chat History viewer - update session names anytime to keep your conversation library organized.

### Enhanced Display
Chat sessions now show as: `"Custom Name (2026-02-14 15:30)"` making it easy to find specific conversations at a glance.

### Bug Fixes
- ✅ All emoji display issues resolved
- ✅ Fixed bullet points in AI responses  
- ✅ Updated Chat History dialog icon
- ✅ Improved backward compatibility

[See Full Changelog](CHANGELOG.md)

---

## 🎯 Overview

Garmin Chat Desktop brings the power of AI to your Garmin Connect fitness data. Ask questions about your workouts, sleep, health metrics, and get instant insights - all through natural conversation.

### Why Garmin Chat Desktop?

- **💬 Natural Language**: Ask questions in plain English - no complex queries needed
- **🤖 Multiple AI Providers**: xAI (Grok), OpenAI (ChatGPT), Google Gemini, Anthropic (Claude), or Azure OpenAI
- **💰 Cost Effective**: Switch providers to optimize costs - save $180-240/year vs single provider subscriptions
- **📊 Comprehensive Data**: Activities, sleep, heart rate, stress, body battery, nutrition, and more
- **🎨 Modern Interface**: Clean UI with dark mode, conversation history, and easy session management
- **🔒 Privacy First**: Your data stays on your machine - direct connection to Garmin and your chosen AI provider

---

## ✨ Features

### AI & Data Analysis
- **Multi-Provider AI Support**: Choose from 5 AI providers (xAI, OpenAI, Azure, Gemini, Claude)
- **Natural Language Queries**: "How did I sleep last night?" • "Show my last 5 runs" • "What's my training load?"
- **Comprehensive Data Access**: Activities, sleep, steps, heart rate, stress, body battery, nutrition, floors, intensity minutes, SpO2, HRV, training status
- **Date Range Queries**: "Show activities from the last 30 days" • "This week's workouts" • "Last month's runs"
- **Activity Comparisons**: Compare workouts and track progress over time

### Session Management
- **Custom Naming**: Save conversations with meaningful names
- **Rename Anytime**: Update session names in Chat History viewer
- **Browse & Search**: Search through all your saved conversations
- **Load Previous Chats**: Continue where you left off
- **Export Options**: Save as PDF, Word (.docx), or text file

### User Experience
- **Dark Mode**: Eye-friendly theme for extended use
- **Saved Prompts**: Create library of favorite questions
- **Quick Examples**: Pre-loaded questions to get started
- **Context Memory**: AI remembers your conversation for natural follow-ups
- **Multi-line Input**: Compose longer questions with Ctrl+Enter to send

---

## 🚀 Installation

### Option 1: Download Installer (Recommended)

**Latest Release: v4.0.2**

1. Download: [GarminChatDesktop_Setup_v4.0.2.exe](https://github.com/rod-trent/GarminChatDesktop/releases/latest)
2. Run the installer
3. Launch "Garmin Chat" from your Start Menu
4. Configure your credentials in Settings

**System Requirements:**
- Windows 10 or 11 (64-bit)
- 4 GB RAM (8 GB recommended)
- Internet connection for Garmin Connect and AI providers

### Option 2: Run from Source

```bash
# Clone the repository
git clone https://github.com/rod-trent/GarminChatDesktop.git
cd GarminChatDesktop

# Install dependencies
pip install -r requirements.txt

# Run the application
python GarminChatDesktop.py
```

See [BUILD_GUIDE.md](BUILD_GUIDE.md) for detailed build instructions.

---

## 📖 Getting Started

### Initial Setup

1. **Launch the Application**
   
2. **Open Settings** (Settings button in top right)
   
3. **Configure Garmin Connect**
   - Enter your Garmin email and password
   - These are stored locally and never shared

4. **Add AI Provider API Key** (choose one):
   - **xAI (Grok)**: Get key at [console.x.ai](https://console.x.ai/)
   - **OpenAI (GPT)**: Get key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - **Google Gemini**: Get key at [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
   - **Anthropic (Claude)**: Get key at [console.anthropic.com](https://console.anthropic.com/)
   - **Azure OpenAI**: Enter endpoint, deployment name, and API key

5. **Connect to Garmin**
   - Click **🔌 Connect to Garmin**
   - Enter MFA code if prompted

### Example Questions

**Activities**
```
"What was my last workout?"
"Show me my runs from the last week"
"Compare my last two bike rides"
"What's my longest run this month?"
```

**Sleep Analysis**
```
"How did I sleep last night?"
"What's my average sleep duration this month?"
"Show me my sleep quality trends"
"When do I get my best deep sleep?"
```

**Health Metrics**
```
"What's my resting heart rate trend?"
"Show me today's stress levels"
"How is my body battery doing?"
"What's my VO2 max?"
```

**Performance & Training**
```
"Am I improving my 5K times?"
"What's my training load this week?"
"Show me my fitness trends"
"How's my recovery looking?"
```

**Nutrition**
```
"How many calories did I consume today?"
"Show my protein intake this week"
"What are my macros looking like?"
```

### Saving Conversations

1. **During/After Chat**: Click **💾 Save Session**
2. **Enter Custom Name**: e.g., "Morning Run Analysis" (optional)
3. **Access Later**: Click **📂 History** to browse saved chats
4. **Rename**: Select a chat and click **✏️ Rename** to update the name
5. **Export**: Click **📄 Export** for PDF, DOCX, or TXT format

---

## 💡 Tips & Best Practices

### Optimize AI Costs

**Save $180-240 Annually** with smart provider usage:

| Provider | Best For | Cost |
|----------|----------|------|
| xAI Grok | Quick questions, general fitness queries | Free tier + competitive pricing |
| Gemini Flash | High volume, bulk queries | Generous free tier |
| GPT-4o | Complex analysis, detailed reports | Pay-per-use |
| Claude Sonnet | Comprehensive insights, long conversations | Mid-tier pricing |

**Strategy:**
1. Use free tiers for daily queries
2. Switch to premium models for complex analysis
3. Save prompts to reduce redundant questions

### Get Better Results

✅ **Be Specific**: "Show my 5K runs from January with pace under 6:00/km"  
✅ **Use Date Ranges**: "Last 30 days" or "this week"  
✅ **Ask Follow-ups**: Build on previous answers  
✅ **Save Useful Prompts**: Create a library of go-to questions

❌ **Avoid Vague**: "show runs" → too broad  
❌ **Don't Repeat**: Save prompts instead of retyping

### Troubleshooting

**Connection Issues**
- Verify Garmin credentials in Settings
- Check internet connection
- Have MFA codes ready

**AI Not Responding**
- Verify API key is correct
- Try different AI provider
- Check provider status page

**Missing Data**
- Click **Refresh** to sync latest from Garmin
- Ensure activities are logged in Garmin Connect

---

## 🛠️ Technology

**Built With:**
- Python 3.8+ with tkinter UI
- Multi-provider AI integration (xAI, OpenAI, Gemini, Anthropic, Azure)
- [garth](https://github.com/matin/garth) for Garmin Connect API
- Modern Fluent Design UI
- PyInstaller + Inno Setup for Windows distribution

**Key Dependencies:**
- `garth` - Garmin Connect authentication
- `openai` - OpenAI API client
- `google-generativeai` - Google Gemini API
- `anthropic` - Anthropic Claude API
- `python-docx` - Word document export
- `reportlab` - PDF generation

See [requirements.txt](requirements.txt) for complete list.

---

## 🗺️ Roadmap

### In Development
- [ ] **Visual Charts**: Interactive graphs for trends and performance
- [ ] **Voice Input**: Speech-to-text for hands-free queries
- [ ] **Voice Output**: Text-to-speech for AI responses
- [ ] **Mobile Apps**: iOS and Android versions

### Planned Features
- [ ] **Windows Store**: Official Microsoft Store listing
- [ ] **Training Plans**: AI-generated custom workout programs
- [ ] **Goal Tracking**: Set and monitor fitness objectives
- [ ] **Social Sharing**: Share insights and achievements
- [ ] **Advanced Analytics**: Predictive modeling for performance

### Future Integrations
- Strava sync
- Apple Health integration
- Fitbit data import
- Multi-language support

[Vote on features](https://github.com/rod-trent/GarminChatDesktop/discussions) or [suggest new ones](https://github.com/rod-trent/GarminChatDesktop/issues/new)!

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

### Report Bugs
1. Check [existing issues](https://github.com/rod-trent/GarminChatDesktop/issues)
2. Create new issue with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots/error messages
   - Version number (Help → About)

### Suggest Features
1. Open [GitHub Discussion](https://github.com/rod-trent/GarminChatDesktop/discussions)
2. Describe the feature and benefits
3. Include examples or mockups

### Contribute Code
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and test thoroughly
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open Pull Request

See [BUILD_GUIDE.md](BUILD_GUIDE.md) for development setup.

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Garmin Connect** for fitness data API
- **AI Providers** (xAI, OpenAI, Google, Anthropic) for language models
- **[garth](https://github.com/matin/garth)** library for Garmin authentication
- **Community** for feedback and contributions

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/rod-trent/GarminChatDesktop/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rod-trent/GarminChatDesktop/discussions)
- **Releases**: [Latest Release](https://github.com/rod-trent/GarminChatDesktop/releases/latest)

---

## 📊 Project Stats

![GitHub release (latest by date)](https://img.shields.io/github/v/release/rod-trent/GarminChatDesktop)
![GitHub all releases](https://img.shields.io/github/downloads/rod-trent/GarminChatDesktop/total)
![GitHub stars](https://img.shields.io/github/stars/rod-trent/GarminChatDesktop?style=social)
![GitHub forks](https://img.shields.io/github/forks/rod-trent/GarminChatDesktop?style=social)

---

<div align="center">

**Version 4.0.2** • Released February 2026

Made with ❤️ for the fitness and AI community

[⬆ Back to Top](#garmin-chat-desktop)

</div>
