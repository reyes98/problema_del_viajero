class Grafo(object):

    def __init__(self, grafo=None):
        
        if grafo == None:
            grafo = {}
        self.__grafo = grafo

    def vertices(self):
        # retorna los vertices del grafo
        return list(self.__grafo.keys())

    def aristas(self):
        # rotorna las aristas del grafo
        return self.__generar_aristas()

    def add_vertice(self, vertice):
    	# Adiciona un vertice al grafo
        if vertice not in self.__grafo:
            self.__grafo[vertice] = []

    def add_arista(self, arista):
        """ asume que la arista es de tipo set, tuple or list; 
            entre dos vertices pueden haber muchas aristas! 
        """
        arista = set(arista)
        (vertice1, vertice2) = tuple(arista)
        if vertice1 in self.__grafo:
            self.__grafo[vertice1].append(vertice2)
            self.__grafo[vertice2].append(vertice1)
        else:
            self.__grafo[vertice1] = [vertice2]
            self.__grafo[vertice2] = [vertice1]

    def __generar_aristas(self):
        """ metodo estatico que genera las aristas del 
            grafo "grafo". aristas son representada con sets 
        """
        aristas = []
        for vertice in self.__grafo:
            for adyacente in self.__grafo[vertice]:
                if {adyacente, vertice} not in aristas:
                    aristas.append({vertice, adyacente})
        return aristas

    def encontrar_camino(self, vertice_inicio, vertice_final, camino=None):
        """ encuentra un camino desde el vertic_inicio al vertice_final 
            en el grafo"""
        if camino == None:
            camino = []
        grafo = self.__grafo
        camino = camino + [vertice_inicio]
        if vertice_inicio == vertice_final:
            return camino
        if vertice_inicio not in grafo:
            return None
        for vertice in grafo[vertice_inicio]:
            if vertice not in camino:
                camino_extendido = self.encontrar_camino(vertice, vertice_final,camino)
                if camino_extendido: 
                    return camino_extendido
        return None
    def encontrar_caminos(self, inicio, fin, camino=[]):
        """ encuantra todos los caminos de un vertice al otro """
        grafo = self.__grafo
        camino = camino + [inicio]
        if inicio == fin:
            return [camino]
        if inicio not in grafo:
            return []
        caminos = []
        for vertice in grafo[inicio]:
            if vertice not in camino:
                caminos_extendidos = self.encontrar_caminos(vertice,fin,camino)
                for c in caminos_extendidos: 
                    caminos.append(c)
        return caminos

    def camino_euler(self):
    	if self.esta_conectado():    			
    		vertices = self.vertices()

    		impares = []
    		for vertice in vertices:
    			if self.grado_vertice(vertice) % 2 != 0:    				
    				impares.append(vertice)    				
    		if len(impares)==2:
    			caminos = self.encontrar_caminos(impares[0], impares[1]) 			    		

    		for c in caminos:
    			if len(c)== len(vertices):
    				return c

    		return None
    	else:	
    		return None

    def grado_vertice(self, vertice):
        """ Retorna el número de vertices adyacentes al vertice. """ 
        adj_vertices =  self.__grafo[vertice]
        grado = len(adj_vertices) + adj_vertices.count(vertice)
        return grado

    def grado_vertices(self):
    	vertices = self.vertices() # lista de vertices
    	grados = []
    	for vertice in vertices:    		
    		grados.append(self.grado_vertice(vertice))    		
    	return grados

    def esta_conectado(self,vertices_encontrados = None,vertice_inicio = None):
        """ Determina si el grafo está conectado"""
        if vertices_encontrados is None:
            vertices_encontrados = set()
        g = self.__grafo        
        vertices = list(g.keys()) # lista de vertices
        if not vertice_inicio:
            # escoge un vertice de inicio en el grafo
            vertice_inicio = vertices[0]
        vertices_encontrados.add(vertice_inicio)
        if len(vertices_encontrados) != len(vertices):
            for vertice in g[vertice_inicio]: # recorremos los adyacentes a ese vertice
                if vertice not in vertices_encontrados:
                    if self.esta_conectado(vertices_encontrados, vertice):
                        return True
        else:
            return True
        return False


    def __str__(self):
        res = "vertices: "
        for k in self.__grafo:
            res += str(k) + " "
        res += "\naristas: "
        for arista in self.__generar_aristas():
            res += str(arista) + " "
        return res

if __name__ == "__main__":

    grafo = Grafo()
    grafo.add_vertice("a")
    grafo.add_vertice("b")
    grafo.add_vertice("c")
    grafo.add_vertice("d")
    grafo.add_vertice("e")

    #grafo.add_arista({"a","b"})
    #grafo.add_arista({"a","c"})
    #grafo.add_arista({"d","c"})

    grafo.add_arista({"a","b"})
    grafo.add_arista({"a","c"})
    grafo.add_arista({"c","b"})
    grafo.add_arista({"a","d"})
    grafo.add_arista({"d","e"})
    grafo.add_arista({"d","c"})
    grafo.add_arista({"d","b"})
    grafo.add_arista({"c","e"})
    

    print("Ciudades:")
    print(grafo.vertices())

    print("grado de las ciudades:")
    print(grafo.grado_vertices())

    print("aristas:")
    print(grafo.aristas())    

    print("Todas las ciudades están conectadas?")
    print(grafo.esta_conectado())

    print("Recorrido de ciudades: ")
    caminos =grafo.camino_euler()
    print(caminos)
    
