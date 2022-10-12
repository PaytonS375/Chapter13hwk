from msilib.schema import RadioButton
import tkinter
import tkinter.messagebox

class JB_Pizza:

    def __init__(self):

        self.main_window = tkinter.Tk()

        self.shop_info_frame = tkinter.Frame(self.main_window)
        self.order_name_frame = tkinter.Frame(self.main_window)
        self.pizza_size_frame = tkinter.Frame(self.main_window)
        self.crust_type_frame = tkinter.Frame(self.main_window)
        self.sauce_type_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.command_buttons_frame = tkinter.Frame(self.main_window)


        self.shop_name = tkinter.Label(self.shop_info_frame, text='JB Pizza Shop', font=('Times New Roman',20,'bold underline'), fg='blue')
        self.shop_name.pack(side='top')

        self.shop_info_frame.pack(side='top')


        self.prompt_name_label = tkinter.Label(self.order_name_frame, text='Name for Order: ', font=('Times New Roman',10,'bold'))
        self.name_entry = tkinter.Entry(self.order_name_frame, width=20)

        self.prompt_name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.order_name_frame.pack(side='top')


        self.pizza_size = tkinter.Label(self.pizza_size_frame, text='Pizza Size: ', font=('Times New Roman',10,'bold'))
        self.pizza_size_var = tkinter.IntVar()

        self.small = tkinter.Radiobutton(self.pizza_size_frame, text='Small: $10', variable=self.pizza_size_var, value=10)
        self.medium = tkinter.Radiobutton(self.pizza_size_frame, text='Medium: $14', variable=self.pizza_size_var, value=14)
        self.large = tkinter.Radiobutton(self.pizza_size_frame, text='Large: $18', variable=self.pizza_size_var, value=18)
        self.extra_large = tkinter.Radiobutton(self.pizza_size_frame, text='Extra Large: $20', variable=self.pizza_size_var, value=20)

        self.pizza_size.pack()

        self.small.pack(side='left')
        self.medium.pack(side='left')
        self.large.pack(side='left')
        self.extra_large.pack(side='left')

        self.pizza_size_frame.pack()


        self.crust = tkinter.Label(self.crust_type_frame, text='Crust Type: ', font=('Times New Roman',10,'bold'))
        self.crust_var = tkinter.IntVar()

        self.regular = tkinter.Radiobutton(self.crust_type_frame, text='Regular: $0', variable=self.crust_var, value=0)
        self.thin = tkinter.Radiobutton(self.crust_type_frame, text='Thin: $2', variable=self.crust_var, value=2)
        self.brooklyn = tkinter.Radiobutton(self.crust_type_frame, text='Brooklyn: $4', variable=self.crust_var, value=4)

        self.crust.pack()

        self.regular.pack(side='left')
        self.thin.pack(side='left')
        self.brooklyn.pack(side='left')

        self.crust_type_frame.pack()


        self.sauce = tkinter.Label(self.sauce_type_frame, text='Sauce Type: ', font=('Times New Roman',10,'bold'))
        self.sauce_var = tkinter.IntVar()
        self.marinara = tkinter.Radiobutton(self.sauce_type_frame, text='Marinara: $0', variable=self.sauce_var, value=0)
        self.white = tkinter.Radiobutton(self.sauce_type_frame, text='White: $2', variable=self.sauce_var, value=2)
        self.buffalo = tkinter.Radiobutton(self.sauce_type_frame, text='Buffalo: $4', variable=self.sauce_var, value=4)

        self.sauce.pack()

        self.marinara.pack(side='left')
        self.white.pack(side='left')
        self.buffalo.pack(side='left')

        self.sauce_type_frame.pack()


        self.toppings_label = tkinter.Label(self.toppings_frame, text='Select Toppings: ', font=('Times New Roman',10,'bold'))
        self.cheese = tkinter.IntVar()
        self.pepperoni = tkinter.IntVar()
        self.sausage = tkinter.IntVar()
        self.bacon = tkinter.IntVar()
        self.onions = tkinter.IntVar()

        self.cheese.set(0)
        self.pepperoni.set(0)
        self.sausage.set(0)
        self.bacon.set(0)
        self.onions.set(0)

        self.cheese = tkinter.Checkbutton(self.toppings_frame, text='Cheese: $0', variable=self.cheese)
        self.pepperoni = tkinter.Checkbutton(self.toppings_frame, text='Pepperoni: $2', variable=self.pepperoni)
        self.sausage = tkinter.Checkbutton(self.toppings_frame, text='Sausage: $3', variable=self.sausage)
        self.bacon = tkinter.Checkbutton(self.toppings_frame, text='Bacon: $4', variable=self.bacon)
        self.onions = tkinter.Checkbutton(self.toppings_frame, text='Onions: $1', variable=self.onions)

        self.toppings_label.pack()

        self.cheese.pack(side='left')
        self.pepperoni.pack(side='left')
        self.sausage.pack(side='left')
        self.bacon.pack(side='left')
        self.onions.pack(side='left')

        self.toppings_frame.pack()

        def order_complete():
        
            total = 0

            RadioButtonTotal = (self.pizza_size_var.get() + self.crust_var.get() + self.sauce_var.get())

            CheckboxTotal = 0

            if self.cheese == 1:
                CheckboxTotal += 0

            if self.pepperoni == 1:
                CheckboxTotal += 2

            if self.sausage == 1:
                CheckboxTotal += 3

            if self.bacon == 1:
                CheckboxTotal += 4

            if self.onions == 1:
                CheckboxTotal += 1

            tkinter.messagebox.showinfo('Order Summary', 'Name: ' + self.name_entry.get() + '\nTotal: $' + str(RadioButtonTotal + CheckboxTotal))


        self.complete_order = tkinter.Button(self.command_buttons_frame, text='Order Complete', font=('Times New Roman',10,'bold'), command=order_complete)
        self.quit_button = tkinter.Button(self.command_buttons_frame, text='Quit', command=self.main_window.destroy, font=('Times New Roman',10,'bold'))

        self.complete_order.pack(side='left')
        self.quit_button.pack(side='right')

        self.command_buttons_frame.pack()

        tkinter.mainloop()


Pizza = JB_Pizza()