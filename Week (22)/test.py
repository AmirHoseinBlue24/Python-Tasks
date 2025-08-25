import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TitleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Title Web Finder")
        self.root.geometry("400x300")
        
        # ایجاد ویجت‌ها
        self.label = tk.Label(root, text="Website URL: ", font=('Arial', 12))
        self.label.pack(pady=10)
        
        self.url_entry = tk.Entry(root, width=40, font=('Arial', 10))
        self.url_entry.pack(pady=5)
        
        self.open_button = tk.Button(root, text="Opening Website", command=self.open_website, bg='#4CAF50', fg='white')
        self.open_button.pack(pady=15)
        
        self.result_label = tk.Label(root, text="", font=('Arial', 10))
        self.result_label.pack(pady=10)
        
        self.close_button = tk.Button(root, text="Exit", command=root.quit, bg='#f44336', fg='white')
        self.close_button.pack(pady=5)
    
    def open_website(self):
        url = self.url_entry.get()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            options = webdriver.ChromeOptions()
           # options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            
            title = driver.title
            self.result_label.config(text=f"Website Title: {title}")
            
            driver.quit()
            messagebox.showinfo("Succes", "Title Find")
        except Exception as e:
            messagebox.showerror("Error", f"Error: \n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TitleApp(root)
    root.mainloop()