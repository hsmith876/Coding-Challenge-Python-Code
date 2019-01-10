def extract(query):
	q = "a"
	wd = set()
	def add1(c):
		if c=='z':
			return 0
		return chr(ord(c)+1)
	while q!='':
		part=query(q)
#		print(q)
#		print(part)
		wd =wd.union(set(part))
		if len(part)==5:
			q = q + part[-1][len(q)]
		else:
			next = add1(q[-1]) 
			while q!='' and next==0:
				q=q[:-1]
				if q!='':
					next = add1(q[-1]) 
			if q!='':
				q=q[:-1]+next
	return sorted(list(wd))
def main():
    database = ["aabracadara","abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
main()
