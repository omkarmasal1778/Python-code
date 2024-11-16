import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.balance = 1000  # Starting balance
        self.root = root
        self.root.title("ATM")
        
        # Create the main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()
        
        # Welcome label
        self.welcome_label = tk.Label(self.main_frame, text="Welcome to the ATM", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)
        
        # Button to open balance window
        self.balance_button = tk.Button(self.main_frame, text="Check Balance", command=self.check_balance, width=20)
        self.balance_button.pack(pady=5)
        
        # Button to open deposit window
        self.deposit_button = tk.Button(self.main_frame, text="Deposit Money", command=self.deposit_money, width=20)
        self.deposit_button.pack(pady=5)
        
        # Button to open withdrawal window
        self.withdraw_button = tk.Button(self.main_frame, text="Withdraw Money", command=self.withdraw_money, width=20)
        self.withdraw_button.pack(pady=5)
        
        # Exit button
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=5)
        
    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")
    
    def deposit_money(self):
        self.clear_frame()
        
        self.amount_label = tk.Label(self.main_frame, text="Enter amount to deposit:")
        self.amount_label.pack(pady=5)
        
        self.amount_entry = tk.Entry(self.main_frame)
        self.amount_entry.pack(pady=5)
        
        self.deposit_confirm_button = tk.Button(self.main_frame, text="Deposit", command=self.confirm_deposit)
        self.deposit_confirm_button.pack(pady=5)
        
        self.back_button = tk.Button(self.main_frame, text="Back", command=self.back_to_main)
        self.back_button.pack(pady=5)
    
    def confirm_deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            messagebox.showinfo("Success", f"${amount} deposited successfully!")
            self.back_to_main()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
    
    def withdraw_money(self):
        self.clear_frame()
        
        self.amount_label = tk.Label(self.main_frame, text="Enter amount to withdraw:")
        self.amount_label.pack(pady=5)
        
        self.amount_entry = tk.Entry(self.main_frame)
        self.amount_entry.pack(pady=5)
        
        self.withdraw_confirm_button = tk.Button(self.main_frame, text="Withdraw", command=self.confirm_withdraw)
        self.withdraw_confirm_button.pack(pady=5)
        
        self.back_button = tk.Button(self.main_frame, text="Back", command=self.back_to_main)
        self.back_button.pack(pady=5)
    
    def confirm_withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0 or amount > self.balance:
                raise ValueError
            self.balance -= amount
            messagebox.showinfo("Success", f"${amount} withdrawn successfully!")
            self.back_to_main()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount or ensure sufficient balance.")
    
    def back_to_main(self):
        self.clear_frame()
        self.__init__(self.root)
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATM(root)
    root.mainloop()
