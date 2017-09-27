# Gestão Urbana SP

Repositório para o código do site: [http://gestaourbana.prefeitura.sp.gov.br/](http://gestaourbana.prefeitura.sp.gov.br/)


## O que é o Gestão Urbana SP?

Com a Constituição Federal de 1988 e o Estatuto da Cidade canais foram legalmente abertos para que a população pudesse participar das tomadas de decisão dos três níveis de governo, isto é, municipal, estadual e federal. Em São Paulo, cidade com dinâmica e complexidade próprias, a situação não é diferente, já que o planejamento urbano precisa ser resultado do diálogo entre o poder público e a sociedade.

Para dar transparência aos instrumentos de planejamento e implementar canais e ferramentas de participação social, a Prefeitura de São Paulo, por meio da Secretaria Municipal de Urbanismo e Licenciamento – SMUL, criou em abril de 2013 a plataforma Gestão Urbana SP. O Gestão Urbana SP visa aproximar os cidadãos do poder público, tanto por meio da informação, quanto pelo recebimento de colaborações nos projetos urbanísticos desenvolvidos pela SMUL.


## Como montar e desenvolver o ambiente?


### Pré-requisitos do sistema

- Python 2.7 ([link](https://www.python.org/downloads/))
- pip ([link](https://pypi.python.org/pypi/pip/))
- virtualenv ([link](https://pypi.python.org/pypi/virtualenv/))

- Node.js e npm ([link](https://nodejs.org/en/))
- webpack ([link](https://www.npmjs.com/package/webpack))


### Montar

```

git clone https://github.com/SPURB/gestaourbanasp.git # clonar o repositório

virtualenv env # criar o ambiente virtual
env\Scripts\activate # ativar o ambiente virtual
pip install -r requirements.txt # instalar as dependencias de python
python manage.py makemigrations && python manage.py migrate # gerar banco de dados

cd gestaourbana
npm install # instalar as dependencias de node
npm run build # construir o ambiente

```


### Desenvolver

Para o desenvolvimento serão necessárias duas janelas do terminal:

```

# Na pasta inicial do projeto:
virtualenv env # criar o ambiente virtual
env\Scripts\activate # ativar o ambiente virtual
python manage.py runserver # roda o servidor

```

```

# Na pasta \gestaourbana
npm run watch # assiste e monta os recursos quando necessário

```


## Licença

Este repositório está sob a licensa [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
