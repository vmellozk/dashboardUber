# Uber Pickups em NYC - Projeto com Streamlit

### Visão Geral
Este projeto demonstra a integração do Streamlit com análise de dados, focando nos pickups da Uber em Nova York. Abaixo você encontrará detalhes sobre como o código funciona, requisitos para utilizá-lo e um link para visualizar o projeto implantado.

### Bibliotecas Utilizadas
- `streamlit`: Para construir aplicativos web interativos.
- `pandas`, `numpy`: Para manipulação e análise de dados.

### Detalhes do Projeto

#### Explicação do Código

- **Carregamento de Dados**:
   - Os dados são obtidos de um arquivo CSV hospedado na AWS S3.
   - A função `load_data` lê os dados, converte colunas de data/hora para o formato datetime e armazena em cache o resultado usando o decorador `@st.cache_data` para otimizar o tempo de carregamento.

- **Exibição dos Dados Raw**:
   - Um checkbox permite aos usuários exibirem os dados brutos obtidos do CSV.

- **Análise de Pickups por Hora**:
   - Exibe o número de pickups da Uber por hora usando um gráfico de barras.

- **Mapa de Pickups por Hora**:
   - Permite aos usuários selecionar uma hora através de um slider e exibe um mapa dos pickups naquela hora utilizando `st.map`.

#### Prévia de Implantação

- **Link de Implantação:** [Link para a Implantação](#)  
- **Prévia:** [Inserir imagem de prévia aqui]

### Como Utilizar

Para executar este código localmente ou em sua própria instância do Streamlit, siga estes passos:

- **Dependências**: Certifique-se de ter o Python instalado juntamente com as bibliotecas necessárias (`streamlit`, `pandas`, `numpy`).

- **Executar o Aplicativo**: Execute o script que contém o código fornecido. O Streamlit irá hospedar o aplicativo localmente, geralmente em `http://localhost:8501`.

### O que Você Precisa

- **Software**: Python 3.6+ com `pip` para instalação de pacotes.
- **Fonte de Dados**: Acesso à internet para baixar os dados do URL fornecido da AWS S3.

### O que Fazer

1. **Clonar o Repositório**: Se estiver utilizando controle de versão, clone o repositório que contém os arquivos do projeto.

2. **Instalar Dependências**: Use `pip install -r requirements.txt` para instalar os pacotes Python necessários.

3. **Executar o Aplicativo**: Execute `streamlit run app.py` (supondo que seu script seja chamado `app.py`).

4. **Explorar o Aplicativo**: Interaja com o aplicativo localmente para visualizar os dados de pickups da Uber.
