# Name:Amandeep Kaur
# Date:18-Oct_2018
import copy
def valid(a,b):
	"""compares two numbers in binary to help group them into different grouping levels"""
	count=0
	ans=''
	for i in range(len(a)):
		if a[i]==b[i]:
			count+=1
			ans+=a[i]
		elif a[i]=='-' or b[i]=='-':
		 	ans+='*'
		else:
			ans+='-'

	if ans.count('-')==1 and count==5 and ans.count('*')==0:
		return '1'+ans
	elif ans.count('-')==2 and count==5 and ans.count('*')==0:
		return '2'+ans
	elif ans.count('-')==3 and count==5 and ans.count('*')==0:
		return '3'+ans

def grp_creator(m,n):
	"""takes in two lower level groups and creates a group of higher level"""
	create={}
	for i in m:
		for j in n:
			if valid(m[i],n[j])!=None:
				if valid(m[i],n[j])[0]=='1':
					create[i,j]=valid(m[i],n[j])[1:]
				elif valid(m[i],n[j])[0]=='2':
					create[i,j]=valid(m[i],n[j])[1:]
				elif valid(m[i],n[j])[0]=='3':
					create[i,j]=valid(m[i],n[j])[1:]
	return create

def left_outs(m,n):
	"""takes in two groups and lists out the terms not covered in the higher level group"""
	lst=copy.deepcopy(m)
	for i in m:
		for j in n:
			if i in j and i in lst:
				del lst[i]
	return lst

def minFunc(numVar,stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any print statements in the function.
	
	"""
	EPI=[]
	ans=''
	if stringIn[stringIn.find('(')+1]==')':
		ans='0*'
	else:	
		raw=list(map(int,stringIn[1:stringIn.find(')')].split(',')))
		if '-' in stringIn:
			dc=[]
		else:
			dc=list(map(int,stringIn[stringIn.find('d')+2:-1].split(',')))
		binaries={}
		for i in dc:
			binaries[i]=bin(i)
		main_dict={}
		for i in raw:
			main_dict[i]=bin(i)
		main_dict.update(binaries)
		for i in main_dict:
			while len(main_dict[i])<6:
				main_dict[i]=main_dict[i][:2]+'0'+main_dict[i][2:]

		# GROUPING LEVEL 1
		gr0={};gr1={};gr2={};gr3={};gr4={}
		for i in main_dict:
			if main_dict[i].count('1')==0:
				gr0[i]=main_dict[i]
			elif main_dict[i].count('1')==1:
				gr1[i]=main_dict[i]
			elif main_dict[i].count('1')==2:
				gr2[i]=main_dict[i]
			elif main_dict[i].count('1')==3:
				gr3[i]=main_dict[i]
			else:
				gr4[i]=main_dict[i]

		G1={}
		G1.update(gr0);G1.update(gr1);G1.update(gr2);G1.update(gr3);G1.update(gr4)

		# GROUPING LEVEL 2
		gro0=(grp_creator(gr0,gr1))
		gro1=(grp_creator(gr1,gr2))
		gro2=(grp_creator(gr2,gr3))
		gro3=(grp_creator(gr3,gr4))
		
		G2={}
		G2.update(gro0),G2.update(gro1);G2.update(gro2);G2.update(gro3)

		# GROUPING LEVEL 3
		grou0=grp_creator(gro0,gro1)
		grou1=grp_creator(gro1,gro2)
		grou2=grp_creator(gro2,gro3)
		G3={}
		G3.update(grou0);G3.update(grou1);G3.update(grou2)

 		# GROUPING LEVEL 4
		group0=grp_creator(grou0,grou1)
		group1=grp_creator(grou1,grou2)
		G4={}
		G4.update(group0);G4.update(group1)

		# GROUPING LEVEL 5
		grouped=grp_creator(group0,group1)
		G5={}
		G5.update(grouped)

		extension1=left_outs(G1,G2)
		extension2=left_outs(G2,G3)
		extension3=left_outs(G3,G4)
		extension4=left_outs(G4,G5)

		#Taking in the left outs
		final={}
		fi={}
		fi.update(grouped);fi.update(extension1);fi.update(extension2);fi.update(extension3);fi.update(extension4)
		for i in fi:
			if fi[i] not in final.values():
				final[i]=fi[i]

		#Formatting entities
		pfinal={}
		ppfinal={}
		for i in final:
			if type(i)==tuple:
				for j in i:
					if type(j)==tuple:
						pfinal[sum(i,())]=final[i]
					else:
						pfinal[i]=final[i]
			else:
				pfinal[i]=final[i]
		for i in pfinal:
			if type(i)==tuple:
				for j in i:
					if type(j)==tuple:
						ppfinal[sum(i,())]=pfinal[i]
					else:
						ppfinal[i]=pfinal[i]
			else:
				ppfinal[i]=pfinal[i]

		#Converting binaries to variables and handling case of 2,3 and 4 variables
		table={}
		if numVar==4:
			for i in ppfinal:
				samp='WXYZ'
				value=''
				for j in range(len(ppfinal[i][2:])):
					if ppfinal[i][2:][j]=='1':
						value+=samp[j]
					elif ppfinal[i][2:][j]=='0':
						value+=samp[j]+'\''
				table[i]=value	
		elif numVar==3:
			for i in ppfinal:
				samp='*WXY'
				value=''
				for j in range(1,len(ppfinal[i][2:])):
					if ppfinal[i][2:][j]=='1':
						value+=samp[j]
					elif ppfinal[i][2:][j]=='0':
						value+=samp[j]+'\''
				table[i]=value	
		elif numVar==2:
			for i in ppfinal:
				samp='**WX'
				value=''
				for j in range(2,len(ppfinal[i][2:])):
					if ppfinal[i][2:][j]=='1':
						value+=samp[j]
					elif ppfinal[i][2:][j]=='0':
						value+=samp[j]+'\''
				table[i]=value	

		TABLE={}
		TABLE.update(table)
		for i in table:
			if table[i]=='':
				del TABLE[i]
		if len(TABLE)==1:
			for i in TABLE:
				ans=TABLE[i]+'*'
		else:
			#Forming chart for the Quince-McClusky algorithm
			chart={}
			for i in TABLE:
				chart[TABLE[i]]=[]
				for j in range(2**numVar):
					if j in i and j not in dc:     
						chart[TABLE[i]].append('x')
					else:
						chart[TABLE[i]].append(' ')

			def reducer1(m):
				"""finds the row which covers maximum crosses and adds the corresponding minterm to the list 'EPI'"""
				for i in m:
					trash=''
					for j in range(2**numVar):
						if m[i][j]=='x':
							for k in m.values():
								trash+=k[j]
					cnt=trash.count('x')
					m[i].append(cnt)

				numbers=[]
				for i in m.values():
					numbers.append(i[-1])
				for i in m:
					if max(numbers)==m[i][-1]:
						epi=i
						culp=m[i]
				for j in range(2**numVar):
					if culp[j]=='x':
						for k in m:
							m[k][j]=' '
				
				EPI.append(epi)

			def reducer2(m):
				"""finds columns which have single crosses and adds corresponding minterms to 'EPI'"""
				n={}
				for i in range(2**numVar):
					trash=''
					for j in m:
						trash+=m[j][i]
						cnt=trash.count('x')
						n[i]=cnt
				
				for i in n:
					if n[i]==1:
						for j in m:
							if m[j][i]=='x' and j not in EPI:
								EPI.append(j)
				for i in m:
					if i in EPI:
						for j in range(2**numVar):
							if m[i][j]=='x':
								for k in m:
									m[k][j]=''

				"""First we find the EPIs(by reducer1),then find the PIs needed to cover all crosses(by reducer2)"""
				for i in m.values():
					if 'x' in i:
						for j in m:
							while 'x' in m[j]:
								reducer1(m)
				EPI.sort()

			"""Solving the chart"""
			reducer2(chart)

			"""Formatting and printing the answer"""
			ans=''
			for i in EPI:
				ans+=i+'+'
			if ans=='':
				ans='1*'
	stringOut=(ans[:-1])
	return stringOut

