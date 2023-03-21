import  tkinter as  tk
import  re
import  time
import  iliyasov_bubble
import  iliyasov_insertion
import  iliyasov_selection
import  iliyasov_shell
import  pyperclip


class inter_face:
    def __init__(self) -> None:
        root = tk.Tk()
        root.geometry("1440x720")

        bg_image = tk.PhotoImage(file="topo-blue-gradient.png")
        canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
        canvas.pack()
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        self.status_line = tk.Label(root,text="Строка состояния",font=('Arial', 9))
        self.status_line.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.05)
    
        self.input_field = tk.Entry(root,font=('Arial', 12), width= 70,)
        self.input_field.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.05)
        
        self.output_line = tk.Label(root,text="Выходные данные",font=('Arial', 9), wraplength = 960)
        self.output_line.place(relx=0.15, rely=0.8, relwidth=0.7, relheight=0.05)


        # создаем 5 кнопок с разными названиями
        button_bubble_sort      = tk.Button(
            root, text="bubble sort",font=("Arial", 12),bg="#ffffff",fg="#000000",command=self.initialize_bubble_sort
        )
        button_insertion_sort   = tk.Button(
            root, text="insertion sort", font=("Arial", 12), bg="#ffffff", fg="#000000", command=self.initialize_insertion_sort
        )
        button_selection_sort   = tk.Button(
            root, text="selection sort", font=("Arial", 12), bg="#ffffff", fg="#000000", command=self.initialize_selection_sort
        )
        button_shell_sort       = tk.Button(
            root, text="shell sort", font=("Arial", 12), bg="#ffffff", fg="#000000",command=self.initialize_shell_sort
        )
        

        # располагаем кнопки на окне
        button_bubble_sort.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
        button_insertion_sort.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.1)
        button_selection_sort.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.1)
        button_shell_sort.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.1)

        root.mainloop()

    def get_input_value(self):
        input_data = self.input_field.get()
        if len(input_data) == 0:
            self.status_line.configure(
                text    =   "Вы ничего не ввели",
                font    =   ('Arial', 9)
            )
        else:
            status_valid_data = True
            for char in input_data:
                if char == "-" or char == " ":
                    pass
                elif not char.isdigit():
                    status_valid_data = False
                    self.status_line.configure(
                        text = f"В введенных данных содержится символ ('{char}'), который не является числом.",
                        font    =   ('Arial', 9)
                    )
            if status_valid_data == True:
                list_numbers = [int(num) for num in re.findall(r'-?\d+', input_data)]

                self.status_line.configure(
                        text = f"Введенные данные определы как {list_numbers}",
                        font    =   ('Arial', 9)
                )
                return list_numbers

    def initialize_bubble_sort(self):
        start_time = time.time()
        data = self.get_input_value()
        if isinstance(data, list):
            sorted_data  = iliyasov_bubble.bubble_sort(data)
            pyperclip.copy(str(sorted_data).replace("[", "").replace("]", "").replace(",", ""))
            delay = round(time.time() - start_time, 3)
            self.status_line.configure(
                text    =   f"отсортированный массиив в буфере обмена (время на сортировку: {delay} сек.)",
                font    =   ('Arial', 9)
            )
            self.output_line.configure(
                text = f"{sorted_data}",
                font = ('Arial', 9)
            )

    def initialize_insertion_sort(self):
        start_time = time.time()
        data = self.get_input_value()
        if isinstance(data, list):
            sorted_data  = iliyasov_insertion.insertion_sort(data)
            pyperclip.copy(str(sorted_data).replace("[", "").replace("]", "").replace(",", ""))
            delay = round(time.time() - start_time, 3)
            self.status_line.configure(
                text    =   f"отсортированный массиив в буфере обмена (время на сортировку: {delay} сек.)",
                font    =   ('Arial', 9)
            )
            self.output_line.configure(
                text = f"{sorted_data}",
                font = ('Arial', 9)
            )

    def initialize_selection_sort(self):
        start_time = time.time()
        data = self.get_input_value()
        if isinstance(data, list):
            sorted_data  = iliyasov_selection.selection_sort(data)
            pyperclip.copy(str(sorted_data).replace("[", "").replace("]", "").replace(",", ""))
            delay = round(time.time() - start_time, 3)
            self.status_line.configure(
                text    =   f"отсортированный массиив в буфере обмена (время на сортировку: {delay} сек.)",
                font    =   ('Arial', 9)
            )
            self.output_line.configure(
                text = f"{sorted_data}",
                font = ('Arial', 9)
            )

    def initialize_shell_sort(self):
        start_time = time.time()
        data = self.get_input_value()
        if isinstance(data, list):
            sorted_data  = iliyasov_shell.shellSort(data)
            pyperclip.copy(str(sorted_data).replace("[", "").replace("]", "").replace(",", ""))
            delay = round(time.time() - start_time, 3)
            self.status_line.configure(
                text    =   f"отсортированный массиив в буфере обмена (время на сортировку: {delay} сек.)",
                font    =   ('Arial', 9)
            )
            self.output_line.configure(
                text = f"{sorted_data}",
                font = ('Arial', 9)
            )

inter_face()