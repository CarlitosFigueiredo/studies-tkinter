import tkinter as tk


def submit():
    # recupera os dados dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    # exibe os dados no console
    print(f"Nome: {nome}")
    print(f"Email: {email}")

# criar a janela principal
root = tk.Tk()
root.title("Formulário de Inscrição")

# cria um frame para conter os widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# labels e campos de entrada
lbl_nome = tk.Label(frame, text="Nome:")
lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")

nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

lbl_email = tk.Label(frame, text="Email:")
lbl_email.grid(row=1, column=0, padx=5, pady=5, sticky="e")

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# botão de submissão
submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

# inicializa o loop da GUI
root.mainloop()