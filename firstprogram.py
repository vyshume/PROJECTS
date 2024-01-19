#this is my first program
'''this is my first programn
iam very happy to learn python programming
print('welcome to vyshume')
#program to calculate number of guides

a = b = c = d = 40
oneguidecost=110
total=a+b+c+d
name='vyshu'
CHANNEL="vyshu"

print(total)
print(total/oneguidecost)
print(type(a))
print(type(name))

#program to demonstrate input and output

pin,cash=input('enter your pin and cash:').split('----')
print('pin and cash are,pin,cash')
cashValue=int(cash)
totalAmount=50000
remainingAmount=totalAmount-cashValue
print('take your cash',cash,remainingAmount,sep="-----",end='\t')
print('thank for using our ATM')
print('kindly come back')

#Arithmetic operators
a=7
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a=99
b=200

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#relational operators
a=9
b=2
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

#logical operators


a=True
b=False
print(a and b)
print(not b) 
print(a or b)
print(not a)

#Assignment operators
a=5
b=2
a+=b
print(a)
a-=b
print(a)
a/=b
print(a)
a*=b
print(a)
a//=b
print(a)
a%=b
print(a)
b%=3
print(b)


#finding age by  birth year


yearofBirth = int(input('please tell ur date of year'))
currentYear = date.today().year
age = currentYear-yearofBirth
print('your age is:',age)

#Data types program
print('Data types')

#Numeric (int,float,complex)
marks = 455
percentage = (marks/600)*100
print('percentage',percentage)
print(type(marks)) 
print(type(percentage ))

#x+yj

x = 10 + 5j
y = 11 + 2j 

print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())

#creating strings

branch='electronics & communication engineering'
statement = 'iam very glad to have this course & i got a 2000 rank in my Ecet' 
print("Accessing elements from string")
print('yourBranch is:',branch)
print(statement)
print(len(branch))
print(branch[-8])
print(branch[1:4])
print(branch[:4])
print(branch[5:10:2])
print(branch[::-1])
branch='electronics & communication engineering' * 4   
print('hello' not in branch)
print(branch)

#list
print('======list========')  
#telugu,maths,social,science,english                 
marks=[50,20,90,65,98]
print(type(marks))
print(marks)
friends=['Pandu','Munny','Sri','Chikki','Chinni','Puppi']

print('friends count',len(friends))
print(friends)

bioDataList=[27,"888888","address",friends]  
print(bioDataList)
print('last friend',friends[5])
print('last friend',friends[-1])
print(friends + marks)
friends.append('kutti')
print(friends)
friends.extend(['  bunny','sunny','mintu'])
friends.insert(4,'vyshu')
print(friends)

friends[1:1]=['a','b','c']
print(friends)
del friends[1]
print(friends)
friends.remove('b')
print(friends)

print("======tuple=======")

marks=(20,50,80,100,30)
print(type(marks))
friends='pandu','munny','puppi','chikki','chinni'
print(friends)
print(type(friends))
print(friends[1])


#boolean
print('=======boolean=======')
subscribed=True
print(type(subscribed))
a=10
b=10

print(type(a==b))

print('=====SET=====')
students={'puppi,pandu,munny,chinni,mintu'}
print(students)
print(type(students))

#union

a={10,20,30,40}
b={20,80,70,100}
abUnion=a.union(b)
print(abUnion)

#difference

a={10,20,30,40}
b={20,80,70,100}
abdifference=a.difference(b)
print(abdifference)

#symmetric difference
a={10,20,30,40}
b={20,80,70,100}

absymmetricDifference=a.symmetric_difference(b)
print(absymmetricDifference)'''

#dictionary

bioData = {'name':'vyshnavi','address':'peddapelli','cute':'True'}
print(bioData)
print(type(bioData))

information = {"channel":'vyshume','info':bioData}
print(information)
















