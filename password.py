import tkinter as tk
from tkinter import messagebox
import json
import os


def salveaza_parola():
    site = intrare_site.get().strip()
    email = intrare_email.get().strip()
    parola = intrare_parola.get().strip()

    if not site or not email or not parola:
        messagebox.showwarning("Atenție", "Te rog completează toate câmpurile!")
        return

    date_noi = {
        site: {
            "email": email,
            "parola": parola
        }
    }

    if not os.path.isfile("parole.json"):
        with open("parole.json", "w") as f:
            json.dump({}, f)

    try:
        with open("parole.json", "r") as f:
            date = json.load(f)

        date.update(date_noi)

        with open("parole.json", "w") as f:
            json.dump(date, f, indent=4)

        messagebox.showinfo("Succes", f"Datele pentru {site} au fost salvate!")

        intrare_site.delete(0, tk.END)
        intrare_parola.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Eroare", f"Nu s-a putut salva: {e}")


def cauta_parola():
    site = intrare_site.get().strip()
    if not os.path.isfile("parole.json"):
        messagebox.showinfo("Eroare", "Nu ai nicio parolă salvată încă.")
        return

    try:
        with open("parole.json", "r") as f:
            date = json.load(f)

        if site in date:
            email = date[site]["email"]
            parola = date[site]["parola"]
            messagebox.showinfo(site, f"Email: {email}\nParolă: {parola}")
        else:
            messagebox.showwarning("Oops", f"Nu am găsit date pentru {site}.")
    except Exception:
        messagebox.showerror("Eroare", "Eroare la citirea fișierului.")


fereastra = tk.Tk()
fereastra.title("My Passwords")
fereastra.geometry("400x500")
fereastra.configure(bg="#121212")

tk.Label(fereastra, text="🔑 Password Manager", font=("Arial", 20, "bold"), bg="#121212", fg="#BB86FC").pack(pady=30)

tk.Label(fereastra, text="Site / Aplicație:", bg="#121212", fg="white").pack()
intrare_site = tk.Entry(fereastra, width=35, bg="#1E1E1E", fg="white", insertbackground="white", borderwidth=0)
intrare_site.pack(pady=5, ipady=5)

tk.Label(fereastra, text="Email / Utilizator:", bg="#121212", fg="white").pack()
intrare_email = tk.Entry(fereastra, width=35, bg="#1E1E1E", fg="white", insertbackground="white", borderwidth=0)
intrare_email.pack(pady=5, ipady=5)
intrare_email.insert(0, "numele_tau@email.com")  

tk.Label(fereastra, text="Parolă:", bg="#121212", fg="white").pack()
intrare_parola = tk.Entry(fereastra, width=35, bg="#1E1E1E", fg="white", insertbackground="white", borderwidth=0,
                          show="*")
intrare_parola.pack(pady=5, ipady=5)

btn_cauta = tk.Button(fereastra, text="Caută după Site", width=30, bg="#03DAC6", fg="black", command=cauta_parola)
btn_cauta.pack(pady=10)

btn_salveaza = tk.Button(fereastra, text="Salvează Datele", width=30, bg="#BB86FC", fg="black", command=salveaza_parola)
btn_salveaza.pack(pady=10)

tk.Label(fereastra, text="Datele sunt salvate local în 'parole.json'", font=("Arial", 10, "italic"), bg="#121212",
         fg="#757575").pack(side="bottom", pady=20)

fereastra.mainloop()
