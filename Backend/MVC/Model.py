from flask import jsonify

lista = [

    {
        'id': 1,
        'item': 'laranja',
        'quantidade': '12',
        'unidade': 'un'
    },


    {
        'id': 2,
        'item': 'pao',
        'quantidade': '1',
        'unidade': 'kg'
    },


    {'id': 3,
     'item': 'file de frango',
     'quantidade': '4',
     'unidade': 'kg'
     },


    {'id': 4,
     'item': 'suco de uva',
     'quantidade': '3',
     'unidade': 'litros'
     }

]



class Model():
    global lista
    

    def jsonReturn():
        return lista

    def visualizar_item(item_id):
        cont = 0
        for i in lista:
            if i['id'] == item_id:
                return i
            elif i['id'] != item_id:
                cont = cont + 1
            if cont == len(lista):
                return 'Esse id não pertence a lista!'

    def adicionar_item(nome, quantidade, unidade):
        lista_id = len(lista) + 1
        nome = nome
        quantidade = quantidade
        unidade = unidade
        item = {'id':lista_id,
                'item':nome,
                'quantidade':quantidade,
                'unidade':unidade
                }
        lista.append(item)
        return 'Item adicionado a lista com sucesso!'

    def excluir_item(item_id):
        item_id = int(item_id)
        print(type(item_id))
        cont = 0
        for i in lista:
            if i['id'] == item_id:
                lista.pop(item_id - 1)
                return 'Item excluido!'
            elif i['id'] != item_id:
                cont = cont + 1
            if cont == len(lista):
                print(cont)
                return 'Esse id nao pertence a lista!'

    def atualizar_item(item_id, nome, quantidade, unidade):
        id = int(item_id)
        no = nome
        quant = quantidade
        uni = unidade
        item = {
            'id': id,
            'item': no,
            'quantidade': quant,
            'unidade': uni
        }
        for i in lista:
            if i['id'] == item['id']:
                i.update(item)
        return 'Atualizado com sucesso!'

