import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_remetente = 'ayrtonsenna0110@gmail.com'
senha = 'fzro zxfk zhnq bfoq' 


email_destinatario = 'wesleyfreire1707@gmail.com'


mensagem = MIMEMultipart()
mensagem['From'] = email_remetente
mensagem['To'] = email_destinatario
mensagem['Subject'] = 'Teste de E-mail com Python'

# Corpo do e-mail
corpo = ' mensagem  do email'
mensagem.attach(MIMEText(corpo, 'plain'))


try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(email_remetente, senha)
    servidor.send_message(mensagem)
    servidor.quit()
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')