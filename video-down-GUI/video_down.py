import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
from yt_dlp import YoutubeDL

def baixar_video():
    url = entrada_url.get().strip()

    if "youtube.com/watch" not in url:
        messagebox.showerror("Erro", "Insira uma URL válida do YouTube.")
        return

    pasta = filedialog.askdirectory(title="Escolha a pasta para salvar o vídeo")
    if not pasta:
        label_status.config(text="Download cancelado.")
        return

    label_status.config(text="Baixando...")

    ydl_opts = {
        'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
        'format': 'best',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        label_status.config(text="Download concluído com sucesso!")
        messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso!")
    except Exception as e:
        label_status.config(text="Erro ao baixar.")
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo:\n{e}")

def iniciar_download():
    threading.Thread(target=baixar_video).start()

# Interface
janela = tk.Tk()
janela.title("YouTube Downloader (yt-dlp)")
janela.geometry("420x200")
janela.resizable(False, False)

tk.Label(janela, text="URL do vídeo do YouTube:").pack(pady=10)
entrada_url = tk.Entry(janela, width=55)
entrada_url.pack(pady=5)

tk.Button(janela, text="Baixar Vídeo", command=iniciar_download).pack(pady=15)

label_status = tk.Label(janela, text="", fg="blue")
label_status.pack()

janela.mainloop()
