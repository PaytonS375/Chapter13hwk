'''
Design a creative UI using Python's tkinter module to calculate the total cost of a pizza.
The UI should have (at least) each widget that was covered in class:

    Frames
    Labels
    input box
    buttons
    radio buttons
    check boxes

You can use check boxes for for selecting toppings (each with a different cost),
radio buttons for the type of crust selected (each with a different cost), buttons for calculation and quit.

The input box can be used to record the name of the person placing the order.

Use a message box to display the total cost of the pizza along with the name of the person placing the order.

Make sure your design is well laid out and intuitive to the user. Take account of spacing and packing so that everything is properly aligned and professional looking. Be creative with font, color, size, etc.
'''

import tkinter
import tkinter.messagebox

class Pizza:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.shop_info_frame = tkinter.frame(self.main_window)
        self.order_name_frame = tkinter.frame(self.main_window)
        self.pizza_size_frame = tkinter.frame(self.main_window)
        self.crust_type_frame = tkinter.frame(self.main_window)
        self.sauce_type_frame = tkinter.frame(self.main_window)
        self.toppings_frame = tkinter.frame(self.main_window)
        self.command_buttons_frame = tkinter.frame(self.main_window)

        # shop info frame

        self.shop_name = tkinter.Label(self.shop_info_frame, text='JB Pizza Shop', font=('Times New Roman',20,'bold underline'), fg='blue')
        self.shop_name.pack(side='top')

        self.shop_info_frame.pack(side='top')

        # order name frame

        self.prompt_name_label = tkinter.Label(self.order_frame, text='Name for Order: ', font=('Times New Roman',10,'bold'))

        self.name_entry = tkinter.Entry(self.order_name_frame, width=20)

        self.prompt_name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.order_name_frame.pack(side='top')

        # pizza size frame

        self.pizza_size = tkinter.Label(self.pizza_size_frame, text='Pizza Size: ', font=('Times New Roman',10,'bold'))

        # pizza size buttons

        self.pizza_size_var = tkinter.IntVar()
        self.pizza_size_var.set(0)

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

        # crust size frame

        self.crust = tkinter.Label(self.crust_type_frame, text='Crust Type: ', font=('Times New Roman',10,'bold'))

        # crust size buttons

        self.crust_var = tkinter.IntVar()
        self.crust_var.set(0)

        self.regular = tkinter.Radiobutton(self.crust_type_frame, text='Regular: $0', variable=self.crust_var, value=0)
        self.thin = tkinter.Radiobutton(self.crust_type_frame, text='Thin: $2', variable=self.crust_var, value=2)
        self.brooklyn = tkinter.Radiobutton(self.crust_type_frame, text='Brooklyn: $4', variable=self.crust_var, value=4)

        self.crust.pack()

        self.regular.pack(side='left')
        self.thin.pack(side='left')
        self.brooklyn.pack(side='left')

        self.crust_type_frame.pack()

        # sauce type frame

        self.sauce = tkinter.Label(self.sauce_type_frame, text='Sauce Type: ', font=('Times New Roman',10,'bold'))

        # sauce type buttons

        self.sauce_var = tkinter.IntVar()
        self.sauce_var.set(0)

        self.marinara = tkinter.Radiobutton(self.sauce_type_frame, text='Marinara: $0', variable=self.sauce_var, value=0)
        self.white = tkinter.Radiobutton(self.sauce_type_frame, text='White: $2', variable=self.sauce_var, value=2)
        self.buffalo = tkinter.Radiobutton(self.sauce_type_frame, text='Buffalo: $4', variable=self.sauce_var, value=4)

        self.sauce.pack()

        self.marinara.pack(side='left')
        self.white.pack(side='left')
        self.buffalo.pack(side='left')

        self.sauce_type_frame.pack()

        # toppings frame

        self.toppings = tkinter.Label(self.toppings_frame, text='Select Toppings: ', font=('Times New Roman',10,'bold'))

        # toppings check boxes

        self.cheese = tkinter.IntVar()
        self.pepperoni = tkinter.IntVar()
        self.sausage = tkinter.IntVar()
        self.bacon = tkinter.IntVar()
        self.onions = tkinter.IntVar()

        # IntVar objects

        self.cheese.set(0)
        self.pepperoni.set(0)
        self.sausage.set(0)
        self.bacon.set(0)
        self.onions.set(0)

        self.cheese = tkinter.Checkbutton(self.toppings_frame, text='Cheese: $0', variable=self.cheese, value=0)
        self.pepperoni = tkinter.Checkbutton(self.toppings_frame, text='Pepperoni: $2', variable=self.pepperoni, value=2)
        self.sausage = tkinter.Checkbutton(self.toppings_frame, text='Sausage: $3', variable=self.sausage, value=3)
        self.bacon = tkinter.Checkbutton(self.toppings_frame, text='Bacon: $4', variable=self.bacon, value=4)
        self.onions = tkinter.Checkbutton(self.toppings_frame, text='Onions: $1', variable=self.onions, value=1)

        self.toppings_label.pack()

        self.cheese.pack(side='left')
        self.pepperoni.pack(side='left')
        self.sausage.pack(side='left')
        self.bacon.pack(side='left')
        self.onions.pack(side='left')

        self.toppings_frame.pack()

        # command buttons frame

        self.complete_order = tkinter.Button(self.command_buttons_frame, text='Order Complete', font=('Times New Roman',10,'bold'))
        self.quit_button = tkinter.Button(self.command_buttons_frame, text='Quit', command=self.main_window.destroy, font=('Times New Roman',10,'bold'))

        self.complete_order.pack(side='left')
        self.quit_button.pack(side='right')

        self.command_buttons_frame.pack()

        tkinter.mainloop()


    def order_complete(self):

        total = (self.pizza_size_var.get() + self.crust_var.get() + self.sauce_var.get() +
                self.cheese.get()*0 + self.pepperoni.get()*2 + self.sausage.get()*3 + self.bacon.get()*4 + self.onions.get()*1)

        tkinter.messagebox.showinfo('Order Summary', 'Name: ' + self.name_entry.get() + '\nTotal: $' + str(total))

        tkinter.mainloop()


JB_Pizza = Pizza()

print('moving on...')







