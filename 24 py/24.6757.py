el = open('C:\\Users\\БАТЯ\\Downloads\\24_6757.txt').readline()
el = el.replace('CFE','*').replace('FCE','*').replace('C', ' ').replace('D', ' ').replace('E', ' ').replace('F',' ')
print(max(len(c) for c in el.split()))
