# Garmin Chat Desktop v4.0 - Release Files

## 🎉 What's New in v4.0

**Multi-Provider AI Support!** Choose from 5 AI providers:
- xAI (Grok)
- OpenAI (ChatGPT)
- Azure OpenAI
- Google Gemini
- Anthropic (Claude)

**Features:**
- ✅ Save multiple API keys
- ✅ Switch providers anytime
- ✅ Automatic model migration for deprecated models
- ✅ Enhanced error messages with provider-specific guidance
- ✅ Dark mode support for Settings dialog
- ✅ All provider keys stored securely

---

## 📦 Files Included

### Core Application Files
- `GarminChatDesktop.py` - Main application (v4.0)
- `ai_client.py` - Unified AI client for all providers
- `garmin_handler.py` - Garmin Connect integration
- `requirements-desktop.txt` - Python dependencies

### Build Files
- `GarminChatDesktop.spec` - PyInstaller configuration
- `build.bat` - Automated build script
- `version_info.txt` - Windows executable version info
- `installer.iss` - Inno Setup installer script

### User Files
- `Setup.bat` - Easy dependency installation
- `Startup.bat` - Launch application
- `logo.ico` - Application icon
- `LICENSE.txt` - MIT License

---

## 🚀 Quick Start (From Source)

### 1. Install Dependencies
```bash
Setup.bat
```

### 2. Run Application
```bash
Startup.bat
```

### 3. Configure Settings
- Open Settings in the app
- Select your AI provider
- Enter API key and Garmin credentials
- Save and start chatting!

---

## 🔨 Building Executable

### Prerequisites
- Python 3.12 or 3.13
- PyInstaller: `pip install pyinstaller`
- Inno Setup: https://jrsoftware.org/isinfo.php

### Build Steps

**1. Build Executable:**
```bash
build.bat
```
This creates `dist\GarminChat.exe`

**2. Create Installer:**
- Open `installer.iss` in Inno Setup Compiler
- Click Build → Compile
- Installer created: `installer\GarminChatDesktop_Setup_v4.0.exe`

---

## 📋 Dependencies

```
garminconnect>=0.2.0
garth>=0.4.0
openai>=1.0.0
anthropic>=0.18.0
google-generativeai>=0.3.0
requests>=2.31.0
```

---

## 🔑 Getting API Keys

### xAI (Grok)
https://console.x.ai/

### OpenAI (ChatGPT)
https://platform.openai.com/api-keys

### Google Gemini
https://makersuite.google.com/app/apikey

### Anthropic (Claude)
https://console.anthropic.com/

### Azure OpenAI
https://portal.azure.com/

---

## 📝 Version History

### v4.0.0 (February 2025)
- Multi-provider AI support (5 providers)
- Automatic model migration
- Enhanced error handling
- Dark mode Settings improvements
- Provider-specific rate limit guidance

### v3.1.0 (January 2025)
- 14 health metrics
- Enhanced nutrition tracking
- Improved date range detection

---

## 📄 License

MIT License - See LICENSE.txt

---

## 🔗 Links

- GitHub: https://github.com/rod-trent/JunkDrawer
- Issues: https://github.com/rod-trent/JunkDrawer/issues

---

## ⚙️ Technical Notes

### PyInstaller Build
The `.spec` file includes all necessary hidden imports for:
- All 5 AI provider SDKs
- Garmin Connect integration
- Tkinter GUI components

### Inno Setup Installer
Creates a professional Windows installer with:
- Start Menu shortcuts
- Optional desktop icon
- Automatic uninstaller
- Post-install welcome message

### Configuration Storage
All settings stored in: `%USERPROFILE%\.garmin_chat\config.json`

---

## 🆘 Support

For issues, questions, or feature requests:
https://github.com/rod-trent/JunkDrawer/issues
