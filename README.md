🥛 Detector de Copo — Cheio ou Vazio

Aplicação web desenvolvida com Python, Flask e Teachable Machine para identificar se um copo está cheio ou vazio a partir de uma imagem enviada pelo usuário.

O projeto utiliza um modelo de classificação de imagens treinado no Teachable Machine e uma interface web simples para permitir que qualquer pessoa envie uma foto e visualize o resultado da análise.

🎯 Objetivo

Desenvolver uma aplicação de reconhecimento de imagens capaz de classificar copos em duas categorias:

Cheio: o modelo identifica um copo cheio.
Vazio: o modelo identifica um copo vazio.

O objetivo é integrar um modelo de inteligência artificial a uma aplicação web utilizando Flask.

✨ Funcionalidades
📷 Envio de imagens pelo computador ou celular.
🖼️ Visualização da imagem selecionada.
🤖 Classificação automática usando o modelo treinado.
🥛 Identificação das classes "Cheio" e "Vazio".
📊 Exibição da confiança estimada da previsão.
💻 Interface simples e responsiva.
🛠️ Tecnologias utilizadas
Python — linguagem utilizada no backend.
Flask — framework para criação da aplicação web.
HTML5 — estrutura da página.
CSS3 — estilização da interface.
JavaScript — integração com o modelo e interação com o usuário.
TensorFlow.js — execução do modelo de aprendizado de máquina no navegador.
Teachable Machine — treinamento e exportação do modelo de classificação de imagens.
📁 Estrutura do projeto
projeto-final/
├── app.py
├── model/
│   ├── model.json
│   ├── metadata.json
│   └── weights.bin
└── templates/
    └── index.html

Descrição dos arquivos
app.py: configura as rotas e inicia o servidor Flask.
templates/index.html: contém a interface e a lógica de classificação da imagem.
model/model.json: define a arquitetura do modelo exportado.
model/metadata.json: contém os metadados e os nomes das classes.
model/weights.bin: armazena os pesos treinados da rede neural.
⚙️ Como executar o projeto
1. Pré-requisitos

Instale o Python 3 e o Git. Recomenda-se utilizar uma versão recente do Python compatível com o Flask.

2. Clone o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git


Entre na pasta do projeto:

cd SEU-REPOSITORIO


Substitua SEU-USUARIO e SEU-REPOSITORIO pelos dados do seu repositório no GitHub.

3. Instale as dependências
pip install flask

4. Inicie a aplicação
python app.py

5. Acesse o site

Abra o navegador e acesse:

http://127.0.0.1:5000

🚀 Como utilizar
Abra a aplicação no navegador.
Clique em Escolher arquivo.
Selecione uma imagem de um copo.
Clique em Analisar imagem.
Aguarde a classificação realizada pelo modelo.
Visualize o resultado e a confiança estimada.
🧠 Sobre o modelo de inteligência artificial

O modelo foi treinado utilizando o Google Teachable Machine, uma ferramenta que permite criar modelos de aprendizado de máquina sem precisar implementar todo o processo de treinamento manualmente.

As classes utilizadas são:

Cheio
Vazio

Após o treinamento, o modelo foi exportado para uso com TensorFlow.js, permitindo executar as previsões diretamente no navegador.

📌 Limitações
A qualidade das previsões depende das imagens utilizadas no treinamento.
Iluminação, ângulo, transparência do copo e fundo da imagem podem influenciar os resultados.
A confiança apresentada pelo modelo não garante que a classificação esteja correta.
O modelo classifica as imagens de acordo com o que aprendeu durante o treinamento e pode falhar em situações diferentes das utilizadas no conjunto de treinamento.
🔮 Melhorias futuras
Melhorar o design e a experiência do usuário.
Permitir arrastar e soltar imagens.
Adicionar histórico das classificações.
Ampliar o conjunto de imagens de treinamento.
Melhorar a precisão da classificação.
Publicar a aplicação em uma plataforma de hospedagem.
👨‍💻 Autor

Desenvolvido por benício david.

Projeto criado para praticar desenvolvimento web com Flask e integração de modelos de inteligência artificial para classificação de imagens.

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
