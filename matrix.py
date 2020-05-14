class matrix:
	row=1
	col=1
	def __init__(self,m,n,deflist=None,rowwise=None):
		self.row=m
		self.col=n
		self.deflist=deflist
		x=f"Matrix created. {m}x{n}"
		#ANSITerminal only: print('\033[1;32m'+x+'\033[1;m')
		print(x)
		if deflist is None:
			deflist=[]
			self.deflist=deflist
		if rowwise is None:
                        rowwise=[]
                        self.rowwise=rowwise
		fill=self.fill(deflist)
		if fill==0:
			#print('\033[1;31m'+"Warning: Matrix is not filled yet. Use \nobj.fill(linear list(left to right,up to down))\nto fill the matrix."+'\033[1;0m');
                        print("Warning: Matrix is not filled yet. Use \nobj.fill(linear list(left to right,up to down))\nto fill the matrix.")
	
	def fill(self,deflist):
		if(deflist==[] or deflist is None):
			return 0
		else:
			for i in range(0,self.row):
				for j in range(0,self.col):
					if j==0:
						self.rowwise.append([])
					self.rowwise[i].append(deflist[i*self.col + j])
	
	def cofactor(self,r,c):
		l=[]
		for i in range(0,self.row):
			for j in range(0,self.col):
				if(r!=self.row and c!=self.col):
					l.append(self.rowwise[i][j])
		a=matrix(self.row-1,self.col-1,l)
		return a
	
	def issquare(self):
		if self.row==self.col:
			return 1
		else:
			return 0
	
	def det(self):
		if not self.issquare():
			return "NA"
		else:
			if(self.col==2):
				return (self.rowwise[0][0]*self.rowwise[1][1] - self.rowwise[0][1]*self.rowwise[1][0])
			else:
				d=0
				for i in range(0,self.col):
					d=d+(self.det(self.cofactor(0,i))*i)
				return d
	
	def transpose(self):
		l=[]
		for j in range(0,self.col):
			for i in range(0,self.row):
				l.append(self.rowwise[i][j])
		t=matrix(self.col,self.row,l)
		return t
	
	def inverse(self):
		pass
	
	def disp(self):
		for i in range(0,self.row):
			for j in range(0,self.col):
				print(self.rowwise[i][j],end=' ')
			print()
		print("\n")
	
	def info(self):
                        print(f"Matrix:\n{self.row}x{self.col}\n")
                        self.disp()
                        print(f"Determinant: {self.det()}")
                        self.transpose()
                        self.inverse()
	
