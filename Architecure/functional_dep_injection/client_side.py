from server_side_one_func import API


class Client:
    def run(self):
        while True:
            command = input("Enter command: ")
            API(command)
            if command == "stop":
                break


client = Client()
client.run()
