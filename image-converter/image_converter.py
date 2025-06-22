import os
import tkinter as tk
from tkinter import filedialog, messagebox
from io import BytesIO
import cairosvg
from PIL import Image
import svgwrite
import base64

# --- Conversion Functions ---

def convert_svg_to_raster(input_svg, output_path, output_format):
    """Convert SVG to PNG/JPG/ICO using CairoSVG."""
    if output_format in ['PNG', 'JPG', 'JPEG']:
        cairosvg.svg2png(url=input_svg, write_to=output_path)
        if output_format in ['JPG', 'JPEG']:
            img = Image.open(output_path)
            img = img.convert('RGB')
            img.save(output_path, 'JPEG')
    elif output_format == 'ICO':
        temp_png = os.path.splitext(output_path)[0] + ".png"
        cairosvg.svg2png(url=input_svg, write_to=temp_png)
        img = Image.open(temp_png)
        img.save(output_path, format="ICO", sizes=[(16,16), (32,32), (48,48), (256,256)])
        os.remove(temp_png)

def convert_raster_to_raster(input_path, output_path, output_format):
    """Convert between PNG, JPG, JPEG, and ICO using Pillow."""
    img = Image.open(input_path)
    if output_format in ['JPG', 'JPEG']:
        if img.mode in ['RGBA', 'P']:
            img = img.convert('RGB')
        img.save(output_path, 'JPEG')
    elif output_format == 'PNG':
        img.save(output_path, 'PNG')
    elif output_format == 'ICO':
        img.save(output_path, format='ICO', sizes=[(16,16), (32,32), (48,48), (256,256)])

def convert_to_svg(input_path, output_path):
    """Convert any raster image to SVG by embedding it."""
    img = Image.open(input_path)
    byte_io = BytesIO()
    img.save(byte_io, format='PNG')
    png_data = byte_io.getvalue()
    encoded = base64.b64encode(png_data).decode()
    width, height = img.size
    dwg = svgwrite.Drawing(output_path)
    dwg.viewbox(width=width, height=height)
    dwg.add(dwg.image(href=f"data:image/png;base64,{encoded}", width=width, height=height))
    dwg.save()

def convert_file(input_path, input_format, output_path, output_format):
    """Main conversion function based on input/output format."""
    if input_format == output_format:
        raise ValueError("Input and Output formats are the same.")

    if input_format == 'SVG':
        if output_format in ['PNG', 'JPG', 'JPEG']:
            convert_svg_to_raster(input_path, output_path, output_format)
        elif output_format == 'ICO':
            convert_svg_to_raster(input_path, output_path, output_format)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

    elif output_format == 'SVG':
        convert_to_svg(input_path, output_path)

    else:
        convert_raster_to_raster(input_path, output_path, output_format)

# --- GUI Application ---

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Image Format Converter")

        # Variables
        self.input_file = tk.StringVar()
        self.input_format = tk.StringVar(value="PNG")
        self.output_format = tk.StringVar(value="JPG")
        self.output_file = tk.StringVar()

        # Layout
        tk.Label(root, text="Input File:").grid(row=0, column=0, sticky='e')
        tk.Entry(root, textvariable=self.input_file, width=40).grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.select_input_file).grid(row=0, column=2)

        tk.Label(root, text="Input Format:").grid(row=1, column=0, sticky='e')
        tk.OptionMenu(root, self.input_format, 'PNG', 'JPG', 'JPEG', 'ICO', 'SVG').grid(row=1, column=1, sticky='w')

        tk.Label(root, text="Output Format:").grid(row=2, column=0, sticky='e')
        tk.OptionMenu(root, self.output_format, 'PNG', 'JPG', 'JPEG', 'ICO', 'SVG').grid(row=2, column=1, sticky='w')

        tk.Label(root, text="Output File:").grid(row=3, column=0, sticky='e')
        tk.Entry(root, textvariable=self.output_file, width=40).grid(row=3, column=1)
        tk.Button(root, text="Save As", command=self.select_output_file).grid(row=3, column=2)

        tk.Button(root, text="Convert", command=self.do_convert).grid(row=4, column=1, pady=10)

    def select_input_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("All Image Files", "*.png *.jpg *.jpeg *.ico *.svg")]
        )
        if path:
            self.input_file.set(path)
            ext = os.path.splitext(path)[1].lower()
            if ext == ".svg":
                self.input_format.set("SVG")
            elif ext in [".png", ".jpg", ".jpeg", ".ico"]:
                self.input_format.set(ext[1:].upper())

    def select_output_file(self):
        input_fmt = self.input_format.get()
        default_ext = self.output_format.get().lower()
        initialfile = f"output.{default_ext}"
        path = filedialog.asksaveasfilename(
            defaultextension=default_ext,
            filetypes=[(f"{default_ext.upper()} files", f"*.{default_ext}")],
            initialfile=initialfile
        )
        if path:
            self.output_file.set(path)

    def do_convert(self):
        input_path = self.input_file.get()
        input_fmt = self.input_format.get()
        output_path = self.output_file.get()
        output_fmt = self.output_format.get()

        if not input_path or not input_fmt or not output_path or not output_fmt:
            messagebox.showerror("Error", "All fields must be filled.")
            return

        try:
            convert_file(input_path, input_fmt, output_path, output_fmt)
            messagebox.showinfo("Success", "Conversion completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# --- Run the App ---

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
  
# --- Made with the help of Qwen3-Demo ---
