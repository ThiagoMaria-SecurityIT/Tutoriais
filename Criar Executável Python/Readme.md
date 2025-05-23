 # Criar Executável Python  🚀

📚 __Esse guia/tutorial é para mostrar como criar um executável em Python.__  
__Então o que você precisa:__ 
```
1) Python (3.12.4 ou +)
2) PyInstaller (pip install PyInstaller)
3) Navegue até o diretório onde o seu script Python está localizado:  
     cd caminho/para/seu/script   
4) Execute o comando para criar o executável:  
     pyinstaller --onefile <seu_script.py>
 ```
## 📌 Sumário Rápido  
- [O que você precisa](#o-que-você-precisa)
- [O que você precisa](#o-que-voce-precisa)
- [O que você precisa](#-o-que-voce-precisa)
- [Seção 1](manual-anchor)
- 
- [Introdução](#-introdução)
- [Ferramentas populares](#ferramentas-populares)  
  - [PyInstaller](#1-pyinstaller-recomendado)  
  - [cx_Freeze](#2-cx_freeze)  
  - [Nuitka](#3-nuitka)  
  - [Py2exe](#4-py2exe)  
  - [Py2app](#5-py2app)  
- [Tutorial passo a passo com PyInstaller](#-passo-a-passo-com-pyinstaller-)  
- [Considerações finais](#-considerações-finais)  
- [Tabela comparativa](#-tabela-de-resumo)  

---
<a id="manual-anchor"></a>
## 🛠️ O que você precisa  
Antes de começar, certifique-se de ter:  
- [Python 3.12.4 ou superior](#-o-que-você-precisa)
- [PyInstaller instalado](#1-pyinstaller-recomendado) (`pip install pyinstaller`)  
- Seu script Python pronto no diretório desejado  

🔹 *Dica: [Use um ambiente virtual](#-considerações-finais) para evitar conflitos!*  

---

## 💡 Introdução  
Transformar um script Python em um executável permite distribuir sua aplicação para usuários que **não têm Python instalado**. Este guia cobre:  

1. [Comparativo das 5 melhores ferramentas](#-ferramentas-populares) (incluindo a recomendada, PyInstaller)  
2. [Tutorial detalhado com PyInstaller](#-passo-a-passo-com-pyinstaller-)  
3. [Dicas para testes e distribuição](#-considerações-finais)  

*Continue lendo para escolher a melhor ferramenta para seu projeto!*  

[▶️ Ir direto para o tutorial prático](#-passo-a-passo-com-pyinstaller-)  

---
## 🧑🏽‍🏫 Quer entender? Então você veio no lugar certo: 

Transformar um código Python em um executável é um processo que pode facilitar a distribuição de suas aplicações, permitindo que usuários finais executem seus programas sem a necessidade de ter o Python instalado em seus sistemas. Existem várias ferramentas disponíveis para essa tarefa, cada uma com suas próprias características e vantagens. Neste guia, vamos explorar as principais ferramentas e fornecer um passo a passo detalhado para criar um executável com Python.

### Ferramentas Populares

1. **PyInstaller (Recomendado)** 👈🏽
   - **Descrição**: O PyInstaller é uma das ferramentas mais populares para transformar scripts Python em executáveis. Ele empacota seu código Python junto com o interpretador Python, criando um executável independente que pode ser executado em qualquer sistema operacional compatível.
   - **Instalação**: 
     ```sh
     pip install pyinstaller
     ```
   - **Uso Básico**:
     ```sh
     pyinstaller --onefile seu_script.py
     ```
   - **Opções Adicionais**:
     - `--onefile`: Cria um único arquivo executável.
     - `--windowed`: Para aplicativos com interface gráfica, evita a abertura da janela do terminal.
     - `--icon=seu_icone.ico`: Especifica um ícone para o executável.

2. **cx_Freeze**
   - **Descrição**: O cx_Freeze é outra ferramenta popular que permite empacotar seu código Python em um executável independente. Ele suporta várias plataformas e é fácil de usar.
   - **Instalação**:
     ```sh
     pip install cx_Freeze
     ```
   - **Uso Básico**:
     ```sh
     cxfreeze seu_script.py --target-dir dist
     ```
   - **Opções Adicionais**:
     - `--target-dir`: Especifica o diretório de saída.
     - `--icon=seu_icone.ico`: Especifica um ícone para o executável.

3. **Nuitka**
   - **Descrição**: Nuitka é uma ferramenta que compila Python para código C++ e, em seguida, o compila para um executável. É menos conhecida, mas pode ser mais eficiente em termos de desempenho e segurança.
   - **Instalação**:
     ```sh
     pip install nuitka
     ```
   - **Uso Básico**:
     ```sh
     nuitka --standalone --onefile seu_script.py
     ```
   - **Opções Adicionais**:
     - `--standalone`: Cria um pacote standalone.
     - `--onefile`: Cria um único arquivo executável.

4. **Py2exe**
   - **Descrição**: O Py2exe é uma ferramenta específica para criar executáveis para Windows. É fácil de usar e oferece suporte a recursos avançados.
   - **Instalação**:
     ```sh
     pip install py2exe
     ```
   - **Uso Básico**:
     - Crie um arquivo `setup.py`:
       ```python
       from distutils.core import setup
       import py2exe

       setup(console=['seu_script.py'])
       ```
     - Execute o comando:
       ```sh
       python setup.py py2exe
       ```

5. **Py2app**
   - **Descrição**: O Py2app é semelhante ao Py2exe, mas voltado para a criação de executáveis para macOS.
   - **Instalação**:
     ```sh
     pip install py2app
     ```
   - **Uso Básico**:
     - Crie um arquivo `setup.py`:
       ```python
       from setuptools import setup

       APP = ['seu_script.py']
       DATA_FILES = []
       OPTIONS = {'argv_emulation': True}

       setup(
           app=APP,
           data_files=DATA_FILES,
           options={'py2app': OPTIONS},
           setup_requires=['py2app'],
       )
       ```
     - Execute o comando:
       ```sh
       python setup.py py2app
       ```

### 📚 Passo a Passo com PyInstaller 👈🏽

1. **Instalação do PyInstaller**:
   ```sh
   pip install pyinstaller
   ```

2. **Criação do Arquivo Executável**:
   - Navegue até o diretório onde o seu script Python está localizado:
     ```sh
     cd caminho/para/seu/script
     ```
   - Execute o comando para criar o executável:
     ```sh
     pyinstaller --onefile seu_script.py
     ```

3. **Opções Adicionais**:
   - **Ícone**:
     ```sh
     pyinstaller --onefile --icon=seu_icone.ico seu_script.py
     ```
   - **Interface Gráfica**:
     ```sh
     pyinstaller --onefile --windowed seu_script.py
     ```

4. **Localização do Executável**:
   - Após a execução do comando, o PyInstaller criará uma pasta `dist` no diretório atual. Dentro dessa pasta, você encontrará o seu arquivo executável.

### Considerações Finais

- **Ambiente Virtual**: É recomendável usar um ambiente virtual para evitar conflitos com outras instalações de Python. Você pode criar um ambiente virtual usando:
  ```sh
  python -m venv nome_do_ambiente
  ```
  Ative o ambiente virtual:
  - **Windows**:
    ```sh
    nome_do_ambiente\Scripts\activate
    ```
  - **Linux/MacOS**:
    ```sh
    source nome_do_ambiente/bin/activate
    ```

- **Testes**: Antes de criar o executável, certifique-se de que o seu script Python está funcionando corretamente. O executável não mostrará erros de código, então é importante testar antes.

- **Distribuição**: Ao distribuir seu executável, lembre-se de que ele pode ter dependências específicas do sistema operacional. Teste o executável em diferentes ambientes para garantir a compatibilidade.

### Tabela de Resumo

| Ferramenta     | Descrição                                                                 | Instalação                       | Uso Básico                                      | Opções Adicionais                                                                 |
|----------------|---------------------------------------------------------------------------|----------------------------------|-------------------------------------------------|----------------------------------------------------------------------------------|
| PyInstaller    | Empacota código Python em um executável independente.                     | `pip install pyinstaller`        | `pyinstaller --onefile seu_script.py`           | `--onefile`, `--windowed`, `--icon=seu_icone.ico`                                |
| cx_Freeze      | Suporta várias plataformas e é fácil de usar.                             | `pip install cx_Freeze`          | `cxfreeze seu_script.py --target-dir dist`      | `--target-dir`, `--icon=seu_icone.ico`                                          |
| Nuitka         | Compila Python para código C++ e, em seguida, para um executável.         | `pip install nuitka`             | `nuitka --standalone --onefile seu_script.py`   | `--standalone`, `--onefile`                                                      |
| Py2exe         | Específico para Windows, fácil de usar.                                   | `pip install py2exe`             | `python setup.py py2exe`                        | `setup(console=['seu_script.py'])`                                               |
| Py2app         | Específico para macOS, semelhante ao Py2exe.                             | `pip install py2app`             | `python setup.py py2app`                        | `setup(app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS})`             |

Espero que este guia tenha sido útil para você. Agora você está pronto para transformar seus scripts Python em executáveis e distribuí-los de forma eficiente.Transformar um código Python em um executável é um processo que pode facilitar a distribuição de suas aplicações, permitindo que usuários finais executem seus programas sem a necessidade de ter o Python instalado em seus sistemas. Existem várias ferramentas disponíveis para essa tarefa, cada uma com suas próprias características e vantagens. Neste guia, vamos explorar as principais ferramentas e fornecer um passo a passo detalhado para criar um executável com Python.

### Ferramentas Populares

1. **PyInstaller**
   - **Descrição**: O PyInstaller é uma das ferramentas mais populares para transformar scripts Python em executáveis. Ele empacota seu código Python junto com o interpretador Python, criando um executável independente que pode ser executado em qualquer sistema operacional compatível.
   - **Instalação**: 
     ```sh
     pip install pyinstaller
     ```
   - **Uso Básico**:
     ```sh
     pyinstaller --onefile seu_script.py
     ```
   - **Opções Adicionais**:
     - `--onefile`: Cria um único arquivo executável.
     - `--windowed`: Para aplicativos com interface gráfica, evita a abertura da janela do terminal.
     - `--icon=seu_icone.ico`: Especifica um ícone para o executável.

2. **cx_Freeze**
   - **Descrição**: O cx_Freeze é outra ferramenta popular que permite empacotar seu código Python em um executável independente. Ele suporta várias plataformas e é fácil de usar.
   - **Instalação**:
     ```sh
     pip install cx_Freeze
     ```
   - **Uso Básico**:
     ```sh
     cxfreeze seu_script.py --target-dir dist
     ```
   - **Opções Adicionais**:
     - `--target-dir`: Especifica o diretório de saída.
     - `--icon=seu_icone.ico`: Especifica um ícone para o executável.

3. **Nuitka**
   - **Descrição**: Nuitka é uma ferramenta que compila Python para código C++ e, em seguida, o compila para um executável. É menos conhecida, mas pode ser mais eficiente em termos de desempenho e segurança.
   - **Instalação**:
     ```sh
     pip install nuitka
     ```
   - **Uso Básico**:
     ```sh
     nuitka --standalone --onefile seu_script.py
     ```
   - **Opções Adicionais**:
     - `--standalone`: Cria um pacote standalone.
     - `--onefile`: Cria um único arquivo executável.

4. **Py2exe**
   - **Descrição**: O Py2exe é uma ferramenta específica para criar executáveis para Windows. É fácil de usar e oferece suporte a recursos avançados.
   - **Instalação**:
     ```sh
     pip install py2exe
     ```
   - **Uso Básico**:
     - Crie um arquivo `setup.py`:
       ```python
       from distutils.core import setup
       import py2exe

       setup(console=['seu_script.py'])
       ```
     - Execute o comando:
       ```sh
       python setup.py py2exe
       ```

5. **Py2app**
   - **Descrição**: O Py2app é semelhante ao Py2exe, mas voltado para a criação de executáveis para macOS.
   - **Instalação**:
     ```sh
     pip install py2app
     ```
   - **Uso Básico**:
     - Crie um arquivo `setup.py`:
       ```python
       from setuptools import setup

       APP = ['seu_script.py']
       DATA_FILES = []
       OPTIONS = {'argv_emulation': True}

       setup(
           app=APP,
           data_files=DATA_FILES,
           options={'py2app': OPTIONS},
           setup_requires=['py2app'],
       )
       ```
     - Execute o comando:
       ```sh
       python setup.py py2app
       ```

### Passo a Passo com PyInstaller

1. **Instalação do PyInstaller**:
   ```sh
   pip install pyinstaller
   ```

2. **Criação do Arquivo Executável**:
   - Navegue até o diretório onde o seu script Python está localizado:
     ```sh
     cd caminho/para/seu/script
     ```
   - Execute o comando para criar o executável:
     ```sh
     pyinstaller --onefile seu_script.py
     ```

3. **Opções Adicionais**:
   - **Ícone**:
     ```sh
     pyinstaller --onefile --icon=seu_icone.ico seu_script.py
     ```
   - **Interface Gráfica**:
     ```sh
     pyinstaller --onefile --windowed seu_script.py
     ```

4. **Localização do Executável**:
   - Após a execução do comando, o PyInstaller criará uma pasta `dist` no diretório atual. Dentro dessa pasta, você encontrará o seu arquivo executável.

### Considerações Finais

- **Ambiente Virtual**: É recomendável usar um ambiente virtual para evitar conflitos com outras instalações de Python. Você pode criar um ambiente virtual usando:
  ```sh
  python -m venv nome_do_ambiente
  ```
  Ative o ambiente virtual:
  - **Windows**:
    ```sh
    nome_do_ambiente\Scripts\activate
    ```
  - **Linux/MacOS**:
    ```sh
    source nome_do_ambiente/bin/activate
    ```

- **Testes**: Antes de criar o executável, certifique-se de que o seu script Python está funcionando corretamente. O executável não mostrará erros de código, então é importante testar antes.

- **Distribuição**: Ao distribuir seu executável, lembre-se de que ele pode ter dependências específicas do sistema operacional. Teste o executável em diferentes ambientes para garantir a compatibilidade.

### Tabela de Resumo

| Ferramenta     | Descrição                                                                 | Instalação                       | Uso Básico                                      | Opções Adicionais                                                                 |
|----------------|---------------------------------------------------------------------------|----------------------------------|-------------------------------------------------|----------------------------------------------------------------------------------|
| PyInstaller    | Empacota código Python em um executável independente.                     | `pip install pyinstaller`        | `pyinstaller --onefile seu_script.py`           | `--onefile`, `--windowed`, `--icon=seu_icone.ico`                                |
| cx_Freeze      | Suporta várias plataformas e é fácil de usar.                             | `pip install cx_Freeze`          | `cxfreeze seu_script.py --target-dir dist`      | `--target-dir`, `--icon=seu_icone.ico`                                          |
| Nuitka         | Compila Python para código C++ e, em seguida, para um executável.         | `pip install nuitka`             | `nuitka --standalone --onefile seu_script.py`   | `--standalone`, `--onefile`                                                      |
| Py2exe         | Específico para Windows, fácil de usar.                                   | `pip install py2exe`             | `python setup.py py2exe`                        | `setup(console=['seu_script.py'])`                                               |
| Py2app         | Específico para macOS, semelhante ao Py2exe.                             | `pip install py2app`             | `python setup.py py2app`                        | `setup(app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS})`             |

Espero que este tuto tenha sido útil para você. Agora você está pronto para transformar seus scripts Python em executáveis e distribuí-los de forma eficiente.

by: Thiago Maria

