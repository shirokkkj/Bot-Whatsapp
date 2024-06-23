from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
import customtkinter as ct
import os
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)        

navegador.get('https://web.whatsapp.com/')

# INTERFACE
janela = ct.CTk()

    # Janela Principal
janela.title('Messager Whatsapp Bot')
janela.geometry('500x300')
janela.maxsize(width=600, height=400)
janela.minsize(width=500, height=300)

    # Fonts
my_font = ct.CTkFont(family="Helvetica", size=16, weight="bold", slant="italic", underline=False, overstrike=False)
my_font1 = ct.CTkFont(family="Arial Blod", size=10, weight="bold", slant="italic", underline=True, overstrike=False)
my_font2 = ct.CTkFont(family="Arial Blod", size=13, weight="bold", slant="italic", underline=False, overstrike=False)

ct.CTkLabel(janela, text='MESSAGER BOT WHATSAPP', font=my_font).place(x=140, y=30)
ct.CTkLabel(janela, text='Este é um bot criado a fim de testes.\nCaso ocorra problemas, o responsabilizado será o usuário.', font=my_font2).place(x=85, y=70)

    # Criar jannela do messager
while True:
    def nova_janela():
        global nome, ctt, msg, ctgt, ctms, new_janela
        new_janela = ct.CTkToplevel(janela, fg_color='#8EE53F')
        new_janela.geometry('500x400')
        new_janela.title('MESSAGER')
        frame1 = ct.CTkFrame(new_janela, width=200, height=330, fg_color='#FFDB58', border_width=10, corner_radius=50).place(x=140, y=40)

        # Nome do contato
        ct.CTkLabel(new_janela, text='Nome do contato:', font=my_font1, fg_color='#2E8B57', corner_radius=10, bg_color='transparent').place(x=170, y=70)
        ctt = ct.CTkEntry(master=new_janela, placeholder_text='Nome...')
        ctt.place(x=170, y=110)

        # Mensagem
        ct.CTkLabel(master=new_janela, text='Mensagem a ser enviada: ', font=my_font1, fg_color='#2E8B57', corner_radius=10, bg_color='transparent').place(x=165, y=180)
        msg = ct.CTkEntry(master=new_janela, placeholder_text='Mensagem...')
        msg.place(x=170, y=220)
        botao = ct.CTkButton(master=new_janela, text='Salvar dados', fg_color='#2E8B57', corner_radius=10, font=my_font1, command=coleta_dados).place(x=170, y=300)
        sbotao = ct.CTkButton(master=new_janela, text='FINISH', fg_color='#2E8B57', corner_radius=10, font=my_font1, command=encerrar_processo).place(x=170, y=330)
    # Button to finish prog
    def encerrar_processo():
        janela.destroy()    
        os.kill(janela, navegador)
    # Criar a coleta de dados e o envio deles para o whatsapp
    def coleta_dados():
        global nome, ctt, msg, ctgt, ctms
        # Requerir e pegar nome e mensagem a ser enviada
        ctgt = ctt.get()
        ctms = msg.get()

        # Envio da mensagem/Contato
        navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
        navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(ctgt)
        navegador.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(2)
            
        navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(ctms)
        navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)

    buton = ct.CTkButton(master=janela, text='Abrir messager', fg_color='green', corner_radius=20,font=my_font,command=nova_janela).place(x=180, y=170)
    janela.mainloop()
input()