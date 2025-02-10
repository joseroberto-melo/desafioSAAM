import time
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuracao do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='automation.log', filemode='w')
logger = logging.getLogger(__name__)

# Inicia log
logger.info("Inicio do processo")

# Configuracao do Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options().add_argument("--headless"))
logger.info("Navegador configurado")

# Ler os dados da planilha do drive
df = pd.read_csv('https://docs.google.com/spreadsheets/d/1FJeNr6pSydj4dNNmjklWWDsdUiCo55Uw/export?format=csv')
df.columns = df.columns.str.lower().str.strip()
logger.info("Planilha carregada")

# Acessar o site do formulário
driver.get("https://uibank.uipath.com/loans/apply")
time.sleep(3)

sucessos, falhas = 0, 0

for _, row in df.iterrows():
    try:
        driver.find_element(By.ID, "email").send_keys(row['email do solicitante'])
        driver.find_element(By.ID, "amount").send_keys(str(row['montante do empréstimo']))
        driver.find_element(By.ID, "term").send_keys(str(row['termo do empréstimo']))
        driver.find_element(By.ID, "income").send_keys(str(row['renda anual atual( antes dos impostos)']))
        driver.find_element(By.ID, "age").send_keys(str(row['idade']))
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]" ).click()
        
        response_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/body/div/app-loan/app-loan-result/div/div[2]"))
        )
        response_text = response_element.text.split("Apply")[0].strip()
        print(f"{row['email do solicitante']}: {response_text}")
        logger.info(f"{row['email do solicitante']}: Concluido com sucesso")
        sucessos += 1
    except:
        print(f"{row['email do solicitante']}: Falha")
        logger.info(f"{row['email do solicitante']}: Falha")
        falhas += 1
    
    try:
        apply_buttons = [
            "/html/body/app-root/body/div/app-loan/app-loan-result/div/div[2]/div/button",
            "/html/body/app-root/body/div/app-loan/app-loan-result/div/div[2]/div/div[3]/button",
            "/html/body/app-root/body/div/app-loan/app-loan-result/div/div[2]/div/div[1]/button"
        ]
        for xpath in apply_buttons:
            try:
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                ).click()
                break
            except:
                continue
    except:
        logger.info("Erro ao tentar clicar no botao 'Apply for another loan'")

logger.info(f"Processo concluido: {sucessos} sucessos, {falhas} falhas")
print(f"Processo concluido: {sucessos} sucessos, {falhas} falhas")
driver.quit()
