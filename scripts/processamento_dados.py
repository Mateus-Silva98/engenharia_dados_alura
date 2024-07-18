class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados

    class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
                dict_temp = {}
                for old_key, value in old_dict.items():
                        dict_temp[key_mapping[old_key]] = value
                new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self.__get_columns()