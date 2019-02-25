import re, sys, getopt

def main(argv):
    in_path = ''
    out_path = ''
    loci_path = ''
    try:
        opts, args = getopt.getopt(argv,"hi:l:o:",["input=","loci=","output="])
    except:
        print 'trim_fasta.py -i [input] -loci [loci] -o [output]'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-help", "-h"):
            print 'trim_fasta.py -i [input] -loci [loci] -o [output]'
            sys.exit()
        elif opt in ("-i", "--input"):
            in_path = arg
        elif opt in ("-l", "--loci"):
            loci_path = arg
        elif opt in ("-o", "--output"):
            out_path = arg
    with open(in_path, 'r') as inFile:
        input = inFile.read()
    loci=[]
    with open(loci_path) as text:
        loci = text.readlines()
    for i in loci:
        replace = '>' + i.rstrip() + '(.*)\\n([A-Z]|[a-z]|\\n)*'
        input = re.sub(replace, '', input)
    with open(out_path, 'w') as outFile:
        outFile.write(input)
if __name__ == '__main__':
    main(sys.argv[1:])
