from collections import OrderedDict
import csv



with open('selections.csv', 'rb') as f:
    reader = csv.reader(f)
    data_list = list(reader)

#OrderedDict: ID as key, Selections as list
data_dict = OrderedDict()
#the number of unregistered IDs submitted together
n_count = dict()
allocation_dict = {'A':[],'B':[],'C':[],'D':[]}




#for each first submission of ID put it in an ordered dict with its selections
for n in range(0,len(data_list)):
    count = 0
    if data_list[n][0] not in data_dict:
        data_dict[data_list[n][0]]=data_list[n][3:8]
        data_dict[data_list[n][0]].append(n)
        count += 1
    if data_list[n][1] != '':
        if data_list[n][1] not in data_dict:
            data_dict[data_list[n][1]]=data_list[n][3:8]
            data_dict[data_list[n][1]].append(n)
            count += 1
    if data_list[n][2] != '':
        if data_list[n][2] not in data_dict:
            data_dict[data_list[n][2]]=data_list[n][3:8]
            data_dict[data_list[n][2]].append(n)
            count += 1
    n_count[n] = count

print n_count

print data_dict


#check duplicated choices
for ID in data_dict:
        for n in data_dict[ID]:
            if data_dict[ID].count(n) > 1:
                print 'duplicated choices, please check/delete manually %s %s' %(ID,data_dict[ID])
                break

#allocate 75 spaces
for ID in data_dict:
    if len(allocation_dict[data_dict[ID][0]]) < 75:
        allocation_dict[data_dict[ID][0]].append(ID+' #1 '+str(data_dict[ID][4])+' '+str(data_dict[ID][5])+' '+str(n_count[data_dict[ID][5]]))
    elif len(allocation_dict[data_dict[ID][1]]) < 75:
        allocation_dict[data_dict[ID][1]].append(ID+' #2 '+str(data_dict[ID][4])+' '+str(data_dict[ID][5])+' '+str(n_count[data_dict[ID][5]]))
    elif len(allocation_dict[data_dict[ID][2]]) < 75:
        allocation_dict[data_dict[ID][2]].append(ID+' #3 '+str(data_dict[ID][4])+' '+str(data_dict[ID][5])+' '+str(n_count[data_dict[ID][5]]))
    elif len(allocation_dict[data_dict[ID][3]]) < 75:
        allocation_dict[data_dict[ID][3]].append(ID+' #4 '+str(data_dict[ID][4])+' '+str(data_dict[ID][5])+' '+str(n_count[data_dict[ID][5]]))


print '%s %i' %('A',len(allocation_dict['A']))
print allocation_dict['A']
print '%s %i' %('B',len(allocation_dict['B']))
print allocation_dict['B']
print '%s %i' %('C',len(allocation_dict['C']))
print allocation_dict['C']
print '%s %i' %('D',len(allocation_dict['D']))
print allocation_dict['D']