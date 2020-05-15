class matrix:
	def __init__(self,m=None,n=None,deflist=None,rowwise=None,displ=0):
		'''Constructor for matrix. (default values if not initialised are (self,1,1,[],[],0))'''
		if m is None:
			self.row=1
		else:
			self.row=m
		if n is None:
			self.col=1
		else:
			self.col=n
		x=f"Matrix created. {m}x{n}"
		defset=1
		rwset=0
		#ANSITerminal only: print('\033[1;32m'+x+'\033[1;m')
		if deflist is None:
			deflist=[]
			self.deflist=deflist
			defset=0
		else:
			self.deflist=deflist
		if rowwise is None:
			rowwise=[]
			self.rowwise=rowwise
		else:
			self.rowwise=rowwise
			rwset=1
		if(defset==0 and rwset==1):
			self.setdeflist()
		fill=0
		if(rwset==0 and defset==1):
			fill=self.fill(deflist)
		if displ==1:
			print(x)
			if fill==0:
				#print('\033[1;31m'+"Warning: Matrix is not filled yet. Use \nobj.fill(linear list(left to right,up to down))\nto fill the matrix."+'\033[1;0m');
				print("Warning: Matrix is not filled yet. Use \nobj.fill(linear list(left to right,up to down))\nto fill the matrix.")
			else:
				disp(self)
	
	def __str__(self):
		'''Returns a value if object is printed'''
		return f"Matrix object {self.row}x{self.col}"
	
	def add(a,b):
		'''Adds two matrices a and b and returns the resulting matrix, or \"NA\" if incompatible.'''
		if a.row==b.row and a.col==b.col:
			l=[]
			for i in range(0,a.row*a.col):
				l.append(a.deflist[i]+b.deflist[i])
			return matrix(a.row,a.col,l)
		else:
			return "NA"
	
	def cofactor(self,r,c):
		'''Returns cofactor matrix excluding row r and column c from \'self\''''
		l=[]
		for i in range(0,self.row):
			for j in range(0,self.col):
				if(r!=self.row and c!=self.col):
					l.append(self.rowwise[i][j])
		return matrix(self.row-1,self.col-1,l)
	
	def colspace(self):
		'''Returns the Column space of the matrix.'''
		pass
	
	def colswap(self,s,d):
		'''Returns a matrix with a swap of s column with the d column of the source matrix (s,d start from 1)'''
		l=[]
		for i in range(0,self.row):
			for j in range(0,self.col):
				if j==s-1:
					l.append(self.rowwise[i][d-1])
				elif j==d-1:
					l.append(self.rowwise[i][s-1])
				else:
					l.append(self.rowwise[i][j])
		return matrix(self.row,self.col,l)
	
	def det(self):
		'''Returns determinant of a matrix (NA if not applicable, number if applicable)'''
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
	
	def disp(self):
		'''Displays the calling matrix object \'self\'.'''
		for i in range(0,self.row):
			for j in range(0,self.col):
				print(self.rowwise[i][j],end=' ')
			print()
		print("\n")
	
	def fill(self,deflist):
		'''Fills a matrix \'self\' if a list of numbers \'deflist\' is defined.'''
		if(deflist==[] or deflist is None):
			return 0
		else:
			for i in range(0,self.row):
				for j in range(0,self.col):
					if j==0:
						self.rowwise.append([])
					self.rowwise[i].append(deflist[i*self.col + j])
	
	def geliminate(self):
		'''Performs Gaussian elimination on the matrix and returns the resulting matrix.'''
		pass
	
	def info(self):
		'''Displays various attributes of the matrix \'self\''''
		print(f"Matrix:\n{self.row}x{self.col}\n")
		self.disp()
		print(f"Determinant: {self.det()}")
		self.transpose()
		self.inverse()
	
	def inputfill(self):
		'''Inputs a matrix row wise, and sets parameters automatically with the first row input.'''
		print("Enter your matrix row wise:\n(separate entries with spaces, end row with newline)\n")
		i=0
		while True:
			bc=0
			while True:
				s=input()
				if s!="":
					s=s.split()
					try:
						s=[int(k) for k in s]
					except:
						print("Enter numbers, nothing else. Please reenter row!\n")
						continue
					if i!=0:
						if len(s)==self.col:
							break
						else:
							print("Row length mismatch! Reenter with same length as row 1.")
							continue
				else:
					bc=1
					break
				self.rowwise.append(s)
				i=i+1
				jc=0
			if(bc==1):
				break
			for j in s:
				if(jc==0):
					self.deflist.append([])
				jc=jc+1
				self.deflist[i].append(j)
			if(i==1):
				self.col=jc
		self.row=i
		print("Entry is done.")
		self.disp()
	
	def inverse(self):
		'''Returns the inverse of the matrix \'self\' using Gauss-Jordan method'''
		pass
	
	def issquare(self):
		'''Checks if matrix is a square matrix. (returns 0 for false, 1 for true)'''
		if self.row==self.col:
			return 1
		else:
			return 0
	
	def lnspace(self):
		'''Returns Left Null space of the matrix.'''
		pass
	
	def mmul(a,b):
		'''Returns the product of 2 matrices a.b, or \"NA\" if incompatible'''
		if(a.col==b.row):
			r=a.row
			c=b.col
			l=[]
			for i in range(0,r):
				for j in range(0,c):
					sum=0
					for k in range(0,a.col):
						sum=sum+(a.rowwise[i][k]*b.rowwise[j][k])
					l.append(sum)
			return matrix(r,c,l)
		else:
			return "NA"
	
	def multiply(a,b):
		'''Combines the smul and mmul features, multiplies a quantity with the other quantity and returns answer, \"NA\" if incompatible.'''
		if(isinstance(a,matrix)):
			if(isinstance(b,matrix)):
				return mmul(a,b)
			else:
				return smul(a,b)
		else:
			if(isinstance(b,matrix)):
				return smul(b,a)
			else:
				return a*b
	
	def nullspace(self):
		'''Returns null space of the matrix.'''
		pass
	
	def revgeliminate(self):
		'''Performs Reverse Gaussian elimination (from last pivot on Upper Triangle) on the matrix and returns the resulting matrix.'''
		pass
	
	def rowspace(self):
		'''Returns Row space of matrix.'''
		pass
	
	def rowswap(self,s,d):
		'''Returns a matrix with a swap of s row with the d row of the source matrix (s,d start from 1)'''
		l=[]
		for i in range(0,self.row):
			if i==s-1:
				l.append(self.rowwise[d-1])
			elif i==d-1:
				l.append(self.rowwise[s-1])
			else:
				l.append(self.rowwise[i])
		return matrix(self.row,self.col,rowwise=l)
	
	def setdeflist(self):
		'''Fills the deflist if the rowwise list of lists is given'''
		l=[]
		for i in range(0,self.row):
			for j in range(0,self.col):
				l.append(self.rowwise[i][j])
		self.deflist=l
	
	def smul(self,scalar):
		'''Returns a matrix having all terms of \'self\' multiplied by a scalar'''
		l=[]
		for i in self.deflist:
			l.append(scalar*i)
		return matrix(self.row,self.col,l)

	def spaces(self):
		'''Displays and returns data about the subspaces of the matrix.'''
		pass
		
	def subtract(a,b):
		'''Subtracts two matrices a and b and returns the resulting matrices with both differences (a-b,b-a), or \"NA\" if incompatible.'''
		if a.row==b.row and a.col==b.col:
			l=[]
			m=[]
			for i in range(0,a.row*a.col):
				l.append(a.deflist[i]-b.deflist[i])
				m.append(b.deflist[i]-a.deflist[i])
			return matrix(a.row,a.col,l,disp=1),matrix(a.row,a.col,m,disp=1)
		else:
			return "NA"
	
	def transpose(self):
		'''Returns the transposed matrix of \'self\''''
		l=[]
		for j in range(0,self.col):
			for i in range(0,self.row):
				l.append(self.rowwise[i][j])
		t=matrix(self.col,self.row,l)
		return t
	
