# Ollama Setup Guide for Garmin Chat Desktop

Garmin Chat Desktop now supports **Ollama**, a free, local AI solution that runs entirely on your computer. This means:
- ✅ **No API costs** - Unlimited usage with no subscription fees
- ✅ **Complete privacy** - Your data never leaves your machine
- ✅ **Works offline** - No internet connection needed after initial setup
- ✅ **Multiple models** - Choose from Llama, Mistral, Phi, and more

## System Requirements

- **Operating System**: Windows 10/11, macOS, or Linux
- **RAM**: 8GB minimum (16GB+ recommended for larger models)
- **Disk Space**: 4-20GB depending on model size
- **CPU/GPU**: Modern processor (GPU optional but recommended for faster inference)

## Installation Steps

### Step 1: Install Ollama

#### Windows
1. Download Ollama for Windows from: https://ollama.com/download
2. Run the installer (`OllamaSetup.exe`)
3. Follow the installation wizard
4. Ollama will start automatically in the background

#### macOS
1. Download Ollama for Mac from: https://ollama.com/download
2. Open the downloaded `.dmg` file
3. Drag Ollama to your Applications folder
4. Launch Ollama from Applications
5. Ollama will run in your menu bar

#### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2: Install a Model

Open your terminal/command prompt and pull a model. Start with a smaller model for testing:

#### Recommended Models for Fitness Data Analysis:

**For Most Users (Fast, Efficient):**
```bash
ollama pull llama2
```
- Size: ~3.8GB
- Speed: Very fast
- Quality: Good for general fitness queries

**For Better Quality:**
```bash
ollama pull llama3.2
```
- Size: ~2.0GB
- Speed: Fast
- Quality: Excellent balance of speed and capability

**For Maximum Quality (Requires 16GB+ RAM):**
```bash
ollama pull llama3.1:70b
```
- Size: ~40GB
- Speed: Slower
- Quality: Best results for complex analysis

**Other Popular Models:**
```bash
ollama pull mistral        # Fast, efficient
ollama pull phi3           # Small, surprisingly capable
ollama pull codellama      # Good for technical queries
```

### Step 3: Verify Installation

Test that Ollama is running:

```bash
ollama list
```

This should show your installed models. If you see models listed, you're ready!

## Configuring Garmin Chat Desktop

1. Open Garmin Chat Desktop
2. Click **Settings** (gear icon)
3. Under **AI Provider Selection**, choose **Ollama (Local)**
4. The endpoint should auto-fill as `http://localhost:11434`
5. Click **Test Connection** to verify Ollama is running
6. Select your model from the dropdown (models will be auto-detected)
7. Click **Save**

## Troubleshooting

### "Cannot connect to Ollama" Error

**Solution 1: Start Ollama**
- **Windows**: Ollama should start automatically. If not, search for "Ollama" in Start menu and launch it
- **macOS**: Click the Ollama icon in your menu bar
- **Linux**: Run `ollama serve` in terminal

**Solution 2: Check if Ollama is Running**
```bash
# Test the connection
curl http://localhost:11434/api/tags
```

If this returns JSON with your models, Ollama is running correctly.

### "No models found" Error

You need to pull at least one model:
```bash
ollama pull llama2
```

Then restart Garmin Chat Desktop.

### Slow Performance

1. **Use a smaller model**: Try `llama2` or `phi3` instead of larger models
2. **Check RAM usage**: Large models need 8GB+ free RAM
3. **Enable GPU acceleration**: Ollama will automatically use your GPU if available

### Model Download is Slow

Model downloads can be large (2-40GB). Download times depend on your internet speed:
- llama2 (~3.8GB): ~5-15 minutes on typical broadband
- llama3.1:70b (~40GB): ~1-2 hours on typical broadband

## Model Recommendations by Hardware

### 8GB RAM
- ✅ llama2 (3.8GB)
- ✅ phi3 (2.3GB)
- ✅ mistral (4.1GB)
- ❌ Avoid 70B models

### 16GB RAM
- ✅ All 7B models
- ✅ llama3.1:13b
- ⚠️ llama3.1:70b (will be slow)

### 32GB+ RAM
- ✅ All models work well
- ✅ llama3.1:70b recommended for best quality

## Advanced Configuration

### Custom Ollama Endpoint

If you're running Ollama on a different port or machine:

1. In Garmin Chat settings, change the endpoint to:
   - Different port: `http://localhost:PORT`
   - Different machine: `http://192.168.1.100:11434`

### Running Multiple Models

You can have multiple models installed and switch between them in Settings:

```bash
ollama pull llama2          # Fast responses
ollama pull llama3.1:70b    # Detailed analysis
```

Switch models in Garmin Chat Desktop based on your needs!

## Cost Comparison

### Traditional AI Services (Monthly)
- ChatGPT Plus: $20/month
- Claude Pro: $20/month
- Gemini Advanced: $20/month

### Ollama
- **Cost**: $0 (free forever)
- **Usage Limits**: None
- **Privacy**: 100% local

## Learn More

- **Ollama Website**: https://ollama.com
- **Model Library**: https://ollama.com/library
- **Ollama GitHub**: https://github.com/ollama/ollama
- **Ollama Discord**: https://discord.gg/ollama

## Support

If you encounter issues with Ollama integration in Garmin Chat Desktop:

1. Check this troubleshooting guide first
2. Review the logs in Garmin Chat Desktop
3. Test Ollama directly with: `ollama run llama2 "Hello"`
4. Report issues at: [Your GitHub Issues URL]

---

**Note**: Ollama is a third-party tool maintained by Ollama Team. Garmin Chat Desktop integrates with Ollama but does not control its development or support.
