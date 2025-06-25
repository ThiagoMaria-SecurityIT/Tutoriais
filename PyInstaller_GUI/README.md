
# PyInstaller Automation Tool

## Overview

The PyInstaller Automation Tool is a user-friendly graphical interface (GUI) built with Tkinter that simplifies the process of converting Python scripts (`.py` files) into standalone executable applications (`.exe` files) using PyInstaller. This tool streamlines common PyInstaller options, making it easier for developers to package their Python applications for distribution without needing to remember complex command-line arguments.  
![image](https://github.com/user-attachments/assets/e76d3c14-487a-4814-b7a4-1c49a7abf8ac)  

## Features

*   **Intuitive GUI:** Easy-to-use interface for selecting scripts, icons, and output directories.
*   **Common Options:** Supports frequently used PyInstaller options like `--onefile` (single executable), `--windowed` (no console window), and `--clean` (clean build cache).
*   **Icon Support:** Easily add custom icons to your executables, with built-in validation for common icon sizes (16x16, 32x32, 256x256).
*   **Real-time Console Output:** Displays PyInstaller's build process output directly within the GUI, providing immediate feedback and error messages.
*   **Error Handling:** Basic input validation and informative error messages for common issues.
*   **Cross-Platform (GUI is Tkinter):** While the generated `.exe` is platform-specific (Windows in this case), the GUI itself is cross-platform compatible.

## Prerequisites
> [!WARNING]  
> When running this code, use the same Python version of your venv
> If your venv was created with Python 3.12 then run this code with Python 3.13

Before running this tool, ensure you have the following installed:

*   **Python 3.x:**It's highly recommended to use a Python version that matches the one you intend to use for building your executables.
*   **`pip`:** Python's package installer (usually comes with Python).
*   **`venv` (Virtual Environments):** Strongly recommended for managing project dependencies.
*   **`PyInstaller`:** The core library for converting Python scripts to executables.
*   **`Pillow`:** Required for icon validation.

## Installation

Follow these steps to set up and run the PyInstaller Automation Tool:

1.  **Clone or Download the Repository:**
    (Assuming you have the code in a file, place it in your desired project directory.)

2.  **Create and Activate a Virtual Environment (Recommended):**
    Open your terminal or command prompt, navigate to your project directory, and run:

    ```bash
    # Create a virtual environment named 'venv'
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
    You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

3.  **Install Required Python Packages:**
    With your virtual environment activated, install `PyInstaller` and `Pillow`:

    ```bash
    pip install pyinstaller Pillow
    ```

4.  **Save the Code:**
    Save the provided Python code (from our discussion) into a file named `pyinstaller_gui.py` (or any other `.py` name) within your project directory.

## Usage

1.  **Run the Tool:**
    Ensure your virtual environment is activated (as per step 2 in Installation), then run the script:

    ```bash
    python pyinstaller_gui.py
    ```

2.  **Select Python Script:**
    Click "Browse" next to "Python Script" and choose the `.py` file you want to convert.

3.  **Select Output Directory:**
    Click "Browse" next to "Output Directory" and choose where you want the `.exe` file to be saved. By default, it will suggest the script's directory.

4.  **Add Icon (Optional):**
    Check "Add Icon" and click "Browse" to select an `.ico` file. The tool validates if the icon contains required sizes (16x16, 32x32, 256x256).

5.  **Choose Build Options:**
    *   **`--onefile` (checked by default):** Creates a single `.exe` file. If unchecked, PyInstaller will create a folder containing the `.exe` and its dependencies (`--onedir` mode).
    *   **`--windowed` (checked by default):** Builds an executable that runs without a console window.
    *   **`--clean`:** Cleans PyInstaller's build cache before starting the build.

6.  **Build EXE:**
    Click the "Build EXE" button. The "Console Output" section will display the build progress and any messages from PyInstaller. A success or error message box will appear upon completion.

## Important Considerations

### Understanding `--onefile` vs. `--onedir`

*   **`--onefile` (Default):** This option bundles your entire application, including Python interpreter and all dependencies, into a single executable file. This is convenient for distribution as it's just one file. The `.exe` will be placed directly in your chosen "Output Directory".
*   **`--onedir` (When `--onefile` is unchecked):** This is PyInstaller's default behavior if `--onefile` is not specified. It creates a directory (named after your script) within your "Output Directory". Inside this folder, you'll find the main `.exe` along with all necessary libraries and data files. This mode can sometimes be more robust for complex applications with many external data files.

### `--windowed` (or `--noconsole`) for Command-Line Interface (CLI) Applications

The `--windowed` option (which is checked by default in this GUI) tells PyInstaller to build an executable that runs **without displaying a console (command prompt) window**.

*   **Purpose:** This is ideal for **Graphical User Interface (GUI) applications** (like this tool itself, or any app with a visual window) where you only want the graphical interface to appear, not a distracting black console window.
*   **Behavior with CLI Scripts:** If you build a **Command-Line Interface (CLI) Python script** (e.g., a script that primarily uses `print()` statements, `input()`, or performs background tasks without a GUI) with `--windowed` enabled:
    *   The program *will* execute.
    *   Any `print()` output will be sent to a console that is never opened.
    *   If your CLI script finishes quickly (like a simple `print("Hello, World!")` script), it will appear as if the `.exe` "didn't open" or "closed immediately" because there was no visible console window to display its output or keep it open.
*   **Solution:**
    *   If you are building a CLI application and want to see its output in a console window, **uncheck the `--windowed` option** in the GUI before building.
    *   This will create an executable that, when run, will open a console window to display its output.
    *   For CLI scripts that run very quickly, you might consider adding a line like `input("Press Enter to exit...")` or `time.sleep(5)` at the end of your Python script to keep the console window open for a moment after execution.

## Troubleshooting

*   **`venv\Scripts\python.exe: No module named pyinstaller`:**
    This error indicates that `PyInstaller` (or `Pillow`) is not installed in the specific Python virtual environment that your script is running in.
    *   **Solution:** Ensure your virtual environment is activated (e.g., `.\venv\Scripts\activate` on Windows) and then run `pip install pyinstaller Pillow` again within that activated environment.
*   **`PyInstaller not found or not accessible`:**
    Similar to the above, ensure PyInstaller is correctly installed in your active environment. The tool includes a detailed check that will output diagnostic information to the console within the GUI.
*   **`Build failed - check console output`:**
    Always review the "Console Output" section in the GUI for specific error messages from PyInstaller. These messages are crucial for diagnosing build failures (e.g., missing dependencies, syntax errors in your script, etc.).

## Contributing

Feel free to fork this repository, submit pull requests, or open issues if you find bugs or have suggestions for improvements.

## License

This project is open-source and available under the [MIT License](LICENSE). (You might want to create a `LICENSE` file in your repository if you choose this.)

## AI in the code 
The code ```pyinstaller_gui.py ```was created with the help of **Manus** AI and **DeepSeek**.  

## About the Author   

**Thiago Maria | From Brazil to the World 🌎**  
*Senior Security Information Professional | Passionate Programmer | AI Developer*

With a professional background in security analysis and a deep passion for programming, I created this repo share some knowledge about security information, cybersecurity, Python and development practices. Most of my work here focuses on implementing security-first approaches in developer tools while maintaining usability.

## Lets Connect:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/thiago-cequeira-99202239/)  
[![Hugging Face](https://img.shields.io/badge/🤗Hugging_Face-AI_projects-yellow)](https://huggingface.co/ThiSecur)

 
## Ways to Contribute:   
 Want to see more upgrades? Help me keep it updated!    
 [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/ThiagoMaria-SecurityIT)  
