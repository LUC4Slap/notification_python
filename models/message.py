from typing import List, Optional
from pydantic import BaseModel, Field
from models.documento import Documento
from datetime import datetime

class Mensagem(BaseModel):
  historyId: str
  parameterSistemaId: str
  sistema: str
  deUsusario: str
  paraUsuario: str
  perfil: str
  assunto: str
  mensagem: str
  dataInclusao: datetime = Field(default_factory=datetime.now)
  dataEnvio: datetime = Field(default_factory=datetime.now)
  dataLeitura: Optional[str] = None
  tipoMensagensId: int
  mensagensParametros: str
  mensagemAlerta: bool
  statusMensagem: bool
  apresentacaoApp: bool
  qtdDiasApresentacao: int
  emailsAdicionais: str
  numeroIdentificacao: str
  status: str
  iconeClass: str
  tipoMensagens: int
  documento: Optional[List[Documento]] = None
