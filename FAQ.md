# Garmin Chat Desktop - Frequently Asked Questions (FAQ)

**Last Updated:** February 15, 2026 | **Version:** 4.0.3

---

## 📑 Table of Contents

- [General Questions](#general-questions)
- [Installation & Setup](#installation--setup)
- [AI Provider Questions](#ai-provider-questions)
- [Garmin Connect Questions](#garmin-connect-questions)
- [Features & Usage](#features--usage)
- [Troubleshooting](#troubleshooting)
- [Privacy & Security](#privacy--security)
- [Technical Questions](#technical-questions)

---

## General Questions

### What is Garmin Chat Desktop?

Garmin Chat Desktop is a Windows desktop application that lets you chat with AI about your Garmin fitness data. Ask questions in plain English like "How did I sleep last night?" or "What was my longest run this month?" and get intelligent, conversational answers.

### What can I ask about?

You can query any data tracked by your Garmin device:
- **Activities:** Runs, walks, bikes, swims, workouts, etc.
- **Sleep:** Total sleep, deep/light/REM stages, sleep quality
- **Daily Stats:** Steps, distance, calories, floors climbed
- **Health Metrics:** Body Battery, stress, heart rate, HRV, SpO2
- **Nutrition:** Food logged, calories consumed, macros
- **Training:** VO2 Max, fitness age, training status, training load
- **Trends:** Weekly/monthly comparisons, progress tracking

### Is this an official Garmin product?

No. Garmin Chat Desktop is an independent third-party application. It uses Garmin's public APIs but is not affiliated with, endorsed by, or supported by Garmin Ltd.

### How much does it cost?

The application is **free and open source** (MIT License). However, you'll need an API key from an AI provider:
- **xAI (Grok):** ~$1-3/month for typical use ⭐ Best value
- **OpenAI:** ~$3-5/month for typical use
- **Anthropic (Claude):** ~$3-5/month for typical use
- **Google Gemini:** ~$1-2/month (but currently in beta)
- **Azure OpenAI:** Variable pricing (enterprise)

### What's new in v4.0.3?

**Major Features:**
- ⚙️ Customizable Quick Questions (up to 8 personalized shortcuts)
- 🚀 Professional splash screen with logo
- 🎨 Rounded hover effects and polished UI

**Bug Fixes:**
- ✅ Fixed character encoding issues (emojis, bullets, symbols)
- 🪟 Fixed dialog flashing
- 📝 Clean markdown formatting

**Technical:**
- 📦 Migrated to new `google-genai` package (old one deprecated)
- 🔧 Enhanced error handling
- 💾 Persistent custom quick questions

---

## Installation & Setup

### What are the system requirements?

- **Operating System:** Windows 10 or later (64-bit)
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 200MB free space
- **Internet:** Required for AI and Garmin Connect access
- **Python:** Not required for installer version; 3.8+ for source

### How do I install it?

**Option 1: Installer (Recommended)**
1. Download `GarminChatDesktop_v4.0.3_Setup.exe`
2. Run the installer
3. Follow the setup wizard
4. Launch from Start Menu

**Option 2: Portable**
1. Download `GarminChat.exe`
2. Place in any folder
3. Double-click to run
4. No installation needed!

**Option 3: Build from Source**
See [INSTALL.md](INSTALL.md) for detailed instructions.

### What do I need to get started?

1. **Garmin Connect Account** (free)
   - Your Garmin email and password
2. **AI Provider API Key** (one of):
   - xAI (Grok) - [Get key](https://console.x.ai/)
   - OpenAI - [Get key](https://platform.openai.com/api-keys)
   - Anthropic (Claude) - [Get key](https://console.anthropic.com/)
   - Google Gemini - [Get key](https://makersuite.google.com/app/apikey)
   - Azure OpenAI - Contact Azure sales

### Why won't the app launch?

**Common solutions:**
1. **Antivirus blocking:** Add exception for `GarminChat.exe`
2. **Missing Visual C++ Runtime:** Download from [Microsoft](https://aka.ms/vs/17/release/vc_redist.x64.exe)
3. **Windows SmartScreen:** Click "More info" → "Run anyway"
4. **Corrupted download:** Re-download the installer

### How do I update to v4.0.3?

**If using installer:**
1. Download new installer
2. Run it (will upgrade automatically)
3. Your settings and chat history are preserved

**If using portable:**
1. Download new `GarminChat.exe`
2. Replace old file
3. Your settings are in `%USERPROFILE%\.garmin_chat` (safe)

**If upgrading from v4.0.2 or earlier and using Gemini:**
```bash
pip uninstall google-generativeai
pip install google-genai
```

---

## AI Provider Questions

### Which AI provider should I choose?

**Best for most users:**
- ⭐ **xAI (Grok)** - Best value, fast, reliable, $1-3/month
- ⭐ **OpenAI (ChatGPT)** - Most popular, well-tested, $3-5/month
- ⭐ **Anthropic (Claude)** - Great conversation quality, $3-5/month

**Other options:**
- **Google Gemini** - Cheap but currently in beta (use with caution)
- **Azure OpenAI** - For enterprises with existing Azure

### Why is Gemini giving me errors?

**Common error:**
```
404 NOT_FOUND: models/gemini-1.5-pro is not found for API version v1beta
```

**Reasons:**
- Google's new `google-genai` SDK is in beta (v0.2.x)
- API availability varies by region
- Some models aren't stable yet

**Solutions:**
1. Try `gemini-1.5-flash-8b` or `gemini-1.5-flash` (more stable)
2. **Recommended:** Switch to xAI, OpenAI, or Anthropic
3. Wait for SDK v0.3+ (more mature)

See [GEMINI_TROUBLESHOOTING.md](GEMINI_TROUBLESHOOTING.md) for details.

### Can I use multiple AI providers?

Yes! You can configure API keys for all providers and switch between them in Settings. This lets you:
- Compare response quality
- Take advantage of different pricing
- Have a backup if one provider is down

### How much will API usage cost?

**Typical monthly cost for average user (30-50 queries/day):**
- xAI (Grok): $1-3
- OpenAI (GPT-4o): $3-5
- Anthropic (Claude): $3-5
- Gemini: $1-2
- Azure: Varies

**Cost-saving tips:**
- Start with free tier credits
- Use shorter conversations (reset between topics)
- Choose efficient models (grok-3, gemini-1.5-flash)
- Switch providers based on current promotions

### What if I run out of API credits?

1. App will show an error message
2. Check your provider's dashboard for usage
3. Add more credits or upgrade your plan
4. Or switch to a different provider in Settings

---

## Garmin Connect Questions

### Do I need a Garmin device?

Yes. You need:
- A Garmin device (watch, bike computer, etc.)
- An active Garmin Connect account
- Recent synced data

### Is my Garmin password safe?

**Yes!** Your credentials are:
- Stored locally on your computer only
- Never sent to any AI provider
- Encrypted in Windows Credential Manager (optional)
- Used only to connect to Garmin's official API

See [Privacy & Security](#privacy--security) for more details.

### What if I use two-factor authentication (MFA)?

Fully supported! When you connect:
1. App detects MFA is required
2. Shows a code entry field
3. Enter your 6-digit code from authenticator app
4. Connection completes

### Why can't I see my latest workout?

**Possible reasons:**
1. **Not synced yet:** Sync your device with Garmin Connect
2. **Sync delay:** Can take 5-10 minutes after sync
3. **Need to refresh:** Click the "Refresh" button
4. **Connection expired:** Click "Connect to Garmin" again

### Can I see data from multiple devices?

Yes! Garmin Connect aggregates data from all your devices. The app will show activities and data from any device linked to your account.

### What Garmin data is NOT available?

Due to Garmin API limitations:
- ❌ Granular strength training (sets, reps, weights per exercise)
- ❌ Golf scorecards (holes, shots)
- ❌ Some advanced cycling metrics (FTP tests, power curves)
- ❌ Private/hidden activities
- ❌ Real-time live tracking

Everything else is accessible!

---

## Features & Usage

### How do I customize Quick Questions?

**New in v4.0.3!**

1. Right-click any Quick Question button
2. Select "Edit Quick Questions"
3. Create up to 8 custom questions
4. They're saved automatically
5. Use them with one click!

**Examples:**
- "What's my weekly running mileage?"
- "Did I hit my sleep goal last night?"
- "Show my Body Battery trend this week"
- "Compare this month to last month"

### How do I save a conversation?

1. Click the "💾 Save" button
2. Enter a custom name (optional)
3. File saved to `%USERPROFILE%\.garmin_chat\chat_history\`
4. View later with "📂 History" button

### How do I search my chat history?

1. Click the "🔍" search button (top right)
2. Enter your search term
3. See all matching messages
4. Results show context and timestamps

### Can I export conversations?

Yes! Click "📄" export button:
- **PDF** - Professional formatted document
- **Word (.docx)** - Editable document
- **Text (.txt)** - Plain text

Options to include/exclude timestamps and system messages.

### How do I use Dark Mode?

Click the "🌙" button in the top-right corner. Your preference is saved automatically.

### What are "Saved Prompts"?

Save frequently-used questions for quick reuse:
1. Click "💾 Prompts"
2. Create new prompt with name and text
3. Select and use anytime
4. Great for complex queries you use often

### Can I ask about date ranges?

Yes! Examples:
- "Show activities from last 30 days"
- "How did I sleep this week?"
- "What's my mileage for January?"
- "Compare my last 10 runs"

The app automatically fetches the right data range.

---

## Troubleshooting

### "Not connected" - can't connect to Garmin

**Solutions:**
1. **Check credentials:** Verify email/password in Settings
2. **Check internet:** Ensure you're online
3. **MFA required:** Enter your 6-digit code when prompted
4. **Garmin down:** Check [Garmin Connect Status](https://connect.garmin.com/)
5. **Too many attempts:** Wait 15 minutes, try again

### "API Error" or "Invalid API Key"

**Solutions:**
1. **Check key:** Copy/paste carefully (no extra spaces)
2. **Check provider:** Ensure key is for selected provider
3. **Check credits:** Verify you have API credits remaining
4. **Regenerate key:** Create a new key in provider dashboard
5. **Enable API:** Some providers require API activation

### App is slow or freezing

**Solutions:**
1. **Close other apps:** Free up RAM
2. **Reset chat:** Click "🗑️ Reset" to clear conversation
3. **Smaller queries:** Ask about shorter time periods
4. **Update app:** Download latest version
5. **Reinstall:** Uninstall and reinstall fresh

### Character encoding issues (weird symbols)

**Fixed in v4.0.3!** If you still see issues:
1. Update to v4.0.3
2. Restart the app
3. Check your Windows is set to UTF-8 encoding

### Window opens off-screen

**Solutions:**
1. Delete config file: `%USERPROFILE%\.garmin_chat\config.json`
2. Restart app (will center on screen)
3. Or: Alt+Space → M → Arrow keys to move window

### Antivirus keeps blocking the app

**Why:** PyInstaller executables sometimes trigger false positives

**Solutions:**
1. Add exception for `GarminChat.exe`
2. Add exception for the installation folder
3. Check with VirusTotal: [virustotal.com](https://www.virustotal.com/)
4. Build from source yourself to verify it's clean

### "Module not found" error when running from source

**Solutions:**
```bash
# Uninstall old Google package (if upgrading)
pip uninstall google-generativeai

# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install garminconnect requests Pillow openai google-genai anthropic
```

---

## Privacy & Security

### What data does the app collect?

**None!** The app:
- ✅ Runs completely locally on your computer
- ✅ Stores data only on your machine
- ✅ Never sends analytics or telemetry
- ✅ No user tracking whatsoever

### Where is my data stored?

All data is stored locally in:
```
%USERPROFILE%\.garmin_chat\
├── config.json              # Settings
├── saved_prompts.json       # Your saved prompts
└── chat_history\            # Conversation history
```

**You can:**
- Back up this folder
- Delete it to reset everything
- Move it between computers

### What data is sent to AI providers?

Only what's needed for your question:
- Your question text
- Relevant Garmin data (only what matches your query)
- Conversation history (last 10 messages for context)

**Never sent:**
- Your Garmin password
- Your personal information
- Unrelated Garmin data
- Your location
- Device information

### Are my Garmin credentials stored securely?

**Yes!** Two options:
1. **Default:** Stored in `config.json` (local file, not encrypted)
2. **Secure:** Enable Windows Credential Manager integration (future feature)

**Recommendations:**
- Use a strong, unique Garmin password
- Enable Garmin MFA
- Don't share your computer with untrusted users
- Back up config.json to secure location

### Can I use this on a shared computer?

**Not recommended** for privacy reasons. If you must:
1. Use portable version (keep on USB drive)
2. Delete chat history after each use
3. Don't save Garmin credentials (re-enter each time)
4. Log out of Garmin Connect after use

### Is my chat history private?

**Yes!** Chat history:
- Stored locally only
- Not shared with anyone
- Not backed up to cloud (unless you do it)
- Can be deleted anytime (🗑️ Reset button)

---

## Technical Questions

### Can I run this on Mac or Linux?

**Experimental support:**
- App is written in Python (cross-platform)
- Tkinter works on Mac/Linux
- No pre-built executables yet

**Limitations:**
- Build scripts are Windows-specific
- Testing primarily on Windows
- Some UI elements may look different

### What Python version is required?

- **Minimum:** Python 3.8
- **Recommended:** Python 3.11 or 3.12
- **Not supported:** Python 2.x, Python 3.7 or older

### Can I contribute to the project?

**Yes!** The project is open source:
- Fork on GitHub
- Submit pull requests
- Report bugs in Issues
- Suggest features in Discussions

### How do I build from source?

**Quick version:**
```bash
git clone https://github.com/rod-trent/GarminChatDesktop.git
cd GarminChatDesktop/Code
pip install -r requirements.txt
python GarminChatDesktop.py
```

### Why is the executable so large (50-70 MB)?

The .exe includes:
- Python interpreter
- All required libraries
- GUI framework (Tkinter)
- AI SDK packages
- Image processing libraries

This is normal for PyInstaller applications.

### Can I use a different AI model?

**Yes!** In Settings, you can choose:
- **xAI:** grok-3, grok-2
- **OpenAI:** gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo
- **Gemini:** gemini-1.5-pro, gemini-1.5-flash, gemini-1.5-flash-8b
- **Anthropic:** claude-sonnet-4-5, claude-opus-4-5, claude-haiku-4-5
- **Azure:** Your deployed models

### What's the difference between installer and portable?

| Feature | Installer | Portable |
|---------|-----------|----------|
| **Installation** | Required | None |
| **Start Menu** | ✅ Yes | ❌ No |
| **Desktop shortcut** | ✅ Yes | ❌ No |
| **Uninstaller** | ✅ Yes | ❌ No (just delete) |
| **Auto-update** | Future feature | Manual |
| **Settings location** | Same (`%USERPROFILE%\.garmin_chat`) | Same |
| **Size** | 60-80 MB | 50-70 MB |

### How do I uninstall?

**Installer version:**
1. Windows Settings → Apps
2. Find "Garmin Chat Desktop"
3. Click Uninstall

**Portable version:**
1. Delete the .exe file
2. Optional: Delete `%USERPROFILE%\.garmin_chat` folder

---

## Still Have Questions?

### Documentation
- [README.md](README.md) - Complete user guide
- [INSTALL.md](INSTALL.md) - Installation instructions
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [Code/Readme.md](Code/Readme.md) - Developer documentation

### Support Channels
- **Bug Reports:** [GitHub Issues](https://github.com/rod-trent/GarminChatDesktop/issues)
- **Feature Requests:** [GitHub Discussions](https://github.com/rod-trent/GarminChatDesktop/discussions)
- **General Questions:** [GitHub Discussions](https://github.com/rod-trent/GarminChatDesktop/discussions)

### Quick Links
- [Download Latest Release](https://github.com/rod-trent/GarminChatDesktop/releases)
- [View Source Code](https://github.com/rod-trent/GarminChatDesktop/tree/main/Code)
- [Gemini Migration Guide](https://github.com/rod-trent/GarminChatDesktop/blob/main/Code/GEMINI_MIGRATION_GUIDE.md)

---

**Last Updated:** February 15, 2026  
**Version:** 4.0.3  
**Made with ❤️ for the fitness community**

*Not affiliated with Garmin Ltd. All trademarks are property of their respective owners.*
