from httpx import get
import smtplib
from email.mime.text import MIMEText

servidor = 'smtp.gmail.com'
porta = 587
usuario = 'freireyago51@gmail.com'
senha = 'Thifler47!'


leads = get(
   "https://habitnet.nocrm.io/api/v2/leads",
   headers={"X-USER-TOKEN": "Mblvwkxo9YL-wavpEJ9CGA"}
   ).json()


oportunidades = list(filter(lambda lead: lead['step'] == 'Oportunidade', leads))



app_password = "zjug gbjy zeeb uhuv"
    
# Configuração do email
remetente = usuario
destinatario = 'thizilplays8606@gmail.com'
mensagem = """\
Olá, {}! Tudo bem ?
Eu sou o Yago Freire da HABITNET.
Vi que você se interessou por nossos empreendimento, quero te a ajudar o seu imóvel sem enrolação.

whataspp -> https://wa.me/5585996954551
Entre em contato comigo para eu te acompanhar melhor na compra do seu imóvel!
"""
# --- PASSO CRUCIAL ---
# 1. Crie o objeto MIMEText, especificando o tipo de conteúdo (plain)
#    e, mais importante, a codificação (charset='utf-8').


# 2. Defina os cabeçalhos (também suportam UTF-8 implicitamente neste método)

# Configurações do Servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'freireyago51@gmail.com'
EMAIL_PASSWORD = app_password

    
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls() 
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        # O método send_message() lida nativamente com o objeto MIME criado
        # e suas codificações.
        for op in oportunidades:
            email_client = op.get('description').split("\n")[2].replace('Email: ', '').replace('E-mail: ', '')
            print(f'Enviado mensagem para: {email_client}', flush=True)
            
            msg = MIMEText(mensagem.format(op.get('title')), 'plain', 'utf-8') 
            msg['From'] = 'freireyago51@gmail.com'
            msg['Subject'] = "Corretor de imóeveis da HABITNET"
            msg['To'] = email_client 
            smtp.send_message(msg)

            print("E-mail enviado com sucesso!")

except Exception as e:
    # Se você ainda tiver um erro aqui, ele será um erro SMTP/Login, e não de codificação.
    print(f"Erro ao enviar email: {e}")