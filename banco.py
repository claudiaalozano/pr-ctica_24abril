
import concurrent.futures

class Banco:
    def __init__(self, saldo):
        self.saldo = saldo
    
    async def sacar(self, valor1):
        self.saldo -= valor1

    async def depositar(self, valor2):
        self.saldo += valor2
    
    def getSaldo(self):
        print(f"El saldo es: {self.saldo} euros.")


def main():
    banco = Banco(100)
    depositar100= [100] * 40
    depositar50 = [50] * 20
    depositar20 = [20] * 60
    sacar50 = [50] * 20
    sacar20 = [20] * 60
    sacar100 = [100] * 40

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for saldo in depositar100 + depositar50 + depositar20:
            executor.submit(banco.depositar, saldo)
        for saldo in sacar50 + sacar20 + sacar100:
            executor.submit(banco.sacar, saldo)
    banco.getSaldo()


