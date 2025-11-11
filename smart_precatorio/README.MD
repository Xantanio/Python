# Smart Precatorio - Case de Funções Python

Este repositório contém um notebook Jupyter (`smart_precatorio_case.ipynb`) com a implementação e testes de diversas funções utilitárias em Python. O notebook é dividido em cinco seções, abordando desde algoritmos básicos até manipulação de dados com Pandas e um exemplo de query SQL.

---

## Conteúdo do Notebook

O notebook está dividido nas seguintes seções:

1.  **Calculadora de Média de Notas:** Uma função (`weighted_average_grade_calculator`) que calcula a média ponderada de um conjunto de notas e pesos.
2.  **Ordenador de Lista:** Uma implementação do algoritmo de ordenação **Merge Sort** (`merge_sort`).
3.  **Contador de Caracteres:** Uma função (`character_counter`) que conta a frequência de cada caractere em uma string.
4.  **Processamento de Dados (Precatórios):** Três funções usando a biblioteca **Pandas** para analisar uma lista de dicionários de precatórios:
    * `total_per_status`: Calcula o valor total agrupado por status.
    * `group_by_year`: Agrupa todos os registros por ano.
    * `order_by_value`: Ordena os registros com base no valor.
5.  **Banco de Dados (Exemplo SQL):** Um diagrama de entidade-relacionamento (ERD) e uma query SQL para um sistema de gerenciamento de precatórios.

Cada seção no notebook inclui seus próprios testes (usando `assert`) para verificar a corretude das funções.

---

## Pré-requisitos

Para rodar este notebook, você precisará ter os seguintes softwares instalados:

* **Python 3.x**
* **Jupyter Notebook** ou **Jupyter Lab**
* A biblioteca **Pandas**

---

## Como Baixar e Rodar o Projeto

Siga estes passos para baixar o código do GitHub e executá-lo em sua máquina.

### 1. Baixando o Repositório

**Clonando com Git**

Abra seu terminal e execute o seguinte comando:

```bash
# Clone este repositório
git clone https://github.com/Xantanio/Python.git

# Entre na pasta que foi criada
cd Python/smart_precatorio

# Instale o pandas e o jupyter
pip install pandas jupyter
```

### 2. Executando

```bash
# Dentro da pasta do projeto execute
jupyter notebook
```

Agora basta abrir o arquivo smart_precatorio_case.ipynb e executar as células desejadas.