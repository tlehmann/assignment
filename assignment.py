"""Module docstring.
Readers, Sorters, Writers

-i <input filename>
-o <output filename>
-s "bubble", "quick", "insertion"
"""
import sys
import getopt

class Reader:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        f = open(self.filename)
        list = f.readlines()
        return(list)

class Sorter:
    def __init__(self, algo):
        self.algo = algo
        if algo == "bubble":
            self.internal_sorter = bubble_sorter
        elif algo == "quick":
            self.internal_sorter = quick_sorter
        elif algo == "insertion":
            self.internal_sorter = insertion_sorter
        else:
            self.internal_sorter = default_sorter

    def sort(self, list):
        sorted_list = self.internal_sorter(list)
        return(sorted_list)

class Writer:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, list):
        f = open(self.filename, "w")
        for s in list:
            f.write(s)

def bubble_sorter(list):
    swap_test = False
    for i in range(0, len(list) - 1):
        # as suggested by kubrick, makes sense
        swap_test = False
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # swap
            swap_test = True
        if swap_test == False:
            break
    return(list)

def quick_sorter(list):
    return [] if list==[]  else quick_sorter([x for x in list[1:] if x < list[0]]) + [list[0]] + quick_sorter([x for x in list[1:] if x >= list[0]])

def insertion_sorter(list):
    for i in range(1, len(list)):
        save = list[i]
        j = i
        while j > 0 and list[j - 1] > save:
            list[j] = list[j - 1]
            j -= 1
        list[j] = save
    return(list)

def default_sorter(list):
    m = sorted(list)
    return m

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:s:", ["input file", "output file", "sorter"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-i", "--ifilename"):
            input_filename = a
        elif o in ("-o", "--ofilename"):
            output_filename = a
        elif o in ("-s", "--sorter"):
            sort_algo = a


    print("input filename = " + input_filename)
    print("output filename = " + output_filename)
    print("sort algo = " + sort_algo)
    
    reader = Reader(input_filename)
    list = reader.read()
   
    s = Sorter(sort_algo)
    sorted_list = s.sort(list)

    w = Writer(output_filename)
    w.write(sorted_list)

if __name__ == "__main__":
    main()


