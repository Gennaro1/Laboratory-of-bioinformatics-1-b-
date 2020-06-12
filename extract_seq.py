# !/usr/bin/python
import sys

def get_ids(idfile):
    ids=open(idfile).read().rstrip().split("\n")
    return(ids)

def print_seqs(ids,dbfile):
    with open(dbfile, "r") as fdb: #IDK the meaning of the sintaxt "with open..."
        for line in fdb:
            if line[0]==">":
                #pid=line.split("|")[1] #If the fasta file is in the standard format, the ID of the sequences are between the "|"
                pid=line[1:].rstrip() #In the case the fasta file has been modified and "cleaned"
            if pid in ids: # You will put: if pid NOT IN ids: --> If you wanna extract whatever sequence is in the fasta file that is not in the list with the ID. Otherwise, if you wanna extract all the sequences in the fasta file for which you have the ID you put: if pid IN ids:
                print(line.rstrip())

if __name__=="__main__":
    idfile=sys.argv[1]  #sequence ID that you wanna find
    dbfile=sys.argv[2]  #fasta file with all the sequences
    ids=get_ids(idfile)
    fin=print_seqs(ids,dbfile)
    print(fin)
