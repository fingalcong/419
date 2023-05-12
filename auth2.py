import sqlite3
import sys


conn = sqlite3.connect('419.db')

def createtable():
    c = conn.cursor()
    c2 = conn.cursor()
    c3 = conn.cursor()
    # print()
    c.execute('''CREATE TABLE if not exists USER
    (USER_NAME    TEXT   NOT NULL,
    password      TEXT     NOT NULL,
    domain        CHAR(50));''')
    c2.execute('''CREATE TABLE if not exists OBJECTS 
    (name    TEXT   NOT NULL,
    types    TEXT   NOT NULL);''')
    c3.execute('''CREATE TABLE if not exists ACCESS
    (operation  TEXT    NOT NULL,
    domain   TEXT    NOT NULL,
    types    TEXT    NOT NULL);''')
    conn.commit()

def AddUser(user,password):
    if user == '':
        exit("Error: username missing")
    c = conn.cursor()
    cursor = c.execute("SELECT USER_NAME ,password,domain from USER where USER_NAME = ?;",[user])
    for row in cursor:
        if row[0] == user:
            exit("Error: user exists")
    list1 = [user,password,'NULL']

    #c.execute("INSERT INTO USER (USER_NAME,password,domain) \
          #VALUES ('Paul', 'dsfadf','NULL')")

    #c.execute("INSERT INTO USER (USER_NAME,password,domain) \
     #         VALUES ('fingal', 'dfadf','NULL')")

    c.execute("INSERT INTO USER (USER_NAME,password,domain) \
             VALUES (?,?,?)",list1)
    conn.commit()
    return("Success")



def Authenticate(user,password):
    c = conn.cursor()
    cursor = c.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    #print (cursor)
    #if len(list(cursor)) == 0:
        #return("Error: No such user")
    for row in cursor:
        #if row[0] == None:
         #   return("Error: No such user")
        if row[0] == user:
            if row[1] != password:
                exit("Error: Bad password")
            else:
                return("Success")
    if len(list(cursor)) == 0:
        exit("Error: No such user")
    conn.commit()

def select(name1,name2):
    c = conn.cursor()
    cursor = c.execute("SELECT USER_NAME ,password,domain from USER where USER_NAME = ? or USER_NAME = ? ;",[name1,name2] )
    #cursor = c.execute("SELECT USER_NAME ,password from USER")
    for row in cursor:
        #print("ID = ", row[0])
        print("USER_NAME = ", row[0])
        print("password = ", row[1])
        print("domain = ", row[2])
       # print("SALARY = ", row[3], "\n")

    conn.commit()

def SetDomain(user,domain):
    c = conn.cursor()
    c1 = conn.cursor()
    cursor1 = c1.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    cursor = c.execute("SELECT USER_NAME, password, domain from USER where USER_NAME = ?;", [user])
    if domain == '':
        exit ("Error: missing domain")
    if len(list(cursor1)) == 0:
        exit ("Error: No such user")

    for row in cursor:
        if row[2] == 'NULL':
            c.execute("UPDATE USER set domain = ? where USER_NAME = ?;", [domain, user])
        else:
            list1 = [row[0], row[1], domain]
            print (list1)
            c.execute("INSERT INTO USER (USER_NAME,password,domain) \
                         VALUES (?,?,?)", list1)

        #c.execute("")
    conn.commit()
    return ("Success")
#    print
 #   "Total number of rows updated :", conn.total_changes

    #cursor = conn.execute("SELECT USER_NAME, password, domain  from USER")
    #for row in cursor:
     #   print ("USER_NAME = ", row[0])
      #  print ("password = ", row[1])
       # print ("domain = ", row[2])
    #conn.commit()

def DomainInfo(domain):
    c = conn.cursor()
    if domain == '':
        exit ('Error: missing domain')
    cursor = c.execute("SELECT USER_NAME from USER where domain = ?;", [domain])
    for row in cursor:
        print (row[0])

    conn.commit()

def SetType(objectname,type):
    c = conn.cursor()
    if objectname == '':
        exit ("Error: missing object")
    if type == '':
        exit ("Error: missing type")
    list2 = [objectname,type]
    c.execute("INSERT INTO OBJECTS (name,types) \
             VALUES (?,?)",list2)

    conn.commit()
    return ("Success")

def select_for_objects(name1,name2):
    c = conn.cursor()
    cursor = c.execute("SELECT name,types from OBJECTS where name = ? or name = ? ;",[name1,name2] )
    #cursor = c.execute("SELECT USER_NAME ,password from USER")
    for row in cursor:
        #print("ID = ", row[0])
        print("object_name = ", row[0])
        print("type = ", row[1])
        #print("domain = ", row[2])
       # print("SALARY = ", row[3], "\n")

    conn.commit()

def TypeInfo(type):
    c = conn.cursor()
    if type == '':
        exit('Error: missing type')
    cursor = c.execute("SELECT name from OBJECTS where types = ?;", [type])
    for row in cursor:
        print(row[0])

    conn.commit()

def AddAccess(operation,domain_name,type_name):
    c = conn.cursor()
    if operation == '':
        exit ('Error: missing operation')
    if domain_name == '':
        exit ('Error: missing domain')
    if type_name == '':
        exit ('Error: missing type')
    c.execute("INSERT INTO ACCESS (operation,domain,types) \
                     VALUES (?,?,?)", [operation, domain_name, type_name])
    conn.commit()
    return ("Success")

def CanAccess(operation,user,object):
    c0 = conn.cursor()
    c1 = conn.cursor()
    c2 = conn.cursor()

    cursor0 = c0.execute("select distinct domain,types from ACCESS where operation = ? ;", [operation])
    cursor1 = c1.execute("select distinct domain from USER where USER_NAME = ? ;", [user])
    cursor2 = c2.execute("select distinct types from OBJECTS where name = ? ;", [object])
    # print(cursor1[0][0])
    domainlist = []
    for row in cursor1:
        temp = str(row[0])  # domain
        domainlist.append(temp)
    #print(list)
    #domainlist = [domainlist.split for domainlist in list]
    #domainlist = (list.split(','))  # domain
    #print(domainlist)

    typelist = []
    for row in cursor2:
        # print("type = ", row[0])
        typelist.append(row[0])

    #print(domianlist)
    # print(typelist)
    for row in cursor0:
        # print("domainname = ", str(row[0]))
        # print("typename = ", str(row[1]))
        t1 = row[0]
        t2 = row[1]
        if (t1 in domainlist) & (t2 in typelist):
            conn.commit()
            return ("Success")
    conn.commit()
    return ("Error: Access denied")

#createtable()
#AddUser('peter','asdad')
#print(SetDomain('peter','fucker'))
#select('peter','Paul')
#select_for_objects('fifa','food')
#print(Authenticate('fingal','dfadf'))
#DomainInfo('son')
#TypeInfo('mp4')
#AddAccess('read','fkingson','pdf')
#print(CanAccess('read','peter','NBA'))
#SetType('NBA','txt')
#conn.close()

def execute(args):

    args_passed = len(args)
    if args_passed < 2:
        return ("not enough arguments")

    else:
        base_cmd = args[1].lower()

        if base_cmd == 'AddUser':
            if args_passed > 4:
                return ' Error: too many arguments for AddUser'
            elif args_passed < 4:
                return ' Error: not enough arguments for AddUser'

            return AddUser(args[2], args[3])

        elif base_cmd == 'Authenticate':
            if args_passed > 4:
                return ' Error: too many arguments for Authenticate'
            elif args_passed < 4:
                return ' Error: not enough arguments for Authenticate'

            return Authenticate(args[2], args[3])

        elif base_cmd == 'SetDomain':
            if args_passed > 4:
                return ' Error: too many arguments for SetDomain'
            elif args_passed < 4:
                return ' Error: not enough arguments for SetDomain'

            return SetDomain(args[2], args[3])

        elif base_cmd == 'DomainInfo':
            if args_passed != 3:
                return 'Error: Input argument DomainInfo domain'
            ans = DomainInfo(args[2])
            for item in ans:
                print(item)

        #return DomainInfo(args[2])

        elif base_cmd == 'SetType':
            if args_passed > 4:
                return ' Error: too many arguments for SetType'
            elif args_passed < 4:
                return ' Error: not enough arguments for SetType'

            return SetType(args[2], args[3])

        elif base_cmd == 'TypeInfo':
            if args_passed != 3:
                return 'Error: Input argument TypeInfo type'

            ans = TypeInfo(args[2])
            for item in ans:
                print(item)

        #return Typeinfo(args[2])

        elif base_cmd == 'AddAccess':
            if args_passed != 5:
                return 'Error: Input argument operation domain type'

            return AddAccess(args[2], args[3], args[4])

        elif base_cmd == 'CanAccess':
            if args_passed != 5:
                return 'Error: Input argument CanAccess operation user object'

            return CanAccess(args[2], args[3], args[4])

        #else:
            #return "make sure the command is correct"


def main():
    #if not os.path.exists('419.db'):
        #createtable()
    print(execute(sys.argv))


if __name__ == '__main__':  # pragma: no cover
    main()