# ViaCEP Flask
Este projeto é uma API desenvolvida em Python com Flask que consulta endereços através da API ViaCEP e armazena os dados obtidos em um banco de dados SQLite local. Além disso, o projeto foi desenvolvido seguindo a Arquitetura Hexagonal, o que facilita a separação de responsabilidades e a manutenção do código.

![image](https://github.com/user-attachments/assets/a8027401-332c-4015-8f2e-25e18b6cc304)


# 🚀 Funcionalidades
    •	Consulta de endereços a partir de um CEP.
	•	Armazenamento e recuperação dos dados em um banco SQLite.
	•	Resposta estruturada em JSON.
	•	Tratamento de erros para CEPs inválidos.
	•	Projeto estruturado com Arquitetura Hexagonal para separar a lógica de domínio, a aplicação e as integrações com serviços externos.
    •	Documentação interativa das APIs com Swagger, permitindo que o usuário visualize e teste os endpoints.


# 🔨 Tecnologias Utilizadas
    •	Python
	•	Flask
	•	Requests
	•	SQLite
	•	Arquitetura Hexagonal

# 📦 Como instalar

1. Clone o repositorio:

```
git clone https://github.com/andradenatalie/viacep.git
cd viacep.git
```

2. Crie e ative um ambiente virtual:
• No Windows (Prompt de Comando)

```
python -m venv venv
venv\Scripts\activate
```

Caso apareça erro relacionado à política de execução, execute:

```
Set-ExecutionPolicy Unrestricted-ScopeProcess
```

3. Instale as depedências:

```
pip install -r requirements.txt
```

# 📃 Exemplo de uso da API com Swagger

O projeto integra o Swagger por meio da biblioteca Flasgger, permitindo que o usuário visualize e interaja com a documentação dos endpoints. Após iniciar o servidor, basta acessar a URL:

```
http://localhost:8080/apidocs/#/
```

Nessa interface interativa, o usuário poderá:

	•	Visualizar a descrição de cada endpoint.
	•	Testar os endpoints diretamente pelo navegador.
	•	Conferir os parâmetros de entrada e as respostas esperadas

# 📡 Arquitetira Hexagonal

O projeto foi estruturado utilizando a Arquitetura Hexagonal (ou Ports and Adapters), dividindo o sistema em três camadas principais:
	•	Domínio: Contém a lógica de negócio e regras principais, sem dependência de frameworks ou detalhes de infraestrutura.
	•	Aplicação: Coordena a interação entre o domínio e os serviços externos, facilitando a orquestração das operações.
	•	Infraestrutura: Responsável pela comunicação com serviços externos, como a API do ViaCEP e o banco de dados SQLite.

Essa abordagem promove maior manutenibilidade, escalabilidade e testabilidade do sistema.

# 📂 Banco de Dados

Os dados consultados na API do ViaCEP são armazenados em um banco SQLite local, permitindo:
	•	Persistência dos dados: Para reduzir chamadas repetitivas à API externa.
	•	Cache local: Melhor desempenho nas consultas.

# 📝 Author
Natalie Andrade Ezzaher, 13 de março de 2025
