# workidea-s
Sistema de seleção e desenvolvimento de ideias através de Hackathons. Trabalho de Projeto de SW2

## Django e dependências

### Instalação dos pacotes necessários:
- Instale o python3
- Instale o repositório de pacotes: python3-pip
- Instale o restante dos pacotes executando:
    - *pip3 install -r requirements.txt*

### Execução:
- **Modo Desenvolvedor:**
    - Copie o arquivo *"local_settings.py.EXAMPLE"*
    - Cole no mesmo local com o nome *"local_settings.py"*
    - Execute:
        - *python3 manage.py makemigrations*
        - *python3 manage.py migrate*
        - *python3 manage.py runserver*

- **Modo Produção:**
    - Execute:
        - *python3 manage.py makemigrations*
        - *python3 manage.py migrate*
        - *python3 manage.py collectstatic*
    - Configure seu servidor web. Os arquivos estáticos são criados na pasta 'static' dentro do projeto


###Referência de estrutura
Aplicação Django referência para estrutra, organização e codigos, Django SIGE:
```sh
https://github.com/thiagopena/djangoSIGE

```
