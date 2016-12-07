
def main():
	f=open("node2.tsv","r")
	for line in f:
		part=line.strip().split("\t")
		nodeno=part[0]
		rev=part[1]
		zipc=part[2]
		print ' {"id":"'+str(nodeno)+'", "group": '+str(zipc)+',"rev":' +rev+' },'
	
	flink=open("links.tsv",'r')
	src_ref={}
	for line in flink:
		part=line.strip().split("\t")
		src=part[0]
		tgt=part[1]
		zipc=part[2]
		strength=part[3]	
		#print '{"source":'+str(int(src)-1)+', "target":'+str(int(tgt)-1)+',"strength":'+str(strength)+',"zip":'+str(zipc)+'},'
		if src in src_ref.keys():
			src_ref[src].append(tgt)
		else:
			src_ref[src]=[tgt]
	#print src_ref	
	#for k,v in src_ref.items():
	#	print '{"id":' "'"+k+"'"+',"references":'+str(v)+'},'

if __name__ == '__main__':
	main()