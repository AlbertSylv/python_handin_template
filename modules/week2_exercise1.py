

def print_file_content(file):
    with open(file) as file_object:
        for line in file_object:
           print(line.rstrip())
    




def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as write_file:
        for tup in lst:
                for element in tup:
                    write_file.write(str(element) + "\n")


def write_stuff_to_file(output_file, *args):
    with open(output_file, 'w') as write_file:
        for stuff in args:
                    write_file.write(str(stuff) + "\n")



def append_stuff_to_file(output_file, *args):
    with open(output_file, 'a') as write_file:
        for stuff in args:
                    write_file.write(str(stuff) + "\n")




def read_csv(input_file, output_file):
     with open(input_file, "r") as file_object:
                for line in file_object:
                     append_stuff_to_file(output_file, line)


