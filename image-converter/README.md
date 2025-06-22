# 🖼️ ICON Image Format Converter  
A simple GUI-based tool to convert between SVG, PNG, JPG, JPEG, and ICO formats.

![image](https://github.com/user-attachments/assets/7a08c015-791f-460a-ae69-9a590d4b8c93)  

> [!WARNING]
> ⚠️ **Attention Windows Users**  
> CairoSVG requires native libraries on Windows.  
> **Fix**: Download the [PyGObject All-in-One Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) and install GTK3 runtime to get Cairo.   
> Click in the Tutorial to FIX: [3. Windows Fix: Install Cairo](3-windows-fix-install-cairo)   

---

## 📦 Features
- Convert **SVG ↔ PNG/JPG/ICO**
- Convert **PNG/JPG/ICO ↔ PNG/JPG/ICO**
- Simple **Tkinter GUI** for file selection and format conversion
- Supports **batch conversion** (not shown here but extendable)

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/image-converter.git
cd image-converter
```

### 2. Install Dependencies
```bash
pip install cairosvg pillow svgwrite
```

### 3. Windows Fix: Install Cairo  
> [!IMPORTANT]   
> **Critical Step for Windows Users!**  

#### Option 1: Use PyGObject Installer (Recommended)
1. Download the **PyGObject Installer** for Windows:
   - [GTK3 Runtime Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
2. Run the installer and select:
   - `Install for all users`
   - Install path: `C:\GTK`
3. Add Cairo to your system PATH:
   ```bash
   C:\GTK\bin
   ```
4. Restart your terminal or IDE.

#### Option 2: Use MSYS2 (Advanced)
1. Install [MSYS2](https://www.msys2.org/)
2. Run:
   ```bash
   pacman -Syu
   pacman -S mingw-w64-x86_64-gtk3
   ```
3. Add `C:\msys64\mingw64\bin` to your system PATH.

---

## 🧪 Usage
Run the converter:
```bash
python image_converter.py
```

### Example Conversions
| Input Format | Output Format | Notes |
|--------------|----------------|-------|
| SVG          | PNG / JPG / ICO | Uses CairoSVG |
| PNG / JPG    | SVG             | Embeds image in SVG |
| PNG / JPG / ICO | PNG / JPG / ICO | Uses Pillow |

---

## 🖥️ GUI Interface
1. Select input file (supports `.svg`, `.png`, `.jpg`, `.jpeg`, `.ico`)
2. Choose input format (auto-detected from file extension)
3. Choose output format
4. Specify output file path
5. Click **Convert**

---

## 🛠️ Troubleshooting (Windows)

### ❌ Error: `no library called "cairo-2" was found`
- **Solution**: Install GTK3 runtime via PyGObject Installer or MSYS2 (see above).

### ❌ ICO Conversion Fails
- **Fix**: Simplify ICO size requirements:
  ```python
  img.save(output_path, format='ICO', sizes=[(256,256)])
  ```

### ❌ File Dialogs Not Working
- **Fix**: Run the script from the terminal instead of double-clicking.

---

## 📝 Notes
- SVG-to-raster uses **CairoSVG** for accurate rendering.
- Raster-to-SVG embeds the image as a **base64-encoded PNG** inside the SVG.
- JPG output is always RGB (no alpha channel).
- ICO files support multiple resolutions (16x16, 32x32, 48x48, 256x256).

---

## 📄 License
MIT License (see [LICENSE](LICENSE))

---

