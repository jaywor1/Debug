from ast import arg

class Debug:
    def ok(*args):
        # If there is more than one argument function will assume that the first argument is action (makes it bold)
        if(len(args) == 1):
            print(f"[   \033[92mO.K\033[0m   ] {args[0]}")
        else:
            msg = args[1]
            for i in range(2,len(args)):
                msg += str(args[i])
            print(f"[   \033[92mO.K\033[0m   ] \033[1m{args[0]} \033[0m{msg}")

    def error(*args):
        # If there is more than one argument function will assume that the first argument is action (makes it bold)
        if(len(args) == 1):
            print(f"[  \033[91mERROR\033[0m  ] {args[0]}")
        else:
            msg = args[1]
            for i in range(2,len(args)):
                msg += str(args[i])
            print(f"[  \033[91mERROR\033[0m  ] \033[1m{args[0]} \033[0m{msg}")

    def log(*args):
        # If there is more than one argument function will assume that the first argument is action (makes it bold)
        if(len(args) == 1):
            print(f"[   \033[33mLOG\033[0m   ] {args[0]}")
        else:
            msg = args[1]
            for i in range(2,len(args)):
                msg += str(args[i])
            print(f"[   \033[33mLOG\033[0m   ] \033[1m{args[0]} \033[0m{msg}")