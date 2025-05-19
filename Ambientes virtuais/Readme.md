# 📚 Tutorial: Criando Ambientes Virtuais no Python (para Iniciantes)

## 💡 O que é um ambiente virtual?

Um **ambiente virtual** é como uma "caixinha" isolada onde você pode instalar pacotes e rodar programas Python sem afetar o resto do sistema. Isso ajuda a manter seu computador organizado e evitar conflitos entre projetos.

---

## ✅ Requisitos

- Ter o **Python instalado** no computador (versão 3.x).
- Ter acesso ao **PowerShell** (Windows) ou terminal equivalente.
- Um editor de código, como o **VS Code** (recomendado).

---

## 🛠️ Passo a Passo: Criando os 3 Ambientes Virtuais

Vamos criar 3 pastas diferentes, cada uma com seu próprio ambiente virtual:

1. `gerador_senhas`
2. `calculadora_financeira`
3. `tradutor_es_br`

### 🔹 Passo 1: Criar as pastas

No PowerShell:

```powershell
mkdir gerador_senhas calculadora_financeira tradutor_es_br
```

Agora entre na primeira pasta:

```powershell
cd gerador_senhas
```

---

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

---

## 🧮 Projeto 2: Calculadora Financeira Simples

Volte para fora da pasta anterior:

```powershell
cd ..
cd calculadora_financeira
```

### 2.1 - Criar o ambiente virtual

```powershell
python -m venv venv
```

### 2.2 - Ativar o ambiente

```powershell
.\venv\Scripts\Activate.ps1
```

### 2.3 - Criar o código da calculadora

```powershell
code calculadora.py
```

Cole este código:

```python
def juros_simples(capital, taxa, tempo):
    return capital * taxa * tempo

def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

print("Calculadora Financeira")
print("1 - Juros Simples")
print("2 - Juros Compostos")

opcao = int(input("Escolha uma opção: "))
capital = float(input("Capital inicial: "))
taxa = float(input("Taxa de juros (ex: 0.05): "))
tempo = float(input("Tempo em anos: "))

if opcao == 1:
    print("Juros Simples:", juros_simples(capital, taxa, tempo))
elif opcao == 2:
    print("Juros Compostos:", juros_compostos(capital, taxa, tempo))
else:
    print("Opção inválida.")
```

Execute:

```powershell
python calculadora.py
```

✅ Funcionando! Uma mini calculadora financeira.

---

## 🇪🇸➡🇧🇷 Projeto 3: Tradutor de Espanhol para Português do Brasil

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

---

## 🧼 Dica Bônus: Desativar o ambiente

Sempre que quiser sair do ambiente virtual:

```powershell
deactivate
```

---

## 🗁 Estrutura Final das Pastas

```
SeuDiretorio/
├── gerador_senhas/
│   ├── venv/
│   └── gerador.py
├── calculadora_financeira/
│   ├── venv/
│   └── calculadora.py
└── tradutor_es_br/
    ├── venv/
    └── tradutor.py
```

---

## 🎉 Parabéns!

Você agora sabe:

- Criar ambientes virtuais em Python ✅  
- Rodar scripts simples ✅  
- Organizar seus projetos em pastas distintas ✅  
