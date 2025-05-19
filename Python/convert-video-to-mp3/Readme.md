# 🎓 Tutorial Completo: Converter Vídeo para MP3 no Windows 11 com Python (sem erros)

## ✅ O Que Você Vai Aprender:
- Como instalar FFmpeg corretamente
- Como configurar as variáveis do sistema
- Como rodar o script Python para converter vídeos para MP3
- Como usar um seletor de arquivos (janela gráfica)

---

## 🧰 Requisitos

- **Windows 11**
- **Python 3.10+ instalado** (funciona com Python 3.12)
- Conhecimento básico em CMD ou PowerShell

---

## 🔽 Passo 1: Baixar o FFmpeg para Windows

1. Acesse este link:
   🔗 [https://github.com/btbn/ffmpeg-builds/releases](https://github.com/btbn/ffmpeg-builds/releases)

2. Procure pelo último build compatível com Windows 64-bit, como:
   ```
   ffmpeg-n7.1.x-win64-gpl-x.x.zip
   ```

3. Exemplo recente:
   ```
   ffmpeg-n7.1.1-14-g7eaa8c110e-win64-gpl-7.1.zip
   ```

4. Baixe o arquivo ZIP.

---

## 📁 Passo 2: Extrair e Renomear a Pasta

1. Extraia o conteúdo do `.zip` para uma pasta.
2. Dentro do ZIP, você verá uma pasta com nome parecido com:
   ```
   ffmpeg-n7.1.1-14-g7eaa8c110e-win64-gpl-7.1
   ```

3. **Renomeie essa pasta para:** `ffmpeg`

4. Cole a pasta renomeada na raiz do disco C:  
   Exemplo:
   ```
   C:\ffmpeg
   ```

---

## 🧪 Passo 3: Adicionar FFmpeg ao PATH (para funcionar no terminal)

1. Abra o painel de controle:
   - Aperte `Win + S`, digite **"Editar variáveis de ambiente do sistema"**

2. Na janela que abrir:
   - Clique em **Variáveis de Ambiente**
   - Em **Variáveis do Sistema**, selecione **Path** > clique em **Editar**
   - Clique em **Novo** e adicione:
     ```
     C:\ffmpeg\bin
     ```

3. Clique em **Ok** para salvar todas as alterações.

---

## 🖥️ Passo 4: Testar o FFmpeg no Terminal

1. Abra o **Prompt de Comando (CMD)** como administrador.

2. Execute:

```bash
cd C:\ffmpeg\bin
ffmpeg -version
```

Se aparecer a versão do FFmpeg, está tudo certo!

---

## 🐍 Passo 5: Instalar os Pacotes Necessários no Python

Abra o CMD como administrador e execute:

```bash
pip install pydub
```

---

## 📄 Passo 6: Código Python para Converter Vídeo para MP3

Crie um novo arquivo chamado `convert_video_to_mp3.py` com o seguinte conteúdo:

```python
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
import os

# Oculta a janela principal do Tkinter
Tk().withdraw()

def convert_video_to_mp3(input_path, output_path=None):
    """
    Converte o áudio de um vídeo para MP3 usando pydub + ffmpeg.
    
    :param input_path: Caminho do arquivo de vídeo
    :param output_path: Caminho de saída do arquivo MP3 (opcional)
    """
    if not os.path.isfile(input_path):
        print(f"❌ Arquivo não encontrado: {input_path}")
        return

    try:
        # Carrega o arquivo de vídeo (pydub extrai o áudio automaticamente)
        audio = AudioSegment.from_file(input_path)

        # Define o nome do arquivo de saída
        if output_path is None:
            base = os.path.splitext(input_path)[0]
            output_path = base + ".mp3"

        # Exporta como MP3
        audio.export(output_path, format="mp3")

        print(f"✅ Conversão concluída! Arquivo salvo em: {output_path}")

    except Exception as e:
        print(f"❌ Erro durante a conversão: {e}")

# Execução principal
if __name__ == "__main__":
    print("📂 Selecione o arquivo de vídeo...")
    video_file = askopenfilename(
        title="Escolha um vídeo",
        filetypes=[("Vídeos", "*.mp4 *.avi *.mkv *.mov *.flv")]
    )

    if video_file:
        convert_video_to_mp3(video_file)
    else:
        print("❌ Nenhum arquivo foi selecionado.")
```

---

## ▶️ Passo 7: Executar o Script

No CMD, navegue até a pasta onde está o seu script:

```bash
cd caminho\para\sua\pasta
python convert_video_to_mp3.py
```

Uma janela será aberta para você escolher o vídeo.

Após selecionar, o programa irá extrair o áudio e salvar como **`.mp3`** na mesma pasta do vídeo.

---

## 💡 Dica Bônus: Criar um Executável (.exe)

Se quiser transformar esse script em um `.exe` para rodar sem Python:

```bash
pip install pyinstaller
pyinstaller --onefile convert_video_to_mp3.py
```

O executável será criado na pasta `dist/`.

---

## 📌 Resumo Final

| Etapa | Descrição |
|-------|-----------|
| 1 | Baixar FFmpeg do GitHub |
| 2 | Extrair e renomear pasta |
| 3 | Adicionar ao PATH |
| 4 | Testar FFmpeg no CMD |
| 5 | Instalar `pydub` |
| 6 | Rodar o script Python |
| 7 | (Opcional) Gerar `.exe` |

## *Recomendo criar um ambiente virtual para e utilizar o Python 3.12.4
## Obrigado e Tchau!
