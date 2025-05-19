## 🇪🇸➡🇧🇷 Projeto 3: Tradutor de Espanhol para Português do Brasil 

> [!IMPORTANT]
>### <mark>***Funciona somente com internet, ou seja, online***</mark>
> <mark>pip install legacy-cgi</mark>   <<-- Se der erro instale  
>Esse tutorial faz parte do Tutorial Ambientes virtuais e conta com mais 2 tutoriais simples com esse. \
Check it out: 
 [Acesse a pasta "Ambientes virtuais"](https://github.com/ThiagoMaria-SecurityIT/Tutoriais/tree/main/Ambientes%20virtuais )

Volte para fora da pasta:

```powershell
cd ..
cd tradutor_es_br
```

### 3.1 - Criar o ambiente virtual

```powershell
python -m venv venv
```

### 3.2 - Ativar o ambiente

```powershell
.\venv\Scripts\Activate.ps1
```

### 3.3 - Instalar biblioteca de tradução

```powershell
pip install googletrans==4.0.0-rc1
```

> Essa versão funciona melhor offline.

### 3.4 - Criar o arquivo de tradução

```powershell
code tradutor.py
```

Cole o seguinte código:

```python
from googletrans import Translator

translator = Translator()

texto_esp = input("Digite o texto em espanhol: ")
traducao = translator.translate(texto_esp, src='es', dest='pt')

print("Tradução para português:")
print(traducao.text)
```

Rode:

```powershell
python tradutor.py
```

Exemplo de uso:

```
Digite o texto em espanhol: Hola, ¿cómo estás?
Tradução para português:
Olá, como vai você?
```

✅ Pronto! Agora você tem um tradutor funcional!
