# 🌦️ Clima Urbano: Dashboard Interativo de Clima

Um aplicativo web desenvolvido em Python e Streamlit que fornece informações meteorológicas em tempo real para diversas capitais e cidades globais. Além dos dados do clima, o dashboard exibe informações e imagens de cada localidade selecionada.


## ✨ Funcionalidades

* **Seleção de Cidades:** Escolha entre uma lista de diversas cidades globais em uma barra lateral interativa.
* **Informações Locais:** Veja uma imagem e uma breve descrição da cidade selecionada.
* **Dados em Tempo Real:** Consulte o clima atual através da API do OpenWeatherMap.
* **Widget Detalhado:** Visualize informações como temperatura, sensação térmica, umidade, e temperaturas mínima/máxima.
* **Ícones Dinâmicos:** Os ícones do clima se adaptam para condições diurnas e noturnas.
* **Identificação Visual:** Exibição da bandeira do país correspondente à cidade.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Streamlit
* **Comunicação API:** Biblioteca Requests
* **APIs Externas:**
    * [OpenWeatherMap](https://openweathermap.org/api) para dados meteorológicos.
    * [Flag CDN](https://flagcdn.com/) para as imagens das bandeiras.
* **Versionamento:** Git & GitHub

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação em seu ambiente local.

### Pré-requisitos

* Python 3.8 ou superior
* pip (gerenciador de pacotes do Python)

### Passos

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO]/[SEU_REPOSITORIO].git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd [NOME_DO_REPOSITORIO]
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure sua chave de API:**
    * Crie uma pasta `.streamlit` na raiz do projeto.
    * Dentro dela, crie um arquivo chamado `secrets.toml`.
    * Adicione sua chave da API do OpenWeatherMap ao arquivo:
        ```toml
        OPENWEATHER_KEY = "SUA_CHAVE_AQUI"
        ```

6.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

O aplicativo deverá abrir automaticamente no seu navegador padrão.

---



* **GitHub:** [@[SEU_USUARIO]](https://github.com/[SEU_USUARIO])
* **LinkedIn:** [Seu Nome](https://linkedin.com/in/[SEU_LINKEDIN])
