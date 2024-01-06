from pydantic import BaseModel

class ComptesEspece(BaseModel):
    IdCompte: int
    IdClient: int
    IdDepositaire: int
    DateCreation: str  # Assuming DateCreation is a string for simplicity
    Web: str
    Etat: str