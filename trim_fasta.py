import re, sys, getopt

def main(argv):
    # initializing variables
    in_path = ''
    out_path = ''
    loci_path = ''
    # read command line input
    # -h or -help for basic usage info
    # -i or --input for input fasta
    # -l or --loci for locus file, a text file where each row contains a locus name (generally uce)
    # -o or --output for output location for trimmed fasta, assuming format is ">[locus][other text]\n[sequence]\n"
    try:
        opts, args = getopt.getopt(argv,"hi:l:o:",["input=","loci=","output="])
    except:
        print 'trim_fasta.py -i [input] -l [loci] -o [output]'
        print 'Input is a fasta reference. Loci is a text file where each row contains a locus name (generally uce).'
        print 'The input should have the format ">[locus][other text]\\n[sequence]\\n".'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-help", "-h"):
            print 'trim_fasta.py -i [input] -l [loci] -o [output]'
            print 'Input is a fasta reference. Loci is a text file where each row contains a locus name (generally uce).'
            print 'The input should have the format ">[locus][other text]\\n[sequence]\\n".'
        elif opt in ("-i", "--input"):
            in_path = arg
        elif opt in ("-l", "--loci"):
            loci_path = arg
        elif opt in ("-o", "--output"):
            out_path = arg
    
    # reads input file as one string
    with open(in_path, 'r') as inFile:
        input = inFile.read()
    loci=[]
    # reads in loci
    with open(loci_path) as text:
        loci = text.readlines()
    # replaces each locus assuming format is >[locus][other text]\n[sequence]\n
    for i in loci:
        replace = '>' + i.rstrip() + '(.*)\\n([A-Z]|[a-z]|\\n)*'
        input = re.sub(replace, '', input)
    # writes output
    with open(out_path, 'w') as outFile:
        outFile.write(input)
if __name__ == '__main__':
    main(sys.argv[1:])
