from flask import Flask, jsonify, request

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as sql_session

import psycopg2

from datetime import datetime

app = Flask(__name__) # Inicializa a aplicação

def conectar_db():
    con = psycopg2.connect(host='localhost', database='alunos', user='postgres', password='pgs2022')
    return con

Base = declarative_base(conectar_db())


def criar_tb(sql):
    con = conectar_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

sql = '''CREATE TABLE IF NOT EXISTS ALUNO (
        RA SERIAL NOT NULL,
        NOME VARCHAR(255) NOT NULL,
        END_EMAIL VARCHAR(255) NOT NULL,
        CURSO VARCHAR(255) NOT NULL,
        TURMA VARCHAR(500) NOT NULL,
        CONSTRAINT RA_KEY PRIMARY KEY(RA));
        '''

class ALN(Base):
    __tablename__ = 'ALUNO'
    id = Column('RA', Integer, primary_key=True)
    nome = Column('NOME',String(255), nullable=False)
    end_email = Column('END_EMAIL', String(255), nullable=False)
    curso = Column('CURSO', String(255), nullable=False)
    turma = Column('TURMA', Text)

    def __init__(self, nome, end_email, curso, turma):
        self.nome = nome
        self.end_email = end_email
        self.curso = curso
        self.turma = turma


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

@app.route('/adicionar', methods=['POST'])
def adicionar():
  if request.method == 'POST':
    nome = request.args.get('nome')
    ra = request.args.get('ra')
    email = request.args.get('email')
    curso = request.args.get('curso')
    turma = request.args.get('turma')

    if (nome == '') or (email == '') or (curso == '') or (turma == '') or (ra == ''):
      try:
        return jsonify("Está faltando dados!")
      except Exception as ex:
                return jsonify({"status":"ERRO", "msg":str(ex)})
    else:
      sql = '''
      INSERT into msg(ra, nome, end_email, curso, turma)
      values('{}', '{}', '{}', '{}', '{}');
      '''.format( ra, nome, email, curso, turma )
      inserir_db(sql)
      return jsonify("Enviado com sucesso!")

@app.route('/deletar/<int:ra>' methods= ['DELETE'])
def deletar(ra):
  if request.method == 'DELETE':
    


if __name__ == '__main__':
  app.run(host= 'localhost', port= 9001, debug=True) # Executa a aplicação