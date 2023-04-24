import asyncio

class Banco:
    def __init__(self, saldo):
        self.saldo = 100
    
    async def sacar(self, valor1):
        await asyncio.sleep(1)
        self.saldo -= valor1

    async def depositar(self, valor2):
        await asyncio.sleep(1)
        self.saldo += valor2
    
    def getSaldo(self):
        return self.saldo


async def main():
    banco = Banco()
    depositar100 = await asyncio.gather(banco.depositar(100))
    depositar50 = await asyncio.gather(20 * banco.depositar(50))
    depositar20 = await asyncio.gather(60 * banco.depositar(20))
    sacar50 = await asyncio.gather(20 * banco.sacar(50))
    sacar20 = await asyncio.gather(60 * banco.sacar(20))
    sacar100 = await asyncio.gather(40 * banco.sacar(100))

    tareas = []
    for saldo in depositar100 + depositar20 + depositar50:
        tareas.append(asyncio.create_task(banco.depositar(saldo)))
    await asyncio.gather(*tareas)
    for saldo in sacar50 + sacar20 + sacar100:
        tareas.append(asyncio.create_task(banco.sacar(saldo)))
    await asyncio.gather(*tareas)
    print(f'Saldo final: {banco.getSaldo()}')