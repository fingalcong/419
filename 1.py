def execute(args):

    args_passed = len(args)
    if args_passed < 2:
        exit ("not enough arguments")

    else:
        base_cmd = args[1].lower()

        if base_cmd == 'AddUser':
            if args_passed > 4:
                exit (' Error: too many arguments for AddUser')
            elif args_passed < 4:
                exit(' Error: not enough arguments for AddUser')

            print (AddUser(args[2], args[3]))

        elif base_cmd == 'Authenticate':
            if args_passed > 4:
                exit(' Error: too many arguments for Authenticate')
            elif args_passed < 4:
                exit(' Error: not enough arguments for Authenticate')

            print(Authenticate(args[2], args[3]))

        elif base_cmd == 'SetDomain':
            if args_passed > 4:
                exit ('Error: too many arguments for SetDomain')
            elif args_passed < 4:
                exit (' Error: not enough arguments for SetDomain')

            print(SetDomain(args[2], args[3]))

        elif base_cmd == 'DomainInfo':
            if args_passed != 3:
                exit('Error: Input argument DomainInfo domain')
            ans = DomainInfo(args[2])
            for item in ans:
                print(item)

        #return DomainInfo(args[2])

        elif base_cmd == 'SetType':
            if args_passed > 4:
                exit (' Error: too many arguments for SetType')
            elif args_passed < 4:
                exit (' Error: not enough arguments for SetType')

            print(SetType(args[2], args[3]))

        elif base_cmd == 'TypeInfo':
            if args_passed != 3:
                exit ('Error: Input argument TypeInfo type')

            ans = TypeInfo(args[2])
            for item in ans:
                print(item)

        #return Typeinfo(args[2])

        elif base_cmd == 'AddAccess':
            if args_passed != 5:
                exit ('Error: Input argument operation domain type')

            print ( AddAccess(args[2], args[3], args[4]))

        elif base_cmd == 'CanAccess':
            if args_passed != 5:
                print ('Error: Input argument CanAccess operation user object')

            print(CanAccess(args[2], args[3], args[4]))
        else :
            exit ('Error: too many arguments for Authenticate')