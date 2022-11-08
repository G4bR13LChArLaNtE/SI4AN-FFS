class Model():

    def tab_get(id):
        tabela = ''
        if id >= 1 and id < 10:
            tabela = '/tabela1'
        elif id >= 10:
            tabela = '/tabela2'

        return tabela