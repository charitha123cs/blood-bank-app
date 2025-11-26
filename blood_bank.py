import tkinter as tk
from tkinter import messagebox

# ------------------- Data Storage -------------------
donors = []

# ------------------- Functions -------------------
def register_donor():
    name = entry_name.get()
    blood_group = entry_blood.get()
    contact = entry_contact.get()
    city = entry_city.get()

    if not name or not blood_group or not contact or not city:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    donors.append({"name": name, "blood": blood_group, "contact": contact, "city": city})
    messagebox.showinfo("Success", f"Donor {name} registered successfully!")

    entry_name.delete(0, tk.END)
    entry_blood.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_city.delete(0, tk.END)


def search_donor():
    group = entry_search.get().upper()
    results = [d for d in donors if d["blood"].upper() == group]

    listbox_results.delete(0, tk.END)

    if results:
        for d in results:
            listbox_results.insert(
                tk.END,
                f"{d['name']} - {d['blood']} - {d['city']} – {d['contact']}"
            )
    else:
        listbox_results.insert(tk.END, "No donors found for this blood group.")


# ------------------- GUI Setup -------------------
root = tk.Tk()
root.title("Cloud-Based Blood Bank Management System")
root.geometry("700x500")
root.config(bg="#e3f2fd")

# ------------------- Title -------------------
title = tk.Label(
    root,
    text="🩸 Cloud-Based Blood Bank Management System",
    font=("Arial", 16, "bold"),
    bg="#e3f2fd",
    fg="#0d47a1"
)
title.pack(pady=10)

# ------------------- Donor Registration Frame -------------------
frame_reg = tk.LabelFrame(root, text="Donor Registration", bg="#bbdefb", font=("Arial", 12, "bold"))
frame_reg.pack(padx=10, pady=10, fill="x")

tk.Label(frame_reg, text="Name:", bg="#bbdefb").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(frame_reg, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_reg, text="Blood Group:", bg="#bbdefb").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_blood = tk.Entry(frame_reg, width=30)
entry_blood.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_reg, text="Contact No:", bg="#bbdefb").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_contact = tk.Entry(frame_reg, width=30)
entry_contact.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_reg, text="City:", bg="#bbdefb").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_city = tk.Entry(frame_reg, width=30)
entry_city.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_reg, text="Register Donor", bg="#0d47a1", fg="white", command=register_donor)\
    .grid(row=4, column=0, columnspan=2, pady=10)

# ------------------- Donor Search Frame -------------------
frame_search = tk.LabelFrame(root, text="Search Donor", bg="#c8e6c9", font=("Arial", 12, "bold"))
frame_search.pack(padx=10, pady=10, fill="x")

tk.Label(frame_search, text="Enter Blood Group:", bg="#c8e6c9").grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(frame_search, width=20)
entry_search.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_search, text="Search", bg="#1b5e20", fg="white", command=search_donor)\
    .grid(row=0, column=2, padx=10)

# ------------------- Results -------------------
listbox_results = tk.Listbox(root, width=80, height=10)
listbox_results.pack(pady=10)

root.mainloop()