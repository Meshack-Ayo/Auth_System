database = dict()

database["daniel"] = "password123"
def login(u_name, p_word):
    if u_name in database.keys():
        password = database.grt(u_name)
        if password == None or password  != p_word:
            print("Invalide Password")
        else:
            print("logges n Successfully")
    else:
        print("Invalide usename or password")           


def singnup(_name, p_word,p_word2):
    if p_word != p_word2:
        print(" The two password do not match")
    elif u_name in database.keys():
        print("This username is taken")    
    else:
        database[u_name] = p_word    



