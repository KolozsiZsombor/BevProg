def main():
    k = 1
    for i in range(1,13):
        print()
        for k in range(1,13):
            txt = str(i*k)
            txt = txt+"\t"
            print(txt.expandtabs(4),end="")
        
if __name__ == "__main__":
    main()
