def main():
    print("\t".expandtabs(5),end="")
    for j in range(1,13):
        l=str(j)
        l=l+"\t"
        print(l.expandtabs(4),end="")
    print()
    print("-"*((4*12)+6))
    for i in range(1,13):
        l=str(i)
        l=l+"\t"
        print(l.expandtabs(3),": ",sep="",end="")
        for k in range(1,13):
            txt = str(i*k)
            txt = txt+"\t"
            print(txt.expandtabs(4),end="")
        print()
            
if __name__ == "__main__":
    main()
