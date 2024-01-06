from pydantic import BaseModel

class ImputationsEspeces(BaseModel):
    IdImputation: int
    IdCompteEspece: int
    Montant: float
    Sens: str
    DateImputation: str  # Assuming DateImputation is a string for simplicity
    IdDateImputation: int
    IdSDBCompte: int
    DateValeur: str  # Assuming DateValeur is a string for simplicity
    IdDateValeur: int
    Nature: str
    Etat: str
    DateEtat: str  # Assuming DateEtat is a string for simplicity
    libelle: str