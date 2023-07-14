# ChatGPT Api Flask Frontend

Não esqueça de dar uma estrela ao repositório para mostrar seu apoio e reconhecimento!

---

Para pedidos e sugestões, poderá usar a aba issues, neste repositório, ou me enviar um e-mail neste endereço:

filipe@filipeteixeira.com.br

---

## Instalação:

```
git clone https://github.com/shuantsu/chatgpt-api-frontend.git
cd chatgpt-api-frontend
python3 -m venv venv
```

---

Se estiver no Windows, ative o ambiente virtual com esse comando:
```
venv\Scripts\activate
```
Se estiver no Linux, ative o ambiente virtual com esse comando:
```
source venv/bin/activate
```

---

Instale os módulos no ambiente virtual.

```
python3 -m pip install -r requirements.txt
```

---

## Crie um arquivo de configurações com as suas credenciais, nesse formato:

`config.json` :
```
{
    "openai.organization": "org-XXXXXXXXXXXXXXXXXXXX",
    "openai.api_key": "sk-XXXXXXXXXXXXXXXXXXXX"
}
```


Para gerar a chave da API, acesse esse endereço:

https://platform.openai.com/account/api-keys

Para acessar a chave da Organização, copie desse endereço:

https://platform.openai.com/account/org-settings

---
## Rode o servidor local:
```
python3 app.py
```
---
O front estará acessivel na porta 5000 do localhost:

`http://127.0.0.1:5000`

---

Não esqueça de dar uma estrela ao repositório para mostrar seu apoio e reconhecimento!