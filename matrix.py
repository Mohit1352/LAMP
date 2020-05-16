class matrix:
	def __init__(self,m=None,n=None,deflist=None,rowwise=None,displ=0,mode='n'):
		'''Constructor for matrix. (default values if not initialised are (self,1,1,[],[],0))'''
		self.defset=1
		self.rwset=0
		if m is None:
			self.row=1
		else:
			self.row=m
		if n is None and mode=='n':
			self.col=1
		elif n is None and mode=='i':
			self.col=self.row
		else:
			self.col=n
		x=f"Matrix created. {m}x{n}"
		#ANSITerminal only: print('\033[1;32m'+x+'\033[1;m')
		if deflist is None:
			deflist=[]
			self.deflist=deflist
			self.defset=0
		else:
			self.deflist=deflist
		if(rowwise is None):
			rowwise=[]
			self.rowwise=rowwise
		else:
			self.rowwise=rowwise
			self.rwset=1
		if mode=='i':
			self.fill(self.deflist,mode='i')
			self.fill(self.deflist)
		if(self.defset==0 and self.rwset==1 and mode=='n'):
			self.setdeflist()
		fille=0
		if(self.rwset==0 and self.defset==1 and mode=='n'):
			fill=self.fill(deflist)
		if displ==1:
			print(x)
			if fille==0:
				#print('\033[1;31m'+"Warning: Matrix is not filled yet. Use \nobj.fill(linear list(left to right,up to down))\nto fill the matrix."+'\033[1;0m');
				print("Warning: Matrix is not filled yet. Use \nobj.fill(linear list(left to right,up to down))\nto fill the matrix.")
			else:
				self.disp()
	
	def __str__(self):
		'''Returns a value if object is printed'''
		return f"Matrix object {self.row}x{self.col}\nDefset:{self.defset}\nRWset:{self.rwset}\nDeflist:{self.deflist}\nRowwise:{self.rowwise}"
	
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
	
	def copymat(self):
		return matrix(self.row,self.col,self.deflist)
	
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
					d=d+(((self.cofactor(0,i)).det())*i)
				return d
	
	def disp(self):
		'''Displays the calling matrix object \'self\'.'''
		for i in range(0,self.row):
			for j in range(0,self.col):
				print(self.rowwise[i][j],end=' ')
			print()
	
	def disp2(self):
		'''disp(), but prints elements with proper spacing.'''
		maxv=max([len(str(x)) for x in self.deflist])
		print(self.deflist,maxv)
		for i in range(0,self.row):
			for j in range(0,self.col):
				y=self.rowwise[i][j]
				x=y-int(y)
				if(x==0):
					y=int(y)
				t=str(y)
				s=""
				for k in range(0,maxv-len(t)):
					s=s+" "
				s=s+t
				print(s,end=' ')
			print()
	
	def fill(self,deflist=None,mode='n'):
		'''Fills a matrix \'self\' if a list of numbers \'deflist\' is defined.'''
		if(mode=='i'):
			l=[]
			for i in range(0,self.row):
				for j in range(0,self.col):
					if(i==j):
						l.append(1)
					else:
						l.append(0)
			self.deflist=l
			self.defset=1
		elif(deflist==[] or deflist is None):
			return 0
		else:
			for i in range(0,self.row):
				for j in range(0,self.col):
					if j==0:
						self.rowwise.append([])
					self.rowwise[i].append(deflist[i*self.col + j])
		self.rwset=1
		if(self.defset==0 and self.rwset==1):
			self.setdeflist()
	
	def geliminate(self):
		'''Performs Gaussian elimination on the matrix and returns the resulting matrices.'''
		mat=self.copymat()
		pivot=0
		l=[]
		el=[]
		maxr=0
		pivots=0
		for i in range(0,self.col):
			pivot=mat.rowwise[i][i]
			if(i>=maxr):
				maxr=i;
			if pivot==0 and i==0:
				for j in range(i,mat.row):
					if mat.rowwise[j][i]!=0:
						mat=mat.rowswap(i,j)
						break
			elif pivot==0 and i!=0:
				for j in range(i,mat.row):
					if mat.rowwise[j][i]!=0:
						pivot=mat.rowwise[j][i]
						maxr=j
						break
			pivots=pivots+1
			for j in range(i+1,mat.row):
				lterm=-mat.rowwise[j][i]/pivot
				li=[lterm,j,i]
				for k in range(0,mat.col):
					mat.rowwise[j][k]=mat.rowwise[j][k]+lterm*mat.rowwise[i][k]
				l.append(li)
			if maxr==self.row-1:
				break
		for i in range(0,pivots):
			for j in range(0,pivots):
				if i==j:
					el.append(1)
				elif j>i:
					el.append(0)
				else:
					for k in l:
						if k[1]==i and k[2]==j:
							el.append(k[0])
							break
		mat.setdeflist()
		return mat,matrix(pivots,pivots,el)		
	
	def info(self):
		'''Displays various attributes of the matrix \'self\''''
		print(f"Matrix:\n{self.row}x{self.col}")
		self.disp()
		print(f"Determinant: {self.det()}")
		print("Transpose:")
		self.transpose().disp()
		print("Inverse: NPY")
		self.inverse()
	
	def inputfill(self): #needs fix
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
					break
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
				print(jc)
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
						sum=sum+(a.rowwise[i][k]*b.rowwise[k][j])
					l.append(sum)
			return matrix(r,c,l)
		else:
			return "NA"
	
	def multiply(a,b):
		'''Combines the smul and mmul features, multiplies a quantity with the other quantity and returns answer, \"NA\" if incompatible.'''
		if(isinstance(a,matrix)):
			if(isinstance(b,matrix)):
				return a.mmul(b)
			else:
				return a.smul(b)
		else:
			if(isinstance(b,matrix)):
				return b.smul(a)
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
		self.defset=1
		if(self.rwset==0 and self.defset==1):
			fill=self.fill(deflist)
	
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
			return matrix(a.row,a.col,l,displ=1),matrix(a.row,a.col,m,displ=1)
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