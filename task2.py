#Get symbols to delete.
input_string = input('Enter symbols: ')

#Number of deleted strings.
deleted_strings = 0

#Get array of file names.
filenames = []
for i in range(100):
    filenames.append(f'file{i+1}.txt')

with open('main_file.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                #Add line to the new file.
                if input_string not in line:
                    outfile.write(line)
                #Skip the line.
                else:
                    deleted_strings += 1
                    continue

print('Amount of deleted strings is ' + str(deleted_strings))
