import numpy as np

class Grafo:

      def __init__(self ,iteravel, **kwargs):
            self.__iteravel = iteravel
            self.__ponderado = kwargs.get('ponderado', False)
            self.__direcionado = kwargs.get('direcionado', False)
            self.__dicionario = self._construtor_dicionario(self.__iteravel)
            self.__dicionario = self._construtor_adj()

      def _matriz_print(self):
            for indice, value in enumerate(self._lista_vertices(self.__dicionario)):
                  if indice== 0:
                        print(end = "     ")
                  print(value, end = " ")
            print()
            for indice, value in enumerate(self._lista_vertices(self.__dicionario)): 
                  print(f'{value} ', end = " ")
                  print(self._matriz(self.__iteravel)[indice])
            return ""
      
      def _matriz(self, iteravel):
            lista = self._lista_vertices(self.__dicionario)
            self.__vertices = len(lista)
            self.__matriz_adj = np.zeros((self.__vertices, self.__vertices), dtype = int)

            if not self.__ponderado and self.__direcionado:
                  for i, j  in self.__iteravel:
                        self.__matriz_adj [lista.index(i)][lista.index(j)] = 1
                  return self.__matriz_adj
                  
            elif self.__ponderado and self.__direcionado:
                  for i, j, k  in self.__iteravel:
                        self.__matriz_adj [i][j] = k          
                  return self.__matriz_adj
         
            elif not self.__ponderado and not self.__direcionado:
                  for i, j in self.__iteravel:
                        self.__matriz_adj [lista.index(i)][lista.index(j)] = 1
                        self.__matriz_adj [lista.index(j)][lista.index(i)] = 1                
                  return self.__matriz_adj          
            else:
                  for i, j, k  in self.__iteravel:
                         self.__matriz_adj [lista.index(i)][lista.index(j)] = k
                         self.__matriz_adj [lista.index(j)][lista.index(i)] = k             
                  return self.__matriz_adj
            
      def adjacencia(self):
            result = ""
            for i,j in self.__dicionario.items():
                  self.__dicionario[i].sort()
                  result += f"{i}: {j}" + '\n'
            return result

      def __len__(self):
                  tamanho = 0
                  for i in self.__dicionario.keys():
                       tamanho += 1
                  return tamanho

      def _construtor_dicionario(self, iteravel):
                  dicionario = dict()
                  if self.__ponderado:
                        for i, j, k in self.__iteravel:
                              if i not in dicionario:
                                    dicionario[i] = list()
                              if j not in dicionario:
                                    dicionario[j] = list()
                  else:
                        for i, j in self.__iteravel:
                              if i not in dicionario:
                                    dicionario[i] = list()
                              if j not in dicionario:
                                    dicionario[j] = list()
                  return dicionario
            
      def _construtor_adj(self):
                  dicionario = self.__dicionario
                  if self.__ponderado:
                         for i, j, k in self.__iteravel:
                              if not self.__direcionado: 
                                    tupla_1 = (j, k)
                                    tupla_2 = (i, k)
                                    dicionario[i].append(tupla_1)
                                    dicionario[j].append(tupla_2)
                              else:
                                    tupla = (j, k)
                                    dicionario[i].append(tupla)                 
                  else:                  
                        for i, j in self.__iteravel:
                              if not self.__direcionado:
                                          dicionario[i].append(j)
                                          dicionario[j].append(i)
                              else:
                                          dicionario[i].append(j)
                  return dicionario

      def __contains__(self, vertice):
                  for i in self.__dicionario.keys():
                        if i == vertice:
                              return True
                  return False

      def add_vertice(self, vertice):
                  self.__dicionario[vertice]  = list()

      def add_aresta(self, aresta):
                  lista = list(self.__iteravel)
                  lista.append(aresta)
                  self.__iteravel = tuple(lista)
                  self.__dicionario = self._construtor_dicionario(self.__iteravel)
                  self._construtor_adj()

      def _find(self, lista, elem):
                  for i in lista:
                        if i == elem:
                              return True
                  return False

      def vertices_ligados(self, vertice_1, vertice_2):
                  return self._find(self.__dicionario[vertice_1], vertice_2)

      def grau_entrada(self, vertice):
                  if self.__contains__(vertice):
                        if not self.__direcionado:
                              return len(self.__dicionario[vertice])
                        else:
                              grau = 0
                              for chave, valor in self.__dicionario.items():
                                   if vertice !=  chave:
                                         if self.__ponderado:
                                               for i in range(len(valor)): 
                                                     if valor[i][0] == vertice:
                                                           grau += 1
                                         else:
                                                if self._find(valor, vertice):
                                                      grau += 1
                              return grau
                  raise ValueError(f"O vértice {vertice} não faz parte o grafo")

      def grau_saida(self, vertice):
                  if self.__contains__(vertice):
                        return len(self.__dicionario[vertice])
                  raise ValueError(f"O vértice {vertice} não faz parte o grafo")

      def adjacentes(self, vertice):
                  return self.__dicionario[vertice]

      def menor_aresta(self):
                  if self.__ponderado:
                        menor = self.__iteravel[0][2]
                        for i in range(1, len(self.__iteravel)):
                              if self.__iteravel[i][2] < menor:
                                    menor = self.__iteravel[i][2]
                        return menor
                  raise ValueError(f"Erro, grafo não ponderado!")

      def maior_aresta(self):
                  if self.__ponderado:
                        maior = self.__iteravel[0][2]
                        for i in range(1, len(self.__iteravel)):
                              if self.__iteravel[i][2] > maior:
                                    maior = self.__iteravel[i][2]
                        return maior
                  raise ValueError(f"Erro, grafo não ponderado!")

      def _lista_vertices(self, dicionario):
                  lista = list()
                  for i in dicionario.keys():
                        lista.append(i)
                  return lista

      def busca_largura(self, vertice):
                  if self.__contains__(vertice):
                        lista = self._lista_vertices(self.__dicionario)
                        marcado = [False] * self.__len__()
                        fila = list()
                        fila.append(vertice)
                        marcado[lista.index(vertice)] = True
                        while fila:
                              v = fila.pop(0)
                              print(v, end = " ")
                              for i in self.__dicionario[v]:
                                    if not marcado[lista.index(i)]:  
                                          if self.__ponderado:
                                                fila.append(i[0])
                                          else:
                                                fila.append(i)
                                          marcado[lista.index(i)] = True
                  else:
                        raise ValueError(f"O vértice {vertice} não faz parte o grafo")
      
      def busca_profundidade(self, vertice):
                  if self.__contains__(vertice):
                        marcado = [False] * self.__len__()
                        self._busca_aux(vertice, marcado)
                  else:
                        raise ValueError(f"O vértice {vertice} não faz parte o grafo")
                  
      def _busca_aux(self, vertice, marcado):
                  lista = self._lista_vertices(self.__dicionario)
                  marcado[lista.index(vertice)] = True
                  print(vertice, end = " ")
                  for i in self.__dicionario:
                        if self.__ponderado:
                              if not marcado[lista.index(j[0])]:
                                    self._busca_aux(i[0], marcado)
                        else:
                              if not marcado[lista.index(i)] :
                                    self._busca_aux(i, marcado)

class Lista(Grafo):

      def __init__(self, iteravel, **kwargs):
            self.__iteravel = iteravel
            self.__ponderado = kwargs.get('ponderado', False)
            self.__direcionado = kwargs.get('direcionado', False)
            super().__init__(iteravel, **kwargs)

      def grafo_matriz(self):
            print(Matriz(self.__iteravel, ponderado = self.__ponderado, direcionado = self.__direcionado).__str__())

      def __str__(self):
            if not self.__ponderado and self.__direcionado:
                  print('-=-=-= Lista Adjacência (Sem Pesos) e Grafo Direcionado -=-=-=')
                  print()
                  return(self.adjacencia())
                             
            elif self.__ponderado and self.__direcionado:
                  print('-=-=-= Lista Adjacência (Com Pesos) e Grafo Direcionado -=-=-=')
                  print()
                  return(self.adjacencia())
                   
            elif not self.__ponderado and not self.__direcionado:
                  print('-=-=-= Lista Adjacência (Sem Pesos) e Grafo Não Direcionado -=-=-=')
                  print()
                  return(self.adjacencia())
                         
            else:
                  print('-=-=-= Lista Adjacência (Com Pesos) e Grafo Não Direcionado -=-=-=')
                  print()
                  return(self.adjacencia()) 
                   
      def __repr__(self):
            return 'Grafo_Lista({}), ponderado = {}, direcionado = {}'.format(self.__iteravel, self.__ponderado, self.__direcionado)
      
class Matriz(Grafo):

      def __init__(self, iteravel, **kwargs):
            self.__iteravel = iteravel
            self.__ponderado = kwargs.get('ponderado', False)
            self.__direcionado = kwargs.get('direcionado', False)
            super().__init__(iteravel, **kwargs)

      def grafo_lista(self):
            print(Lista(self.__iteravel, ponderado = self.__ponderado, direcionado = self.__direcionado).__str__())
              
      def __str__(self):
            if not self.__ponderado and self.__direcionado:
                  print('-=-=-= Lista Adjacência (Sem Pesos) e Grafo Direcionado -=-=-=')
                  print()
                  return "{}".format(self._matriz_print())
            
            elif self.__ponderado and self.__direcionado:
                  print('-=-=-= Lista Adjacência (Com Pesos) e Grafo Direcionado -=-=-=')
                  print()
                  return "{}".format(self._matriz_print())
                   
            elif not self.__ponderado and not self.__direcionado:
                  print('-=-=-= Lista Adjacência (Sem Pesos) e Grafo Não Direcionado -=-=-=')
                  print()
                  return "{}".format(self._matriz_print())
                         
            else:
                  print('-=-=-= Lista Adjacência (Com Pesos) e Grafo Não Direcionado -=-=-=')
                  print()
                  return "{}".format(self._matriz_print())
                   
      def __repr__(self):
            return 'Grafo_Matriz({}), ponderado = {}, direcionado = {}'.format(self.__iteravel, self.__ponderado, self.__direcionado)
      
if __name__ == "__main__":
      
      x = Lista(((1, 3), (2, 1), (4, 2), (3, 3)), ponderado = False, direcionado = True)
      y = Matriz(((0, 1, 4), (2, 1, 3), (0, 2, 2), (0, 3, 1), (4, 2, 9)), ponderado = True, direcionado = True)
      a = Lista(((0, 1), (2, 1), (0, 2), (0, 3), (4, 2)), ponderado = False, direcionado = False)
      b = Matriz(((0, 1, 4), (2, 1, 3), (0, 2, 2), (0, 3, 1), (4, 2, 9)), ponderado = True, direcionado = False)
      h = Lista(((1, 2), (1, 3), (2, 4), (4, 5), (4, 6), (6, 5), (6, 7), (7, 5), (7, 8), (6, 8)), ponderado = False, direcionado = False)
