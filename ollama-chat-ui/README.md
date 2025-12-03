
# Ollama Chat UI  
   ![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)  ![License](https://img.shields.io/badge/license-MIT-green)   
A lightweight desktop GUI for interacting with Ollama models, supporting both single and multi-model conversations.  
>[!IMPORTANT]  
>Ollama must be installed and running locally with at least one model (for multi-model: 2 models installed in your Ollama are recommended)   
>```
> ollama serve
>```  

![image](https://github.com/user-attachments/assets/9b0f0596-0ff9-4780-ab77-04122127bca8)  

![image](https://github.com/user-attachments/assets/a3f4ad0a-4899-4e31-9a63-b7a23bf79ec6)  
- The image above is the same prompt for both models: "Write code that asks the user for their name and says 'Hello' followed by the name".


## Features

- **Dual Chat Modes**:
  - Single chat with one model
  - Multi-chat comparison between two models
- **Model Selection**:
  - Automatic detection of locally available Ollama models
  - Dropdown selection for easy switching
- **Conversation Flow**:
  - Clear separation of user prompts and model responses
  - Auto-scrolling chat history
- **Lightweight**:
  - Pure Python implementation
  - Minimal dependencies

## Requirements

- Python 3.7+
- Ollama installed and running locally
- At least one Ollama model downloaded (e.g., `llama3`)

## Installation

1. Download or copy the code `main.py`

2. Install dependencies (a virtual environment is reccomended):
   ```bash
   pip install ollama tkinter
   ```

3. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

4. Download at least one model (in a separate terminal):
   ```bash
   ollama pull deepseek-r1:1.5b
   ```
## How to run
1. After install, just run the main code: python main.py

### Interface Controls:
- **Mode Selection**: Toggle between single and multi-chat modes
- **Model Dropdowns**: Select which model(s) to chat with
- **Prompt Entry**: Type your message and press Enter or click Send
- **Chat Display**: View conversation history with automatic scrolling

### Multi-Chat Mode:
Compare responses from two different models side-by-side in real-time.

## Troubleshooting

**No models appearing?**
- Ensure Ollama is running (`ollama serve`)
- Verify you've downloaded at least one model (`ollama pull deepseek-r1:1.5b`)
- Check the terminal for error messages

**Connection issues?**
- Make sure Ollama's API is accessible (default: `http://localhost:11434`)
- Firewall may be blocking the connection
- Again: ensure Ollama is running (`ollama serve`)  

### Dependencies
- `ollama`: Python client for Ollama API
- `tkinter`: Standard Python GUI library

### Code Structure
- `OllamaChatUI` class: Main application window
- Model loading: Automatic detection of available Ollama models
- Threaded responses: Non-blocking UI during model generation

## Future Roadmap  
Consider  [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/ThiagoMaria-SecurityIT)   

- [ ] Implement conversation history saving
- [ ] Add dark/light mode toggle
- [ ] Support for more than two models in multi-chat

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)  

## Transparency Notice

🔍 **Development Transparency**  
This application was created with assistance from AI technologies including:
- [DeepSeek](https://deepseek.com)
- [Manus AI](https://manus.ai)

>[!WARNING]  
>⚠️ **Important Disclaimer**  
> While this software is functional for local use, please note:
> - This is a **proof-of-concept** implementation
> - Not recommended for production environments without further testing
> - Use at your own risk with sensitive data
> - Always verify model outputs before relying on them

  ## Safety Considerations

1. **Local Only**: By default, this only connects to your local Ollama instance
2. **Data Privacy**: 
   - 🔍 No data is collected or transmitted externally by this Python code but consider review the License of Ollama and the AI models you are using with
   - All conversations remain on your machine
3. **Model Safety**:
   - Be aware that LLM outputs may be inaccurate or harmful
   - Review the [Ollama model documentation](https://ollama.com/library) for specific model limitations

## Recommended Usage

✅ Appropriate for:
- Personal experimentation
- Local model testing
- Educational purposes

❌ Not recommended for:
- Production systems
- Sensitive data processing
- Mission-critical applications  


## About the Author   

**Thiago Maria - From Brazil to the World 🌎**  
*Senior Security Information Professional | Passionate Programmer | AI Developer*

With a professional background in security analysis and a deep passion for programming, I created this Github acc to share some knowledge about security information, cybersecurity, Python and AI development practices. Most of my work here focuses on implementing security-first approaches in developer tools while maintaining usability.

Lets Connect:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/thiago-cequeira-99202239/)  
[![Hugging Face](https://img.shields.io/badge/🤗Hugging_Face-AI_projects-yellow)](https://huggingface.co/ThiSecur)

 
## Ways to Contribute:   
 Want to see more upgrades? Help me keep it updated!    
 [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/ThiagoMaria-SecurityIT) 



