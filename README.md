# A simple file encryptor

-----

This program allows you to generate a key, encrypt files anh decrypt them  

- Encrypted files have a '.meow' extension (hence the name)
- Key has a '.catsound' extension  

-----

# How to:
(I will make it simpler eventually)
- Make sure to install Tkinter
- Run 'pip install -r requirements.txt'
- For Graphical Interface
  - Run 'python dme_gui.py'
  - Generate Key button creates a file secret.catsound that contains an encryption key, the key has to be inside the same directory that the .py file are for the encryption to work
  - Encrypt/Decrypt buttons do what they say using the beformentioned key
  - After encrypting/decrypting move the generated key somewhere safe
  - If you want to decrypt previously encrypted files, move the secret file back to the encrypted dir and hit Decrypt button
- For Command Line Interface
  - coming soon...

-----
# TODO:
- [x] add multiple file encryption and decryption
- [x] improve exception handling
- [x] add a GUI
- [ ] add a operational CLI
