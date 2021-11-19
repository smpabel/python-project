import os
os.chdir('F:\pabel mail backup\Python work\First_Project\Coursera _Project\image')
i=1
for file in os.listdir():
      s=file
      d="smpp"+str(i)+".jpg"
      os.rename(s,d)
      i+=1
