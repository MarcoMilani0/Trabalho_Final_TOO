from model.carga import ArrozEmCasca, ArrozEnsacado, PaletePiso


class CargaFactory:

    __TIPOS = {
        "casca": ArrozEmCasca,
        "ensacado": ArrozEnsacado,
        "palete": PaletePiso,
    }

    @staticmethod
    def criar(tipo, **dados):
        classe = CargaFactory.__TIPOS.get(tipo)
        if classe is None:
            validos = ", ".join(CargaFactory.__TIPOS)
            raise ValueError(f"Tipo de carga desconhecido: '{tipo}'. Tipos válidos: {validos}")
        return classe(**dados)