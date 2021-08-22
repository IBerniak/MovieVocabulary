
class XmlParser:
    '''
    '''
    def __init__(
                 self,
                 sequence,
                 header='?xml version="1.0" encoding="utf-8"?',
                 method_name='methodResponse',
                 array_markers=['params'],
                 dict_markers=['struct'],
                 el_name_markers=['name'],
                 el_val_markers=['value'],
                 ignore_list=['string', 'int', 'double', '']
                 ):

        self.result_dict = {}
        path = []
        waiting_name = ''
        current_instance = self.result_dict
        path_markers = array_markers + dict_markers

        temp_sequence = sequence.split('<')
        sequence = []

        while temp_sequence:
            item = temp_sequence.pop(0)
            if item.startswith('/') and item.endswith('>'):
                if item[1:-1] in path_markers:
                    sequence.append('upper')
                else:
                    continue
            elif item.endswith('>'):
                sequence.append(item[0:-1])
            elif '>' in item:
                temp_list = item.split('>')
                if temp_list[0] in ignore_list:
                    sequence.append(temp_list[1])
                else:
                    sequence.append(temp_list[0])
                    sequence.append(temp_list[1])
            elif item[:-1] in ignore_list:
                continue
            else:
                sequence.append(item)

        for (item, index) in zip(sequence, range(len(sequence))):
            if item == 'upper':
                path.pop()
                current_instance = self.result_dict
                for step in path:
                    current_instance = current_instance[step]
            elif item in el_val_markers:
                if waiting_name:
                    # print('approved')
                    current_instance[waiting_name] = sequence[index+1]
                    waiting_name = ''
                elif isinstance(current_instance, dict):
                    current_instance['value'] = sequence[index+1]
                else:
                    current_instance.append(sequence[index+1])
            elif item in el_name_markers:
                waiting_name = sequence[index+1]
                current_instance[waiting_name] = None
            elif item in dict_markers:
                if isinstance(current_instance, dict):
                    key = dict_markers[dict_markers.index(item)]
                    current_instance[key] = {}
                    current_instance = current_instance[key]
                    path.append(key)
                else:
                    current_instance.append({})
                    index = len(current_instance) - 1
                    current_instance = current_instance[index]
                    path.append(index)
            elif item in array_markers:
                if isinstance(current_instance, dict):
                    key = array_markers[array_markers.index(item)]
                    current_instance[key] = []
                    current_instance = current_instance[key]
                    path.append(key)
                else:
                    current_instance.append([])
                    index = len(current_instance) - 1
                    current_instance = current_instance[index]
                    path.append(index)
            elif item == method_name:
                self.result_dict['Method Name'] = method_name
            elif item.startswith('?') and item.endswith('?'):
                headers = item.strip('?')
                self.result_dict['headers'] = headers
            else:
                continue

    def __repr__(self):
        return str(self.result_dict)

    def __iter__(self):
        return iter(self.result_dict)

    def print(self):

        def printed(sequence, indent='        ', count=0):

            if isinstance(sequence, dict):
                for key, value in sequence.items():
                    print(indent*count, key + ':', sep='', end=' ')
                    if isinstance(value, dict) or isinstance(value, list):
                        count += 1
                        print('\n')
                        printed(value, count=count)
                    else:
                        print(value)
            elif isinstance(sequence, list):
                for value in sequence:
                    if isinstance(value, dict) or isinstance(value, list):
                        count += 1
                        print('\n')
                        printed(value, count=count)
                    else:
                        print(indent*count, value + ':', sep='')

        printed(self.result_dict)

    def find(self, tag_name):
        def searching(sequence):
            answer = None
            if isinstance(sequence, dict):
                for key, value in sequence.items():
                    if isinstance(value, dict) or isinstance(value, list):
                        answer = searching(value) or answer
                    else:
                        if key == tag_name: return value
            elif isinstance(sequence, list):
                for value in sequence:
                    if isinstance(value, dict) or isinstance(value, list):
                        answer = searching(value) or answer
                    else:
                        continue
            return answer
        return searching(self.result_dict)
