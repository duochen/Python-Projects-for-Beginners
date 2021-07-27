from random import choices

def str2gene(s):
    gene = []
    for i in range(len(s)//3):
        codon = (s[3*i], s[3*i + 1], s[3*i + 2])
        gene.append(codon) 
    return gene

def linear(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return gene.index(key_codon)

def binary(gene, key_codon) :
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return mid

gene_str="".join(choices('ATCG',k=300))
print(f"gene: {gene_str}")
gene = str2gene(gene_str)
sorted_gene = sorted(gene)
key="TCG"
print(f"codon: {key}")
codon = str2gene(key)[0]
print(f"Linear: codon found at number {linear(gene, codon)} of gene")
print(f"Binary: codon found at number {binary(sorted_gene, codon)} of sorted gene")
