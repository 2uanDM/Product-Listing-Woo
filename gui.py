from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils.wooapi import APIKey, upload_product
from woocommerce import API

# Path to the assests
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_cookies_list(textbox: Text) -> list:
    values = textbox.get('1.0', 'end').strip()
    # Change true -> True
    while True:
        occur = values.find('true')
        if occur == -1:
            break
        else:
            values = values[:occur] + 'True' + values[occur+4:]

    # Change false -> False
    while True:
        occur = values.find('false')
        if occur == -1:
            break
        else:
            values = values[:occur] + 'False' + values[occur+5:]

    # Change null -> Null
    while True:
        occur = values.find('null')
        if occur == -1:
            break
        else:
            values = values[:occur] + 'None' + values[occur+4:]

    # Convert to list
    result = eval(values)

    return eval(values)


def get_product_data(name, ) -> dict:
    pass


def create_canvas(window: Tk) -> Canvas:
    # Background for the canvas
    canvas = Canvas(
        window,
        bg="#D9D9D9",
        height=720,
        width=1270,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        1.0,
        305.0,
        728.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        323.0,
        18.0,
        1252.0,
        565.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        323.0,
        581.0,
        1252.0,
        702.0,
        fill="#FFFFFF",
        outline="")

    return canvas

def text_cookies(canvas: Canvas) -> None:
    # Text Cookies
    canvas.create_text(
        14.0,
        308.0,
        anchor="nw",
        text="Cookies",
        fill="#000000",
        font=("RobotoRoman Regular", 18 * -1)
    )

def text_domain(canvas: Canvas) -> None:
    # Text Domain
    canvas.create_text(
        12.0,
        230.0,
        anchor="nw",
        text="Domain",
        fill="#000000",
        font=("RobotoRoman Regular", 18 * -1)
    )

def text_price(canvas: Canvas) -> None:
    canvas.create_text(
        964.0,
        111.0,
        anchor="nw",
        text="Price ($)",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )
    
def text_images(canvas: Canvas) -> None:
    canvas.create_text(
        801.0,
        204.0,
        anchor="nw",
        text="Images (Nếu có nhiều ảnh, mỗi link ảnh trên một dòng)",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )
    
def text_images(canvas: Canvas) -> None:
    canvas.create_text(
        801.0,
        204.0,
        anchor="nw",
        text="Images (Nếu có nhiều ảnh, mỗi link ảnh trên một dòng)",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )

def text_sku(canvas: Canvas) -> None:
    canvas.create_text(
            345.0,
            111.0,
            anchor="nw",
            text="SKU",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )
    
def text_name(canvas: Canvas) -> None: 
    canvas.create_text(
        655.0,
        111.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )

def test_description(canvas: Canvas) -> None:
    canvas.create_text(
        345.0,
        204.0,
        anchor="nw",
        text="Description",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )

def test_tags(canvas: Canvas) -> None: 
    canvas.create_text(
        801.0,
        467.0,
        anchor="nw",
        text="Tags (Cách nhau bởi dấu phẩy)",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )

def test_categories(canvas: Canvas) -> None:
    canvas.create_text(
        345.0,
        467.0,
        anchor="nw",
        text="Categories (Cách nhau bởi dấu phẩy) ",
        fill="#000000",
        font=("RobotoRoman SemiBold", 16 * -1)
    )

    
if __name__ == '__main__':
    # Initiate
    window = Tk()
    window.geometry("1270x720")
    window.configure(bg="#D9D9D9")

    # Create canvas background
    canvas = create_canvas(window)

    # Add logo
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png")
    )
    image_1 = canvas.create_image(
        152.0,
        118.0,
        image=image_image_1
    )
    
    # Product 1st
    canvas.create_rectangle(
        323.0,
        18.0,
        436.0,
        92.0,
        fill="#7F54B3",
        outline="")

    canvas.create_text(
        336.0,
        43.0,
        anchor="nw",
        text="Product 1",
        fill="#FFFFFF",
        font=("Helvatica Bold", 20 * -1)
    )

    canvas.create_text(
        462.0,
        43.0,
        anchor="nw",
        text="Mode: ",
        fill="#000000",
        font=("RobotoRoman SemiBold", 18 * -1)
    )

    canvas.create_text(
        598.0,
        43.0,
        anchor="nw",
        text="Basic",
        fill="#000000",
        font=("RobotoRoman SemiBold", 18 * -1)
    )

    canvas.create_rectangle(
        561.0,
        43.0,
        582.0,
        64.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        721.0,
        43.0,
        anchor="nw",
        text="Advance",
        fill="#000000",
        font=("RobotoRoman SemiBold", 18 * -1)
    )

    canvas.create_rectangle(
        684.0,
        43.0,
        705.0,
        64.0,
        fill="#D9D9D9",
        outline="")

    '''
        Text Box Field
    '''
    # Cookies entry
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png")
    )
    entry_bg_1 = canvas.create_image(
        152.5,
        484.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Courier", 16 * -1),
    )
    entry_1.place(
        x=20.0,
        y=342.0,
        width=265.0,
        height=282.0
    )

    # Domain entry
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png")
    )
    entry_bg_2 = canvas.create_image(
        152.5,
        281.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_2.place(
        x=20.0,
        y=265.0,
        width=265.0,
        height=31.0
    )

    # Categories entry
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        547.5,
        516.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_3.place(
        x=346.0,
        y=499.0,
        width=403.0,
        height=32.0
    )

    
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        466.5,
        164.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_4.place(
        x=346.0,
        y=147.0,
        width=241.0,
        height=32.0
    )
    
    # Name entry
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        775.5,
        164.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_5.place(
        x=655.0,
        y=147.0,
        width=241.0,
        height=32.0
    )
    
    # Description entry
    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        547.0,
        342.0,
        image=entry_image_6
    )
    entry_6 = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_6.place(
        x=345.0,
        y=240.0,
        width=404.0,
        height=202.0
    )

    # Tags entry
    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        1003.5,
        516.0,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_7.place(
        x=802.0,
        y=499.0,
        width=403.0,
        height=32.0
    )
    
    # Images entry
    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        1003.0,
        342.0,
        image=entry_image_8
    )
    entry_8 = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_8.place(
        x=801.0,
        y=240.0,
        width=404.0,
        height=202.0
    )

    # Price
    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        1084.5,
        164.0,
        image=entry_image_9
    )
    entry_9 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_9.place(
        x=964.0,
        y=147.0,
        width=241.0,
        height=32.0
    )

    '''
        Text
    '''
    text_cookies(canvas)
    text_domain(canvas)
    test_description(canvas)
    test_tags(canvas)
    text_sku(canvas)
    text_images(canvas)
    test_categories(canvas)
    text_price(canvas)
    text_name(canvas)

    '''
        Button
    '''
    # -- Upload
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png")
    )
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(get_cookies_list(entry_1)),
        relief="flat"
    )
    button_1.place(
        x=14.1260986328125,
        y=652.8167114257812,
        width=127.8072509765625,
        height=39.01483154296875
    )

    # -- Export CSV
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png")
    )
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(entry_2.get().strip()),
        relief="flat"
    )
    button_2.place(
        x=157.4046630859375,
        y=652.8167114257812,
        width=127.80718994140625,
        height=39.01483154296875
    )
    

    window.resizable(False, False)
    window.mainloop()
