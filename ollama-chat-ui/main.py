import tkinter as tk
from tkinter import ttk
import ollama
import threading

class OllamaChatUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Light Ollama Chat")
        self.geometry("800x600")

        self.create_widgets()
        self.load_ollama_models()

    def create_widgets(self):
        # Main frame for layout
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Mode selection (Single/Multi-chat)
        self.mode_var = tk.StringVar(value="single")
        mode_frame = ttk.Frame(main_frame)
        mode_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Radiobutton(mode_frame, text="Single Chat", variable=self.mode_var, value="single", command=self.toggle_chat_mode).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(mode_frame, text="Multi-Chat", variable=self.mode_var, value="multi", command=self.toggle_chat_mode).pack(side=tk.LEFT, padx=5)

        # Model selection frame (will be used for both modes, with elements hidden/shown)
        self.model_selection_frame = ttk.Frame(main_frame)
        self.model_selection_frame.pack(fill=tk.X, pady=(0, 10)) # Always pack this frame

        self.model1_label = ttk.Label(self.model_selection_frame, text="Model:") # Changed label to be generic
        self.model1_label.pack(side=tk.LEFT, padx=5)
        self.model1_combo = ttk.Combobox(self.model_selection_frame)
        self.model1_combo.pack(side=tk.LEFT, padx=5)

        # These will be hidden in single chat mode
        self.model2_label = ttk.Label(self.model_selection_frame, text="Model 2:")
        self.model2_combo = ttk.Combobox(self.model_selection_frame)

        # Chat display area
        self.chat_display_frame = ttk.Frame(main_frame)
        self.chat_display_frame.pack(fill=tk.BOTH, expand=True)

        self.single_chat_text = tk.Text(self.chat_display_frame, wrap=tk.WORD, state=tk.DISABLED)
        # self.single_chat_text.pack(fill=tk.BOTH, expand=True) # Will be packed by toggle_chat_mode

        # Multi-chat display (initially hidden)
        self.multi_chat_frame = ttk.Frame(self.chat_display_frame)
        self.multi_chat_frame.grid_columnconfigure(0, weight=1)
        self.multi_chat_frame.grid_columnconfigure(1, weight=1)
        self.multi_chat_frame.grid_rowconfigure(0, weight=1) # Make rows expandable

        self.model1_chat_text = tk.Text(self.multi_chat_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.model1_chat_text.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        self.model2_chat_text = tk.Text(self.multi_chat_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.model2_chat_text.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

        # Input area
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(10, 0))

        self.prompt_entry = ttk.Entry(input_frame)
        self.prompt_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.prompt_entry.bind("<Return>", self.send_prompt)

        send_button = ttk.Button(input_frame, text="Send", command=self.send_prompt)
        send_button.pack(side=tk.RIGHT)

        self.toggle_chat_mode() # Initialize UI based on default mode

    def load_ollama_models(self):
        try:
            ollama_response = ollama.list()
            # print(f"Ollama list raw response: {ollama_response}") # Keep this for debugging if needed

            models = []
            if "models" in ollama_response and isinstance(ollama_response["models"], list):
                for model_info in ollama_response["models"]:
                    if "model" in model_info:
                        models.append(model_info["model"])
                    else:
                        self.append_to_chat(self.single_chat_text, f"Warning: Found a model entry without a 'model' key: {model_info}\n")
            else:
                self.append_to_chat(self.single_chat_text, "Warning: Ollama list response did not contain a 'models' list or was malformed.\n")

            self.model1_combo["values"] = models
            self.model2_combo["values"] = models
            if models:
                self.model1_combo.set(models[0]) # Set default for single and multi model 1
                if len(models) > 1:
                    self.model2_combo.set(models[1]) # Set default for multi model 2
                else:
                    self.model2_combo.set(models[0]) # Fallback if only one model for multi model 2
            else:
                self.append_to_chat(self.single_chat_text, "No Ollama models found. Please ensure Ollama is running and you have downloaded models (e.g., 'ollama run llama3').\n")
        except ollama.ResponseError as e:
            self.append_to_chat(self.single_chat_text, f"Error from Ollama server: {e}\nPlease ensure Ollama is running and accessible.\n")
        except Exception as e:
            self.append_to_chat(self.single_chat_text, f"Error connecting to Ollama: {e}\nPlease ensure Ollama is running.\n")

    def toggle_chat_mode(self):
        if self.mode_var.get() == "single":
            # Show single chat elements
            self.model1_label.config(text="Model:") # Update label for single mode
            self.model1_label.pack(side=tk.LEFT, padx=5)
            self.model1_combo.pack(side=tk.LEFT, padx=5)
            self.model2_label.pack_forget() # Hide model 2 label
            self.model2_combo.pack_forget() # Hide model 2 combo

            self.multi_chat_frame.pack_forget() # Hide multi-chat display
            self.single_chat_text.pack(fill=tk.BOTH, expand=True) # Show single chat display
        else: # Multi-chat mode
            # Show multi chat elements
            self.model1_label.config(text="Model 1:") # Revert label for multi mode
            self.model1_label.pack(side=tk.LEFT, padx=5)
            self.model1_combo.pack(side=tk.LEFT, padx=5)
            self.model2_label.pack(side=tk.LEFT, padx=5) # Show model 2 label
            self.model2_combo.pack(side=tk.LEFT, padx=5) # Show model 2 combo

            self.single_chat_text.pack_forget() # Hide single chat display
            self.multi_chat_frame.pack(fill=tk.BOTH, expand=True) # Show multi-chat display

    def send_prompt(self, event=None):
        prompt = self.prompt_entry.get()
        if not prompt: return

        self.prompt_entry.delete(0, tk.END)

        if self.mode_var.get() == "single":
            selected_model = self.model1_combo.get() # Get selected model for single chat
            if not selected_model:
                self.append_to_chat(self.single_chat_text, "Error: No model selected for single chat.\n")
                return
            self.append_to_chat(self.single_chat_text, f"You: {prompt}\n")
            threading.Thread(target=self.get_ollama_response, args=(prompt, self.single_chat_text, selected_model)).start()
        else:
            model1 = self.model1_combo.get()
            model2 = self.model2_combo.get()
            
            if not model1 or not model2:
                self.append_to_chat(self.single_chat_text, "Error: Please select both models for multi-chat.\n")
                return

            # Display user prompt once for multi-chat in both panes
            self.append_to_chat(self.model1_chat_text, f"You: {prompt}\n")
            self.append_to_chat(self.model2_chat_text, f"You: {prompt}\n")

            threading.Thread(target=self.get_ollama_response, args=(prompt, self.model1_chat_text, model1)).start()
            threading.Thread(target=self.get_ollama_response, args=(prompt, self.model2_chat_text, model2)).start()

    def get_ollama_response(self, prompt, text_widget, model_name): # model_name is now always provided
        try:
            if not model_name: # Should not happen with the current logic, but good for safety
                self.append_to_chat(text_widget, "Error: No model specified for response generation.\n")
                return

            self.append_to_chat(text_widget, f"{model_name}: Generating...\n")
            response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
            self.append_to_chat(text_widget, f"{model_name}: {response["message"]["content"]}\n")
        except ollama.ResponseError as e:
            self.append_to_chat(text_widget, f"Error from Ollama server ({model_name}): {e}\n")
        except Exception as e:
            self.append_to_chat(text_widget, f"Error: {e}\n")

    def append_to_chat(self, text_widget, message):
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, message)
        text_widget.see(tk.END)
        text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = OllamaChatUI()
    app.mainloop()
