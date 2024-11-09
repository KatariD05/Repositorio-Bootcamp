class TarjetaCredito:

    todas_las_tarjetas = []

    def __init__(self, nombre_tarjeta, saldo_pagar, limite_credito, intereses):
        self.nombre_tarjeta = nombre_tarjeta
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.todas_las_tarjetas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self
    
    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f'{self.nombre_tarjeta} Saldo a pagar: {self.saldo_pagar}')
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def tarjetas_creadas(cls):
        for tarjeta in cls.todas_las_tarjetas:
            print(tarjeta.saldo_pagar, tarjeta.limite_credito, tarjeta.intereses)

Tarjeta1 = TarjetaCredito('tarjeta1', 0, 1000, 0.02)
Tarjeta2 = TarjetaCredito('tarjeta2', 0, 2000, 0.05)
Tarjeta3 = TarjetaCredito('tarjeta3', 0, 3000, 0.10)
Tarjeta4 = TarjetaCredito('tarjeta4', 0, 1500, 0.06)
Tarjeta5 = TarjetaCredito('tarjeta5', 0, 1200, 0.04)
Tarjeta6 = TarjetaCredito('tarjeta6', 0, 2500, 0.05)
Tarjeta7 = TarjetaCredito('tarjeta7', 0, 1500, 0.10)
Tarjeta8 = TarjetaCredito('tarjeta8', 0, 2200, 0.07)
Tarjeta9 = TarjetaCredito('tarjeta9', 0, 1000, 0.08)

TarjetaCredito.tarjetas_creadas()

class Usuario:

    def __init__(self, nombre, tarjetas):
        self.nombre = nombre
        self.tarjetas = tarjetas


    def hacer_compra(self, monto, tarjeta):  
        tarjeta.compra(monto)
        return self

    def pago(self, monto, tarjeta):
        tarjeta.pago(monto)
        return self

    def cobrar_interes(self, tarjeta):
        tarjeta.cobrar_interes()
        return self

    def mostrar_info_tarjeta(self, tarjeta):
        print(f'{tarjeta.nombre_tarjeta} Saldo a pagar: {tarjeta.saldo_pagar}')
        return self
    
    def mostrar_usuario(self, nombre):
        print(self.nombre)
        return self

Usuario1 = Usuario("lee", [Tarjeta1, Tarjeta2, Tarjeta3])
Usuario2 = Usuario("Min", [Tarjeta4, Tarjeta5, Tarjeta6])
Usuario3 = Usuario("Kim", [Tarjeta7, Tarjeta8, Tarjeta9])

Usuario1.mostrar_usuario(Usuario1).hacer_compra(500, Usuario1.tarjetas[0]).pago(300, Usuario1.tarjetas[0]).mostrar_info_tarjeta(Usuario1.tarjetas[0])
Usuario1.hacer_compra(700, Usuario1.tarjetas[1]).mostrar_info_tarjeta(Usuario1.tarjetas[1])
Usuario1.hacer_compra(3500, Usuario1.tarjetas[2]).mostrar_info_tarjeta(Usuario1.tarjetas[2])

Usuario2.mostrar_usuario(Usuario2).hacer_compra(300, Usuario2.tarjetas[0]).mostrar_info_tarjeta(Usuario2.tarjetas[0])
Usuario2.hacer_compra(100, Usuario2.tarjetas[1]).mostrar_info_tarjeta(Usuario2.tarjetas[1])
Usuario2.hacer_compra(2500, Usuario2.tarjetas[2]).mostrar_info_tarjeta(Usuario2.tarjetas[2])

Usuario3.mostrar_usuario(Usuario3).hacer_compra(800, Usuario3.tarjetas[0]).mostrar_info_tarjeta(Usuario3.tarjetas[0])
Usuario3.hacer_compra(400, Usuario3.tarjetas[1]).mostrar_info_tarjeta(Usuario3.tarjetas[1])
Usuario3.hacer_compra(3200, Usuario3.tarjetas[2]).mostrar_info_tarjeta(Usuario3.tarjetas[2])
