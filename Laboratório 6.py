import random

class Criptografia:

    def __init__(self, caracteres='ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%abcdefghijklmnopqrstuvwxyz'):
        self.caracteres = caracteres
       
    def criptografar(self, caracter, chave):
        '''método para criptografar um caracter de acordo com a chave passada'''
        self.caracter = caracter
        self.chave = int(chave)
        tamanho = len(self.caracteres)
        if caracter in self.caracteres:
            posicao = self.caracteres.index(caracter)
            if posicao + chave >= len(self.caracteres):
                return self.caracteres[(posicao+chave)%tamanho]
            else:
                return self.caracteres[posicao+chave]
        else:
            return self.caracter
        
    
    def descriptografar(self, caracter, chave):
        '''método para descriptografar um caracter de acordo com a chave passada'''
        self.caracter = caracter
        self.chave = int(chave)
        tamanho = len(self.caracteres)
        if caracter in self.caracteres:
            posicao = self.caracteres.index(caracter)
            if posicao + chave >= len(self.caracteres):
                return self.caracteres[(posicao-chave)%tamanho]
            else:
                return self.caracteres[posicao-chave]
        else:
            return self.caracter

    def criptografar_arquivo(self, file_name="", k=0):
        '''método para criptografar um arquivo texto e sobrescrevê-lo, agora, criptografado'''
        new_message = ""
        try:
            file = open(file_name, "r")
            file_extension = file_name.index(".")
            new_file_name = file_name[:file_extension] + "Cripto" + file_name[file_extension:]
            file_cripto = open(new_file_name, "w")
            for letter in file.read():
                new_letter = self.criptografar(letter, k)
                new_message += new_letter
            file_cripto.write(new_message)
            file.close()
            file_cripto.close()
            
            print("Procedimento de criptografia concluido.\nArquivo criptografado: {}".format(new_file_name))
        except FileNotFoundError:
            print("O arquivo não existe ou seu nome foi digitado incorretamente.")
        except IOError:
            print("Não foi possivel escrever no arquivo.")
        except TypeError:
            print("O valor de K está fora dos limites (-70 a 70)")
             
    def descriptografar_arquivo(self, file_name, k):
        '''método para descriptografar um arquivo .txt'''
        new_message = ""
        try:
            file = open(file_name, "r")
            if file_name.find("Cripto") > 0:
                file_pos_strCripto = file_name.index("Cripto")
                new_file_name = file_name[:file_pos_strCripto] + "Des" + file_name[
                    file_pos_strCripto].lower() + file_name[file_pos_strCripto + 1:]
            else:
                file_extension = file_name.index(".")
                new_file_name = file_name[:file_extension] + "Descripto" + file_name[file_extension:]
            file_descripto = open(new_file_name, 'w')
            for letter in file.read():
                new_letter = self.descriptografar(letter, k)
                new_message += new_letter
            file_descripto.write(new_message)
            file.close()
            file_descripto.close()
            print("Procedimento de descriptografia concluido.\nArquivo descriptografado: {}".format(new_file_name))
        except FileNotFoundError:
            print("O arquivo não existe ou seu nome foi digitado incorretamente.")
        
        except TypeError:
            print("O valor de K está fora dos limites (-70 a 70)")

     
    def sobreescrever_arquivo(self, file_name="", k=0):
        '''método para criptografar um arquivo texto e sobrescrevê-lo, agora, criptografado'''
        new_message = ""
        try:
            file = open(file_name, "r+")
            for letter in file.read():
                new_letter = self.criptografar(letter, k)
                new_message += new_letter
            file.seek(0)
            file.write(new_message)
            file.close()

            print(
                "Procedimento de sobrescrita de arquivo com criptografia concluido.\nArquivo criptografado: {}".format(
                    file_name))
        except FileNotFoundError:
            print("O arquivo não existe ou seu nome foi digitado incorretamente.")
        except IOError:
            print("Não foi possivel escrever no arquivo.")
        except TypeError:
            print("O valor de K está fora dos limites (-70 a 70)")
