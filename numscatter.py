import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_numbers_from_text_file(file_path):
    numbers = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = float(line.strip())
                numbers.append(number)
    except Exception as e:
        print(f"Hata: {e}")

    return numbers

def create_table_and_chart(numbers, chart_type):
    root = tk.Tk()
    root.title("Sayı Tablosu ve Grafik")

    frame = ttk.Frame(root)
    frame.pack()

    tree = ttk.Treeview(frame)
    tree["columns"] = ("Sayı", "Karesi", "Küpü")

    tree.heading("#0", text="İndex")
    tree.heading("Sayı", text="Sayı")
    tree.heading("Karesi", text="Karesi")
    tree.heading("Küpü", text="Küpü")

    tree.column("#0", width=50)
    tree.column("Sayı", width=100)
    tree.column("Karesi", width=100)
    tree.column("Küpü", width=100)

    for i, num in enumerate(numbers, start=1):
        tree.insert("", i, values=(num, num**2, num**3))

    tree.pack(padx=10, pady=10)

    fig, ax = plt.subplots()

    def update_chart(new_chart_type):
        ax.clear()
        if new_chart_type == 'Pie Chart':
            labels = ['Sayı', 'Karesi', 'Küpü']
            sizes = [sum(numbers), sum(num**2 for num in numbers), sum(num**3 for num in numbers)]
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.set_title('Pasta Grafiği')
        elif new_chart_type == 'Bar Plot':
            categories = ['Sayı', 'Karesi', 'Küpü']
            values = [sum(numbers), sum(num**2 for num in numbers), sum(num**3 for num in numbers)]
            ax.bar(categories, values, color=['blue', 'orange', 'green'])
            ax.set_title('Çubuk Grafiği')
        elif new_chart_type == 'Scatter Plot':
            x = list(range(1, len(numbers) + 1))
            ax.scatter(x, numbers, label='Scatter Plot', color='red', marker='o')
            ax.set_title('Nokta Grafiği')
        elif new_chart_type == 'Line Plot':
            x = list(range(1, len(numbers) + 1))
            ax.plot(x, numbers, label='Line Plot', color='purple')
            ax.set_title('Çizgi Grafiği')

        canvas.draw()

    # Düğmeleri ekleyin
    pie_chart_button = tk.Button(frame, text="Pie Chart", command=lambda: update_chart('Pie Chart'))
    pie_chart_button.pack(side=tk.LEFT, padx=5)

    bar_plot_button = tk.Button(frame, text="Bar Plot", command=lambda: update_chart('Bar Plot'))
    bar_plot_button.pack(side=tk.LEFT, padx=5)

    scatter_plot_button = tk.Button(frame, text="Scatter Plot", command=lambda: update_chart('Scatter Plot'))
    scatter_plot_button.pack(side=tk.LEFT, padx=5)

    line_plot_button = tk.Button(frame, text="Line Plot", command=lambda: update_chart('Line Plot'))
    line_plot_button.pack(side=tk.LEFT, padx=5)

    tree.pack(padx=10, pady=10)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()

if __name__ == "__main__":
    file_path = filedialog.askopenfilename(
        title="Bir metin dosyası seçin",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    numbers = read_numbers_from_text_file(file_path)

    if numbers:
        create_table_and_chart(numbers, 'Pie Chart')
