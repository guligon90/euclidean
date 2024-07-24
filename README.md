# "Amansa-burro" básico do `pytest`

## Preliminares

Para ser rodado localmente (de preferência em ambiente Debian-based, porque em Ruindows™, basta ver o que aconteceu com o gigolôs da Cloudstrike), devem estar instalados localmente:

- Python: [v3.10](https://github.com/python/peps/blob/main/peps/pep-0619.rst) ou superior (duuuuh!!)
- Poetry: gerenciador de ambiente virtual Python, porque eu estou assumindo que estou lidando com pessoas civilizadas. [Aqui](https://python-poetry.org/docs/#installing-with-the-official-installer) explica como instalá-lo.

## Manipulação

### Dependências

Com o `poetry` devidamente instalado e configurado localmente, na raíz do projeto, execute o seguinte comando para instalar as dependências:

```bash
poetry install
```

Para ativar o ambiente virtual do Python localmente:

```bash
poetry shell
```

### Testes

Para executar os testes unitários via `pytest`, basta rodar o comando:

```bash
pytest -svv # Com parâmetros de verbosidade
```

O resultado deve ser similar a:

![Peek 2024-07-24 18-31](https://github.com/user-attachments/assets/d4446337-a2c5-4434-8e0d-36ddd644b573)
