# Dashboard Interativo de Dados

Bem-vindo ao **Dashboard Interativo de Dados**, um projeto desenvolvido com Python utilizando as bibliotecas Dash, Pandas, Plotly e Dash Bootstrap Components. Este dashboard permite a visualização e análise interativa de dados, proporcionando insights valiosos de forma dinâmica e intuitiva.

## 📊 Funcionalidades

- **Visualizações Interativas:** Gráficos dinâmicos criados com Plotly que respondem às interações do usuário.
- **Filtros Dinâmicos:** Permite filtrar dados por categorias, datas ou outros critérios relevantes.
- **Design Responsivo:** Interface amigável e adaptável a diferentes tamanhos de tela, graças aos componentes Bootstrap.
- **Atualização em Tempo Real:** Possibilidade de atualizar os dados em tempo real (se aplicável).

## 🛠 Tecnologias Utilizadas

- **Python 3.12.4**
- **Dash:** Framework para construção de aplicações web interativas.
- **Pandas:** Manipulação e análise de dados.
- **Plotly:** Criação de gráficos interativos.
- **Dash Bootstrap Components:** Estilização e componentes visuais baseados no Bootstrap.

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **app.py:** Arquivo principal que define a estrutura do aplicativo Dash.
- **data:** Diretório contendo os dados utilizados no dashboard.
- **assets:** Diretório para armazenar recursos estáticos como imagens, CSS, etc.
- **components:** Diretório para armazenar componentes reutilizáveis.
- **pages:** Diretório para armazenar páginas do aplicativo.

## 🚀 Começando

Estas instruções irão ajudá-lo a configurar e rodar o projeto em sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Certifique-se de ter o seguinte instalado em sua máquina:

- [Python 3.12.4](https://www.python.org/downloads/)
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
- [Git](https://git-scm.com/downloads)

### 🔧 Instalação

1. **Clone o Repositório**

   Abra o terminal no diretório onde deseja clonar o projeto e execute:

   ```bash
   git clone https://github.com/seu-usuario/data_dashboard.git
   ```

2. **Navegue até o Diretório do Projeto**

   ```bash
   cd data_dashboard
   ```

3. **Criar e Ativar o Ambiente Virtual**

   - **No Prompt de Comando (CMD):**

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **No PowerShell:**

     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

     > **Nota:** Se encontrar erros relacionados à política de execução, execute:
     >
     > ```powershell
     > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     > ```
     >
     > E tente ativar novamente o ambiente virtual.

4. **Instalar as Dependências**

   Com o ambiente virtual ativado, instale as dependências listadas no `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### 🏃 Executando o Aplicativo

Para rodar o aplicativo, execute o seguinte comando no terminal:

```bash
python app.py
```
Abra o seu navegador e acesse [http://127.0.0.1:8050/](http://127.0.0.1:8050/) para visualizar o dashboard.

## 🛠️ Próximas Etapas

1. **Adicionar Mais Visualizações:** Incorpore diferentes tipos de gráficos e visualizações para enriquecer o dashboard.
2. **Implementar Funcionalidades Avançadas:** Como exportação de dados, filtros adicionais, etc.
3. **Melhorar a Interface do Usuário:** Refinar o design e a experiência do usuário com CSS personalizado ou temas Bootstrap.
4. **Hospedar o Dashboard:** Utilize plataformas como Heroku, Vercel ou Netlify para disponibilizar seu dashboard online.
5. **Documentação e Testes:** Adicione documentação detalhada e testes para garantir a qualidade do projeto.

## 📚 Recursos Úteis

- [Documentação do Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Guia de Deploy do Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

## 👤 Autor

**Leandro**  
[Seu LinkedIn](https://www.linkedin.com/in/leandro-souza-8b040a151/) | [Seu GitHub](https://github.com/lldsouzadev)

---
