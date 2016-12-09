import networkx as nx
import matplotlib.pyplot as plt

def main():
	G=nx.Graph()
	f=open("node2.tsv","r")
	for line in f:
		part=line.strip().split("\t")
		nodeno=part[0]
		rev=part[1]
		G.add_node(nodeno, rev=rev)
	
	flink=open("link2.tsv",'r')
	src_ref={}
	for line in flink:
		part=line.strip().split("\t")
		src=part[0]
		tgt=part[1]
		zipc=part[2]
		strength=part[3]	
		G.add_edge(src, tgt, weight=strength )
		G.add_node(src,zipcode=zipc)
	
	#print G.nodes()
	#print G.nodes("1")
	#nx.draw_graphviz(G)
	print("Degree centrality")
	d=nx.degree_centrality(G)
	for v in G.nodes():
		if d[v]>0:
			print v,d[v]

	#c = nx.communicability(G)
	print c
	#for i in nx.connected_component_subgraphs(G):
	#	print i
	#nx.draw(G,with_labels = True)
	#plt.show()
	#plt.savefig("path.png")

if __name__ == '__main__':
	main()