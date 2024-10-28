# Como usar

## Bibliotecas usadas
fastapi
Union
pyMongo

### Como instalar as Bibliotecas
```sh
  # insall fastapi
  pip3 install fastapi

  #install unicron
  pip3 install "uvicorn[standard]"

  #install pymongo
  pip3 install pyMongo


  #Rodar a api
  uvicorn app:app --reload
````

### Exemplo de request para salvar uma mensagem
```json
    {
      "historyId": "123456",
      "parameterSistemaId": "sistema-01",
      "sistema": "IPVA",
      "deUsusario": "user001",
      "paraUsuario": "lpetrolli",
      "perfil": "admin",
      "assunto": "Atualização do Sistema",
      "mensagem": "Houve uma atualização importante no sistema.",
      "tipoMensagensId": 1,
      "mensagensParametros": "parametros-mensagem",
      "mensagemAlerta": true,
      "statusMensagem": true,
      "apresentacaoApp": false,
      "qtdDiasApresentacao": 7,
      "emailsAdicionais": "email@example.com",
      "numeroIdentificacao": "AB123456",
      "status": "nova",
      "iconeClass": "icon-update",
      "tipoMensagens": 1,
      "documento": [
        {
          "url_arquivo": "https://example.com/documento.pdf"
        }
      ]
    }
```