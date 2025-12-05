from networkx.algorithms.community.modularity_max import greedy_modularity_communities
import sys
import networkx as nx
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort

# Importiamo il grafico ZKC :
ZKC_graph = nx.karate_club_graph()

# Teniamo traccia di quali nodi rappresentano John A e Mr Hi
Mr_Hi = 0
John_A = 33

# Mostriamo le etichette di quale club ogni membro si è unito a
club_labels = nx.get_node_attributes(ZKC_graph, 'club')

# mostra solo un paio di etichette
print({key: club_labels[key] for key in range(10, 16)})

A = nx.convert_matrix.to_numpy_matrix(ZKC_graph)

print(A)

# Per tracciare usando networkx dobbiamo prima ottenere le posizioni che vogliamo per ogni nodo.
# Qui useremo un layout circolare ma ci sono molte altre varianti che potresti scegliere!
circ_pos = nx.circular_layout(ZKC_graph)

# Utilizzare la funzione di disegno networkx per visualizzare facilmente il grafico
nx.draw(ZKC_graph, circ_pos)

# evidenziamo Mr Hi (verde) e John A (rosso)
nx.draw_networkx_nodes(ZKC_graph, circ_pos, nodelist=[
                       Mr_Hi], node_color='g', alpha=1)
nx.draw_networkx_nodes(ZKC_graph, circ_pos, nodelist=[
                       John_A], node_color='r', alpha=1)

plt.show()

density = nx.density(ZKC_graph)

print('La densità del bordo è: ' + str(density))

# la funzione degree in networkx restituisce un oggetto DegreeView in grado di scorrere le coppie (nodo, degree)
degree = ZKC_graph.degree()

degree_list = []

for (n, d) in degree:
    degree_list.append(d)

av_degree = sum(degree_list) / len(degree_list)

print('Il grado medio è ' + str(av_degree))

# ora tracciamo la distribuzione dei gradi per avere una visione migliore
plt.hist(degree_list, label='Degree Distribution')
plt.axvline(av_degree, color='r', linestyle='dashed', label='Average Degree')
plt.legend()
plt.ylabel("Numero di nodi")
plt.title("Karate Club: Node Degree")
plt.show()

# Ora possiamo calcolare il coefficiente di clustering locale
local_clustering_coefficient = nx.algorithms.cluster.clustering(ZKC_graph)

# consente di trovare il coefficiente di clustering medio
av_local_clustering_coefficient = sum(
    local_clustering_coefficient.values()) / len(local_clustering_coefficient)

# analogamente al grado consente di tracciare la distribuzione del coefficiente di clustering locale
plt.hist(local_clustering_coefficient.values(),
         label='Distribuzione del coefficiente di clustering locale')
plt.axvline(av_local_clustering_coefficient, color='r',
            linestyle='dashed', label='Average Local Clustering Coefficient')
plt.legend()
plt.ylabel("Numero di nodi")
plt.title('Coefficiente di clustering locale')
plt.show()


# preforma il rilevamento della comunità
c = list(greedy_modularity_communities(ZKC_graph))

# Scopriamo quante comunità abbiamo rilevato
print(len(c))

# Vediamo questi 3 cluster
community_0 = sorted(c[0])
community_1 = sorted(c[1])
community_2 = sorted(c[2])

print(community_0)
print(community_1)
print(community_2)

#disegna ogni set di nodi in un colore separato 
nx.draw_networkx_nodes(ZKC_graph,circ_pos, nodelist=community_0, node_color='g', alpha=0.5)
nx.draw_networkx_nodes(ZKC_graph,circ_pos, nodelist=community_1, node_color='r', alpha=0.5)
nx.draw_networkx_nodes(ZKC_graph,circ_pos, nodelist=community_2, node_color='b', alpha=0.5)

#ora possiamo aggiungere bordi al disegno  
nx.draw_networkx_edges(ZKC_graph,circ_pos,width = 0.2)

#finally possiamo aggiungere etichette per ciascun nodo corrispondente al club finale ciascun membro unito 
nx.draw_networkx_labels(ZKC_graph,circ_pos,club_labels,font_size=9)

plt.show()

combined_community = community_1 + community_2

#disegna la rete come prima 
nx.draw_networkx_nodes(ZKC_graph, circ_pos, nodelist=community_0, node_color='g', alpha=0.5)
nx.draw_networkx_nodes(ZKC_graph, circ_pos, nodelist=combined_community, node_color='m', alpha=0.5)

nx.draw_networkx_edges(ZKC_graph, circ_pos,width = 0.5)

nx.draw_networkx_labels(ZKC_graph, circ_pos, club_labels, font_size=9)

plt.show()
