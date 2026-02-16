# Privacy Statement for Garmin Chat Desktop

**Last Updated:** February 16, 2026  
**Version:** 3.0

## Introduction

Garmin Chat Desktop ("the Application") is a personal desktop application that allows you to query your Garmin Connect fitness data using natural language and AI. This Privacy Statement explains how the Application handles your data, credentials, and personal information.

## Developer Information

**Developer:** Rod Trent  
**Repository:** https://github.com/rod-trent/GarminChatDesktop  
**License:** MIT License  
**Nature:** Open-source personal project

## Core Privacy Principles

1. **Local-First Architecture** - All data is stored locally on your device
2. **No Cloud Storage** - The Application does not store your data on remote servers
3. **No Telemetry** - The Application does not collect or transmit usage statistics
4. **No Third-Party Sharing** - Your data is never sold or shared with third parties
5. **Transparent Operations** - Open-source code allows full inspection of data handling

## Data Collection and Storage

### What Data the Application Stores Locally

#### 1. Authentication Credentials
- **xAI API Key** - Stored in `~/.garmin_chat/config.json`
- **Garmin Connect Email** - Stored in `~/.garmin_chat/config.json`
- **Garmin Connect Password** - Stored in `~/.garmin_chat/config.json`
- **Storage Format:** Plain text JSON file (not encrypted)
- **Access:** Only accessible to your local user account
- **Purpose:** Automated authentication to Garmin Connect and xAI services

#### 2. Authentication Tokens
- **OAuth1 Tokens** - Stored in `~/.garmin_tokens/oauth1_token`
- **OAuth2 Tokens** - Stored in `~/.garmin_tokens/oauth2_token`
- **Validity:** OAuth tokens expire after approximately 30 days
- **Purpose:** Maintain authenticated sessions with Garmin Connect without requiring repeated MFA codes

#### 3. Application Settings
- **Auto-login Preference** - Stored in `~/.garmin_chat/config.json`
- **Theme Preferences** - Stored locally (dark/light mode)
- **Purpose:** Personalize your application experience

#### 4. Chat History
- **Conversation Logs** - Stored in `~/.garmin_chat/chat_history/`
- **Format:** JSON files with timestamps and message content
- **Content:** Your questions and AI responses containing your fitness data
- **Control:** You can delete chat history files at any time
- **Purpose:** Enable conversation history viewing, search, and export features

#### 5. Saved Prompts
- **Custom Questions** - Stored in `~/.garmin_chat/saved_prompts.json`
- **Purpose:** Quick access to your frequently used queries

#### 6. Context Memory
- **Recent Conversations** - Last 10 messages stored in memory during active session
- **Purpose:** Enable AI to provide context-aware responses
- **Persistence:** Clears when application closes unless chat is saved

### What Data the Application Does NOT Store

- ❌ Credit card or payment information (Application is free)
- ❌ Social Security numbers or government IDs
- ❌ Medical records or health diagnoses
- ❌ Location tracking data beyond what Garmin provides
- ❌ Browser history or web activity
- ❌ Contacts or personal relationships
- ❌ Device identifiers or hardware information
- ❌ IP addresses or network information
- ❌ Usage analytics or telemetry data

## Data Transmission

### External Services the Application Communicates With

#### 1. Garmin Connect API
- **Purpose:** Retrieve your fitness data (activities, sleep, heart rate, steps, etc.)
- **Data Sent:** Your Garmin Connect credentials and OAuth tokens
- **Data Received:** Your personal fitness metrics and activity data
- **Frequency:** On-demand when you connect or refresh data
- **Garmin's Privacy Policy:** https://www.garmin.com/en-US/privacy/

#### 2. xAI API (Grok)
- **Purpose:** Process your questions and generate AI-powered responses
- **Data Sent:** 
  - Your natural language questions
  - Your Garmin fitness data (only data relevant to your query)
  - Conversation context (last 10 messages)
- **Data Received:** AI-generated responses and insights
- **Frequency:** Each time you send a message
- **xAI's Privacy Policy:** https://x.ai/privacy

### What is NOT Transmitted

- ✅ Your passwords are NEVER sent to xAI
- ✅ Your API keys are NEVER sent to Garmin
- ✅ Your full fitness database is NEVER sent unless specifically queried
- ✅ Your chat history is NEVER automatically uploaded or backed up
- ✅ No background data transmission occurs

## Third-Party Services

### Services You Connect To

1. **Garmin Connect**
   - Required: Yes (core functionality)
   - Authentication: OAuth 1.0 and OAuth 2.0
   - MFA Support: Yes (recommended)
   - Your Control: You authenticate directly with Garmin
   - Data Access: Read-only access to your fitness data

2. **xAI (Grok) API**
   - Required: Yes (AI functionality)
   - Authentication: API Key (you provide)
   - Free Tier: Available
   - Your Control: You generate and provide your own API key
   - Data Processing: Your queries are processed to generate responses

### Optional Services

The Application currently does not integrate with any optional third-party services.

## Your Data Rights and Controls

### Access and Management

You have complete control over your data:

1. **View Your Data**
   - All configuration files are plain text JSON
   - Chat history files are human-readable JSON
   - Tokens are stored as text files

2. **Export Your Data**
   - Export conversations to PDF, Word (.docx), or Text (.txt)
   - Copy configuration files to backup locations
   - Chat history files can be copied directly

3. **Delete Your Data**
   - Delete individual chat history files
   - Clear all chat history via the History viewer
   - Delete configuration directory: `~/.garmin_chat/`
   - Delete token directory: `~/.garmin_tokens/`
   - Uninstall the Application and delete its folder

4. **Modify Your Data**
   - Update credentials via Settings dialog
   - Edit configuration files directly (JSON format)
   - Manage saved prompts via the Prompts feature

### Deletion Instructions

To completely remove all Application data:

**Windows:**
```batch
# Delete configuration and chat history
rmdir /s /q "%USERPROFILE%\.garmin_chat"

# Delete authentication tokens
rmdir /s /q "%USERPROFILE%\.garmin_tokens"

# Uninstall the Application
# Delete the GarminChatDesktop folder
```

**macOS/Linux:**
```bash
# Delete configuration and chat history
rm -rf ~/.garmin_chat

# Delete authentication tokens
rm -rf ~/.garmin_tokens

# Uninstall the Application
# Delete the GarminChatDesktop folder
```

## Security Practices

### What the Application Does for Security

1. **Local Storage Only**
   - No cloud uploads or remote backups
   - Files stored in user-specific directories
   - Operating system file permissions apply

2. **Password Masking**
   - Credentials masked in Settings dialog by default
   - Show/hide toggles for viewing when needed

3. **Token Management**
   - OAuth tokens auto-refresh to minimize credential re-entry
   - Tokens expire after ~30 days requiring re-authentication
   - Failed authentication clears invalid tokens

4. **Secure Communication**
   - HTTPS/TLS for all API communications
   - Standard OAuth 1.0/2.0 protocols with Garmin
   - API key authentication with xAI

### Security Limitations and Your Responsibilities

⚠️ **Important Security Notes:**

1. **File Storage is NOT Encrypted**
   - Configuration files (`config.json`) store credentials in plain text
   - Anyone with access to your user account can read these files
   - Shared computers pose a security risk

2. **Your Responsibilities:**
   - Use a strong password for your computer user account
   - Enable disk encryption (BitLocker, FileVault, LUKS)
   - Do not share your computer with untrusted users
   - Protect your xAI API key as a password
   - Enable MFA on your Garmin Connect account
   - Keep your operating system updated

3. **Recommendations:**
   - Use the Application only on personal, secure devices
   - Do not use on public or shared computers
   - Log out of Windows/macOS when away from your device
   - Regularly review who has access to your computer

## Data Retention

### How Long Data is Kept

- **Configuration Files:** Persist until you manually delete them
- **Authentication Tokens:** Auto-deleted after ~30 days of expiration
- **Chat History:** Persists indefinitely until you delete manually
- **Saved Prompts:** Persist until you delete them
- **Context Memory:** Clears when you close the Application (unless saved)

### Automatic Data Deletion

The Application does NOT automatically delete:
- Old chat histories
- Expired configuration files
- Unused saved prompts

You must manually manage and delete data you no longer need.

## Children's Privacy

The Application is not directed at children under 13. However:

- The Application does not collect age information
- Garmin Connect requires users to be 13+ per their Terms of Service
- No special restrictions are implemented for younger users
- Parents/guardians are responsible for monitoring children's use

If you believe a child under 13 has used the Application, please supervise their device usage and delete any stored data as needed.

## Changes to This Privacy Statement

### Notification of Changes

- Major changes will be announced in the GitHub repository README
- The "Last Updated" date at the top of this document will be changed
- Version number will be incremented
- You are responsible for reviewing this statement periodically

### What Constitutes a Major Change

- New third-party service integrations
- Changes to data storage locations or formats
- New data collection practices
- Changes to data sharing policies

### What Does NOT Require Notification

- Clarifications or corrections to existing practices
- Formatting or organizational changes
- Addition of examples or explanatory text

## Open Source Transparency

### Code Inspection

As an open-source project:

- **Full source code available:** https://github.com/rod-trent/GarminChatDesktop
- **No hidden data collection:** All network calls are visible in code
- **Community review:** Anyone can audit the code for privacy concerns
- **Fork and modify:** You can create your own version with enhanced security

### Contributing and Reporting Issues

If you discover privacy concerns:

1. Review the source code in the GitHub repository
2. Open a GitHub Issue describing the concern
3. Submit a Pull Request with proposed improvements
4. Contact the developer through GitHub

## Disclaimer and Limitations

### No Warranty

This Application is provided "AS IS" without warranty of any kind. The developer:

- Makes no guarantees about data security
- Is not responsible for data breaches due to user device compromise
- Does not guarantee continuous availability of third-party services
- Is not liable for data loss or unauthorized access

### Your Assumption of Risk

By using this Application, you acknowledge:

- You understand the security limitations of local plain-text storage
- You accept the risks of storing credentials locally
- You are responsible for securing your device
- You will not hold the developer liable for security incidents

### Third-Party Services

The developer is not responsible for:

- Garmin Connect's privacy practices or data breaches
- xAI's privacy practices or data handling
- Changes to third-party APIs or services
- Third-party service outages or unavailability

## Contact Information

### For Privacy Questions or Concerns

- **GitHub Issues:** https://github.com/rod-trent/GarminChatDesktop/issues
- **Repository:** https://github.com/rod-trent/GarminChatDesktop
- **Developer:** Rod Trent (contact via GitHub)

### Response Time

As a personal open-source project:

- No guaranteed response time for inquiries
- Best effort responses when developer is available
- Community members may also provide assistance

## Compliance Statements

### GDPR (European Users)

While this is a personal project not subject to GDPR requirements, we respect data protection principles:

- **Right to Access:** You can access all your data in configuration files
- **Right to Rectification:** You can edit configuration files directly
- **Right to Erasure:** You can delete all data by removing directories
- **Data Portability:** Export conversations to PDF/Word/Text
- **Right to Object:** You can stop using the Application at any time

### CCPA (California Users)

California users have rights to:

- Know what personal information is collected (see "Data Collection" section)
- Delete personal information (see "Deletion Instructions" section)
- Opt-out of sale of personal information (N/A - we don't sell data)

### Other Jurisdictions

Users in other jurisdictions should consult local privacy laws. The Application's local-only storage model generally aligns with privacy regulations worldwide.

## Additional Resources

### Related Documentation

- **Application README:** Full feature documentation
- **Garmin Connect Privacy:** https://www.garmin.com/en-US/privacy/
- **xAI Privacy Policy:** https://x.ai/privacy
- **OAuth 2.0 Security:** https://oauth.net/2/

### Security Best Practices

For securing your device and data:

- Enable full-disk encryption on your computer
- Use strong, unique passwords for all accounts
- Enable Multi-Factor Authentication where available
- Keep your operating system and software updated
- Use antivirus/antimalware software
- Be cautious with shared or public computers

---

## Summary

**In Plain English:**

Garmin Chat Desktop stores your credentials and chat history locally on your computer in plain text files. It connects to Garmin to get your fitness data and sends that data to xAI's AI service to answer your questions. Nothing is stored in the cloud. You can delete everything at any time by removing a few folders. The app is open-source, so you can verify exactly what it does.

**Your data stays on your computer. Period.**

---

## Acknowledgment

By using Garmin Chat Desktop, you acknowledge that you have read, understood, and agree to this Privacy Statement. If you do not agree, please do not use the Application and delete all associated files from your device.

---

**End of Privacy Statement**
