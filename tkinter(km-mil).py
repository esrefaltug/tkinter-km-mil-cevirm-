import tkinter
import tkinter.messagebox
class Converter:
    def __init__(self):
        self.pencerem = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.labelim = tkinter.Label(self.top_frame,text='Mesafeyi giriniz(KM):')
        self.kilo_entry = tkinter.Entry(self.top_frame,width=5)
        self.labelim.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')

        self.calc_button = tkinter.Button(self.bottom_frame,text = 'ÇEVİR',command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,text = 'ÇIKIŞ',command = self.pencerem.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo*0.6214
        tkinter.messagebox.showinfo('sonuç: ',str(kilo) + 'kilometre = ' +str(miles)+ 'mile eşittir')

conv = Converter()
