import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.balance = 5000
        self.history = []
        
        root.title("ATM System")
        root.geometry("300x400")
        
        # Authentication
        self.pin = "1234"
        self.login_screen(root)

    def login_screen(self, root):
        self.clear_screen(root)
        tk.Label(root, text="Enter PIN:").pack(pady=10)
        self.pin_entry = tk.Entry(root, show="*")
        self.pin_entry.pack(pady=5)
        tk.Button(root, text="Login", command=lambda: self.authenticate(root)).pack(pady=10)
    
    def authenticate(self, root):
        if self.pin_entry.get() == self.pin:
            self.main_menu(root)
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def main_menu(self, root):
        self.clear_screen(root)
        tk.Label(root, text="ATM Main Menu").pack(pady=10)
        tk.Button(root, text="Balance Inquiry", command=self.show_balance).pack(pady=5)
        tk.Button(root, text="Deposit", command=lambda: self.transaction_screen(root, "Deposit")).pack(pady=5)
        tk.Button(root, text="Withdrawal", command=lambda: self.transaction_screen(root, "Withdraw")).pack(pady=5)
        tk.Button(root, text="Transaction History", command=self.show_history).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    def transaction_screen(self, root, action):
        self.clear_screen(root)
        tk.Label(root, text=f"{action} Amount:").pack(pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)
        tk.Button(root, text="Submit", command=lambda: self.process_transaction(root, action)).pack(pady=10)
        tk.Button(root, text="Back", command=lambda: self.main_menu(root)).pack(pady=10)

    def process_transaction(self, root, action):
        try:
            amount = float(self.amount_entry.get())
            if action == "Deposit":
                self.balance += amount
                self.history.append(f"Deposited: ${amount}")
            elif action == "Withdraw":
                if amount > self.balance:
                    messagebox.showerror("Error", "Insufficient funds")
                    return
                self.balance -= amount
                self.history.append(f"Withdrew: ${amount}")
            messagebox.showinfo("Success", f"{action} successful")
            self.main_menu(root)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def show_balance(self):
        messagebox.showinfo("Balance", f"Current Balance: ${self.balance}")

    def show_history(self):
        history_text = "\n".join(self.history) if self.history else "No transactions yet."
        messagebox.showinfo("Transaction History", history_text)

    def clear_screen(self, root):
        for widget in root.winfo_children():
            widget.destroy()

# Run the ATM system
root = tk.Tk()
app = ATM(root)
root.mainloop()
