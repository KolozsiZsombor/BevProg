class Developer:
    def __init__(self, name, project, role):
        self._name = name
        self._project = project
        self._role = role
        print("--Developer létrehozva--")
        print(f"{name} a {project}-en dolgozik {role} szerepkörben.")

developer1 = Developer("Ricsi","SolArch","Frontend")
developer2 = Developer("Angéla","ZerTeng","Tesztelő")
developer3 = Developer("Peti","KefERP","Backend")
developer4 = Developer("Éva","KefERP","Frontend")

developers = [developer1,developer2,developer3,developer4]

n = -1
projects = []
prjs = set()
cproject = ""
cname = ""
kp = []
j = None
ip = None

for i in developers:
    n += 1
    cproject = i._project
    cname = i._name
    projects.append([cproject,cname,n])
    prjs.add(cproject)

k = None

if len(prjs) == len(projects):
    print("Mindenki más-más projecten dolgozik.")
else:
	for i in projects:
		for j in i:
			print(j)
		
		# ip = 
		# k = j
		# j = i[0]
		# if k == j:
			# print(i)
