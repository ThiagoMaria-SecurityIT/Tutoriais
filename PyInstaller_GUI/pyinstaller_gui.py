import os
import subprocess
import sys
import threading # Moved to the top for global availability
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image # Make sure you have Pillow installed: pip install Pillow

class PyInstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyInstaller Automation Tool v1.0")
        self.root.geometry("700x500")
        
        # Variables
        self.script_path = StringVar()
        self.icon_path = StringVar()
        self.output_dir = StringVar()
        self.use_icon = BooleanVar(value=False)
        self.onefile = BooleanVar(value=True)
        self.windowed = BooleanVar(value=True)
        self.clean_build = BooleanVar(value=False)
        
        # GUI Setup
        self.create_widgets()
        
    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=BOTH, expand=True)
        
        # Script Selection
        ttk.Label(main_frame, text="Python Script:").grid(row=0, column=0, sticky=W, pady=5)
        script_entry = ttk.Entry(main_frame, textvariable=self.script_path, width=50)
        script_entry.grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_script).grid(row=0, column=2)
        
        # Icon Selection
        self.icon_frame = ttk.Frame(main_frame)
        self.icon_frame.grid(row=1, column=0, columnspan=3, sticky=EW, pady=5)
        
        ttk.Checkbutton(
            self.icon_frame, text="Add Icon", 
            variable=self.use_icon, command=self.toggle_icon
        ).pack(side=LEFT)
        
        self.icon_entry = ttk.Entry(self.icon_frame, textvariable=self.icon_path, width=45, state=DISABLED)
        self.icon_entry.pack(side=LEFT, padx=5)
        self.icon_btn = ttk.Button(
            self.icon_frame, text="Browse", 
            command=self.browse_icon, state=DISABLED
        )
        self.icon_btn.pack(side=LEFT)
        
        ttk.Label(main_frame, text="(Must include 16x16, 32x32, 256x256)").grid(row=2, column=1, sticky=W)
        
        # Output Directory
        ttk.Label(main_frame, text="Output Directory:").grid(row=3, column=0, sticky=W, pady=5)
        ttk.Entry(main_frame, textvariable=self.output_dir, width=50).grid(row=3, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_output).grid(row=3, column=2)
        
        # Build Options
        options_frame = ttk.LabelFrame(main_frame, text="Build Options", padding=10)
        options_frame.grid(row=4, column=0, columnspan=3, sticky=EW, pady=10)
        
        ttk.Checkbutton(options_frame, text="--onefile", variable=self.onefile).pack(side=LEFT, padx=10)
        ttk.Checkbutton(options_frame, text="--windowed", variable=self.windowed).pack(side=LEFT, padx=10)
        ttk.Checkbutton(options_frame, text="--clean", variable=self.clean_build).pack(side=LEFT, padx=10)
        
        # Console Output
        console_frame = ttk.LabelFrame(main_frame, text="Console Output", padding=10)
        console_frame.grid(row=5, column=0, columnspan=3, sticky=NSEW, pady=10)
        
        self.console_text = Text(console_frame, height=10, wrap=WORD)
        self.console_text.pack(fill=BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(console_frame, command=self.console_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.console_text.config(yscrollcommand=scrollbar.set)
        
        # Action Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=6, column=0, columnspan=3, pady=10)
        
        ttk.Button(btn_frame, text="Build EXE", command=self.build_exe).pack(side=LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.root.quit).pack(side=LEFT, padx=5)
        
        # Configure grid weights
        main_frame.rowconfigure(5, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def toggle_icon(self):
        if self.use_icon.get():
            self.icon_entry.config(state=NORMAL)
            self.icon_btn.config(state=NORMAL)
        else:
            self.icon_entry.config(state=DISABLED)
            self.icon_btn.config(state=DISABLED)
            self.icon_path.set("")
    
    def browse_script(self):
        filepath = filedialog.askopenfilename(
            title="Select Python Script",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if filepath:
            self.script_path.set(filepath)
            if not self.output_dir.get():
                # Set default output directory to script's directory if not already set
                self.output_dir.set(os.path.dirname(filepath))
    
    def browse_icon(self):
        filepath = filedialog.askopenfilename(
            title="Select Icon File",
            filetypes=[("Icon Files", "*.ico"), ("All Files", "*.*")]
        )
        if filepath:
            if self.validate_icon(filepath):
                self.icon_path.set(filepath)
            else:
                messagebox.showwarning(
                    "Invalid Icon",
                    "Icon must include 16x16, 32x32, and 256x256 sizes"
                )
    
    def browse_output(self):
        dirpath = filedialog.askdirectory(title="Select Output Directory")
        if dirpath:
            self.output_dir.set(dirpath)
    
    def validate_icon(self, icon_path):
        required_sizes = {(16, 16), (32, 32), (256, 256)}
        found_sizes = set()
        try:
            with Image.open(icon_path) as img:
                # Iterate through all images (frames) in the ICO file
                for i in range(img.n_frames):
                    img.seek(i)
                    found_sizes.add(img.size)
            return required_sizes.issubset(found_sizes)
        except Exception as e:
            # Log the specific error for debugging
            self.append_console(f"Error validating icon '{icon_path}': {e}\n")
            return False
    
    def build_exe(self):
        # Validate inputs
        if not self.script_path.get():
            messagebox.showerror("Error", "Please select a Python script")
            return
            
        if not os.path.exists(self.script_path.get()):
            messagebox.showerror("Error", "Python script does not exist")
            return
            
        if self.use_icon.get() and not self.icon_path.get():
            messagebox.showerror("Error", "Please select an icon file")
            return
            
        if not self.output_dir.get():
            messagebox.showerror("Error", "Please select an output directory")
            return
            
        # --- NEW: Determine the direct path to the pyinstaller executable ---
        # This assumes pyinstaller.exe is in the same directory as python.exe in the venv
        pyinstaller_exe_path = os.path.join(os.path.dirname(sys.executable), "pyinstaller.exe")
        if not os.path.exists(pyinstaller_exe_path):
            # Fallback for Linux/macOS or if .exe isn't present (e.g., just 'pyinstaller')
            pyinstaller_exe_path = os.path.join(os.path.dirname(sys.executable), "pyinstaller")
            if not os.path.exists(pyinstaller_exe_path):
                messagebox.showerror("Error", "Could not find pyinstaller executable in venv scripts directory.")
                return

        # Prepare PyInstaller command using the direct executable path
        cmd = [
            pyinstaller_exe_path, # Directly call the pyinstaller executable
            self.script_path.get(),
            "--distpath",
            self.output_dir.get()
        ]
        
        if self.onefile.get():
            cmd.append("--onefile")
        if self.windowed.get():
            cmd.append("--windowed")
        if self.clean_build.get():
            cmd.append("--clean")
        if self.use_icon.get() and self.icon_path.get():
            cmd.extend(["--icon", self.icon_path.get()])
        
        # Run in separate thread to keep GUI responsive
        threading.Thread(
            target=self.run_pyinstaller,
            args=(cmd,),
            daemon=True # Allows the thread to exit when the main program exits
        ).start()
    
    def run_pyinstaller(self, cmd):
        self.append_console(f">> Running command: {' '.join(cmd)}\n")

        # Get the current environment variables and explicitly add venv's Scripts to PATH
        current_env = os.environ.copy()
        # Get the directory of the current Python executable (which is in the venv)
        venv_exec_dir = os.path.dirname(sys.executable) 
        
        # Prepend the venv's executable directory to the PATH
        # This ensures that executables/modules within the venv are found first
        current_env["PATH"] = venv_exec_dir + os.pathsep + current_env.get("PATH", "")

        self.append_console(f"PATH for subprocess (first 200 chars): {current_env['PATH'][:200]}...\n") # For debugging

        # Determine creation flags for subprocess (to hide console window on Windows)
        creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0

        # --- ENHANCED DEBUGGING: Detailed PyInstaller installation check ---
        # This check is still valuable to confirm the environment is set up correctly
        self.append_console("Performing detailed PyInstaller installation check in subprocess...\n")
        check_script_content = f"""
import sys
import os
import subprocess

print(f"Subprocess Python executable: {{sys.executable}}")
print(f"Subprocess sys.version: {{sys.version}}")
print(f"Subprocess sys.prefix: {{sys.prefix}}")
print(f"Subprocess os.environ['PATH'] (first 200 chars): {{os.environ.get('PATH', '')[:200]}}...")
print(f"Subprocess sys.path:")
for p in sys.path:
    print(f"  {{p}}")

try:
    import PyInstaller
    print(f"PyInstaller module found at: {{PyInstaller.__file__}}")
    
    # Also try to run a simple PyInstaller command to confirm execution
    print("Attempting PyInstaller --version from subprocess...")
    # Use the direct pyinstaller executable path for this internal check too, for consistency
    pyinstaller_exe_path_internal = os.path.join(os.path.dirname(sys.executable), "pyinstaller.exe")
    if not os.path.exists(pyinstaller_exe_path_internal):
        pyinstaller_exe_path_internal = os.path.join(os.path.dirname(sys.executable), "pyinstaller")

    result = subprocess.run([pyinstaller_exe_path_internal, "--version"], capture_output=True, text=True, check=True, creationflags={creation_flags})
    print(f"PyInstaller --version output from subprocess: {{result.stdout.strip()}}")
    sys.exit(0) # Success
except ImportError:
    print("Error: PyInstaller module not found in sys.path.")
    sys.exit(1) # Indicate failure
except subprocess.CalledProcessError as e:
    print(f"Error running PyInstaller --version in subprocess: {{e}}")
    print(f"Stdout: {{e.stdout}}")
    print(f"Stderr: {{e.stderr}}")
    sys.exit(1) # Indicate failure
except Exception as e:
    print(f"An unexpected error occurred during PyInstaller check in subprocess: {{e}}")
    sys.exit(1) # Indicate failure
"""
        # Create a temporary script file in the same directory as the main script
        temp_check_script_path = os.path.join(os.path.dirname(__file__), "pyinstaller_debug_check.py")
        try:
            with open(temp_check_script_path, "w") as f:
                f.write(check_script_content)

            check_cmd = [sys.executable, temp_check_script_path]
            check_process = subprocess.run(
                check_cmd,
                capture_output=True,
                text=True,
                check=False, # Do not raise CalledProcessError here, we handle it manually
                creationflags=creation_flags,
                env=current_env
            )
            self.append_console(check_process.stdout)
            if check_process.returncode != 0:
                self.append_console(f"Detailed check failed with exit code {check_process.returncode}.\n")
                self.append_console(f"Stderr from detailed check: {check_process.stderr}\n")
                messagebox.showerror("Error", "PyInstaller module not found or failed to import/run in the subprocess environment. Check console for details.")
                return # Stop execution if the check fails
            else:
                self.append_console("PyInstaller found and accessible for main build.\n")

        except Exception as e:
            self.append_console(f"An unexpected error occurred during detailed PyInstaller check setup: {e}\n")
            messagebox.showerror("Error", f"An unexpected error occurred during detailed PyInstaller check setup: {e}")
            return
        finally:
            # Ensure temp script is removed even if an error occurs
            if os.path.exists(temp_check_script_path):
                os.remove(temp_check_script_path)

        # --- Step 2: Run PyInstaller build process ---
        try:
            process = subprocess.Popen(
                cmd, # Use the directly constructed command
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, # Redirect stderr to stdout pipe for unified output
                universal_newlines=True,  # Decode output as text
                creationflags=creation_flags, # Apply the flag here too
                env=current_env # Pass the explicitly set environment here as well
            )

            # Read output line by line and append to console in real-time
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    # Process has finished and no more output
                    break
                if output:
                    self.append_console(output)
            
            # Get the final return code after the process has completed
            return_code = process.poll()
            if return_code == 0:
                self.append_console("\n>> Build completed successfully!\n")
                messagebox.showinfo("Success", "EXE created successfully!")
            else:
                self.append_console(f"\n>> Build failed with exit code {return_code}!\n")
                self.append_console("Please review the console output above for specific error messages.\n")
                messagebox.showerror("Error", "Build failed - check console output for details.")

        except Exception as e:
            self.append_console(f"\n>> An unexpected error occurred during PyInstaller execution: {e}\n")
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    
    def append_console(self, text):
        # Append text to the console Text widget
        self.console_text.insert(END, text)
        # Scroll to the end to show the latest output
        self.console_text.see(END)
        # Force Tkinter to update the GUI
        self.root.update_idletasks()

if __name__ == "__main__":
    root = Tk()
    app = PyInstallerGUI(root)
    root.mainloop()
