# Changelog

All notable changes to Garmin Chat Desktop will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.4] - 2026-03-12

### Added
- **Ollama Support**: Complete integration with Ollama for free, local AI inference
  - No API costs - run unlimited queries for free
  - Complete privacy - data never leaves your machine
  - Works offline - no internet connection needed after setup
  - Support for multiple open-source models (Llama, Mistral, Phi, etc.)
  - Automatic model detection from local Ollama installation
  - Connection test button in settings to verify Ollama is running
  - Dynamic model selection dropdown based on installed models
- **Latest Anthropic Claude Models**: Updated to newest Claude models for improved response quality
- **Expanded Activity Fetch**: Garmin Connect activity retrieval increased from 10 to 50 activities for richer AI context and trend analysis

### Fixed
- Emoji and character encoding issues throughout the UI
- Improved error handling for AI provider connection failures

### Changed
- Initial Garmin login and AI responses may take slightly longer due to the increased activity data fetch (expected behavior)

## [4.1.0] - 2025-02-17

### Added
- **Ollama Support**: Complete integration with Ollama for free, local AI inference
  - No API costs - run unlimited queries for free
  - Complete privacy - data never leaves your machine
  - Works offline - no internet connection needed after setup
  - Support for multiple open-source models (Llama, Mistral, Phi, etc.)
  - Automatic model detection from local Ollama installation
  - Connection test button in settings to verify Ollama is running
  - Dynamic model selection dropdown based on installed models
- Comprehensive Ollama setup guide (OLLAMA_SETUP_GUIDE.md)
- Model recommendations by hardware specifications
- Troubleshooting documentation for Ollama issues

### Fixed
- **Major**: Fixed widespread emoji encoding corruption throughout the application
  - Button emojis now display correctly (▶, ↺, 📝, 💾, 📂, 📊, →, ⚙️)
  - Status indicators display properly (✅, ⚠, 🔍, ◐)
  - Chat formatting symbols corrected (⏎, •)
  - All UI elements now render with proper UTF-8 encoding
- Bullet points in AI responses now display as proper bullets (•) instead of arrows
- Smart quotes and punctuation in AI responses handled correctly
- Message cleanup code properly handles mojibake characters

### Changed
- Updated version to 4.1.0
- Enhanced settings dialog with Ollama-specific configuration UI
- Improved provider selection with clear indicators for local vs cloud providers
- Updated help text to include Ollama installation instructions

### Documentation
- New comprehensive Ollama setup guide with installation instructions
- Hardware requirements and model recommendations
- Cost comparison showing potential savings
- Updated README with Ollama features and benefits
- Added troubleshooting section for Ollama-specific issues

## [4.0.3] - 2025-01-15

### Changed
- Migrated to Google's new `google-genai` SDK (replacing deprecated `google-generativeai`)
- Updated Gemini model strings to stable versions
- Improved error handling for Gemini API calls

### Fixed
- Gemini API compatibility issues with new SDK
- Model migration for deprecated experimental models
- Enhanced logging for API troubleshooting

### Removed
- Strength training detail features (removed due to Garmin API limitations)

## [4.0.2] - 2024-12-20

### Fixed
- Window state restoration on app startup
- Dark mode color scheme consistency
- Minor UI alignment issues

### Changed
- Optimized installer size through dependency exclusion
- Improved build process with PyInstaller

## [4.0.1] - 2024-12-10

### Fixed
- Settings dialog modal behavior
- Configuration persistence across sessions
- Provider switching stability

## [4.0.0] - 2024-12-01

### Added
- Complete UI redesign with Windows Fluent Design principles
- Multi-provider AI support (xAI, OpenAI, Azure, Gemini, Anthropic)
- Dark mode with automatic theme detection
- Conversation history with search functionality
- Save chat sessions with custom names
- Export conversations to PDF, DOCX, or TXT
- Quick Questions customization
- Markdown formatting in responses (bold, headers, bullets, tables)
- Tooltips for all interactive elements
- Auto-login option
- Window state persistence (position and size)

### Changed
- Completely rebuilt UI using modern design patterns
- Switched from single AI provider to multi-provider architecture
- Enhanced chat display with better formatting
- Improved settings organization and layout
- Modernized color scheme and typography

### Fixed
- Connection stability improvements
- Better error messaging
- Memory management optimizations
- API request handling

## [3.x.x] - Previous Versions

Earlier versions focused on basic Garmin Connect integration with single AI provider support.

---

## Upgrade Notes

### Upgrading to 4.1.0
- No breaking changes - existing configurations will work
- Ollama is optional - existing AI providers continue to work
- To use Ollama, install it separately from https://ollama.com
- API keys from previous versions are preserved

### Upgrading to 4.0.x from 3.x
- Settings will be reset (need to re-enter credentials)
- Choose your preferred AI provider in new settings dialog
- Dark mode defaults to off (can be enabled in settings)

## Known Issues

### v4.1.0
- None currently identified

### v4.0.3
- Some Garmin activity types may have limited data available (API limitation)

## Future Roadmap

### Planned Features
- [ ] Voice input using Azure Speech Services
- [ ] Advanced charting with visual trend analysis
- [ ] Workout recommendations based on training history
- [ ] Integration with additional fitness platforms
- [ ] Mobile companion app (.NET MAUI)
- [ ] Windows Store deployment (MSIX packaging)
- [ ] Additional Ollama models and configurations
- [ ] Model performance metrics and benchmarking

### Under Consideration
- [ ] Custom AI model fine-tuning
- [ ] Social features for sharing insights
- [ ] Integration with nutrition tracking
- [ ] Advanced sleep analysis
- [ ] Training plan generation

---

For detailed installation and usage instructions, see [README.md](README.md).

For Ollama setup, see [OLLAMA_SETUP_GUIDE.md](OLLAMA_SETUP_GUIDE.md).
