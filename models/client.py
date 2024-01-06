from pydantic import BaseModel
class Client(BaseModel):
    IdPersonne: int
    IdClasse: int
    IdNatureIdt: int
    IdPays: int
    NatureClient: str
    Etat: str
    IdCategorieAvoir: int
    RaisonSociale: str
    Matricule: str