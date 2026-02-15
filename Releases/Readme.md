# Garmin Chat Desktop - Releases

This folder contains all official releases of Garmin Chat Desktop. Each release includes a standalone Windows installer and source code.

## Latest Release: v4.0.2 (February 2026)

### 📥 Download

**Windows Installer (Recommended)**
- [GarminChatDesktop_Setup_v4.0.2.exe](v4.0.2/GarminChatDesktop_Setup_v4.0.2.exe)
- Size: ~XX MB
- SHA256: `[hash will be added after build]`

### ✨ What's New in v4.0.2

#### Custom Session Naming
- Give your chat sessions meaningful names when saving
- Easier to identify specific conversations at a glance
- Optional - can still use date/time only if preferred

#### Rename Functionality
- New **Rename** button in Chat History viewer
- Update session names anytime
- Names are preserved in both filename and metadata

#### Enhanced Display
- Chat sessions show custom names with timestamps: `"Morning Run Analysis (2026-02-14 15:30)"`
- Sessions without custom names display date/time only
- Improved readability in Chat History list

#### Bug Fixes
- Fixed all emoji display issues (no more corrupted characters)
- Fixed bullet point rendering in AI responses
- Updated Chat History dialog icon
- Improved window positioning on multi-monitor setups

### 📋 System Requirements

- **Operating System**: Windows 10 or later (64-bit)
- **Memory**: 4 GB RAM minimum, 8 GB recommended
- **Storage**: 100 MB free disk space
- **Internet**: Required for Garmin Connect and AI provider connectivity
- **.NET Framework**: 4.7.2 or later (usually pre-installed on Windows 10+)

### 🔧 Installation Instructions

#### Using the Installer

1. Download `GarminChatDesktop_Setup_v4.0.2.exe`
2. Double-click to run the installer
3. Follow the installation wizard
4. Launch from Start Menu → "Garmin Chat"

#### Using the Portable Version

1. Download `GarminChatDesktop_v4.0.2_Portable.zip`
2. Extract to any folder (e.g., `C:\Programs\GarminChat`)
3. Run `GarminChatDesktop.exe`
4. No installation required - settings saved in the app folder

### 🆕 First-Time Setup

1. **Launch the Application**
2. **Click Settings** and configure:
   - Garmin Connect email and password
   - AI provider API key (choose one):
     - xAI: https://console.x.ai/
     - OpenAI: https://platform.openai.com/api-keys
     - Gemini: https://makersuite.google.com/app/apikey
     - Anthropic: https://console.anthropic.com/
     - Azure: Enter endpoint, deployment, and key
3. **Click "Connect to Garmin"**
4. **Start chatting** with your fitness data!

### ⬆️ Upgrading from v4.0.1

**Automatic Upgrade** (Recommended)
1. Run the v4.0.2 installer
2. It will detect and upgrade your existing installation
3. All settings and chat history are preserved

**Manual Upgrade**
1. Save your chat history (optional backup): `%USERPROFILE%\.garmin_chat\`
2. Uninstall v4.0.1 from Windows Settings → Apps
3. Install v4.0.2 using the new installer
4. Your settings and history will be automatically restored

---

## Previous Releases

### v4.0.1 (February 2026)
**Focus**: Window positioning fixes and stability improvements

**Downloads**
- [GarminChatDesktop_Setup_v4.0.1.exe](v4.0.1/GarminChatDesktop_Setup_v4.0.1.exe)

**Changes**
- Fixed window centering on first launch
- Remember window position and size between sessions
- Prevent window from hiding under taskbar
- Improved multi-monitor support
- Removed non-functional strength training features

**Known Issues** (Fixed in v4.0.2)
- Emoji characters display incorrectly in some UI elements
- No ability to rename saved chat sessions
- Chat sessions only show date/time (no custom names)

### v4.0.0 (January 2026)
**Focus**: Major UI overhaul and feature expansion

**Downloads**
- [GarminChatDesktop_Setup_v4.0.0.exe](v4.0.0/GarminChatDesktop_Setup_v4.0.0.exe)

**Changes**
- Modern Fluent Design UI
- Dark mode support
- Multi-provider AI support (xAI, OpenAI, Gemini, Anthropic, Azure)
- Chat history with search
- Export conversations (PDF, DOCX, TXT)
- Saved prompts library
- Enhanced data access (nutrition, stress, body battery, etc.)
- Conversation context memory

---

## 🔐 Security & Privacy

### Data Storage
- All settings stored locally in: `%USERPROFILE%\.garmin_chat\`
- Chat history saved as JSON files (encrypted options coming soon)
- API keys stored in plaintext config file (secure storage coming soon)

### Network Communication
- Direct connection to Garmin Connect (no intermediary servers)
- Direct connection to chosen AI provider
- No analytics or telemetry collected
- No data shared with third parties

### Best Practices
- Keep API keys private
- Use strong Garmin password
- Enable MFA on Garmin Connect
- Regularly review saved conversations
- Don't share config files containing API keys

---

## 🐛 Known Issues & Workarounds

### Current Known Issues
None at this time. Report issues at: https://github.com/rod-trent/GarminChatDesktop/issues

### Resolved Issues

**v4.0.2 Fixes**
- ✅ Emoji display corruption
- ✅ Bullet points showing as garbled characters
- ✅ Missing rename functionality
- ✅ Chat History dialog icon

**v4.0.1 Fixes**
- ✅ Window positioning off-screen
- ✅ Window size not remembered
- ✅ Taskbar collisions

---

## 📝 Version History Summary

| Version | Release Date | Key Features | Download |
|---------|--------------|--------------|----------|
| 4.0.2 | Feb 2026 | Custom session naming, rename feature | [Download](v4.0.2/) |
| 4.0.1 | Feb 2026 | Window positioning fixes | [Download](v4.0.1/) |
| 4.0.0 | Jan 2026 | Modern UI, multi-provider AI | [Download](v4.0.0/) |
| 3.x | 2025 | Legacy versions | [Archive](archive/) |

---

## 💾 File Structure

Each release folder contains:

```
vX.X.X/
├── GarminChatDesktop_Setup_vX.X.X.exe    # Windows installer
├── GarminChatDesktop_vX.X.X_Portable.zip # Portable version
├── CHANGELOG.md                           # Detailed changes
├── SHA256SUMS.txt                         # File checksums
└── source/                                # Source code
    ├── GarminChatDesktop.py
    ├── garmin_handler.py
    ├── ai_client.py
    ├── requirements.txt
    └── build_files/
        ├── build.bat
        ├── GarminChatDesktop.iss
        └── logo.ico
```

---

## 🔄 Update Policy

- **Major Versions** (x.0.0): Significant new features, potential breaking changes
- **Minor Versions** (4.x.0): New features, improvements, maintains compatibility
- **Patch Versions** (4.0.x): Bug fixes, minor improvements

**Update Frequency**: 
- Patch releases: As needed for critical bugs
- Minor releases: Monthly or as features are completed
- Major releases: Quarterly or as major milestones are reached

**Support Policy**:
- Latest version: Full support
- Previous minor version: Security fixes only
- Older versions: Community support via GitHub Issues

---

## 📞 Support & Feedback

### Getting Help
1. Check the [main README](../README.md) for usage instructions
2. Review [Known Issues](#-known-issues--workarounds)
3. Search existing [GitHub Issues](https://github.com/rod-trent/GarminChatDesktop/issues)
4. Create a new issue if your problem isn't listed

### Reporting Problems
When reporting issues, please include:
- Version number (from Help → About)
- Windows version
- Steps to reproduce
- Error messages or screenshots
- Expected vs actual behavior

### Feature Requests
We love hearing your ideas! Please:
1. Check if it's already in the [Roadmap](../README.md#-roadmap)
2. Open a GitHub Issue with the "enhancement" label
3. Describe the feature and its benefits
4. Provide examples or use cases

---

## 🎉 Thank You!

Thank you for using Garmin Chat Desktop! Your feedback and support make this project possible.

If you find this app useful, please:
- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest features
- 📢 Share with fellow fitness enthusiasts
- 🤝 Contribute code or documentation

---

**Latest Update**: February 14, 2026  
**Maintained By**: Rod Trent  
**License**: MIT
