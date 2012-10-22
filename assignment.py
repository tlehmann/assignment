"""Module docstring.
Readers, Sorters, Writers

-i <input filename>
-o <output filename>
-s "bubble", "quick", insertion", "heap"
"""
import sys
import copy
import getopt
import heapq

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
        elif algo == "heap":
            self.internal_sorter = heap_sorter
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
    new_list = copy.copy(list)
    swap_test = False
    for i in range(0, len(new_list) - 1):
        # as suggested by kubrick, makes sense
        swap_test = False
        for j in range(0, len(new_list) - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]  # swap
            swap_test = True
        if swap_test == False:
            break
    return(new_list)

def quick_sorter(list):
    return [] if list==[]  else quick_sorter([x for x in list[1:] if x < list[0]]) + [list[0]] + quick_sorter([x for x in list[1:] if x >= list[0]])

def insertion_sorter(list):
    new_list = copy.copy(list)
    for i in range(1, len(new_list)):
        save = new_list[i]
        j = i
        while j > 0 and new_list[j - 1] > save:
            new_list[j] = new_list[j - 1]
            j -= 1
        new_list[j] = save
    return(new_list)

def heap_sorter(list):
    heap = []
    for element in list:
        heapq.heappush(heap, element)
    return_list =[]
    while heap:
        return_list.append(heapq.heappop(heap))
    return return_list

def default_sorter(list):
    m = sorted(list)
    return m

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:s:", ["help", "input file", "output file", "sorter"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    input_filename = None
    ouput_filename = None
    sort_algo = None

    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit()
        elif o in ("-i", "--ifilename"):
            input_filename = a
        elif o in ("-o", "--ofilename"):
            output_filename = a
        elif o in ("-s", "--sorter"):
            sort_algo = a

    if (not input_filename or not output_filename or not sort_algo):
        print "-i, -o, and -s arguments required, for help use --help"
        sys.exit(2)

    print("input filename = " + input_filename)
    print("output filename = " + output_filename)
    
    reader = Reader(input_filename)
    list = reader.read()
    print "Before:"
    print list
   
    s = Sorter(sort_algo)
    sorted_list = s.sort(list)

    w = Writer(output_filename)
    w.write(sorted_list)
    print "After:"
    print list

if __name__ == "__main__":
    main()


