import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import io
from threading import Thread

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Format Converter")
        self.root.geometry("500x500")
        
        # Variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.output_format = tk.StringVar(value="png")
        self.width_var = tk.StringVar(value="32")
        self.height_var = tk.StringVar(value="32")
        self.fit_mode = tk.StringVar(value="max")
        self.strip_metadata = tk.BooleanVar(value=True)
        self.conversion_in_progress = False
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Input file selection
        ttk.Label(self.root, text="Input File:").pack(pady=(10, 0))
        input_frame = ttk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=10)
        ttk.Entry(input_frame, textvariable=self.input_path, width=40).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(input_frame, text="Browse", command=self.browse_input).pack(side=tk.LEFT, padx=5)
        
        # Output format selection
        ttk.Label(self.root, text="Output Format:").pack(pady=(10, 0))
        format_frame = ttk.Frame(self.root)
        format_frame.pack(fill=tk.X, padx=10)
        formats = [("PNG", "png"), ("JPEG", "jpeg"), ("JPG", "jpg"), ("ICO", "ico"), ("WEBP", "webp")]
        for text, fmt in formats:
            ttk.Radiobutton(format_frame, text=text, variable=self.output_format, value=fmt).pack(side=tk.LEFT, padx=5)
        
        # Output location
        ttk.Label(self.root, text="Output Location:").pack(pady=(10, 0))
        output_frame = ttk.Frame(self.root)
        output_frame.pack(fill=tk.X, padx=10)
        ttk.Entry(output_frame, textvariable=self.output_path, width=40).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(output_frame, text="Browse", command=self.browse_output).pack(side=tk.LEFT, padx=5)
        
        # Resize options
        ttk.Label(self.root, text="Resize Options:").pack(pady=(10, 0))
        resize_frame = ttk.Frame(self.root)
        resize_frame.pack(fill=tk.X, padx=10)
        
        ttk.Label(resize_frame, text="Width:").pack(side=tk.LEFT)
        ttk.Entry(resize_frame, textvariable=self.width_var, width=5).pack(side=tk.LEFT, padx=5)
        ttk.Label(resize_frame, text="Height:").pack(side=tk.LEFT)
        ttk.Entry(resize_frame, textvariable=self.height_var, width=5).pack(side=tk.LEFT, padx=5)
        
        # Fit mode
        ttk.Label(self.root, text="Fit Mode:").pack(pady=(10, 0))
        fit_frame = ttk.Frame(self.root)
        fit_frame.pack(fill=tk.X, padx=10)
        fit_modes = [("Max", "max"), ("Crop", "crop"), ("Scale", "scale")]
        for text, mode in fit_modes:
            ttk.Radiobutton(fit_frame, text=text, variable=self.fit_mode, value=mode).pack(side=tk.LEFT, padx=5)
        
        # Metadata options
        ttk.Label(self.root, text="Metadata:").pack(pady=(10, 0))
        ttk.Checkbutton(self.root, text="Strip Metadata", variable=self.strip_metadata).pack()
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, mode='determinate')
        self.progress.pack(fill=tk.X, padx=10, pady=10)
        
        # Convert button
        self.convert_button = ttk.Button(self.root, text="Convert", command=self.start_conversion)
        self.convert_button.pack(pady=10)
        
        # Status label
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack()
        
    def browse_input(self):
        filetypes = [
            ("Image files", "*.webp *.ico *.png *.jpeg *.jpg"),
            ("All files", "*.*")
        ]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.input_path.set(filename)
            # Set default output path
            base, ext = os.path.splitext(filename)
            self.output_path.set(f"{base}_converted.{self.output_format.get()}")
    
    def browse_output(self):
        initial_file = self.output_path.get()
        filetypes = [
            ("PNG", "*.png"),
            ("JPEG", "*.jpeg"),
            ("JPG", "*.jpg"),
            ("ICO", "*.ico"),
            ("WEBP", "*.webp"),
            ("All files", "*.*")
        ]
        filename = filedialog.asksaveasfilename(
            initialfile=initial_file,
            filetypes=filetypes,
            defaultextension=f".{self.output_format.get()}"
        )
        if filename:
            self.output_path.set(filename)
    
    def start_conversion(self):
        if self.conversion_in_progress:
            return
            
        input_path = self.input_path.get()
        output_path = self.output_path.get()
        
        if not input_path:
            messagebox.showerror("Error", "Please select an input file")
            return
            
        if not output_path:
            messagebox.showerror("Error", "Please select an output location")
            return
            
        try:
            width = int(self.width_var.get()) if self.width_var.get() else None
            height = int(self.height_var.get()) if self.height_var.get() else None
        except ValueError:
            messagebox.showerror("Error", "Width and height must be integers")
            return
            
        self.conversion_in_progress = True
        self.convert_button.config(state=tk.DISABLED)
        self.progress["value"] = 0
        self.status_label.config(text="Converting...")
        
        # Run conversion in a separate thread to keep UI responsive
        Thread(target=self.convert_image, args=(input_path, output_path, width, height), daemon=True).start()
    
    def convert_image(self, input_path, output_path, width, height):
        try:
            # Open the image
            with Image.open(input_path) as img:
                # Convert to RGB if needed (for JPEG)
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGB')
                
                # Resize if dimensions are provided
                if width or height:
                    original_width, original_height = img.size
                    width = width if width is not None else original_width
                    height = height if height is not None else original_height
                    
                    if self.fit_mode.get() == "max":
                        img.thumbnail((width, height))
                    elif self.fit_mode.get() == "crop":
                        img = self.resize_and_crop(img, width, height)
                    else:  # scale
                        img = img.resize((width, height), Image.LANCZOS)
                
                # Update progress
                self.root.after(10, lambda: self.progress.step(30))
                
                # Prepare output with or without metadata
                output = io.BytesIO()
                save_kwargs = {}
                
                if self.output_format.get() == "ico":
                    img.save(output, format='ICO', sizes=[(width or img.width, height or img.height)])
                else:
                    if self.output_format.get() in ('jpeg', 'jpg'):
                        save_kwargs['quality'] = 95
                    
                    img.save(output, format=self.output_format.get(), **save_kwargs)
                
                self.root.after(10, lambda: self.progress.step(30))
                
                # Write to output file
                with open(output_path, 'wb') as f:
                    f.write(output.getvalue())
                
                self.root.after(10, lambda: self.progress.step(40))
                
                # Update UI
                self.root.after(10, self.conversion_complete)
                self.root.after(10, lambda: self.status_label.config(text="Conversion complete!"))
                
        except Exception as e:
            error_message = str(e)
            self.root.after(10, lambda msg=error_message: messagebox.showerror("Error", f"Conversion failed: {msg}"))
            self.root.after(10, self.conversion_complete)
    
    def resize_and_crop(self, img, width, height):
        """Resize and crop image to exactly fit the given dimensions"""
        img_ratio = img.width / img.height
        target_ratio = width / height
        
        if target_ratio > img_ratio:
            # Image is too tall, crop top/bottom
            new_height = int(img.width / target_ratio)
            offset = (img.height - new_height) // 2
            img = img.crop((0, offset, img.width, offset + new_height))
        elif target_ratio < img_ratio:
            # Image is too wide, crop left/right
            new_width = int(img.height * target_ratio)
            offset = (img.width - new_width) // 2
            img = img.crop((offset, 0, offset + new_width, img.height))
        
        return img.resize((width, height), Image.LANCZOS)
    
    def conversion_complete(self):
        self.conversion_in_progress = False
        self.convert_button.config(state=tk.NORMAL)
        self.progress["value"] = 100

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
