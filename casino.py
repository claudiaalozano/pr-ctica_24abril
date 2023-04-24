import multiprocessing
import random
import time

    
def apostar(numero,saldo):
    saldo = 1000
    
    numero = random.randint(1,36)
    while True:
        saldo -=10
        if random.randint(1,36) == numero:
            saldo += 360
        if saldo<0:
            break
    

def apostar_par_impar(par_impar, saldo):
    saldo = 1000
    
    
    par_impar = random.randint(1,36)
    while True:
        saldo-=10
        if par_impar == "par" and random.randint(1,36)%2 == 0:
            saldo += 20
        elif par_impar == "impar" and random.randint(1,36)%2 == 1:
            saldo += 20
        if saldo<0:
            break
        

def jugar_martingala(saldo, numero):
    saldo = 1000
    
    numero = random.randint(1,36)
    c = random.randint(1,36)
    
    apuesta=10
    while True:
        saldo = saldo- apuesta
        if c == numero:
            saldo += apuesta*36
            apuesta=10
        else:
            apuesta*=2
        if saldo<0:
            break    
            

def jugar():
    saldo = 1000
    
    numero = random.randint(1,36)

    hilos=[]
    for i in range(4):
        numero= random.randint(1,36)
        hilo = multiprocessing.Process(target=apostar, args=(numero,saldo))

        hilos.append(hilo)

    for i in range(4, 8):
        par_impar = random.randint(1,36)
        hilo = multiprocessing.Process(target=apostar_par_impar, args=(par_impar,saldo))

        hilos.append(hilo)

    for i in range(8, 12):
        hilo = multiprocessing.Process(target=jugar_martingala, args=(saldo,))

        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    while True:
        numero = random.randint(1,36)
        if numero == 0:
            banca += sum(saldo)
        ganacias = [ 0 for _ in range(12)]
        for i in range(4):
            if random.randint(1,36) ==numero:
                ganacias[i] += 360