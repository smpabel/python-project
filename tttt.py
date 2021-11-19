x = 'From marquard@uct.ac.za'
print(x[14:17])
print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475";
startPos = text.find(':')
piece = text[startPos+1:]
end = float(piece)
print(end)

tfile = open("test.txt")
count = 0
for i in tfile:
    count = count+1
    print(i)
print("total line in txt file:",count)

fname = input("Enter file name: ")
fh = open(fname)
u = fh.upper()
print(u)