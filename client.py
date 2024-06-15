import socket
import threading
import tkinter as tk

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                message_list.insert(tk.END, message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_message(event=None):
    message = my_message.get()
    my_message.set("")  
    client_socket.send(message.encode('utf-8'))

def on_closing(event=None):
    client_socket.close()
    window.quit()

window = tk.Tk()
window.title("Chat Client")

messages_frame = tk.Frame(window)
my_message = tk.StringVar()
my_message.set("Type your messages here.")
scrollbar = tk.Scrollbar(messages_frame) 

message_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_list.pack(side=tk.LEFT, fill=tk.BOTH)
message_list.pack()
messages_frame.pack()

entry_field = tk.Entry(window, textvariable=my_message)
entry_field.bind("<Return>", send_message)
entry_field.pack()
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)

# Setup networking
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
tk.mainloop()
