# GarminChatDesktop.py Modifications for Ollama Support

This document describes the changes needed to add Ollama support to GarminChatDesktop.py.

## Changes Overview

1. Add Ollama endpoint and model storage variables
2. Update settings dialog to include Ollama configuration
3. Add Ollama connection test button
4. Update model selection logic to handle dynamic Ollama models

## Detailed Changes

### 1. Add Configuration Variables (in `__init__` method around line 2800+)

Add these variables to store Ollama settings:

```python
# Ollama settings
self.ollama_endpoint = config.get('ollama_endpoint', 'http://localhost:11434')
self.ollama_model = config.get('ollama_model', 'llama2')
```

### 2. Update `save_config` method

Add Ollama settings to the configuration save:

```python
config = {
    # ... existing settings ...
    'ollama_endpoint': self.ollama_endpoint,
    'ollama_model': self.ollama_model,
}
```

### 3. Update `create_api_key_fields` in SettingsDialog (around line 386+)

Add Ollama-specific fields when Ollama is selected. Insert after the existing provider fields:

```python
# Ollama Configuration (shown when ollama is selected)
if selected_provider == 'ollama':
    # Endpoint
    ttk.Label(self.api_keys_frame,
             text="Ollama Endpoint:",
             style='Settings.CardText.TLabel').grid(row=row, column=0, sticky=tk.W, pady=5)
    
    self.ollama_endpoint_var = tk.StringVar(
        value=self.current_config.get('ollama_endpoint', 'http://localhost:11434')
    )
    
    endpoint_frame = ttk.Frame(self.api_keys_frame, style='Settings.Card.TFrame')
    endpoint_frame.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5)
    endpoint_frame.columnconfigure(0, weight=1)
    
    endpoint_entry = ttk.Entry(endpoint_frame,
                              textvariable=self.ollama_endpoint_var,
                              width=40,
                              style='Settings.TEntry')
    endpoint_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
    
    # Test Connection Button
    test_btn = ttk.Button(endpoint_frame,
                         text="Test Connection",
                         command=self.test_ollama_connection,
                         style='Settings.TButton')
    test_btn.grid(row=0, column=1)
    
    row += 1
    
    # Status label for connection test
    self.ollama_status_var = tk.StringVar(value="")
    status_label = ttk.Label(self.api_keys_frame,
                            textvariable=self.ollama_status_var,
                            style='Settings.Help.TLabel')
    status_label.grid(row=row, column=1, sticky=tk.W, pady=2)
    row += 1
    
    # Help text
    help_text = "Ollama runs locally on your computer. No API key needed!\nInstall from: https://ollama.com"
    ttk.Label(self.api_keys_frame,
             text=help_text,
             style='Settings.Help.TLabel',
             wraplength=400).grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=5)
    row += 1
    
    # Store for later use
    self.api_key_entries['ollama_endpoint'] = self.ollama_endpoint_var
```

### 4. Add `test_ollama_connection` method to SettingsDialog class

```python
def test_ollama_connection(self):
    """Test connection to Ollama server"""
    endpoint = self.ollama_endpoint_var.get().strip()
    
    if not endpoint:
        endpoint = 'http://localhost:11434'
        self.ollama_endpoint_var.set(endpoint)
    
    self.ollama_status_var.set("Testing connection...")
    self.update_idletasks()
    
    # Test in background thread
    def test_thread():
        result = AIClient.test_ollama_connection(endpoint)
        
        # Update UI in main thread
        self.after(0, lambda: self._update_ollama_status(result))
    
    thread = threading.Thread(target=test_thread, daemon=True)
    thread.start()

def _update_ollama_status(self, result):
    """Update Ollama connection status in UI"""
    if result['success']:
        models = result.get('models', [])
        if models:
            self.ollama_status_var.set(f"✓ {result['message']}")
            # Update model dropdown if it exists
            if hasattr(self, 'model_combo'):
                self.model_combo['values'] = models
                if self.current_config.get('ollama_model') in models:
                    self.model_combo.set(self.current_config.get('ollama_model'))
                elif models:
                    self.model_combo.set(models[0])
        else:
            self.ollama_status_var.set("⚠ " + result['message'])
    else:
        self.ollama_status_var.set("✗ " + result['message'])
```

### 5. Update `save_settings` method in SettingsDialog

Add Ollama settings to the save logic:

```python
def save_settings(self):
    """Save settings and close dialog"""
    selected_provider = self.provider_var.get()
    
    # ... existing code ...
    
    # Save Ollama settings
    if selected_provider == 'ollama':
        self.parent_app.ollama_endpoint = self.api_key_entries.get('ollama_endpoint', tk.StringVar()).get().strip()
        if hasattr(self, 'model_combo'):
            self.parent_app.ollama_model = self.model_combo.get()
        
        # Save to config
        config['ollama_endpoint'] = self.parent_app.ollama_endpoint
        config['ollama_model'] = self.parent_app.ollama_model
```

### 6. Update AI Client Initialization in Main App

Modify the `initialize_ai_client` method (or wherever AI client is created) to pass Ollama settings:

```python
def initialize_ai_client(self):
    """Initialize AI client with current settings"""
    try:
        kwargs = {}
        
        if self.ai_provider == 'azure':
            kwargs['azure_endpoint'] = self.azure_endpoint
            kwargs['azure_deployment'] = self.azure_deployment
        elif self.ai_provider == 'ollama':
            kwargs['ollama_endpoint'] = self.ollama_endpoint
        
        self.ai_client = AIClient(
            provider=self.ai_provider,
            api_key=self.api_keys.get(self.ai_provider, ''),
            model=self.get_current_model(),
            **kwargs
        )
        logger.info(f"AI client initialized with {self.ai_provider}")
        
    except Exception as e:
        logger.error(f"Failed to initialize AI client: {e}")
        messagebox.showerror("AI Client Error",
                           f"Failed to initialize AI client:\n{e}")
```

### 7. Update `get_current_model` method

Add Ollama model selection:

```python
def get_current_model(self):
    """Get the currently selected model for the active provider"""
    provider = self.ai_provider
    
    if provider == 'xai':
        return self.xai_model
    elif provider == 'openai':
        return self.openai_model
    elif provider == 'azure':
        return self.azure_model
    elif provider == 'gemini':
        return self.gemini_model
    elif provider == 'anthropic':
        return self.anthropic_model
    elif provider == 'ollama':
        return self.ollama_model
    
    return None
```

## Testing Checklist

After making these changes:

1. ✅ Settings dialog opens without errors
2. ✅ Ollama option appears in provider list
3. ✅ Selecting Ollama shows endpoint field (no API key field)
4. ✅ Test Connection button works
5. ✅ Model dropdown populates with Ollama models
6. ✅ Settings save and persist across app restarts
7. ✅ Chat works with Ollama selected
8. ✅ Error handling works when Ollama is not running

## Additional Files to Update

### requirements.txt
Add if not already present:
```
requests>=2.31.0  # For Ollama API calls
```

### README.md
Add Ollama to the supported providers list:
```markdown
## Supported AI Providers

- xAI (Grok)
- OpenAI (ChatGPT)
- Azure OpenAI
- Google Gemini
- Anthropic (Claude)
- **Ollama (Local, Free)** ← NEW!
```

### CHANGELOG.md
Add entry for version with Ollama support:
```markdown
## [4.1.0] - 2025-XX-XX

### Added
- Ollama support for local, privacy-focused AI inference
- No API costs - run models completely free on your own hardware
- Support for Llama, Mistral, Phi, and other open-source models
- Ollama connection test in settings
- Dynamic model detection from local Ollama installation

### Documentation
- Added comprehensive Ollama setup guide
- Installation instructions for Windows, macOS, and Linux
- Model recommendations by hardware specs
- Troubleshooting guide for common Ollama issues
```

## Notes for Users

When documenting this feature:

1. **Emphasize Privacy**: Data never leaves the user's machine
2. **Highlight Cost Savings**: $0 vs $20/month for ChatGPT Plus
3. **Set Expectations**: Local models may be slower but unlimited
4. **Hardware Requirements**: Be clear about RAM needs
5. **Easy Setup**: Ollama installation is simple and well-documented

## Future Enhancements

Potential improvements for future versions:

- [ ] Show Ollama model details (size, download status)
- [ ] One-click model download from within the app
- [ ] Performance metrics (tokens/second)
- [ ] Model switching without restarting chat
- [ ] GPU acceleration status indicator
- [ ] Custom system prompts per model
