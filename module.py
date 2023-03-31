class Versenyzo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.szul:int = int(v[1])
        self.rajtszam:str = v[2]
        self.nem:bool = v[3] == 'f'
        self.kategoria:str = v[4]
        self.osszido:int = 0
        for i in range(5, len(v)):
            opm:list[str] = v[i].split(':')
            o:int = int(opm[0])
            p:int = int(opm[1])
            m:int = int(opm[2])
            self.osszido += o * 3600 + p * 60 + m