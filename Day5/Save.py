import pickle
favorites={'food':'Meat',
'sport':['swimming', 'football'],
'Colour':'blue',
'Person':'Her'
}
savefile=open('save.dat','wb')
pickle.dump(favorites,savefile)
savefile.close()