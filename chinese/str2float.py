from functools import reduce

def normalize(name):
    n0, n1 = name[0], name[1:]
    nu, nl = n0.upper(), n1.lower()
    return nu + nl

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print L2

def prod(s):
    return reduce(lambda x, y: x*y, s)

print '3 * 5 * 7 * 9 =', prod([3, 5, 7, 9])


def str2float(s):
    intpart = s[:s.find('.')] # find integer part
    decpart = s[s.find('.') + 1:] # find decimal place part
    char2num=lambda ss:{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[ss]
    intnum = reduce(lambda x, y: x * 10 + y, map(char2num, intpart)) # x10 because 100+20+3
    decnum = reduce(lambda x, y: x * 0.1 + y, (map(char2num, decpart[::-1])+[0])) # + 0 to avoid 4 to become 4 instead of 0.4
    # decpart[::-1] = reverse it to times x0.1 because decimal place
    return intnum + decnum

print('str2float(\'123.456\') =', str2float('123.456'))
