from tkinter import *
 
class Calculator:
 
    def __init__(self, master):
        self.master = master
        master.iconbitmap('logo-recortado.ico') 
        master.title("Calculator")
        master.geometry('200x250')
        self.miFrame=Frame(master)
        self.miFrame.pack()

        #--------------------- Inicializamos la pantalla -------------------------------
        self.numPantalla=StringVar()
        self.pantalla=Entry(self.miFrame, textvariable=self.numPantalla)
        self.pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
        self.pantalla.config(bg='black', fg='#03f943', justify='right')

        #--------------------- Inicializamos las variables globales a utilizar -----------
        self.operacion=''
        self.resultado=0
        self.reset_pantalla=True
        self.punto=True
        self.numero_inicio=0
        self.numPantalla.set(self.numero_inicio)

        self.num1=0
        self.contador_resta=0
        self.contador_multi=0
        self.contador_divi=0

        #--------------------- Creamos los botones -----------------------------------------
        botonR=Button(self.miFrame, text='√', width=3, command=lambda:self.raizCuadrada())
        botonCe=Button(self.miFrame, text='CE', width=3, command=lambda:self.tecla_ce())
        botonC=Button(self.miFrame, text='C', width=3, command=lambda:self.tecla_c())
        botonDiv=Button(self.miFrame, text='/', width=3, command=lambda:self.divi(self.numPantalla.get()))
        boton7=Button(self.miFrame, text='7', width=3, command=lambda:self.numPulsado('7'))
        boton8=Button(self.miFrame, text='8', width=3, command=lambda:self.numPulsado('8'))
        boton9=Button(self.miFrame, text='9', width=3, command=lambda:self.numPulsado('9'))
        botonMult=Button(self.miFrame, text='X', width=3, command=lambda:self.multi(self.numPantalla.get()))
        boton4=Button(self.miFrame, text='4', width=3, command=lambda:self.numPulsado('4'))
        boton5=Button(self.miFrame, text='5', width=3, command=lambda:self.numPulsado('5'))
        boton6=Button(self.miFrame, text='6', width=3, command=lambda:self.numPulsado('6'))
        botonRes=Button(self.miFrame, text='-', width=3, command=lambda:self.resta(self.numPantalla.get()))
        boton1=Button(self.miFrame, text='1', width=3, command=lambda:self.numPulsado('1'))
        boton2=Button(self.miFrame, text='2', width=3, command=lambda:self.numPulsado('2'))
        boton3=Button(self.miFrame, text='3', width=3, command=lambda:self.numPulsado('3'))
        botonSum=Button(self.miFrame, text='+', width=3, command=lambda:self.suma(self.numPantalla.get()))
        botonComa=Button(self.miFrame, text=',', width=3,  command=lambda:self.numPulsado('.'))
        botonCero=Button(self.miFrame, text='0', width=3, command=lambda:self.numPulsado('0'))
        botonIgual=Button(self.miFrame, text='=', width=8, command=lambda:self.igual())
        
        #-------------------- Colocamos los Botones --------------------------------------------

        botonR.grid(row=2, column=1)
        botonCe.grid(row=2, column=2)
        botonC.grid(row=2, column=3)
        botonDiv.grid(row=2, column=4)
        boton7.grid(row=3, column=1)
        boton8.grid(row=3, column=2)
        boton9.grid(row=3, column=3)
        botonMult.grid(row=3, column=4)
        boton4.grid(row=4, column=1)
        boton5.grid(row=4, column=2)
        boton6.grid(row=4, column=3)
        botonRes.grid(row=4, column=4)
        boton1.grid(row=5, column=1)
        boton2.grid(row=5, column=2)
        boton3.grid(row=5, column=3)
        botonSum.grid(row=5, column=4)
        botonComa.grid(row=6, column=1)
        botonCero.grid(row=6, column=2)
        botonIgual.grid(row=6, column=3, columnspan=4)

    #-------------------------- Creamos los métodos a llamar ----------------------------    

    def numPulsado(self, num):
               
        if self.reset_pantalla==True: # Si la pantalla está en posición de reset...
            # Si al inicio de la calculadora y se presiona la coma, el valor de num pasa a ser '0.' 
            if num == '.':
                num = '0.'
                # Ponemos la variable punto en False para que no volvamos a poner otro punto en la pantalla.
                self.punto = False
                # Mostramos el num en pantalla
            self.numPantalla.set(num)
            self.reset_pantalla=False # Ponemos la pantalla en posición of reset
        else: # Pantalla posición of reset
            # Si presionamos '.' y la variable punto está en False: num no tiene valor
            if num=='.' and self.punto==False:
                num=''
            # De lo contrario num tiene el valor de '.'
            elif num=='.' and self.punto==True:
                num='.'
                # Y ponemos la variable punto en False
                self.punto=False
            # Insertamos el valor de la pantalla más el valor de num
            self.numPantalla.set(self.numPantalla.get() + num)
        
    def raizCuadrada(self):
    
        try:
            if self.numPantalla.get().isdigit():
                num = int(self.numPantalla.get())
            else:
                num = float(self.numPantalla.get())
            self.resultado = num**0.5
            self.operacion='raiz'

            # Realizamos lo mismo para que no aparezcan decimales, si después de la coma son ceros.
            self.resultado = float(self.resultado)
            if self.resultado.is_integer():
                self.resultado = int(self.resultado)
            self.numPantalla.set(self.resultado)
            self.reset_pantalla=True
        except:
            self.numPantalla.set('Error')

    def suma(self, numP):
        
        try:
            if self.reset_pantalla==True: # Si la pantalla es True, la ponemos en False
                self.reset_pantalla=False
            self.punto=True # Ponemos punto en True para que después de presionar suma se pueda volver a poner decimales.

            if self.numPantalla.get().isdigit(): # Si en la pantalla hay solo número...
                num = int(numP) # Convertir en entero
            else:
                num = float(numP) # Si no en flotante
            self.resultado+=num
            self.operacion='suma' # Renombramos la variable operación con 'suma'
            self.reset_pantalla=True
            self.resultado = float(self.resultado) # Antes de usar el método is_interger(), convertimos el número en flotante para que no nos de una Excepción.
            # Para comprobar que un número es entero o flotante se usa la función is_interger(), que previamente lo hemos pasado a flotante, si el resultado después de la coma son 0, el número es entero y nos dará True.
            if self.resultado.is_integer():
                # Ahora lo converimos a entero.
                self.resultado = int(self.resultado)
            self.numPantalla.set(self.resultado) # El resultado lo insertamos en pantalla
        except:
            # En caso de alguna excepción, insertaremos en pantalla la palabre 'Error'
            self.numPantalla.set('Error')

   
    def resta(self, numP):
        
        try:
            self.punto=True
            if self.reset_pantalla==True:
                self.reset_pantalla=False
            if self.contador_resta==0: # Si el contador está a cero, el valor de resultado es el número pasado con numP

                if self.numPantalla.get().isdigit():
                    self.num1 = int(numP)
                    self.resultado=self.num1
                else:
                    self.num1 = float(numP)
                    self.resultado=self.num1

            else: # Si no...
                if self.contador_resta==1: # Si el contador es 1, resultado es el valor de num1 menos el valor de numP
                    if self.numPantalla.get().isdigit(): # Aquí seleccionamos si el resultado en entero o flotante
                        self.resultado=self.num1-int(numP)
                    else:
                        self.resultado=self.num1-float(numP)
                    
                else:
                    if self.numPantalla.get().isdigit():
                        self.resultado=int(self.resultado)-int(numP)
                    else:
                        self.resultado=float(self.resultado)-float(numP)
                self.numPantalla.set(self.resultado) # Mostramos el resultado en pantalla
                

            self.contador_resta=self.contador_resta+1 # al contador le sumamos 1
            self.operacion='resta'
            self.reset_pantalla=True
        except: # En esta excepción ponemos el contador en cero y la variable num1
            self.contador_resta=0
            self.num1=0
            self.numPantalla.set('Error')
    
    def multi(self, numP):

        try:
            self.punto=True
            if self.reset_pantalla==True:
                self.reset_pantalla=False
            if self.contador_multi==0:

                if self.numPantalla.get().isdigit():
                    self.num1 = int(numP)
                    self.resultado=self.num1
                else:
                    self.num1 = float(numP)
                    self.resultado=self.num1

            else:
                if self.contador_multi==1:
                    if self.numPantalla.get().isdigit():
                        self.resultado=self.num1*int(numP)
                    else:
                        self.resultado=self.num1*float(numP)
                    
                else:
                    if self.numPantalla.get().isdigit():
                        self.resultado=int(self.resultado)*int(numP)
                    else:
                        self.resultado=float(self.resultado)*float(numP)
                self.numPantalla.set(self.resultado)
                
            self.contador_multi=self.contador_multi+1
            self.operacion='multi'
            self.reset_pantalla=True

        except:
            self.contador_multi=0
            self.num1=0
            self.numPantalla.set('Error')

    def divi(self, numP):
      
        try:
            self.punto=True
            if self.reset_pantalla==True:
                self.reset_pantalla=False

            if self.contador_divi==0:
                if self.numPantalla.get().isdigit():
                    self.num1 = int(numP)
                    self.resultado=self.num1
                else:
                    self.num1 = float(numP)
                    self.resultado=self.num1

            else:
                if self.contador_divi==1:
                    if self.numPantalla.get().isdigit():
                        self.resultado=self.num1/int(numP)
                    else:
                        self.resultado=self.num1/float(numP)
                    
                else:
                    if self.numPantalla.get().isdigit():
                        self.resultado=int(self.resultado)/int(numP)
                    else:
                        self.resultado=float(self.resultado)/float(numP)
                self.resultado = float(self.resultado)
                if self.resultado.is_integer():
                    self.resultado = int(self.resultado)
                self.numPantalla.set(self.resultado)
                self.resultado=self.numPantalla.get()

            self.contador_divi=self.contador_divi+1
            self.operacion='divi'
            self.reset_pantalla=True

        except:
            self.contador_divi=0
            self.num1=0
            self.numPantalla.set('Error')

    
    def igual(self):
     
        try:
            if self.numPantalla.get().isdigit(): 
                # Convertimos la variable numero en entero o flotante según corresponda.
                numero = int(self.numPantalla.get())
            else:
                numero = float(self.numPantalla.get())

            if self.operacion=='suma':        
                resulSuma = self.resultado + numero
                resulSuma = float(resulSuma)
                if resulSuma.is_integer():
                    resulSuma = int(resulSuma)
                self.numPantalla.set(resulSuma)
                self.resultado=0
                self.punto=True
                self.reset_pantalla=True
                
            elif self.operacion=='resta':
                # La resta la metemos dentro de la variable resta
                resta = self.resultado-numero
                # La convertimos en flotante
                resta = float(resta)
                # La condicionamos a que si tiene como decimal 0, se convierta en entero.
                if resta.is_integer():
                    resta = int(resta)
                # Mostramos el resultado en pantalla.
                self.numPantalla.set(resta)
                self.resultado=0
                self.reset_pantalla=True
                self.contador_resta=0
            elif self.operacion=='multi':
                multi = self.resultado*numero
                multi = float(multi)
                if multi.is_integer():
                    multi = int(multi)
                self.numPantalla.set(multi)
                self.resultado=0
                self.reset_pantalla=True
                self.contador_multi=0
            elif self.operacion=='divi':
                divi = self.resultado/numero
                divi = float(divi)
                if divi.is_integer():
                    divi = int(divi)
                self.numPantalla.set(divi)
                self.resultado=0
                self.reset_pantalla=True
                self.contador_divi=0

        except:
            self.numPantalla.set('Error')
            self.contador_resta=0
            self.contador_multi=0
            self.contador_divi=0

    def tecla_c(self):
        
        self.contador_resta=0
        self.contador_multi=0
        self.contador_divi=0
        self.reset_pantalla=True
        self.punto=True
        self.resultado=0
        self.numPantalla.set('0')

    def tecla_ce(self):
        
        self.reset_pantalla=False
        self.punto=True
        self.numPantalla.set('')


raiz = Tk()
my_calculator = Calculator(raiz)
raiz.mainloop()