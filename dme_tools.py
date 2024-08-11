from cryptography.fernet import Fernet
from os import listdir, remove, chdir
from os.path import isdir, dirname, abspath
from sys import argv


class EncryptionTools:
    @staticmethod
    def loadKey(fileName: str) -> bytes:
        return open(fileName, 'rb').read()

    @staticmethod
    def generateKey(fileName: str = 'secret') -> None:
        dirContent = listdir()
        filePath = fileName + '.catsound'
        if filePath in dirContent:
            raise FileExistsError('There already exists a key with this name. Provide a different name or move the existing key somewhere else')
        key = Fernet.generate_key()
        with open(filePath, 'wb') as keyFile:
            keyFile.write(key)
    
    @staticmethod
    def encryptFile(fileName: str, f: Fernet, destructive: bool = True) -> None:
        with open(fileName, 'rb') as file:
            originalFile = file.read()
        
        encryptedFileContents = f.encrypt(originalFile)
        encryptedPath = fileName + '.meow'

        with open(encryptedPath, 'wb') as encryptedFile:
            encryptedFile.write(encryptedFileContents)
        
        print(f'{fileName} was successfully encrypted', end='')

        if destructive:
            remove(fileName)
            print(' and the original file was deleted')
        else:
            print()

    
    @staticmethod
    def encryptFiles(f: Fernet, files: list[str], destructive: bool = True) -> None:
        for i in files:
            if isdir(i):
                dirContents = [i + '\\' + file for file in listdir(i)]
                EncryptionTools.encryptFiles(f, dirContents, destructive)
            else:
                if not i.endswith('.meow'):
                    EncryptionTools.encryptFile(i, f, destructive)

    @staticmethod
    def decryptFile(fileName: str, f: Fernet, destructive: bool = True) -> None:
        with open(fileName, 'rb') as encryptedFile:
            encryptedFileContents = encryptedFile.read()
        
        decryptedFileContents = f.decrypt(encryptedFileContents)
        fileName = fileName.rsplit('.', 1)[0]

        with open(fileName, 'wb') as decryptedFile:
            decryptedFile.write(decryptedFileContents)
        
        print(f'{fileName} was successfully decrypted', end='')

        if destructive:
            remove(fileName + '.meow')
            print(' and the original file was deleted')
        else:
            print()

    @staticmethod
    def decryptFiles(f: Fernet, files: list[str], destructive: bool = True) -> None:
        for i in files:
            if isdir(i):
                dirContents = [i + '\\' + file for file in listdir(i)]
                EncryptionTools.decryptFiles(f, dirContents, destructive)
            else:
                if i.endswith('.meow'):
                    EncryptionTools.decryptFile(i, f, destructive)
        

def main():
    EncryptionTools.generateKey()
    key = EncryptionTools.loadKey('secret.catsound')
    f = Fernet(key)
    EncryptionTools.encryptFiles(f, ['dot-test'])
    input()
    EncryptionTools.decryptFiles(f, ['dot-test'])
    

if __name__ == '__main__':
    main()
