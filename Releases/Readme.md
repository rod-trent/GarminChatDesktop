# Garmin Chat Desktop - Releases

Official release packages for Garmin Chat Desktop.

---

## 📦 Latest Release

### **v4.0.0 - Multi-Provider AI Support** (February 2025)

**🎉 Major Update: Choose from 5 AI Providers!**

**Download:**
- **Windows Installer**: `[GarminChatDesktop_Setup_v4.0.exe](https://github.com/rod-trent/GarminChatDesktop/blob/main/Releases/GarminChatDesktop_Setup_v4.0.exe)` 

**What's New:**
- ✅ **5 AI Providers**: xAI (Grok), OpenAI (ChatGPT), Azure OpenAI, Google Gemini, Anthropic (Claude)
- ✅ **Save Multiple API Keys**: Store credentials for all providers
- ✅ **Switch Providers Anytime**: Change AI without losing settings
- ✅ **Automatic Model Migration**: Deprecated models updated automatically
- ✅ **Enhanced Error Messages**: Provider-specific guidance
- ✅ **Rate Limit Handling**: Smart guidance for free tier limits
- ✅ **Dark Mode Improvements**: Fixed hover states in Settings
- ✅ **Consistent Icons**: Proper gear icon everywhere

**System Requirements:**
- Windows 10/11 (64-bit)
- Python 3.12 or 3.13 (for source)
- Internet connection
- API key from at least one AI provider
- Garmin Connect account

**Quick Start:**
1. Download and run the installer
2. Launch Garmin Chat Desktop
3. Open Settings (⚙️)
4. Select your AI provider
5. Enter API key and Garmin credentials
6. Connect and start chatting!

---

## 🤖 AI Provider Comparison

| Provider | Best For | Free Tier | Cost (Paid) | Setup Difficulty |
|----------|----------|-----------|-------------|------------------|
| **xAI (Grok)** | Fast responses, casual use | No | ~$2/1M tokens | ⭐ Easy |
| **OpenAI (ChatGPT)** | Reliability, most tested | No | $0.15/1M tokens | ⭐ Easy |
| **Azure OpenAI** | Enterprise, compliance | No | Custom pricing | ⭐⭐ Moderate |
| **Google Gemini** | Budget-conscious, free tier | **Yes** | $0.15/1M tokens | ⭐⭐⭐⭐ Complex |
| **Anthropic (Claude)** | Long context, quality | No | $0.25/1M tokens | ⭐ Easy |

### Recommendations:
- **New users**: Start with **OpenAI (gpt-4o-mini)** - Cheap, reliable
- **Free tier**: Try **Google Gemini** - Note: 15 req/min rate limit
- **Best quality**: Use **Anthropic Claude** - Excellent for analysis
- **Enterprise**: Consider **Azure OpenAI** - Compliance ready

### Get API Keys:
- **xAI**: https://console.x.ai/
- **OpenAI**: https://platform.openai.com/api-keys
- **Gemini**: https://makersuite.google.com/app/apikey
- **Anthropic**: https://console.anthropic.com/
- **Azure**: https://portal.azure.com/

---

## 📋 Version History

### **v4.0.0** (February 2025) - CURRENT ⭐
**Multi-Provider AI Support**

**Major Features:**
- 5 AI provider options (xAI, OpenAI, Azure, Gemini, Anthropic)
- Multiple API key storage
- Instant provider switching
- Automatic model migration
- Provider-specific error handling
- Rate limit guidance

**Enhancements:**
- Enhanced Settings dialog with provider selection
- Dark mode hover state fixes
- Consistent gear icon everywhere
- Better error messages with dashboard links

**Technical:**
- New unified AI client architecture
- Native SDK support (Anthropic, Gemini)
- Updated build system
- Version 4.0.0.0 metadata

**[Download v4.0.0](../../releases/tag/v4.0.0)**

---

### **v3.1.0** (January 2025)
**Enhanced Health Metrics**

**New Features:**
- 14 comprehensive health metrics
- Body Battery tracking
- Stress level monitoring
- HRV (Heart Rate Variability)
- VO2 Max and fitness age
- Training status and load
- Body composition

**Improvements:**
- Enhanced nutrition tracking (3-tier fallback)
- Better date range detection ("last month", "this week")
- Improved error handling for health data
- Fixed 403 errors with display_name helper

**[Download v3.1.0](../../releases/tag/v3.1.0)**

---

### **v3.0.0** (December 2024)
**Major UI Overhaul**

**New Features:**
- 🌙 **Dark Mode** - Full theme support with instant toggle
- 📂 **Chat History Viewer** - Browse and load past conversations
- 🔍 **Full-Text Search** - Search across all saved chats
- 💾 **Saved Prompts** - Reuse favorite questions
- 📄 **Export Reports** - PDF, Word (.docx), and Text formats
- 💡 **Smart Suggestions** - AI-generated proactive insights
- 🔄 **Follow-up Questions** - Context-aware quick actions

**Improvements:**
- Windows 11 Fluent Design aesthetic
- Card-based layout with elevated components
- Color-coded messages
- Larger, clearer icon buttons with tooltips
- Chat context memory across sessions

**[Download v3.0.0](../../releases/tag/v3.0.0)**

---

### **v2.0.0** (November 2024)
**Desktop Enhancement**

**New Features:**
- ✨ In-app credential management (no .env files)
- 🔐 Persistent MFA token storage (~30 days)
- 🚀 Auto-login on startup (configurable)
- 🎨 Enhanced markdown rendering
- 💬 Multi-line input field

**Improvements:**
- Automatic token refresh
- Better UI spacing and layout
- Enhanced error handling and logging
- Application preferences in Settings

**[Download v2.0.0](../../releases/tag/v2.0.0)**

---

### **v1.0.0** (October 2024)
**Initial Desktop Release**

**Features:**
- Basic desktop application
- xAI (Grok) integration
- Garmin Connect authentication
- Natural language queries
- Activity data access
- Sleep data tracking

**[Download v1.0.0](../../releases/tag/v1.0.0)**

---

## 📥 Installation Methods

### **Option 1: Windows Installer** (Recommended)
**Best for most users**

1. Download `GarminChatDesktop_Setup_v4.0.exe`
2. Run the installer
3. Follow the setup wizard
4. Launch from Start Menu or Desktop

**Advantages:**
- ✅ Easy installation (2 clicks)
- ✅ Start Menu shortcuts
- ✅ Desktop icon (optional)
- ✅ Professional uninstaller
- ✅ No Python required
- ✅ Auto-updates (coming soon)

**Size:** ~50-80 MB

---

### **Option 2: Source Code**
**Best for developers**

1. Download `garmin-chat-v4.0-release.zip`
2. Extract to a folder
3. Run `Setup.bat` (installs Python dependencies)
4. Run `Startup.bat` (launches application)

**Advantages:**
- ✅ View source code
- ✅ Modify as needed
- ✅ Build custom executable
- ✅ Learn from code
- ✅ Contribute improvements

**Requirements:**
- Python 3.12 or 3.13
- Internet connection

---

### **Option 3: Build from Source**
**Best for customization**

1. Clone or download repository
2. Navigate to `/Code` folder
3. Run `Setup.bat` (install dependencies)
4. Run `build.bat` (create .exe with PyInstaller)
5. Use `installer.iss` with Inno Setup (optional)

**Build Tools Needed:**
- Python 3.12+
- PyInstaller
- Inno Setup (for installer)

See `BUILD-INSTRUCTIONS.md` in release package for details.

---

## 🔄 Upgrading from Previous Versions

### **From v3.x to v4.0:**

**Automatic Upgrade:**
1. Install v4.0 over existing installation
2. Launch application
3. Settings dialog opens automatically
4. Select your AI provider (defaults to xAI)
5. Enter API key for chosen provider
6. Save and connect

**What's Preserved:**
- ✅ Garmin credentials
- ✅ Chat history
- ✅ Saved prompts
- ✅ Application preferences (dark mode, auto-login)
- ✅ MFA tokens

**What's New:**
- ⚠️ Must select AI provider on first v4.0 launch
- ⚠️ xAI API key needs re-entry in provider system
- ✅ Can now add keys for all 5 providers
- ✅ Switch providers anytime

---

### **From v2.x or v1.x to v4.0:**

**Fresh Install Recommended:**

1. **Backup** (optional but recommended):
   - Chat history: `%USERPROFILE%\.garmin_chat\chat_history\`
   - Saved prompts: `%USERPROFILE%\.garmin_chat\saved_prompts.json`
   - Config: `%USERPROFILE%\.garmin_chat\config.json`

2. **Uninstall** old version:
   - Control Panel → Programs → Uninstall

3. **Install** v4.0:
   - Run new installer
   - Follow setup wizard

4. **Configure** (fresh setup):
   - Select AI provider
   - Enter new API key
   - Enter Garmin credentials
   - Restore chat history (if backed up)

---

## 🎯 Feature Comparison

| Feature | v1.0 | v2.0 | v3.0 | v3.1 | **v4.0** |
|---------|------|------|------|------|----------|
| Basic chat | ✅ | ✅ | ✅ | ✅ | ✅ |
| xAI (Grok) | ✅ | ✅ | ✅ | ✅ | ✅ |
| **5 AI providers** | ❌ | ❌ | ❌ | ❌ | **✅** |
| **Provider switching** | ❌ | ❌ | ❌ | ❌ | **✅** |
| **Multi API keys** | ❌ | ❌ | ❌ | ❌ | **✅** |
| In-app settings | ❌ | ✅ | ✅ | ✅ | ✅ |
| Auto-login | ❌ | ✅ | ✅ | ✅ | ✅ |
| Dark mode | ❌ | ❌ | ✅ | ✅ | ✅ |
| Chat history | ❌ | ❌ | ✅ | ✅ | ✅ |
| Export reports | ❌ | ❌ | ✅ | ✅ | ✅ |
| Search chats | ❌ | ❌ | ✅ | ✅ | ✅ |
| Health metrics | Basic | Basic | Enhanced | **14+** | 14+ |
| **Model migration** | ❌ | ❌ | ❌ | ❌ | **✅** |
| **Rate limit help** | ❌ | ❌ | ❌ | ❌ | **✅** |

---

## 🐛 Troubleshooting

### **Installation Issues**

**"Windows protected your PC"**
- Click "More info" → "Run anyway"
- This is normal for new installers

**"Python not found" (source install)**
- Install Python 3.12+ from python.org
- Check "Add Python to PATH"
- Restart terminal

**"Setup.bat failed"**
- Run as Administrator
- Check internet connection
- Try: `pip install -r requirements-desktop.txt`

---

### **v4.0 Specific Issues**

**"No AI provider selected"**
- Open Settings (⚙️)
- Select a provider (radio button)
- Enter API key
- Save

**"Model deprecated"**
- App auto-migrates on restart
- Or manually: Settings → Choose new model → Save

**"Rate limit exceeded" (Gemini)**
- Wait 60 seconds (free tier: 15 req/min)
- Or switch to different provider
- Or upgrade Gemini: console.cloud.google.com

**"API key invalid"**
- Verify key from provider dashboard
- Check for typos/extra spaces
- Regenerate key if needed

---

### **General Issues**

**"Configuration Required"**
- Settings → Enter all credentials → Save

**"MFA code failed"**
- Use code within 30 seconds
- Try new code if expired
- Check authenticator app time sync

**"Connection failed"**
- Check internet connection
- Verify Garmin Connect is accessible
- Wait if rate limited (429 error)

---

## 📚 Documentation

- **Main README**: [Repository Root](../../)
- **FAQ**: [Frequently Asked Questions](../../FAQ.md)
- **Build Guide**: `BUILD-INSTRUCTIONS.md` (in release package)
- **Changelog**: `CHANGELOG.md` (in release package)
- **Issues**: [Report Problems](../../issues)

---

## 💡 Getting Help

1. **Check Documentation** - README and FAQ
2. **Search Issues** - Someone may have same problem
3. **Create Issue** - Provide details:
   - Version number
   - Windows version
   - Error messages
   - Steps to reproduce

---

## 🔐 Security & Privacy

- **Local storage only** - No cloud sync
- **Encrypted credentials** - Secure local files
- **No telemetry** - No usage tracking
- **No data sharing** - Your data stays private
- **Multiple API keys** - All stored securely

**Storage Locations:**
- Settings: `%USERPROFILE%\.garmin_chat\config.json`
- Chat history: `%USERPROFILE%\.garmin_chat\chat_history\`
- Garmin tokens: `%USERPROFILE%\.garmin_tokens\`

---

## 📜 License

MIT License - See [LICENSE](../../LICENSE) file

**TL;DR:** Free to use, modify, distribute. No warranty.

---

## 🙏 Acknowledgments

- **Garmin Connect** - Fitness data platform
- **AI Providers** - xAI, OpenAI, Anthropic, Google, Microsoft
- **Python Community** - garminconnect, garth libraries
- **Contributors** - Everyone who reported issues and suggested features

---

## ⭐ Support This Project

If you find Garmin Chat Desktop useful:

1. **⭐ Star this repository**
2. **🐛 Report issues** you find
3. **💡 Suggest features** you want
4. **📢 Share** with friends who use Garmin
5. **🤝 Contribute** code improvements

---

**Ready to chat with your Garmin data using your favorite AI?**

[Download Latest Release](../../releases/latest) | [View All Releases](../../releases) | [Back to Main](../../)
