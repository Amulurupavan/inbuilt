enames = [{'id': 101, 'name': 'rahul', 'sal': 45000},
          {'id': 102, 'name': 'sonia', 'sal': 55000},
          {'id': 103, 'name': 'priya', 'sal': 65000},]

new_names=[]
#new_names=set()

for ename in enames:
    new_names.append(ename['name'])
    print(new_names)
    
    
#new_names=[]
new_names=set()

for id in enames:
    new_names.add(id['id'])
    print(new_names)