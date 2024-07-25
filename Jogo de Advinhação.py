import random
import tkinter as tk
 
 
class JogoDeAdivinhação:
 
    def __init__(self, master):
 
        self.master = master
        master.title('Jogo de Adivinhação')
        master.geometry("500x150")
 
        self.master.configure(bg='#B0C4DE')
 
        self.label = tk.Label(master, text='Bem vindo ao Jogo! Advinhe o número de 1 a 100!', bg='#B0C4DE', fg='black')
        self.label.pack()
 
        self.botao_novo_jogo = tk.Button(master, text='Novo Jogo',command=self.novo_jogo, bg='#32CD32', fg='black')
        self.botao_novo_jogo.pack()
 
        self.botao_tentar = tk.Button(master, text='Tentar',state='disabled',command=self.tentar, bg='#FF4500', fg='black')
        self.botao_tentar.pack()
 
        self.entrada = tk.Entry(master)
        self.entrada.pack()
 
        self.tentativas_restantes = tk.Label(master,text="",bg='#B0C4DE', fg='black')
        self.tentativas_restantes.pack()
 
 
        self.novo_jogo()
 
 
    def novo_jogo(self):
        self.numero_secreto = random.randint(1,100)
 
 
        self.tentativas = 0
        self.botao_tentar.config(state='normal')
        self.tentativas_restantes.config(text=f'Tentativas restantes: {5-self.tentativas}')
 
    def tentar(self):
        self.tentativas +=1
        tentativa = int(self.entrada.get())
 
        if tentativa < (self.numero_secreto):
            self.label.config(text='O número é maior.', fg='#000000')
        elif  tentativa > (self.numero_secreto):
            self.label.config(text='O número é menor.', fg='#000000')
        else:
            self.label.config(text=f'Parabéns! Você acertou o número em {self.tentativas} tentativas!', fg='#008000')
            self.botao_tentar.config(state='disabled')
            return
       
        self.tentativas_restantes.config(text=f'Tentativas Restantes: {5-self.tentativas}')
        self.entrada.delete(0,tk.END)
 
        if self.tentativas == 5:
            self.label.config (text=f'Game over...Você perdeu para mim. O número era {self.numero_secreto} ',fg='#FF0000')
            self.botao_tentar.config(state='disabled')
 
 
root = tk.Tk()
app = JogoDeAdivinhação(root)
root.mainloop()