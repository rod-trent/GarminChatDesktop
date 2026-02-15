# Garmin Chat Desktop - Source Code

This directory contains the complete source code for Garmin Chat Desktop v4.0.3.

## 📁 Project Structure

```
Code/
├── GarminChatDesktop.py       # Main application (Tkinter GUI)
├── ai_client.py               # Multi-provider AI client
├── garmin_handler.py          # Garmin Connect data handler
├── logo.ico                   # Application icon (Windows)
├── logo.png                   # Splash screen logo
├── build.bat                  # PyInstaller build script (Windows)
├── build_installer.bat        # Inno Setup installer builder
├── GarminChat_Installer.iss   # Inno Setup configuration
├── requirements.txt           # Python dependencies
├── requirements-dev.txt       # Development dependencies
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Windows 10/11** (for building .exe)
- **Git** (optional, for cloning)

### Installation

1. **Clone or download** the repository:
```bash
git clone https://github.com/rod-trent/GarminChatDesktop.git
cd GarminChatDesktop/Code
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

**⚠️ Important for v4.0.3:** Google deprecated `google-generativeai`. If upgrading:
```bash
pip uninstall google-generativeai
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python GarminChatDesktop.py
```

## 📦 Dependencies

### Core Dependencies (requirements.txt)

| Package | Version | Purpose |
|---------|---------|---------|
| `garminconnect` | ≥0.2.0 | Garmin Connect API |
| `requests` | ≥2.31.0 | HTTP requests |
| `Pillow` | ≥10.0.0 | Image handling (splash screen, logo) |
| `openai` | ≥1.0.0 | OpenAI and xAI provider |
| `google-genai` | ≥0.2.0 | **NEW** Google Gemini (replaces deprecated package) |
| `anthropic` | ≥0.18.0 | Anthropic Claude provider |
| `pyinstaller` | ≥6.0.0 | Build executable (dev only) |

**Note:** Tkinter comes with Python by default on Windows/Mac. Linux users may need to install separately.

### Development Dependencies (requirements-dev.txt)

- Code formatting: `black`, `autopep8`
- Linting: `pylint`, `flake8`
- Type checking: `mypy`
- Testing: `pytest`, `pytest-cov`
- Documentation: Optional PDF/DOCX export (`reportlab`, `python-docx`)

## 🏗️ Building from Source

### Build Executable (Windows)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run build script
build.bat

# Output: dist\GarminChat.exe
```

### Build Installer (Windows)

**Prerequisites:** [Inno Setup 6](https://jrsoftware.org/isdl.php)

```bash
# 1. Build executable first
build.bat

# 2. Build installer
build_installer.bat

# Output: installer_output\GarminChatDesktop_v4.0.3_Setup.exe
```

### Build Optimizations (v4.0.3)

The build script now includes optimizations to reduce file size:

```batch
--exclude-module=matplotlib    # Not needed
--exclude-module=numpy         # Not needed
--exclude-module=pandas        # Not needed
--exclude-module=scipy         # Not needed
--noupx                        # Better compatibility
```

**Result:** ~50-70 MB executable (was ~80-120 MB)

## 🔧 Architecture

### Main Components

#### 1. **GarminChatDesktop.py** (Main Application)
- Tkinter-based GUI
- Modern Fluent Design styling
- Dark/light theme support
- Window state persistence
- Chat history management
- Multi-dialog system (Settings, Search, History, etc.)

**Key Features:**
- Customizable Quick Questions (v4.0.3)
- Professional splash screen
- Rounded hover effects
- Clean character encoding

#### 2. **ai_client.py** (AI Provider Interface)
Multi-provider AI client supporting:
- **xAI (Grok)** - OpenAI-compatible API
- **OpenAI (ChatGPT)** - Official SDK
- **Azure OpenAI** - Enterprise deployment
- **Google Gemini** - Native SDK (NEW `google-genai` package)
- **Anthropic (Claude)** - Native SDK

**Features:**
- Unified interface across all providers
- Conversation history management
- Context-aware responses
- Error handling with user-friendly messages
- Automatic model migration (deprecated → current)

**v4.0.3 Updates:**
- Migrated from `google-generativeai` to `google-genai`
- Enhanced error handling and logging
- API version management (v1 vs v1beta)

#### 3. **garmin_handler.py** (Garmin Connect Handler)
Interfaces with Garmin Connect to fetch:
- Activities (runs, walks, bikes, workouts)
- Sleep data (total, deep, light, REM, awake)
- Daily summaries (steps, calories, distance)
- Health metrics (Body Battery, stress, HRV, SpO2)
- Nutrition and hydration
- Training status and VO2 Max

**Features:**
- MFA support
- Session management
- Data caching
- Error recovery
- Formatted context for AI

## 🎨 UI Architecture

### Theme System
- Light and dark modes
- Fluent Design principles
- Modern card-based layouts
- Smooth animations
- Persistent theme preference

### Dialog System
All dialogs support:
- Theme inheritance
- Modal operation
- Centered positioning
- Icon consistency
- Smooth transitions (v4.0.3)

### Key Dialogs:
- Settings (AI provider, credentials, theme)
- Search (chat history search)
- Chat History Viewer
- Saved Prompts Manager
- Export Report Generator

## 🔐 Configuration

User settings are stored in:
```
%USERPROFILE%\.garmin_chat\
├── config.json              # Settings and credentials
├── saved_prompts.json       # User-saved prompts
└── chat_history\            # Saved conversations
    ├── chat_YYYYMMDD_HHMMSS.json
    ├── chat_YYYYMMDD_HHMMSS_CustomName.json
    └── ...
```

### config.json Structure:
```json
{
  "ai_provider": "xai",
  "xai_api_key": "...",
  "xai_model": "grok-3",
  "openai_api_key": "...",
  "openai_model": "gpt-4o",
  "gemini_api_key": "...",
  "gemini_model": "gemini-1.5-flash",
  "anthropic_api_key": "...",
  "anthropic_model": "claude-sonnet-4-5-20250929",
  "azure_api_key": "...",
  "azure_endpoint": "...",
  "azure_deployment": "...",
  "garmin_email": "...",
  "garmin_password": "...",
  "auto_login": true,
  "dark_mode": false,
  "window_state": {
    "width": 1200,
    "height": 950,
    "x": 100,
    "y": 100
  }
}
```

## 🧪 Testing

### Run Gemini API Test
```bash
python test_gemini.py
```

This verifies:
- Package installation
- API key validity
- Model availability
- Response extraction

### Manual Testing Checklist
- [ ] Connect to Garmin (with/without MFA)
- [ ] Test each AI provider
- [ ] Save and load chat history
- [ ] Export conversations
- [ ] Search functionality
- [ ] Dark mode toggle
- [ ] Settings persistence
- [ ] Quick questions customization
- [ ] Window position save/restore

## 🐛 Known Issues & Workarounds

### Google Gemini API (v4.0.3)

**Issue:** Some Gemini models return 404 errors
```
404 NOT_FOUND: models/gemini-1.5-pro is not found for API version v1beta
```

**Status:** Google's new `google-genai` SDK is in beta (v0.2.x)

**Workarounds:**
1. Use `gemini-1.5-flash-8b` or `gemini-1.5-flash` (more stable)
2. Switch to xAI, OpenAI, or Anthropic (recommended)
3. Wait for SDK v0.3+ (more mature)

See [GEMINI_TROUBLESHOOTING.md](../GEMINI_TROUBLESHOOTING.md) for details.

### Antivirus False Positives

**Issue:** Some antivirus software flags PyInstaller executables

**Workaround:**
- Add exception for `dist\GarminChat.exe`
- Executables are clean - this is a known PyInstaller issue
- Build from source to verify

## 📚 API Documentation

### ai_client.py

```python
from ai_client import AIClient

# Initialize client
client = AIClient(
    provider='xai',           # 'xai', 'openai', 'azure', 'gemini', 'anthropic'
    api_key='your-api-key',
    model='grok-3'            # Optional, uses default if not specified
)

# Send message with context
response = client.chat(
    user_message="How many steps did I take today?",
    garmin_context="Steps today: 8,543\nGoal: 10,000",
    system_prompt="You are a fitness assistant..."  # Optional
)

# Reset conversation
client.reset_conversation()
```

### garmin_handler.py

```python
from garmin_handler import GarminDataHandler

# Initialize handler
garmin = GarminDataHandler(email, password)

# Authenticate
result = garmin.authenticate()
if result['success']:
    print("Connected!")
elif result['mfa_required']:
    code = input("Enter MFA code: ")
    garmin.submit_mfa(code)

# Get formatted data for AI context
context = garmin.format_data_for_context(
    data_type='activities',  # 'activities', 'sleep', 'summary', 'all', etc.
    activity_limit=10        # Number of recent activities
)

# Get activities by date range
activities = garmin.get_activities_by_date(
    start_date="2026-01-01",
    end_date="2026-02-15"
)
```

## 🔄 Version Migration

### From v4.0.2 to v4.0.3

**Google Gemini Package Change:**
```bash
# Required migration steps
pip uninstall google-generativeai
pip install google-genai
```

**Code Changes:**
- `ai_client.py` - Updated Gemini initialization and API calls
- `build.bat` - Updated hidden imports and collect-data

**No Breaking Changes:**
- Settings format unchanged
- Chat history compatible
- All other providers work as before

### Automated Model Migrations

The app automatically migrates deprecated models:

| Old Model | New Model |
|-----------|-----------|
| `gemini-2.0-flash-exp` | `gemini-1.5-flash` |
| `gemini-exp-1206` | `gemini-1.5-flash` |
| `grok-beta` | `grok-3` |
| `grok-2-1212` | `grok-3` |

## 🛠️ Development

### Setup Development Environment

```bash
# Install all dev dependencies
pip install -r requirements-dev.txt

# Format code
black GarminChatDesktop.py

# Lint
pylint GarminChatDesktop.py

# Type check
mypy GarminChatDesktop.py
```

### Code Style
- **PEP 8** compliance
- **Type hints** where applicable
- **Docstrings** for all classes and functions
- **Comments** for complex logic

### Adding New AI Provider

1. Update `AIClient.PROVIDERS` in `ai_client.py`
2. Add initialization method (`_init_provider`)
3. Add API call method (`_call_provider`)
4. Update settings dialog in `GarminChatDesktop.py`
5. Update documentation

## 📖 Additional Resources

### Documentation
- [Main README](../README.md)
- [Installation Guide](../INSTALL.md)
- [Changelog](../CHANGELOG.md)
- [Gemini Migration Guide](../GEMINI_MIGRATION_GUIDE.md)
- [Gemini Troubleshooting](../GEMINI_TROUBLESHOOTING.md)

### Build Documentation
- [Deployment Checklist](../DEPLOYMENT_CHECKLIST.md)
- [Release Notes v4.0.3](../RELEASE_NOTES_v4.0.3.md)
- [Blog Post v4.0.3](../BLOG_POST_v4.0.3.md)

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] Additional AI providers
- [ ] Visual charts and graphs
- [ ] Voice input/output
- [ ] Mobile companion app
- [ ] Unit tests
- [ ] Integration tests
- [ ] Documentation improvements

## 📄 License

MIT License - See [LICENSE.txt](../LICENSE.txt)

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/rod-trent/GarminChatDesktop/issues)
- **Discussions:** [GitHub Discussions](https://github.com/rod-trent/GarminChatDesktop/discussions)
- **Documentation:** All markdown files in root directory

---

**Version:** 4.0.3  
**Last Updated:** February 15, 2026  
**Python Version:** 3.8+  
**Platform:** Windows 10/11 (primary), Linux/Mac (experimental)

---

*Made with ❤️ for the fitness community*
