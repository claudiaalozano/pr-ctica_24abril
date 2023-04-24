import asyncio

class Banco:
    def __init__(self, saldo):
        self.saldo = saldo
    
    async def sacar(self, valor1):
        await asyncio.sleep(1)
        self.saldo -= valor1

    async def depositar(self, valor2):
        await asyncio.sleep(1)
        self.saldo += valor2
    
    def getSaldo(self):
        return self.saldo


async def main():
    banco = Banco(100)
    await asyncio.gather(40 * banco.depositar(100))
    await asyncio.gather(20 * banco.depositar(50))
    await asyncio.gather(60 * banco.depositar(20))
    await asyncio.gather(20 * banco.sacar(50))
    await asyncio.gather(60 * banco.sacar(20))
    await asyncio.gather(40 * banco.sacar(100))