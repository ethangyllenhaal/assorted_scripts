# assorted_scripts
These are assorted scripts I've made to perform basic tasks. Mostly a way for me to share these with people who want them.

### trim_fasta.py
This script takes in an input fasta (in original case a uce reference for https://github.com/mgharvey/seqcap_pop) with the format ">[locus][other text]\\n[sequence]\\n" and a locus file where each line is the locus name ([locus] in prior notation). The output has those sequences removed. A few basic modifications could also output the chose loci to a new file, but I haven't gotten around to that yet. Feel free to let me know if that's something you'd like and I can add an option for it.
