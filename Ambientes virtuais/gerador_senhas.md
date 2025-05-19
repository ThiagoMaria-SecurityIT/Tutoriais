## 🌐 Projeto 1: Gerador de Senhas Aleatórias

### 1.1 - Criar o ambiente virtual

Dentro da pasta `gerador_senhas`:

```powershell
python -m venv venv
```

Isso cria uma pasta chamada `venv`, que é o ambiente virtual.

### 1.2 - Ativar o ambiente

```powershell
.\venv\Scripts\Activate.ps1
```

> Você verá `(venv)` aparecer no início da linha, indicando que está dentro do ambiente.

### 1.3 - Criar o arquivo Python

Use um editor de texto ou crie o arquivo no PowerShell:

```powershell
code gerador.py
```

Cole esse código:

```python
import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("Senha gerada:", gerar_senha())
```

Salve e execute:

```powershell
python gerador.py
```

✅ Pronto! Você criou um gerador de senhas com ambiente virtual.
