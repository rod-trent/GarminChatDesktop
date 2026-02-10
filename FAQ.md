# FAQ

## Why was Grok chosen for the API during testing?
Grok (via the xAI API) was selected for initial testing for a few key reasons:
- It provides access to more current and up-to-date data compared to many other AI models.
- It's currently the most cost-effective option available.
That said, the app is designed with flexibility in mind. In future updates, users will be able to integrate and switch between their preferred AI APIs, including Gemini, ChatGPT, and others, to ensure the best possible experience based on individual needs and preferences.

## What is Garmin Chat Desktop?
Garmin Chat Desktop is a standalone application that allows you to query your Garmin Connect fitness data using natural language. Powered by AI, it turns raw data into actionable insights through conversational queries. For example, you can ask questions like "How did I sleep last night?" or "What was my last workout?" without navigating through the Garmin Connect interface. It features a modern Fluent Design UI, secure credential management, chat history, exports, and more.

## What are the key features of the app?
- **Natural Language Interface**: Ask questions in plain English, with support for multi-line inputs, markdown-formatted responses, conversation history, and context-aware AI that remembers past interactions.
- **Secure Credentials**: Stores API keys and Garmin login details locally and encrypted, with an easy Settings dialog.
- **Auto-Connect**: Optional automatic login on startup, with persistent MFA tokens for up to ~30 days.
- **UI Enhancements**: Dark mode toggle, card-based layout, color-coded messages, real-time status, and responsive design.
- **AI Capabilities**: Chat memory across sessions, smart suggestions, follow-up question buttons, and learning from user preferences.
- **Data Access**: Covers activities, sleep, daily summaries, heart rate, and more from Garmin Connect.
- **Chat Tools**: Save/load chats, full-text search, saved prompts, and exports to PDF, Word, or text.
- **Session Handling**: MFA support, token refresh, data sync, and reset options.

## What are the system requirements?
- Python 3.11, 3.12, or 3.13 (3.12 or 3.13 recommended).
- Tkinter (usually included with Python).
- An xAI API key from console.x.ai (free tier available).
- A Garmin Connect account (MFA enabled recommended).
- Optional: reportlab for PDF exports, python-docx for Word exports (auto-installed if needed).

For Linux users, install Tkinter via package manager if missing (e.g., `sudo apt-get install python3-tk` on Ubuntu).

## How do I install and set up the app on Windows?
1. Download the repository from https://github.com/rod-trent/GarminChatDesktop.
2. Double-click `Setup.bat` to install dependencies (takes ~30 seconds).
3. Double-click `Startup.bat` to launch the app.
4. In the Settings dialog (opens automatically on first run):
   - Enter your xAI API key.
   - Enter your Garmin email and password.
   - Enable auto-login if desired.
   - Click Save.
5. Click "Connect to Garmin" and enter your MFA code if prompted.
6. Start chatting!

For subsequent launches, just run `Startup.bat`—it auto-connects if enabled.

## How do I install manually (any OS)?
1. Clone the repo: `git clone https://github.com/rod-trent/GarminChatDesktop.git`.
2. Install dependencies: `pip install -r requirements-desktop.txt`.
3. Run the app: `python GarminChatDesktop.py` (or `py GarminChatDesktop.py` on Windows).

## How do I use the app?
- Open Settings to configure credentials.
- Connect to Garmin (auto if enabled).
- Type questions in the input field (use Ctrl+Enter to send, Enter for new lines).
- Use header buttons for search, dark mode, and settings.
- Control panel for connect/refresh/reset, prompts, save, history, and export.
- Example questions: "How many steps did I take today?" or "Compare my running pace this month vs last month."

## Where are my data and configs stored?
- Settings: `~/.garmin_chat/config.json` (Windows: `C:\Users\YourName\.garmin_chat\`).
- Chat history: `~/.garmin_chat/chat_history/`.
- Saved prompts: `~/.garmin_chat/saved_prompts.json`.
- Garmin tokens: `~/.garmin_tokens/`.
All data stays local—no cloud storage.

## How does authentication work?
- First connection: Enter MFA code if enabled; tokens saved for ~30 days.
- Subsequent: Auto-refreshes tokens (access tokens last 1 hour, refresh tokens ~30 days).
- If expired: Prompts for MFA again.
- Best practice: Enable MFA on your Garmin account.

## Can I create a standalone executable?
Yes, for distribution without Python:
1. Install PyInstaller: `pip install pyinstaller`.
2. Run: `pyinstaller --onefile --windowed --name "GarminChat" GarminChatDesktop.py`.
3. Find the .exe in the `dist/` folder.

## How can I customize the app?
- Window size: Edit `self.root.geometry("1200x950")` in `GarminChatDesktop.py`.
- Colors: Modify the `self.colors` dictionary in `setup_styles()`.
- Button styles: Adjust padding and fonts in `setup_styles()`.
- Add examples: Edit the `examples` list in `create_widgets()`.

## What are some troubleshooting tips?
- **Python not installed**: Download from python.org and add to PATH.
- **Tkinter missing**: Reinstall Python or install via package manager.
- **Configuration Required**: Fill in all credentials in Settings.
- **MFA errors**: Ensure 6-digit code is entered quickly; retry if "CSRF token" error.
- **Rate limit (429)**: Wait 15-30 minutes; avoid repeated failed auths.
- **Tokens not persisting**: Check `~/.garmin_tokens/`; delete and re-auth if needed.
- **Display name errors (403)**: Retry; reset and reconnect if persistent.
- General: Delete token files for fresh auth, ensure internet connection, update app.

## Are there any known limitations?
- Requires internet (no offline mode).
- MFA needed every ~30 days.
- Garmin rate limits may apply.
- Data updates every 15-30 minutes.
- Cannot disable MFA.

## Is my data secure?
Yes—all credentials and tokens are stored locally and encrypted. No telemetry or data sharing. The xAI API only receives explicit queries, and Garmin uses standard OAuth. Keep your API key and configs private.

## What are planned future features?
Beyond the current roadmap (like AI context memory and exports), plans include support for switching between multiple AI APIs (e.g., Gemini, ChatGPT) for enhanced flexibility. Check the repo for updates!
