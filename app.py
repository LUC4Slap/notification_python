from typing import Union
from fastapi import FastAPI, HTTPException
from models.message import Mensagem
from infra.conn import GetMensagens
from typing import List, Optional
from pymongo.errors import PyMongoError

tags_metadata = [
    {
        "name": "repots",
        "description": "Endpoint para retornar a ultima pontuação do rastreador.",
    },
]


app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    swagger_ui_parameters={"syntaxHighlight": 'obsidian'})
mensagemRepository = GetMensagens()


@app.get("/mensagens")
def get_messages(usuario: Optional[str] = None, sistema: Optional[str] = None) -> List[Mensagem]:
    notificacoes = mensagemRepository.returnDB(user=usuario, sistema=sistema)
    return notificacoes

@app.post("/add_mensagem", response_model=Mensagem)
def create_message(mensagem: Mensagem) -> Mensagem:
    try:
        # Insere a mensagem no banco de dados
        mensagem_dict = mensagem.dict()  # Converte o Pydantic model para um dicionário
        result = mensagemRepository.insert_message(mensagem_dict)

        # Retorna a mensagem com o ID inserido
        mensagem_dict["_id"] = str(result.inserted_id)  # Converte o ObjectId para string
        return mensagem_dict
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao inserir no banco de dados: {str(e)}")
