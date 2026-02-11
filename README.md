# Garmin Chat Desktop

Chat with your Garmin fitness data using AI! Ask questions about your workouts, sleep, steps, and more in natural language.

![Version](https://img.shields.io/badge/version-4.0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

---
![Garmin Chat Desktop(https://github.com/rod-trent/GarminChatDesktop/blob/main/AppImages/DarkMode.jpg?raw=true "Dark Mode Engaged")

## 🎉 What's New in v4.0.1

**Bug Fix Release**
- ✅ Fixed window positioning on first launch (no longer hidden under taskbar)
- ✅ Added window state persistence (remembers position and size between sessions)
- ✅ Enhanced center_window() with taskbar awareness and boundary checks
- ✅ Clean shutdown with automatic state saving

[See full changelog](CHANGELOG.md)

---

## ✨ Features

### Multi-Provider AI Support
Choose from 5 AI providers:
- **xAI** (Grok) - Fast and capable
- **OpenAI** (GPT-4, GPT-4 Turbo, GPT-3.5) - Industry standard
- **Azure OpenAI** - Enterprise deployment
- **Google Gemini** - Google's latest AI
- **Anthropic Claude** - Advanced reasoning

### Comprehensive Garmin Data Access
- 📊 **Activities**: Workouts, runs, walks, bike rides, strength training
- 😴 **Sleep**: Duration, quality, REM, deep sleep, awake time
- 👣 **Steps**: Daily steps, distance, active minutes
- ❤️ **Heart Rate**: Resting, max, zones, variability (HRV)
- 🔋 **Body Battery**: Energy levels throughout the day
- 😰 **Stress**: Stress levels and patterns
- 💪 **Fitness**: VO2 Max, training status, training load
- 🍎 **Nutrition**: Calories, macros, hydration
- 🏃 **Training**: Performance metrics, recovery time
- 📈 **More**: SpO2, respiration, floors climbed, and more

### User Experience
- 🌙 **Dark Mode**: Easy on the eyes
- 💬 **Natural Conversations**: Ask questions like you would a fitness coach
- 📅 **Smart Date Detection**: "last week", "yesterday", "this month"
- 🔄 **Auto-Login**: Securely save your credentials
- 📝 **Chat History**: Review past conversations
- ⚡ **Quick Questions**: One-click common queries
- 🎨 **Modern UI**: Clean, intuitive interface

---

## 📦 Download & Install

### Option 1: Windows Installer (Recommended)
1. Download the latest installer from [Releases](https://github.com/rod-trent/GarminChatDesktop/releases/)
2. Run `GarminChatDesktop_Setup_v4.0.1.exe`
3. Follow the installation wizard
4. Launch from Start Menu or desktop shortcut

### Option 2: Portable Executable
1. Download `GarminChat.exe` from [Releases](https://github.com/rod-trent/GarminChatDesktop/releases/)
2. Place in any folder
3. Run directly (no installation needed)

### Option 3: Run from Source
```bash
# Clone repository
git clone https://github.com/rod-trent/GarminChatDesktop.git
cd GarminChatDesktop

# Install dependencies
pip install -r requirements-desktop.txt

# Run application
python GarminChatDesktop.py
```

---

## 🚀 Quick Start

### First Time Setup

1. **Launch Application**
   - Windows installer: Start Menu → Garmin Chat
   - Portable: Double-click `GarminChat.exe`
   - Source: `python GarminChatDesktop.py`

2. **Open Settings** (gear icon in top-right)

3. **Configure AI Provider**
   - Select your preferred AI provider
   - Enter API key ([Get API keys](#-getting-api-keys))
   - Choose model (or use default)

4. **Configure Garmin Connect**
   - Enter your Garmin email
   - Enter your Garmin password
   - Check "Auto-login" (optional but recommended)

5. **Save Settings**

6. **Start Chatting!**
   - "How many steps did I take today?"
   - "What was my last workout?"
   - "How did I sleep last night?"
   - "Show me my activities from last week"

---

## 🔑 Getting API Keys

### xAI (Grok) - Recommended for Speed
1. Go to https://console.x.ai/
2. Sign in or create account
3. Navigate to API Keys
4. Create new key
5. Copy and paste into Garmin Chat settings

**Cost**: Pay-as-you-go, very affordable for personal use

### OpenAI (ChatGPT)
1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Create new secret key
4. Copy and paste into settings

**Models**: GPT-4, GPT-4 Turbo, GPT-3.5 Turbo

### Google Gemini
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Create API key
4. Copy and paste into settings

**Models**: Gemini Pro, Gemini Pro Vision

### Anthropic Claude
1. Go to https://console.anthropic.com/
2. Create account
3. Navigate to API Keys
4. Create new key
5. Copy and paste into settings

**Models**: Claude 3 Opus, Claude 3 Sonnet, Claude 3 Haiku

### Azure OpenAI (Enterprise)
1. Go to https://portal.azure.com/
2. Create Azure OpenAI resource
3. Deploy a model
4. Get endpoint URL, API key, and deployment name
5. Enter all three in Garmin Chat settings

---

## 💬 Example Questions

### Activities & Workouts
- "What did I do today?"
- "Show me my last 5 workouts"
- "How many calories did I burn this week?"
- "What was my longest run this month?"
- "Compare my activities from last week to this week"

### Sleep
- "How did I sleep last night?"
- "What was my average sleep time this week?"
- "How much deep sleep did I get?"
- "Show me my sleep patterns for the past month"

### Steps & Movement
- "How many steps did I take today?"
- "Did I reach my step goal?"
- "What's my average daily steps this week?"
- "How many floors did I climb today?"

### Heart Rate & Fitness
- "What was my resting heart rate this morning?"
- "Show me my heart rate during my last workout"
- "What's my current VO2 Max?"
- "Am I training too hard?"

### Body Metrics
- "What's my body battery right now?"
- "How stressed was I today?"
- "Show me my respiration rate"
- "What's my SpO2 level?"

### Date Ranges
- "Show me everything from last week"
- "What did I do between January 1st and January 15th?"
- "Compare this month to last month"
- "Show me my activities from the past 30 days"

---

## 🛠️ Building from Source

### Prerequisites
- Python 3.12 or 3.13
- Windows 10/11 (tested platforms)
- Git

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/rod-trent/GarminChatDesktop.git
cd GarminChatDesktop

# Install dependencies
pip install -r requirements-desktop.txt

# Run application
python GarminChatDesktop.py
```

### Building Executable

**1. Install PyInstaller:**
```bash
pip install pyinstaller
```

**2. Build:**
```bash
build.bat
```

This creates `dist\GarminChat.exe`

**3. Create Installer (Optional):**
- Install [Inno Setup](https://jrsoftware.org/isinfo.php)
- Open `installer.iss` in Inno Setup Compiler
- Click Build → Compile
- Installer created in `installer\` folder

---

## 📋 Requirements

### Python Packages
```
garminconnect>=0.2.0
garth>=0.4.0
openai>=1.0.0
anthropic>=0.18.0
google-generativeai>=0.3.0
requests>=2.31.0
```

Full list in [requirements-desktop.txt](requirements-desktop.txt)

### System Requirements
- **OS**: Windows 10/11, macOS, Linux
- **Python**: 3.12 or 3.13
- **RAM**: 2GB minimum
- **Disk**: 100MB for application + space for dependencies
- **Network**: Internet connection required

---

## 🔒 Privacy & Security

### Data Storage
- **Credentials**: Stored locally in `%USERPROFILE%\.garmin_chat\config.json`
- **Garmin Tokens**: Stored locally in `%USERPROFILE%\.garmin_tokens\`
- **No Cloud Storage**: Everything stays on your machine
- **No Telemetry**: App doesn't send usage data

### Data Transmission
- **Garmin Connect**: Standard OAuth authentication
- **AI Providers**: Only queries and data you explicitly send
- **No Third Parties**: Your data isn't shared

### Security Best Practices
- ✅ Enable MFA on your Garmin account
- ✅ Keep your API keys secure
- ✅ Don't share your config.json file
- ✅ Use strong passwords
- ✅ Keep the app updated

---

## 🤝 Contributing

Contributions are welcome! This project is part of my [JunkDrawer](https://github.com/rod-trent/JunkDrawer) collection of practical tools.

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests

[Open an issue](https://github.com/rod-trent/GarminChatDesktop/issues)

---

## 📝 License

MIT License - See [LICENSE](LICENSE.txt) for details

---

## 🆘 Support

### Having Issues?
1. Check [Releases README](Releases/Readme.md) for version-specific info
2. Review [CHANGELOG](CHANGELOG.md) for known issues
3. Search [existing issues](https://github.com/rod-trent/GarminChatDesktop/issues)
4. Open a [new issue](https://github.com/rod-trent/GarminChatDesktop/issues/new) with:
   - Version number
   - Error message (if any)
   - Steps to reproduce
   - Screenshots (helpful!)

### Common Issues

**"Invalid credentials" error:**
- Verify Garmin email and password
- Check if MFA is enabled (may require token-based auth)
- Try logging into garminconnect.garmin.com directly

**"API key invalid" error:**
- Verify API key is copied correctly
- Check for extra spaces
- Ensure key is active in provider dashboard
- Try regenerating the key

**Window position issues (v4.0.0 only):**
- Fixed in v4.0.1! Download latest release

**App won't start:**
- Check Python version (3.12+ required)
- Verify all dependencies installed
- Try running from command line to see errors

---

## 🔗 Links

- **Author**: Rod Trent
- **Blog**: [Substack](https://rodtrent.substack.com/)
- **GitHub**: [@rod-trent](https://github.com/rod-trent)
- **JunkDrawer**: [More tools](https://github.com/rod-trent/JunkDrawer)
- **Issues**: [Report problems](https://github.com/rod-trent/GarminChatDesktop/issues)

---

## 📊 Version History

- **v4.0.1** (February 2025) - Window positioning bug fixes
- **v4.0.0** (February 2025) - Multi-provider AI support
- **v3.1.0** (January 2025) - 14 health metrics, nutrition tracking
- **v3.0.0** (January 2025) - Desktop app with GUI
- **v2.0.0** (December 2024) - Added sleep and activity tracking
- **v1.0.0** (December 2024) - Initial release

[Full Changelog](CHANGELOG.md)

---

## ⭐ Acknowledgments

Built with:
- [garminconnect](https://github.com/cyberjunky/python-garminconnect) - Garmin Connect API
- [OpenAI](https://openai.com/) - GPT models
- [xAI](https://x.ai/) - Grok models
- [Google](https://ai.google.dev/) - Gemini models
- [Anthropic](https://www.anthropic.com/) - Claude models
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI framework

---

<div align="center">

**Made with ❤️ by Rod Trent**

[⬆ Back to Top](#garmin-chat-desktop)

</div>
