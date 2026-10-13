
# Dashboard SUS — Internações Hospitalares na RIDE-DF

Dashboard interativo para análise de internações hospitalares do Sistema Único de Saúde (SUS), considerando o município de residência dos pacientes na Região Integrada de Desenvolvimento do Distrito Federal e Entorno (RIDE-DF).

## Acessar o projeto

- **Dashboard em produção:** [Acessar aplicação](https://dash-sus-aih-residencia-ride-git-29546019449.us-central1.run.app)
- **Repositório:** [GitHub](https://github.com/felipemoreira-data/dash_sus_aih_residencia_ride)

## Sobre o projeto

O projeto utiliza dados de Autorizações de Internação Hospitalar (AIH) do SUS para explorar a distribuição e a evolução das internações hospitalares na RIDE-DF, com foco no município de residência.

A aplicação permite explorar os dados por meio de filtros e visualizações interativas, facilitando a análise dos indicadores ao longo do tempo e entre municípios.

## Funcionalidades

- Visualização interativa de dados de internações hospitalares.
- Análise de séries temporais e evolução dos indicadores.
- Exploração por município de residência.
- Filtros geográficos para análise dos municípios da RIDE-DF.
- Gráficos interativos para facilitar a exploração dos dados.

## Tecnologias utilizadas

- **Python** — desenvolvimento da aplicação e análise de dados.
- **Dash** — interface web interativa.
- **Plotly** — visualizações e gráficos.
- **Pandas** — manipulação e análise dos dados.
- **PostgreSQL** — armazenamento e consulta dos dados.
- **SQLAlchemy** — conexão com o banco de dados.
- **Docker** — containerização da aplicação.
- **Google Cloud Run** — hospedagem da aplicação.
- **Google Cloud Build** — automação do build da imagem.
- **Artifact Registry** — armazenamento da imagem Docker.

## Executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/felipemoreira-data/dash_sus_aih_residencia_ride.git
cd dash_sus_aih_residencia_ride
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

Ativar no Linux ou WSL:

```bash
source .venv/bin/activate
```

Ativar no Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

Configure as variáveis de ambiente necessárias para a conexão com o PostgreSQL, conforme a implementação de `db_connect.py`.

As credenciais devem ser mantidas em variáveis de ambiente ou em um arquivo `.env` local, nunca publicado no repositório.

### 5. Executar a aplicação

```bash
python dashboard.py
```

Acesse no navegador o endereço local indicado pela aplicação, normalmente:

`http://localhost:8080`

## Deploy

A aplicação é empacotada em um contêiner Docker e hospedada no Google Cloud Run. O repositório está integrado ao Cloud Build para automatizar a construção da imagem a partir da branch `main`.

## Dados

O projeto trabalha com dados de internações hospitalares do SUS, relacionados às Autorizações de Internação Hospitalar (AIH).

Para informações sobre origem, cobertura, metodologia e atualização dos dados, consulte as fontes oficiais do [DATASUS](https://datasus.saude.gov.br/).

---

Projeto de análise e visualização de dados públicos de saúde.
