# .ICON Image Format Converter  
>[!IMPORTANT]
>  Select the output format BEFORE select the file (Check the circle of output format FIRST (ICO, JPEG, etc)
> ![image](https://github.com/user-attachments/assets/0c4126a2-fc2e-48ef-b1d1-c43644e5658b)



>[!TIP]
>If your file is not converted, just select the image again (the first "Browse" button ) and click "Convert" button again  

![image](https://github.com/user-attachments/assets/3131ad12-8c40-4245-9197-be4f9a1ae4da)  
App screenshot   

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [How to Use](#how-to-use)
5. [Installation Tutorial](#installation-tutorial)
6. [Explanation of the Code](#explanation-of-the-code)
7. [Bonus: Creating an EXE](#bonus-creating-an-exe)
8. [About the Author](#about-the-author)

## Overview
This Python application provides a graphical interface for converting images between various formats (WEBP, ICO, PNG, JPEG, JPG) with optional resizing and metadata stripping.

## Features
- Convert between WEBP, ICO, PNG, JPEG, and JPG formats
- Resize images with different fit modes (max, crop, scale)
- Option to strip metadata
- Progress bar showing conversion status
- User-friendly Tkinter interface

## Requirements
- Python 3.6 or later
- Pillow library

## How to Use
1. $\color{red}{\mathrm{Check\ the\ Output\ Format\ FIRST\ Ico,\ Jpeg,\ PNG,\ Jpg,\ Webp }}$    ![image](https://github.com/user-attachments/assets/773c2889-84f2-4ca8-bb0e-b5e157617c83)

2. Select Input File (If you selected the file first, just select it again after choosing the output format)
3. Choose output location
4. Adjust resize settings if needed (width, height, fit mode)
5. Check "Strip Metadata" if desired
6. Click "Convert"
7. Wait for the progress bar to complete

## Installation Tutorial

### 1. Create a Virtual Environment (Recommended)
```sh
python -m venv imgconverter-env
```

### 2. Activate the Virtual Environment
- **Windows:**
  ```sh
  imgconverter-env\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source imgconverter-env/bin/activate
  ```

### 3. Install Requirements
```sh
pip install pillow
```

### 4. Run the Application
```sh
python image_converter.py
```

## Explanation of the Code
We'll focus on the key components that make the converter work:

### Core Conversion Logic
```python
with Image.open(input_path) as img:
    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')
    # ... conversion happens here ...
```
### 1. Image Conversion Core
```python
with Image.open(input_path) as img:
    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')
    
    # Resizing logic here
    
    output = io.BytesIO()
    if self.output_format.get() == "ico":
        img.save(output, format='ICO', sizes=[(width, height)])
    else:
        img.save(output, format=self.output_format.get())
    
    with open(output_path, 'wb') as f:
        f.write(output.getvalue())
```
This is the core conversion logic that:
1. Opens the input image
2. Converts to RGB if needed (required for JPEG)
3. Handles resizing based on user settings
4. Saves to the desired format (with special handling for ICO)

### 2. Resizing Methods
Three different resize modes are implemented:

**Max (maintain aspect ratio):**
```python
img.thumbnail((width, height))
```

**Crop (fill area exactly):**
```python
def resize_and_crop(self, img, width, height):
    # Calculate aspect ratios and crop appropriately
    # ...
    return img.resize((width, height), Image.LANCZOS)
```

**Scale (force exact dimensions):**
```python
img = img.resize((width, height), Image.LANCZOS)
```

### 3. Threading for Responsive UI
```python
Thread(target=self.convert_image, args=(...), daemon=True).start()
```
The conversion runs in a separate thread to keep the UI responsive during processing.

### 4. Progress Updates
```python
self.root.after(10, lambda: self.progress.step(30))
```
The progress bar is updated using Tkinter's `after` method to ensure thread-safe UI updates.  

### Resizing Methods
- **Max (maintain aspect ratio):** `img.thumbnail((width, height))`
- **Crop:** Custom `resize_and_crop()` function
- **Scale:** `img.resize((width, height), Image.LANCZOS)`

### GUI Threading
```python
Thread(target=self.convert_image, args=(...), daemon=True).start()
```
Ensures the UI remains responsive during conversion.

## Bonus: Creating an EXE
To create a standalone Windows executable:

1. Install PyInstaller:
```sh
pip install pyinstaller
```

2. Generate the EXE:
```sh
pyinstaller --onefile --windowed image_converter.py
```

3. The EXE will be in the `dist` folder.

Note: The EXE will be large (50-100MB) as it includes Python.    

---  

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
