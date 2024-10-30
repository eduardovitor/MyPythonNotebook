

def ler_arquivo(arquivo,num_linhas):
    i = 1
    with open(arquivo, "r") as f:
        for line in f.readlines():
            if i <= num_linhas:
                yield line
            i += 1

for linha in ler_arquivo("outfile.txt",5):
    print(linha)