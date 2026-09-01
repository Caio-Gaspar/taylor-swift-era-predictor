# 🎧 Taylor Swift Era Classifier: Machine Learning & Spotify Data

Este projeto aplica técnicas de **Análise Exploratória de Dados (EDA)**, **Engenharia de Features** e **Machine Learning** para classificar a discografia da Taylor Swift em **Super-Eras sonoras** a partir de métricas de áudio extraídas da API do Spotify.

---

## 📌 Visão Geral do Projeto

A meta inicial era prever o álbum exato de cada faixa (entre 12 eras). No entanto, a Análise Exploratória revelou forte sobreposição acústica entre discos da mesma fase de produção. 

Para eliminar o ruído de classe e aumentar a fidelidade do modelo, os álbuns foram reestruturados em **4 Super-Eras**:

* 🎸 **Country:** *Taylor Swift*, *Fearless (TV)*, *Speak Now (TV)*
* 🎈 **Pop:** *Red (TV)*, *Lover*
* 🪩 **Synth-Pop:** *1989 (TV)*, *reputation*, *Midnights*, *The Life of a Showgirl*
* 🌲 **Folk:** *folklore*, *evermore*, *TTPD: The Anthology*

---

## 📊 Principais Resultados

Testamos múltiplos algoritmos supervisionados e observamos a evolução contínua da acurácia à medida que ajustamos a arquitetura do problema:

| Modelo / Abordagem | Escopo das Classes | Acurácia | Destaque |
| :--- | :--- | :---: | :--- |
| Random Forest (Baseline) | 12 Eras Individuais | ~32.76% | Alta confusão em eras da mesma fase. |
| Random Forest + Feature Eng. | 4 Super-Eras | 56.90% | Redução de ruído por agrupamento. |
| XGBoost (Gradient Boosting) | 4 Super-Eras | 60.00% | Aprendizado iterativo nas zonas limítrofes. |
| **SVM (Kernel RBF)** 🏆 | **4 Super-Eras** | **67.24%** | **Modelo Campeão (Dados Padronizados).** |

### 🏆 Modelo Campeão: SVM (Kernel RBF)
Ao aplicar padronização vetorial (`StandardScaler`) e métricas compostas (`energy_acoustic_ratio`, `production_index`), o **Support Vector Machine (SVM)** superou os modelos baseados em árvore, atingindo **83% de Recall na era Country** e **81% na era Folk**.

---

## 📁 Estrutura do Repositório

```text
├── dados/                      # Dataframes extraídos da API do Spotify
│   ├── showgirl.csv
│   ├── taylor_swift_completo.csv
│   ├── taylor_swift_limpo.csv
│   └── taylor_swift_spotify.csv
├── notebooks/                  # Fluxo sequencial do projeto
│   ├── 01_limpeza.ipynb        # Tratamento e filtragem dos dados
│   ├── 02_analise_exploratoria.ipynb  # EDA e geração de hipóteses
│   ├── 03_modelagem_1.ipynb    # Experimentos (Tree-based, XGBoost, GridSearch)
│   └── 04_modelagem_2.ipynb    # Pipeline final com o modelo campeão (SVM)
├── .gitignore
├── LICENSE
├── README.md
├── get_data.py                 # Script de extração da API do Spotify
└── showgirl.py                 # Script utilitário/suporte
```

---

## 🚀 Como Executar o Projeto

```bash
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

# 2. Instale as dependências necessárias no seu ambiente Python
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib spotipy

# 3. Execute os notebooks sequencialmente na pasta /notebooks
jupyter notebook notebooks/01_limpeza.ipynb
```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Manipulação & Visualização:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (SVM, Random Forest, MLP, KNN), XGBoost
* **Fonte de Dados:** Spotify Web API
