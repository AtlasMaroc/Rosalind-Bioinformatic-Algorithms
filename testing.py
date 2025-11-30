class SuffixTree:

   class Node(object):
      def __init__(self, lab):
         self.lab = lab
         self.out = {}


   def __init__(self, set):

      s = ""
      special_characters = [f"${i}" for i in range(len(set))]
      for i, value in enumerate(set):
         s += value + special_characters[i]



      self.root = {}
      self.root[s[0]] = self.Node(s)
      i = 0
      j = i
      cur = self.root
      for i in range(1, len(s)):
       j = i
       cur = self.root
       while j < len(s):
         if s[j] in cur:
            child = cur.out[s[j]]
            child_label = child.lab
            k = j+1
            while k-j < len(child_label) and s[k] == child_label[k-j]:
                 k += 1
            if s[k] != child_label[k-j]:
               #	we	fell	off	in	middle	of	edge
               cExist, cNew = child_label[k - j], s[k]
               #	create	“mid”:	new	node	bisecting	edge
               mid = self.Node(child_label[:k - j])
               mid.out[cNew] = self.Node(s[k:])
               #	original	child	becomes	mid’s	child
               mid.out[cExist] = child
               #	original	child’s	label	is	curtailed
               child.lab = child_label[k - j:]
            #	mid	becomes	new	child	of
               cur.out[s[j]] = mid
         else:
            #	Fell	off	tree	at	a	node:	make	new	edge	hanging	off	it
            cur.out[s[j]] = self.Node(s[j:])