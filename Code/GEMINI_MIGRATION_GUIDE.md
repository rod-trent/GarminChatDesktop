# Google Gemini API Migration Guide

## Important: Package Update Required

Google has deprecated the `google-generativeai` package in favor of the new `google-genai` package.

**All users must update before building v4.0.3!**

---

## For Users (Installing the App)

**No action required!** The installer/executable includes the correct package.

---

## For Developers (Building from Source)

### Quick Fix

**Uninstall old package:**
```bash
pip uninstall google-generativeai
```

**Install new package:**
```bash
pip install google-genai
```

---

## What Changed?

### Package Name
- ❌ **Old**: `google-generativeai`
- ✅ **New**: `google-genai`

### Import Statement (if you maintain ai_client.py)
```python
# Old (deprecated)
import google.generativeai as genai

# New (current)
import google.genai as genai
```

### API Changes
The new `google-genai` package has a slightly different API. If you're using a custom `ai_client.py`:

**Old API:**
```python
import google.generativeai as genai

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name)
response = model.generate_content(prompt)
```

**New API:**
```python
import google.genai as genai
from google.genai import types

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model=model_name,
    contents=prompt
)
```

---

## Build Script Updates

The `build.bat` has been updated:

**Changed lines:**
```batch
# Old
--hidden-import=google.generativeai ^
--collect-data google.generativeai ^

# New
--hidden-import=google.genai ^
--collect-data google.genai ^
```

---

## Deprecation Timeline

- **Google's announcement**: January 2026
- **Support ended**: February 2026
- **No further updates**: After February 2026
- **Recommended migration**: Immediately

---

## Troubleshooting

### Error: "No module named 'google.generativeai'"
**Solution**: You have the old package. Uninstall and install new one:
```bash
pip uninstall google-generativeai
pip install google-genai
```

### Build Warning About Deprecated Package
**Solution**: Update build.bat to use `google.genai` instead of `google.generativeai`

### Import Error in ai_client.py
**Solution**: Update import statement:
```python
import google.genai as genai  # New
```

---

## Migration Checklist

For developers building from source:

- [ ] Uninstall `google-generativeai`
- [ ] Install `google-genai`
- [ ] Update `ai_client.py` imports (if custom)
- [ ] Update `build.bat` hidden-imports
- [ ] Update `build.bat` collect-data
- [ ] Test Gemini provider works
- [ ] Rebuild executable
- [ ] Test executable

---

## References

- [Official Migration Guide](https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md)
- [New google-genai Package](https://pypi.org/project/google-genai/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

---

## Questions?

If you encounter issues with the migration:
1. Check the official migration guide (link above)
2. Search GitHub Issues
3. Create a new issue with:
   - Error message
   - Python version
   - Package versions: `pip list | grep google`

---

**Note**: This migration is required by Google, not specific to Garmin Chat Desktop. All applications using the Gemini API must migrate.

---

Last updated: February 15, 2026
