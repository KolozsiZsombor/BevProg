def main():
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
    j = None

    for i in developers:
        n += 1
        cproject = i._project
        cname = i._name
        projects.append([cproject,cname,n])
        prjs.add(cproject)

    k = None
    Flag = False
    same = []
    n = 0

    if len(prjs) == len(projects):
        print("Mindenki más-más projecten dolgozik.")
        Flag = True

    projects = sorted(projects)

    projectDict = dict()

    if not Flag:
        for i in projects:
            for j in prjs:
                if i[0] == j:
                    n += 1
            projectDict[i] = n
            n = 0
                    
    print(projectDict)

if __name__ == "__main__":
    main()