from abc import ABC, abstractmethod
import pickle

class DAO(ABC):
  @abstractmethod
  def __init__(self, nome_arquivo = ""):
    self.__nome_arquivo = nome_arquivo
    self.__object_cache = {} # dicionário genérico, vai servir para gravar clientes, produtos...
    try:
      self.__load()
    except FileNotFoundError:
      self.__dump()      

  def __load(self): # carrega o arquivo
    self.__object_cache = pickle.load(open(self.__nome_arquivo, 'rb')) #vai sobrescrever o cache

  def __dump(self): # o que vai ser gravado e onde
    pickle.dump(self.__object_cache, open(self.__nome_arquivo, 'wb'))

  def add(self, key, obj):
    self.__object_cache[key] = obj
    self.__dump() # grava no arquivo

  def get(self, key):
    try:
      return self.__object_cache[key]
    except KeyError:
      return None

  def remove(self, key):
    try:
      self.__object_cache.pop(key)
      self.__dump() # grava a alteração no arquivo
    except KeyError:
      pass

  def get_all(self): # retorna a lista de todos os valores
    return list(self.__object_cache.values())
