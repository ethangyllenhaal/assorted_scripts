# assorted_scripts
These are assorted scripts I've made to perform basic tasks. Mostly a way for me to share these with people who want them.

### trim_fasta.py
This script takes in an input fasta (in original case a uce reference for https://github.com/mgharvey/seqcap_pop) with the format ">[locus][other text]\\n[sequence]\\n" and a locus file where each line is the locus name ([locus] in prior notation). The output has those sequences removed. A few basic modifications could also output the chose loci to a new file, but I haven't gotten around to that yet. Feel free to let me know if that's something you'd like and I can add an option for it.

### random_vcf.py
Script for trimming a vcf file to only include one random SNP per locus, which is needed for many pop gen analyses. Code partly inspired by scripts in the seqcap_pop pipeline (https://github.com/mgharvey/seqcap_pop). Assumes the input has a format of '[locus]_ID|<rest of line>' per seqcap_pop UCE SNPs in order to exclude UCE loci with multiple probes. If your format is only '[locus]|<rest of line>' comment lines with locus_list and remove from conditionals. If your format has a different locus name delimiter (e.g. '[locus]-'), change split char in assignment of locus variable.
