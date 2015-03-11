def print_list(in_list,indent=False,level=0):
    for p_list in in_list:
        if isinstance(p_list,list):
            print_list(p_list,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print "\t",
            print(p_list)
            
if __name__=="__main__":
    cities=["jim","loli","jax",["lax","pek","ctu",["3ua","3ub","3uc"],"ckg"],["sha","xmn","ljg"],"tmd"]
    print_list(cities,True,0)