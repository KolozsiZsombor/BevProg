class Developer:
    def __init__(self, name, project, role):
        self.name = name
        self.project = project
        self.role = role
        print("--Developer létrehozva--")
        print(f"{name} a {project}-en dolgozik {role} szerepkörben.")

developer1 = Developer("Ricsi","SolArch","Frontend")
developer2 = Developer("Angéla","ZerTeng","Tesztelő")
developer3 = Developer("Peti","KefERP","Backend")
developer4 = Developer("Éva","KefERP","Frontend")

developers = [developer1,developer2,developer3,developer4]

for i in developers:
    print(i[1])