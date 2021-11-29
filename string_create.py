class ReadFile:

    def create_string(self, s, indexes):
        for index in indexes:
            s = s[:index+1] + s + s[index+1: len(s)]
        return s


    def read_string(self, filename):
        '''
            filename: Path + filename of the input file
        '''
        # Read string from the filename provided as argument and remove the \n from the value
        with open(filename, 'r') as file:
            data = file.readlines()
            data = [i.replace('\n', '') for i in data]
        
        # Create s1 and s2 base strings along with indexes where the strings are supposed to be edited
        s1, s2, j, k = '', '', 0, 0
        s1_index, s2_index = [],  []
        for value in data:
            # If it is the first string, add it to s1 else add it to s2
            if value.isalpha() and s1 == '':
                s1 = value
            elif value.isalpha():
                s2 = value
            
            # If value is not string and is integer, add it to the respective indexes array 
            elif s1 != '' and s2 == '':
                s1_index.append(int(value))
                j += 1
            else:
                s2_index.append(int(value))
                k += 1
        
        # Format the string as required and check if the length matches with the given formula
        new_s1, new_s2 = self.create_string(s1, s1_index), self.create_string(s2, s2_index)
        
        assert len(new_s1) == len(s1) * (2 ** j), 'Mismatch Length'
        assert len(new_s2) == len(s2) * (2 ** k), 'Mismatch Length'
        
        return new_s1, new_s2


def write_output(output_filename, **kwargs):

    if kwargs.get('X_string') == None:
        kwargs['X_string'] = ''

    if kwargs.get('Y_string') == None:
        kwargs['Y_string'] = ''

    data = f'{kwargs.get("X_string")[:50]} {kwargs.get("X_string")[-50:]}\n{kwargs.get("Y_string")[:50]} {kwargs.get("Y_string")[-50:]}\n{kwargs.get("min_cost")}\n{kwargs.get("time")}\n{kwargs.get("memory")}'
    with open(output_filename, 'w') as file:
        file.write(data)
    
    return True

        
# Driver Code: returns tuple of s1, s2
# file_ops = ReadFile()
# print(file_ops.read_string('sample_test_cases/input1.txt'))
# write_output('xyz.txt', Y_string="world", time="0.002", memory="3000")