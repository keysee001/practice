import os
import io


#count lines in a file


def countLines(rootDir):
     _totalCodeLines = 0
     fileType = ['.java', '.py', '.html', '.js']
     f= None
     lines=[]
     list_files = os.listdir(rootDir)
     for child in list_files:
         path = os.path.join(rootDir, child)
         if os.path.isdir(path):
             countLines(path)
         else:
             if os.path.splitext(path)[1] in fileType:
                 print os.path.splitext(path)[1]

                 try:
                     f=open(path,'r')
                     print 'the '+ path + 'is opened'
                 except:
                     print 'failed to open the file'
                 lines=f.readlines()
                 for line in lines:
                     line = line.strip()
                     if len(line)==0:
                         pass
                     else:
                         _totalCodeLines  = _totalCodeLines + 1    #code line increase
                 print 'the total code lines is of this file  '+ path + '  is '+ str(_totalCodeLines)

if __name__ == "__main__":
    countLines('C:\Users\kshi010\Desktop\MiTsuru-master')















