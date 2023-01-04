
class Conta:
    def __init__(self,titular,saldo):

        self._titular = titular
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

conta1 = Conta("João", 200)
conta2 = Conta("Maria", 500)

print(conta1.get_saldo())
print(conta1.get_titular())

print(conta2.get_saldo())
print(conta2.get_titular())

