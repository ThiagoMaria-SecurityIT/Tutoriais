## 🧮 Projeto 2: Calculadora Financeira Simples

> [!IMPORTANT]  
>Esse tutorial faz parte do Tutorial Ambientes virtuais e conta com mais 2 tutoriais simples com esse. \
Check it out: 
 [Acesse a pasta "Ambientes virtuais"](https://github.com/ThiagoMaria-SecurityIT/Tutoriais/tree/main/Ambientes%20virtuais ) 

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
