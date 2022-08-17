class depend:
    List_of_Dep = (
        "python3-pip",
        "rar",
        "unrar",  # pip and iptables not showing in linux
        "python3",
        "mc"
    )
    def __init__(self):
        for i in range(len(self.List_of_Dep)):
            try:
                bash("aptitude show " + self.List_of_Dep[i])

            except FileNotFoundError:
                ans = input("%s was not found , install? [y/n]" % self.List_of_Dep[i])
                if ans == "y":
                    install_depend(self.List_of_Dep[i])