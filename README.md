# 📊 Financial Dashboard 2024

![GitHub repo size](https://img.shields.io/github/repo-size/leonardo-filho/financial-dashboard)
![GitHub last commit](https://img.shields.io/github/last-commit/leonardo-filho/financial-dashboard)
![GitHub](https://img.shields.io/github/license/leonardo-filho/financial-dashboard)

Projeto de análise e visualização de dados financeiros de vendas utilizando **Python**, **Pandas** e **Streamlit**.  
A base de dados contém transações do ano de **2024**, simulando diferentes canais de venda, categorias de produtos, perfis de clientes e representantes de vendas.

## 📁 Estrutura do Projeto

```
financial_dashboard/
├── app/                  # Código do Streamlit
│   ├── app.py
│   └── utils.py
├── data/                 # Base de dados
│   └── sales_data_2024.csv
├── notebooks/            # Análises exploratórias
│   └── analise_exploratoria.ipynb
├── outputs/              # Gráficos e relatórios gerados
├── requirements.txt      # Dependências do projeto
├── .gitignore
└── README.md
```

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/leonardo-filho/financial-dashboard.git
cd financial-dashboard
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

#### No PowerShell (Windows):

```bash
& ".\venv\Scripts\Activate.ps1"
```

> Se necessário, execute:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o app no navegador

```bash
streamlit run app/app.py
```

## 📈 Funcionalidades

- Filtros interativos por produto, canal de venda e região
- Gráficos mensais de vendas (barras, pizza, etc.)
- Identificação de dias sem vendas
- Tabela dinâmica com os dados filtrados
- Base rica com mais de 2000 registros realistas

## 🛠 Tecnologias utilizadas

- Python 3.10+
- Streamlit
- Pandas
- Plotly
- Faker (geração de dados)
- Jupyter Notebook (para análise exploratória)

## 🧠 Autor

**Leonardo Rodrigues do Nascimento Filho**  
💼 Analista de Dados & BI  
🔗 [github.com/leonardo-filho](https://github.com/leonardo-filho)

## 📄 Licença

Este projeto está sob a licença MIT.
