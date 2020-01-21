import pickle
loadfile=open('save.dat', 'rb')
loadfavorites=pickle.load(loadfile)
loadfile.close()
print(loadfavorites)