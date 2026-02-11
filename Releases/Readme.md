# Garmin Chat Desktop - Releases

Official release packages for Garmin Chat Desktop.

---

## 📦 Latest Release

### **v4.0.1 - Window Positioning Bug Fixes** (February 11, 2025)

**🐛 Bug Fix Release**

**Download:**
- **Windows Installer**: `GarminChatDesktop_Setup_v4.0.1.exe`

**What's Fixed:**
- ✅ **Window Centering**: Properly centers on first launch (no more taskbar collision!)
- ✅ **Position Memory**: Remembers window position and size between sessions
- ✅ **Smart Positioning**: Accounts for Windows taskbar height
- ✅ **Off-Screen Protection**: Prevents window from appearing off-screen
- ✅ **Seamless Upgrade**: All v4.0 features intact, fully backward compatible

**Technical Details:**
- Enhanced `center_window()` with taskbar detection (50px)
- Added `window_state` persistence to config.json
- Added `on_closing()` handler for state saving
- Boundary checks prevent off-screen positioning

**System Requirements:**
- Windows 10/11 (64-bit)
- Python 3.12 or 3.13 (for source)
- Internet connection
- API key from at least one AI provider
- Garmin Connect account

**Quick Start:**
1. Download and run the installer
2. Launch Garmin Chat Desktop
3. Window now centers properly!
4. Position/size saved automatically

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

### **v4.0.1** (February 11, 2025) - CURRENT ⭐
**Bug Fix Release**

**Fixes:**
- Window positioning on first launch (no more hidden taskbar)
- Window state persistence (remembers position/size)
- Taskbar collision prevention
- Off-screen window protection

**Technical:**
- Enhanced window centering algorithm
- Added config.json window_state storage
- Clean shutdown with state saving

**[Download v4.0.1](../../releases/tag/v4.0.1)**

---

### **v4.0.0** (February 10, 2025)
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

**Features:**
- 14 comprehensive health metrics
- Enhanced nutrition tracking
- Improved date range detection
- Body Battery, stress, SpO2, HRV support

**Fixes:**
- 403 errors fixed
- Improved date parsing
- Better error handling

**[Download v3.1.0](../../releases/tag/v3.1.0)**

---

### **v3.0.0** (December 2024)
**Desktop Application**

**Features:**
- Tkinter GUI (replaced Gradio)
- Dark mode support
- Auto-login functionality
- Professional Windows installer
- Session persistence

**[Download v3.0.0](../../releases/tag/v3.0.0)**

---

### **v2.0.0** (November 2024)
**xAI Integration**

**Features:**
- Grok AI integration
- Gradio web interface
- Activity analysis

**[Download v2.0.0](../../releases/tag/v2.0.0)**

---

### **v1.0.0** (October 2024)
**Initial Release**

**Features:**
- Basic Garmin Connect integration
- Simple chat interface
- Activity viewing

**[Download v1.0.0](../../releases/tag/v1.0.0)**

---

## 🚀 Installation Methods

### Method 1: Windows Installer (Recommended)

**Easiest way to install:**
1. Download `GarminChatDesktop_Setup_v4.0.1.exe`
2. Run the installer
3. Follow the setup wizard
4. Launch from Start Menu
5. Configure Settings on first run

**Advantages:**
- ✅ Professional installer
- ✅ Start Menu shortcuts
- ✅ Desktop icon option
- ✅ Automatic uninstaller
- ✅ No Python required

---

### Method 2: Run from Source

**For developers:**
```bash
# Clone repository
git clone https://github.com/rod-trent/GarminChatDesktop.git
cd GarminChatDesktop

# Install dependencies
pip install -r requirements-desktop.txt

# Run application
python GarminChatDesktop.py
```

**Advantages:**
- ✅ Latest code
- ✅ Can customize
- ✅ Easy updates

**Requirements:**
- Python 3.12 or 3.13
- Windows 10/11

---

### Method 3: Build from Source

**For packagers:**
```bash
# Install build dependencies
pip install pyinstaller

# Build executable
python -m PyInstaller GarminChatDesktop.spec

# Create installer
# Open installer.iss in Inno Setup Compiler
# Click Compile
```

See [BUILD-INSTRUCTIONS.md](../BUILD-INSTRUCTIONS.md) for details.

---

## 📦 What's Included

### Windows Installer Package:
- `GarminChat.exe` - Application executable
- `README-Desktop.md` - User documentation
- `LICENSE.txt` - MIT License
- Start Menu shortcuts
- Optional desktop icon
- Uninstaller

### Source Code Package:
- `GarminChatDesktop.py` - Main application
- `ai_client.py` - Unified AI client
- `garmin_handler.py` - Garmin Connect integration
- `GarminChatDesktop.spec` - PyInstaller config
- `build.bat` - Build script
- `installer.iss` - Inno Setup script
- `version_info.txt` - Version metadata
- `requirements-desktop.txt` - Dependencies
- Complete documentation

---

## 🔄 Upgrade Guide

### From v4.0.0 to v4.0.1

**Automatic Upgrade:**
1. Install v4.0.1 installer (overwrites v4.0.0)
2. Launch application
3. All settings preserved
4. Window positioning improved

**No Breaking Changes:**
- All v4.0.0 features intact
- Config automatically upgrades
- No manual migration needed

---

### From v3.x to v4.0.1

**Fresh Install Recommended:**
1. Uninstall old version (optional - keeps settings)
2. Install v4.0.1
3. Configure AI provider in Settings
4. All Garmin credentials preserved

**New Features:**
- Choose from 5 AI providers (was 1)
- Save multiple API keys
- Better error handling
- Window positioning fixes

---

### From v2.x or v1.x to v4.0.1

**Fresh Install Required:**
1. Uninstall old version
2. Install v4.0.1
3. Reconfigure all settings (different config format)

**Major Changes:**
- Desktop app (was web-based)
- Multi-provider support
- Dark mode
- Auto-login
- Much faster

---

## 📊 Feature Comparison Matrix

| Feature | v1.x | v2.x | v3.0 | v3.1 | v4.0 | v4.0.1 |
|---------|------|------|------|------|------|--------|
| **Platform** | CLI | Web | Desktop | Desktop | Desktop | Desktop |
| **AI Providers** | 0 | 1 | 1 | 1 | 5 | 5 |
| **Dark Mode** | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Auto-login** | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Health Metrics** | Basic | Basic | Basic | 14 | 14 | 14 |
| **Date Ranges** | ❌ | ❌ | Basic | Advanced | Advanced | Advanced |
| **Provider Switch** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Model Migration** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Window Memory** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Taskbar Fix** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## 🔧 Troubleshooting

### Installation Issues

**"Windows protected your PC"**
- Click "More info" → "Run anyway"
- This is normal for unsigned apps

**"Cannot install to Program Files"**
- Run installer as Administrator
- Right-click → "Run as administrator"

**"Missing DLL" errors**
- Install Visual C++ Redistributable
- https://aka.ms/vs/17/release/vc_redist.x64.exe

---

### v4.0.1 Specific Issues

**Window still appears off-screen**
- Delete config file: `%USERPROFILE%\.garmin_chat\config.json`
- Restart app
- Window will center automatically

**Window position not saving**
- Make sure app closes normally (don't force-close)
- Check file permissions on `%USERPROFILE%\.garmin_chat\`
- Run app as Administrator (once) to fix permissions

**Taskbar still covering window**
- Update to v4.0.1 (this fixes the issue)
- If still happening, report bug with:
  - Windows version
  - Taskbar position (bottom/top/left/right)
  - Screen resolution

---

### General Issues

**"Could not authenticate with Garmin"**
- Check email/password in Settings
- Try logging into Garmin Connect website
- Wait 5 minutes and try again
- Check internet connection

**"Invalid API key"**
- Verify key copied correctly (no spaces/newlines)
- Check provider dashboard (key may be deactivated)
- Ensure billing enabled (if using paid tier)
- Try generating new key

**"Rate limit exceeded" (Gemini)**
- Gemini free tier: 15 requests/minute
- Wait 1 minute between queries
- Consider upgrading to paid tier
- Or switch to different provider

**"Module not found" errors (source)**
- Run: `pip install -r requirements-desktop.txt`
- Make sure using Python 3.12 or 3.13
- Create fresh virtual environment if issues persist

---

### Provider-Specific Troubleshooting

**xAI (Grok):**
- Ensure API key from console.x.ai
- Check billing status
- Verify grok-3 model selected

**OpenAI:**
- Ensure API key from platform.openai.com
- Add payment method (required)
- Check usage limits

**Azure OpenAI:**
- Requires Azure subscription
- Need endpoint URL + deployment name
- Check resource region

**Google Gemini:**
- Free tier has strict rate limits (15/min)
- Complex setup (see provider docs)
- May need to enable billing

**Anthropic (Claude):**
- Ensure API key from console.anthropic.com
- Check usage limits
- Verify model name

---

## 📞 Getting Help

**Before Reporting Issues:**
1. Check this troubleshooting section
2. Search existing issues
3. Make sure you're on latest version
4. Try deleting config and reconfiguring

**When Reporting Issues:**
- App version (check Settings → About)
- Windows version
- AI provider being used
- Error message (exact text)
- Steps to reproduce
- Screenshots if relevant

**Where to Get Help:**
- [GitHub Issues](../../issues) - Bug reports, feature requests
- [Discussions](../../discussions) - Questions, community help
- [RodTrent.com](https://rodtrent.substack.com/) - Blog updates

---

## 📚 Documentation

- **User Guide**: [README.md](../README.md)
- **Changelog**: [CHANGELOG.md](../CHANGELOG.md)
- **Build Instructions**: [BUILD-INSTRUCTIONS.md](../BUILD-INSTRUCTIONS.md)
- **License**: [LICENSE.txt](../LICENSE.txt)

---

## 🔒 Security & Privacy

**Data Storage:**
- All credentials stored locally only
- No telemetry or usage tracking
- No data sent to third parties (except APIs)

**API Keys:**
- Stored in `%USERPROFILE%\.garmin_chat\config.json`
- Not encrypted (file-system permissions only)
- Never transmitted except to respective APIs

**Garmin Password:**
- Stored locally for convenience
- Used only to authenticate with Garmin
- Never transmitted elsewhere

**Session Tokens:**
- Cached for faster reconnection
- Stored in `%USERPROFILE%\.garmin_tokens\`
- Auto-refreshed as needed

**Best Practices:**
- Keep config file secure
- Don't share config file
- Use strong Garmin password
- Review API usage regularly

---

## 📄 License

MIT License - see [LICENSE.txt](../LICENSE.txt) for full text.

Free to use, modify, and distribute with attribution.

---

## 🙏 Acknowledgments

**Built With:**
- garminconnect - Garmin API wrapper
- garth - Garmin authentication
- OpenAI SDK - xAI, OpenAI, Azure
- Anthropic SDK - Claude
- Google Generative AI - Gemini
- Tkinter - GUI framework

**Special Thanks:**
- Garmin Connect community
- Python open source contributors
- Beta testers and early adopters

---

## 🔗 Links

- **Main Repository**: https://github.com/rod-trent/GarminChatDesktop
- **Releases**: https://github.com/rod-trent/GarminChatDesktop/releases
- **Issues**: https://github.com/rod-trent/GarminChatDesktop/issues
- **Blog**: https://rodtrent.substack.com/

---

**Happy Training! 🏃‍♂️💪📊**
