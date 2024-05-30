from cryptography.fernet import Fernet
from os import listdir


class EncryptionTools:
    def loadKey(fileName: str) -> bytes:
        pass

    def generateKey(fileName: str = 'secret') -> None:
        dirContent = listdir()
        filePath = fileName + '.catsound'
        if filePath in dirContent:
            raise FileExistsError('There already exists a key with this name. Provide a different name or move the existing key somewhere else')
        key = Fernet.generate_key()
        with open(filePath, 'wb') as keyFile:
            keyFile.write(key)
    
    def encrypt(fileName: str) -> None:
        pass
        

def main():
    EncryptionTools.generateKey()

if __name__ == '__main__':
    main()
