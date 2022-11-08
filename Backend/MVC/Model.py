from flask import jsonify

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as sql_session

import os

import psycopg2

from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

senha = os.environ.get('PASS')

def conectar_db():
    con = psycopg2.connect(host="localhost", user= "postgres", password = f"{senha}",database = "Item")
    return con

Base = declarative_base(conectar_db())


def criar_tb(sql):
    con = conectar_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

sql = '''CREATE TABLE IF NOT EXISTS ITEM (
        ID SERIAL NOT NULL,
        ITEM VARCHAR(255) NOT NULL,
        QUANTIDADE INT NOT NULL,
        UNIDADE VARCHAR(100) NOT NULL,
        CONSTRAINT ID_KEY PRIMARY KEY(ID));
        ''' 

class ITEM(Base):
    __tablename__ = 'ITEM'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    item = Column('ITEM',String(255), nullable=False)
    quantidade = Column('QUANTIDADE', Integer, nullable=False)
    unidade = Column('UNIDADE',String(100), nullable=False)

    def __init__(self, item, quantidade, unidade):
        self.item = item
        self.quantidade = quantidade
        self.unidade = unidade


criar_tb(sql)

def inserir_db(sql):
    con = conectar_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

def consultar_db(sql):
  con = conectar_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros



class Model():

    def jsonReturn():
        sql = '''SELECT * FROM ITEM'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "item": l[1], "quantidade": l[2], "unidade": l[3] }
            itens.append(i)
        return itens

    def visualizar_item(item_id):
        sql = '''SELECT * FROM ITEM'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "item": l[1], "quantidade": l[2], "unidade": l[3] }
            itens.append(i)
        cont = 0
        for i in itens:
            if i['id'] == item_id:
                return i
            elif i['id'] != item_id:
                cont = cont + 1
            if cont == len(itens):
                return 'Esse id não pertence a lista de itens!'

    def adicionar_item(item, quantidade, unidade):
        item = item
        quantidade = quantidade
        unidade = unidade
        sql  = '''
        INSERT into item(item, quantidade, unidade)
        values( '{}', '{}', '{}');
        '''.format(item, quantidade, unidade)
        inserir_db(sql)
        return 'Item adicionado a lista com sucesso!'

    def excluir_item(item_id):
        sql = '''SELECT * FROM ITEM;'''
        itens = []
        i = {}
        result = consultar_db(sql)
        for l in result:
            i = {"id": l[0], "item": l[1], "quantidade": l[2], "unidade": l[3] }
            itens.append(i)
        item_id = int(item_id)
        cont = 0
        for i in itens:
            if i['id'] == item_id:
                sql = '''
                Delete from item where id = {};
                '''.format(item_id)
                inserir_db(sql)
                return 'Item excluido com sucesso!'
            elif i['id'] != item_id:
                cont = cont + 1
            if cont == len(itens):
                return 'Esse id não pertence a lista de itens!'

    def atualizar_item(item_id, nome, quantidade, unidade):
        sql = '''
        UPDATE item SET item='{}', quantidade='{}', unidade='{}'
        WHERE id={};
        '''.format(nome, quantidade, unidade, item_id)
        inserir_db(sql)
        return 'Atualizado com sucesso!'

