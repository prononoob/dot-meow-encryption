from cryptography.fernet import Fernet
from os import listdir, remove


class EncryptionTools:
    def loadKey(fileName: str) -> bytes:
        return open(fileName, 'rb').read()

    def generateKey(fileName: str = 'secret') -> None:
        dirContent = listdir()
        filePath = fileName + '.catsound'
        if filePath in dirContent:
            raise FileExistsError('There already exists a key with this name. Provide a different name or move the existing key somewhere else')
        key = Fernet.generate_key()
        with open(filePath, 'wb') as keyFile:
            keyFile.write(key)
    
    def encryptFile(fileName: str, f: Fernet, destructive: bool = True) -> None:
        with open(fileName, 'rb') as file:
            originalFile = file.read()
        
        encryptedFileContents = f.encrypt(originalFile)
        encryptedPath = fileName + '.meow'

        with open(encryptedPath, 'wb') as encryptedFile:
            encryptedFile.write(encryptedFileContents)
        
        print(f'{fileName} was succesfully encrypted', end='')

        if destructive:
            remove(fileName)
            print(' and the original file was deleted')
        else:
            print()

    
    def encryptFiles(f: Fernet, files: list[str], destructive: bool = True) -> None:
        for i in files:
            EncryptionTools.encryptFile(i, f, destructive)

    def decryptFile(fileName:str, f: Fernet, destructive: bool = True) -> None:
        with open(fileName, 'rb') as encryptedFile:
            encryptedFileContents = encryptedFile.read()
        
        decryptedFileContents = f.decrypt(encryptedFileContents)
        fileName = fileName.rsplit('.', 1)[0]

        with open(fileName, 'wb') as decryptedFile:
            decryptedFile.write(decryptedFileContents)
        
        print(f'{fileName} was succesfully decrypted', end='')

        if destructive:
            remove(fileName + '.meow')
            print(' and the original file was deleted')
        else:
            print()
        

def main():
    EncryptionTools.generateKey()
    key = EncryptionTools.loadKey('secret.catsound')
    f = Fernet(key)
    # EncryptionTools.encryptFile('testFile.txt', f)
    # input()
    # EncryptionTools.decryptFile('testFile.txt.meow', f)
    EncryptionTools.encryptFiles(f, ['testFile.txt', 'testFile2.txt', 'testFile3.txt'])
    input()
    EncryptionTools.decryptFile('testFile.txt.meow', f)
    EncryptionTools.decryptFile('testFile2.txt.meow', f)
    EncryptionTools.decryptFile('testFile3.txt.meow', f)

if __name__ == '__main__':
    main()
