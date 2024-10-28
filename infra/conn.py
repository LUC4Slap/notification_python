from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class GetMensagens:
    def __init__(self):
        self.cliente = MongoClient("mongodb://localhost:27017/notificacoes") # PARA RODAR NO LOCALHOST
        # self.password = os.getenv("PASSWORD_DB")
        # SE FOR RODAR NO LOCAL COMENTAR A LINHA DE BAIXO
        # self.cliente = MongoClient(f"mongodb+srv://lucasalmeida:{self.password}@radar-pt.3rljncc.mongodb.net/")
        self.db = self.cliente["notificacoes"]
        self.collection = self.db.mensagens
        self.results = None
        self.results_array = []

    def getNorificacoesDB(self, user: str, sistema: str):
        print(user, sistema)
        # query
        pipeline = [
            {
                "$match": {
                    "sistema": sistema.upper(),
                    "paraUsuario": user
                }
            },
            {
                "$sort": {
                    "dataInclusao": -1
                }
            },
            {
                "$group": {
                    "_id": {
                        "sistema": "$sistema",
                        "paraUsuario": "$paraUsuario"
                    },
                    "latest_record": {
                        "$first": "$$ROOT"  # Mantém o primeiro documento para cada grupo de 'sistema' e 'paraUsuario'
                    }
                }
            },
            {
                "$replaceRoot": {
                    "newRoot": "$latest_record"  # Substitui a raiz pelo último registro
                }
            }
        ]
        print(pipeline)
        try:
            self.results = list(self.collection.aggregate(pipeline))
        except Exception as error:
            print("erro para consultar")
            print(error)

    def returnDB(self, user: str, sistema: str):
      self.getNorificacoesDB(user, sistema)
      print(self.results)
      self.results_array = []
      for doc in self.results:
          self.results_array.append(doc)
      return self.results_array

    def insert_message(self, mensagem_data):
        result = self.collection.insert_one(mensagem_data)
        return result
