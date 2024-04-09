# dict = {"a":1,"b":2,"c":3,"d":4}
# pairs = zip(dict.keys(),dict.values())
# print(pairs)

# def average(values: list[float])->float:
#     return sum(values) / len(values)

# print(average(range(1,101)))

# t = list[str]
# print(type(t))
# l = t()
# print(type(l))
# print(type(1))
# print(type(1.1111111111111111111111111111111111111111111111111111111111111111111111111))
# print(type({}))
# print(type(()))
# print(type([]))

# print(repr(list[int]))

import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")
app.grid_columnconfigure(0,weight=1)

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0,column=0,padx=20,pady=20,sticky="ew")

app.mainloop()