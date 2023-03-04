class Command:
    def __int__(self):
        pass

    def ping(self, xxx: str):
        return str("ping " + xxx)

command = Command()
print(command.ping("119.91.141.182"))
