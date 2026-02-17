import os
from cryptography.fernet import Fernet

files = []

Key = Fernet.generate_key() #chave 

with open("chave.key", "rb") as key:
    secretkey = key.read()

for file in os.listdir():
    if file == "arquivo1"  or file == "chave.key" or file == "arquivo2.py": # não inclua 
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

for file in files:
    with open(file,"r") as arquivo:
        conteudo = arquivo.read()
    conteudo_decrypted = Fernet(secretkey).decrypt(conteudo.encode())
    with open(file,"wb") as arquivo:
        arquivo.write(conteudo_decrypted)

