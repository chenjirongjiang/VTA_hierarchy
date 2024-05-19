'''
    m21 =open( r'C:\Users\Chenj\BIBC\Basak\files\gencode.vM21.chr_patch_hapl_scaff.annotation.gtf','r')
    m23 = open(r'C:\Users\Chenj\BIBC\Basak\files\gencode.vM23.chr_patch_hapl_scaff.annotation.gtf', 'r')

    m21_lines =m21.readlines()
    m23_lines = m23.readlines()

    matched = set(m21_lines) &set(m23_lines)
    unmatched_21 = [line for line in m21_lines if line not in matched]
    unmatched_23 = [line for line in m23_lines if line not in matched]

    with open('unmatched_21.txt', 'w') as f:
        for line in unmatched_21:
            f.write(f"{line}\n")

    with open('unmatched_23.txt', 'w') as f:
        for line in unmatched_23:
            f.write(f"{line}\n")


    m21 =open(r'C:\Users\Chenj\BIBC\Basak\files\unmatched_23.txt','r')
    m23 = open(r'C:\Users\Chenj\BIBC\Basak\files\unmatched_23.txt', 'r')

    print(m21.readlines(), '\n')
    print(m23.readlines())
    '''

id = 'adata_g004_filtered_1'
a = ['g004', 'g005', 'g011', 'g012', 'g013', 'g014', 'g015', 'g016', 'g017', 'g018', 'g019', 'g020']
b=[]
for i in a:
    new =id.replace('g004', i)
    b.append(new)
   
    #input("Press Enter to continue...")

print(b)

    