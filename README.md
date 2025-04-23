# Sistema de Monitoramento de Armadilhas para Manejo de Fauna

Este projeto é um sistema de monitoramento de armadilhas para manejo de fauna, desenvolvido em Python. Ele permite gerenciar empresas, funcionários, dispositivos de monitoramento (como gaiolas e gateways), áreas monitoradas e capturas de fauna. O sistema possui uma interface de terminal para interação com usuários administradores e normais.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
├── app.py
├── terminal.py
├── login.py
├── requirements.txt
├── .gitignore
├── data/
│   ├── areas.csv
│   ├── cages.csv
│   ├── capturas.csv
│   ├── companies.csv
│   ├── devices.csv
│   ├── employees.csv
│   ├── gateways.csv
│   ├── install_cage.csv
│   ├── install_gateway.csv
│   ├── sessions.csv
│   ├── users.csv
├── interfaces/
│   ├── Interface_Area.py
│   ├── Interface_Cage.py
│   ├── Interface_Captura.py
│   ├── Interface_Company.py
│   ├── Interface_Device.py
│   ├── Interface_Employee.py
│   ├── Interface_Gateway.py
│   ├── Interface_Install_Cage.py
│   ├── Interface_Install_Gateway.py
│   ├── Interface_Session.py
│   ├── Interface_User.py
│   ├── Interface_User_Admin.py
│   ├── Interface_Wildlife.py
├── output/
│   └── Área Central_mapa.html
```

### Principais Arquivos e Pastas

- **`app.py`**: Arquivo principal que inicializa a aplicação.
- **`terminal.py`**: Contém a lógica principal do sistema, incluindo as interações com o usuário.
- **`login.py`**: Gerencia o login dos usuários.
- **`data/`**: Contém os arquivos CSV que armazenam os dados do sistema, como empresas, dispositivos, áreas, usuários, entre outros.
- **`interfaces/`**: Contém as classes que representam as entidades do sistema, como `Area`, `Company`, `Device`, `User`, entre outras.
- **`output/`**: Pasta onde são salvos os mapas gerados para as áreas monitoradas.

## Funcionalidades

### Para Administradores
- Listar empresas, funcionários e dispositivos.
- Cadastrar novas empresas, funcionários e dispositivos.
- Gerenciar dados de dispositivos e áreas monitoradas.

### Para Usuários Normais
- Exibir informações pessoais e da empresa.
- Visualizar áreas monitoradas e seus detalhes.
- Adicionar novas áreas monitoradas.

## Requisitos

Os requisitos do projeto estão listados no arquivo `requirements.txt`. Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Como Executar

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o arquivo `app.py`:

```bash
python app.py
```

3. Faça login com um dos usuários cadastrados no arquivo `data/users.csv`.

## Dados de Exemplo

Os dados de exemplo estão armazenados na pasta `data/`. Por exemplo:
- Usuários: `data/users.csv`
- Empresas: `data/companies.csv`
- Dispositivos: `data/devices.csv`
- Áreas: `data/areas.csv`

## Mapas

O sistema utiliza a biblioteca `folium` para gerar mapas interativos das áreas monitoradas. Os mapas são salvos na pasta `output/`.

