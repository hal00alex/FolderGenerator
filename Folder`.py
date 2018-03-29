import os
def main():
  #lets me know it didn't crash on start 
  print "Hello Folders!\n"
  #home = "insert name of directoy here"
  for x in range(0, 3):
    name = home+"/Folder"+str(x)
    #check if folder exists
    if not os.path.exists(name):
      #create folder
      os.makedirs(name)
    #add file
    f = open(os.path.join(name, 'file.txt'), 'w')
    f.write('This is the new file.')
    f.close()
  #now go check if the folder and files are there
  print "Goodbye Master\n"
main()
