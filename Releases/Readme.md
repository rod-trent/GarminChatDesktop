# Garmin Chat Desktop - Releases

Official releases of Garmin Chat Desktop are published here.

## Latest Release: v4.0.3 (February 15, 2026)

### 🎉 What's New in v4.0.3

**Major Features:**
- ⚙️ **Customizable Quick Questions** - Create up to 8 personalized quick questions
- 🎨 **Rounded Hover Effects** - Modern, polished button styling
- 🚀 **Professional Splash Screen** - Beautiful startup with logo and version

**Bug Fixes:**
- ✅ Fixed all character encoding issues (emojis, bullets, symbols)
- 🪟 Fixed dialog window flashing on open
- 🔤 Perfect text rendering throughout the app
- 📝 Clean markdown formatting in AI responses

**Technical Updates:**
- 📦 Migrated to new `google-genai` package (replaces deprecated `google-generativeai`)
- 🔧 Enhanced error handling for all AI providers
- 💾 Persistent custom quick questions storage

### 📥 Download v4.0.3

**Windows Installer (Recommended):**
- [GarminChatDesktop_v4.0.3_Setup.exe](https://github.com/rod-trent/GarminChatDesktop/blob/main/Releases/GarminChatDesktop_v4.0.3_Setup.exe)
- Size: ~60-80 MB
- Includes uninstaller
- Creates Start Menu shortcuts

**Portable Version:**
- [GarminChat.exe](https://github.com/rod-trent/GarminChatDesktop/blob/main/Releases/GarminChat.exe)
- Size: ~50-70 MB
- No installation required
- Run from any location

**Source Code:**
- [Source code)](https://github.com/rod-trent/GarminChatDesktop/tree/main/Code)

### 📚 Documentation
- [Complete README](https://github.com/rod-trent/GarminChatDesktop/blob/main/README.md)
- [Installation Guide](https://github.com/rod-trent/GarminChatDesktop/blob/main/INSTALL.md)
- [Changelog](https://github.com/rod-trent/GarminChatDesktop/blob/main/CHANGELOG.md)
- [Release Notes](https://github.com/rod-trent/GarminChatDesktop/blob/main/RELEASE_NOTES_v4.0.3.md)

### ⚠️ Important: Google Gemini Users

Google deprecated the `google-generativeai` package. If upgrading from v4.0.2 or earlier:

```bash
pip uninstall google-generativeai
pip install google-genai
```

**Note:** Gemini API is currently in beta. For production use, we recommend:
- ⭐ **xAI (Grok)** - Most cost-effective and reliable
- ⭐ **OpenAI** - Most popular and well-tested
- ⭐ **Anthropic (Claude)** - Excellent for longer conversations

---

## Previous Releases

### v4.0.2 (February 2026)
💾 Saved Prompts - Save and reuse your favorite questions
🔍 Search History - Find past conversations quickly
🌓 Dark Mode - Easy on the eyes
📊 Markdown Formatting - Clean, readable responses
🔐 Local & Secure - All data stays on your computer


### v4.0.1 (February 2026)
- 🐛 Fixed window positioning bugs
- 📚 Enhanced documentation
- 🔧 Improved stability

[Download v4.0.1](https://github.com/rod-trent/GarminChatDesktop/releases/tag/v4.0.1)

### v4.0.0 (January 2026)
- 🆕 Initial public release
- 🤖 Multi-AI provider support (xAI, OpenAI, Gemini, Anthropic, Azure)
- 💬 Natural language fitness data queries
- 📊 Comprehensive Garmin Connect data access
- 💾 Chat history management
- 🔍 Search functionality
- 📄 Export reports (PDF, DOCX, TXT)
- 🌓 Dark mode

[Download v4.0.0](https://github.com/rod-trent/GarminChatDesktop/releases/tag/v4.0.0)

---

## Installation

### Windows Installer (Easiest)
1. Download the installer
2. Run the .exe file
3. Follow the setup wizard
4. Launch from Start Menu

### Portable Version
1. Download GarminChat.exe
2. Place in any folder
3. Double-click to run
4. No installation needed!

---

## System Requirements

- **OS:** Windows 10 or later (64-bit)
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 200MB free space
- **Internet:** Required for AI API and Garmin Connect

---

## Getting Started

1. **Install** the application
2. **Configure Settings:**
   - Garmin Connect email and password
   - AI provider and API key (xAI, OpenAI, Gemini, Anthropic, or Azure)
3. **Connect** to Garmin
4. **Start chatting** about your fitness data!

Example questions:
- "How many steps did I take today?"
- "What was my last workout?"
- "Show me my activities from last week"
- "How's my sleep been this month?"

---

## AI Provider Setup

You'll need an API key from at least one provider:

| Provider | Get API Key | Cost | Recommendation |
|----------|-------------|------|----------------|
| **xAI (Grok)** | [console.x.ai](https://console.x.ai/) | $ | ⭐ Best value |
| **OpenAI** | [platform.openai.com](https://platform.openai.com/api-keys) | $$ | Most popular |
| **Gemini** | [makersuite.google.com](https://makersuite.google.com/app/apikey) | $ | Beta - use with caution |
| **Anthropic** | [console.anthropic.com](https://console.anthropic.com/) | $$ | Best for conversation |
| **Azure OpenAI** | Azure Portal | $$$ | Enterprise |

**Typical Cost:** $1-5 per month for regular use

---

## Support

- **Documentation:** [Blog](https://rodtrent.substack.com/s/garmin-chat-desktop)
- **Issues:** [GitHub Issues](https://github.com/rod-trent/GarminChatDesktop/issues)
- **Discussions:** [GitHub Discussions](https://github.com/rod-trent/GarminChatDesktop/discussions)

---

## What's Coming

Future features under consideration:
- 📈 Visual charts and graphs
- 🗣️ Voice input/output
- 📱 Mobile companion app
- ☁️ Optional cloud sync
- 🏆 Goal tracking and AI recommendations

---

## Upgrading

### From v4.0.x to v4.0.3
- ✅ Settings and chat history are preserved
- ✅ Just install - no configuration needed
- ⚠️ If using Gemini: uninstall old package, install new one

### From Earlier Versions
- 💾 Export important chat history first
- 📝 Note your API keys (optional backup)
- ✅ Install v4.0.3
- ⚙️ Reconfigure settings if needed

---

## License

MIT License - See [LICENSE.txt](https://github.com/rod-trent/GarminChatDesktop/blob/main/LICENSE.txt)

---


**Made with ❤️ for fitness enthusiasts**

*Not affiliated with Garmin Ltd. All trademarks are property of their respective owners.*
