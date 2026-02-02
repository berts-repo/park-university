The # out lines explain the subsequent code.

#prepare to print table of select results
#set cell size, columns and get rows
cSize = 20
rows = cur.fetchall()
numberOfColumns = 14
#numberOfColumns = cur.field_count()
# Printing table headings
nDashes = 0
for field in cur.description:
#get field name
h = field[0]
#if the name is longer than the cell truncate it
if cSize < len(h):
h = h[:cSize]
#print the field name centered with bars to space the headings
print (h.center(cSize), ' | ', end='')
#add up the length of the field names to calculate length of dashed line
nDashes += cSize+4
print()
#print dashed line below the heading field names
print('-'*nDashes)
# Printing the rows of information
# rows is a list of list, each list is a row, step through the rows
for r in rows:
#check each item within the list for type and if it will fit in the cell
#then print it with a spaced bar after to make the table
for value in r:
v = str(value)
if type(v)== str:
if cSize < len(v):
v = v[:cSize]
print(v.rjust(cSize), ' | ', end='')
elif type(v) == int:
f="{:"+str(cSize)+"d}"
print(f.format(v), ' | ', end='')
elif type(v) == float:
f="{:"+str(cSize)+"f}"
print(f.format(v), ' | ', end='')
#after each row add a space and the dashed line
print()
print('-'*nDashes)
#after the printed table display the rows and columns
print('Number of Columns found:',numberOfColumns)
print('Number of Rows found:',len(rows))
conn.close()
