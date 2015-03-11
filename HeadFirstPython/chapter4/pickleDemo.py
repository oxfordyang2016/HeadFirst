import pickle
import nester
try:
    with open('data.pickle','wb') as data_file:
        cities=["jim","loli","jax",["lax","pek","ctu",["3ua","3ub","3uc"],"ckg"],["sha","xmn","ljg"],"tmd"]
        pickle.dump(cities,data_file)
    with open('data.pickle','rb') as data_file:
        a_list = pickle.load(data_file)
        nester.print_list(a_list,True,0)
except IOError as err:
    print 'error occured when open file: ' + str(err)
except pickle.PickleError as p_err:
    print 'error occured when load file: ' + str(p_err)