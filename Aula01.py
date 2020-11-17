from tkinter import*
root = Tk()
root.geometry("800x400")
class UrnaBtn:
   def insere(self,text):
       Visor.muda(text)
   def __init__(self,window,text,x,y,w,h):
       self.window = window
       self.text = text
       self.x = x
       self.y = y
       self.w = w
       self.h = h 
       Button(self.window,text=self.text,width=w,height=h,command=lambda: self.insere(self.text)).place(x=self.x,y=self.y)



       
class UrnaAction:
    def __init__(self,window,text,x,y,w,h,color,fun):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color  
        self.fun = fun
        if(self.fun == "finaliza"):
            Button(self.window,text=self.text,width=w,height=h,bg=self.color,borderwidth=0.5,command = lambda : self.Confirmar()).place(x=self.x,y=self.y)
        elif(self.fun == "limpa"):
            Button(self.window,text=self.text,width=w,height=h,bg=self.color,borderwidth=0.5, command = lambda: self.corrigir()).place(x=self.x,y=self.y)
        else:
            Button(self.window,text=self.text,width=w,height=h,bg=self.color,borderwidth=0.5,command = lambda: self.Branco()).place(x=self.x,y=self.y)
    
    def corrigir(self):
        Visor.limpa()
    def Branco(self):
        Visor.Anula()
    def Confirmar(self):
        Visor.finaliza()
    
    
class visor:
    def __init__(self,window):
        self.window = window
        self.valor = ""
        self.saida = StringVar()
        Label(self.window,textvariable=self.saida,font=("Arial",30)).place(x=0,y=0)
        self.saida.set(self.valor)
    def muda(self,novo):
        if(len(self.valor) < 5):
            if len(self.valor)  == 1:
                self.valor += novo
                self.saida.set(self.valor)
                Exibe.EncontraPartido(int(self.valor))
            else:
                self.valor += novo
                self.saida.set(self.valor)
        else:
            pass
    
    def limpa(self):
        self.valor = ""
        self.saida.set(self.valor)
        Exibe.zera()

    def finaliza(self):
        Exibe.SomaVoto(int(Visor.valor))
        self.valor = "Fim"
        self.saida.set(self.valor)
    def Anula(self):
        self.valor = "Fim"
        self.saida.set(self.valor)

class exibe:
    def __init__(self,NumeroDePartidos,NomeCandidatos):
        self.NumeroDePartidos = NumeroDePartidos
        self.NomeCandidatos = NomeCandidatos
        self.VotosValidos = []
        self.VotosInvalidos = 0
        self.valor = ""
        self.saida = StringVar()
        self.saida.set(self.valor)
        Label(root,textvariable = self.saida,font = ("Arial",30)).place(x=500,y=100)
        for k in range(NumeroDePartidos):
            self.VotosValidos.append([NomeCandidatos[k][0],NomeCandidatos[k][1],0])
        
    def SomaVoto(self,NumeroCandidato):
        cont = 0
        for k in self.NomeCandidatos:
            cont +=1
            if k[1] == NumeroCandidato:
                for n in self.VotosValidos:
                     if n[1] == NumeroCandidato:
                           n[2] += 1
                           break
            elif cont==3:
                self.VotosInvalidos +=1
        print(self.VotosValidos,self.VotosInvalidos)
    def EncontraPartido(self,NumeroCandidato):
       cont = 0
       for k in self.NomeCandidatos:
           cont += 1
           if k[1] == NumeroCandidato:
               self.valor = k[2]
               self.saida.set(self.valor)
               break
           elif cont == 3 and k[1] != NumeroCandidato:
               self.zera()
               break
    def zera(self):
        self.valor = ""
        self.saida.set(self.valor)
        
Exibe = exibe(3,[["JosédoPT",13,"PT"], ["Antoim da Farmacia",23,"AVANTE"], ["Zezé",45,"PSDB"]])
Visor = visor(root)
Btn0 = UrnaBtn(root,"0",30,140,20,3)
Btn1 = UrnaBtn(root,"1",0,200,5,3)
Btn2 = UrnaBtn(root,"2",50,200,5,3)
Btn3 = UrnaBtn(root,"3",100,200,5,3)
Btn4 = UrnaBtn(root,"4",150,200,5,3)
Btn5 = UrnaBtn(root,"5",0,260,5,3)
Btn6 = UrnaBtn(root,"6",50,260,5,3)
Btn7 = UrnaBtn(root,"7",100,260,5,3)
Btn8 = UrnaBtn(root,"8",150,260,5,3)
Btn9 = UrnaBtn(root,"9",30,320,20,3)
BtnConfirm = UrnaAction(root,"Confirmar",200,200,10,3,"green","finaliza")
BtnCancel = UrnaAction(root,"Corrigir",200,260,10,3,"red","limpa")
BtnBranco = UrnaAction(root,"Branco",200,320,10,3,"white","Anula")





root.mainloop()
