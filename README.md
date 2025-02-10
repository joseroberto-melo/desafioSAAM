# Automação RPA - SAAM Auditoria

## 📌 Descricao
Este projeto automatiza o processo de preenchimento de formulários no site **UiBank Loan Application** utilizando **Selenium** e **Pandas**. A automação lê os dados de uma planilha do Google Sheets, insere as informações no formulário e exibe a resposta da solicitação no terminal.

## 🛠 Requisitos
Antes de rodar o código, instale os seguintes pacotes:

```sh
pip install selenium pandas webdriver-manager
```

Além disso, certifique-se de ter o **Google Chrome** instalado.

## 🚀 Como Executar
1. Clone o repositório:
   ```sh
   git clone https://github.com/joseroberto-melo/desafioSAAM
   cd desafioSAAM
   ```
2. Execute o script:
   ```sh
   python rpaautomation.py
   ```
3. O resultado será exibido no terminal e um log será gerado no arquivo `automation.log`.

## 📂 Estrutura do Repositório
```
📦 projeto-rpaautomation
 ┣ 📜 rpa_automation.py      # Script principal
 ┣ 📜 README.md              # Documentacao
 ┣ 📜 requirements.txt       # Dependencias do projeto
 ┗ 📜 automation.log         # Log de execucao
```

## 📄 Notas
- O código executa no modo **headless** para otimizar o processamento.
- Caso o botão "Apply for another loan" mude de posição, o script tentará clicar em diferentes caminhos possíveis.

🚀 **Desenvolvido para automação de processos com RPA**.

