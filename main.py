from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, Scrollbar
from utils.woo_api import upload_product
from utils.woo_csv import export_csv
import sys 
import os 

if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')

def print_to_text(*args, **kwargs):
    end = kwargs.get("end", "")
    text = " ".join(map(str, args)) + end
    entry_terminal.insert("end", text)
    entry_terminal.see("end")  # Scroll to the bottom

# Redefine the print function
sys.stdout.write = print_to_text
sys.stderr.write = print_to_text

def relative_to_assets(path: str) -> Path:
    return "./assets/frame0" / Path(path)

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

    try:
        result = eval(values)
    except Exception as e:
        print(f'ERROR: {e}')
        return ''
    
    return result

def get_Text(textbox:Text) -> str:
    return textbox.get('1.0','end').strip()

def get_Entry(textbox: Entry) -> str:
    return textbox.get().strip()

def get_product_data(name:str, sku:str, price:str, description:str, images:str, categories:str, tags:str) -> dict:
    data = {
        "type": "simple",
        "sku": sku,
        "name": name,
        "status": "publish",
        "featured": False,
        "catalog_visibility": "visible",
        "short_description": "",
        "description": description,
        "tax_status": "taxable",
        "stock_status": "instock",
        "backorders": "no",
        "sold_individually": False,
        "regular_price": price
    }
    
    # Get the categories
    cat_list = []
    for category in categories.split(','):
        cat_list.append({
            "name": category
        })
    
    data["categories"] = cat_list
    
    # Get the tags
    tags_list = []
    for tag in tags.split(','):
        tags_list.append({
            "name": tag
        })
    
    data["tags"] = tags_list
    
    # Get the images
    meta_fifu_url = '|'.join(images.split('\n'))
    data["meta_data"] = [
            {
                "key": "fifu_list_url",
                "value": meta_fifu_url
            }
        ]
    
    return data

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

    terminal = canvas.create_rectangle(
        323.0,
        581.0,
        1252.0,
        702.0,
        fill="#FFFFFF",
        outline="")
    
    # Calculate the position of the rectangle
    x1, y1, x2, y2 = canvas.coords(terminal)

    # Calculate the position of the text box within the rectangle
    textbox_width = x2 - x1 - 10
    textbox_height = y2 - y1 - 10
    textbox_x = x1 + 5
    textbox_y = y1 + 5

    # Create the text widget
    global entry_terminal 
    entry_terminal = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Courier", 16 * -1),
    )
    entry_terminal.place(
        x=textbox_x, 
        y=textbox_y,
        width=textbox_width,
        height=textbox_height
    )
    
    scrollbar = Scrollbar()
    scrollbar.place(
        x=textbox_x + textbox_width -13,
        y=textbox_y,
        height=textbox_height
    )
    
    entry_terminal.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=entry_terminal.yview)
    
    entry_terminal.bind("<Key>", lambda e: "break")

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
    window.title("Woo Product Creator")

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
    entry_cookies = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Courier", 16 * -1),
    )
    entry_cookies.place(
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
    entry_domain = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_domain.place(
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
    entry_categories = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_categories.place(
        x=346.0,
        y=499.0,
        width=403.0,
        height=32.0
    )

    # SKU
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        466.5,
        164.0,
        image=entry_image_4
    )
    entry_sku = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_sku.place(
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
    entry_name = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_name.place(
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
    entry_description = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_description.place(
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
    entry_tags = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_tags.place(
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
    entry_images = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_images.place(
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
    entry_price = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=2,
        font=("Inter Regular", 16 * -1)
    )
    entry_price.place(
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
        command=lambda: upload_product(
            entry_terminal,
            get_Entry(entry_domain), 
            get_cookies_list(entry_cookies),
            get_product_data(
                name=get_Entry(entry_name),
                sku=get_Entry(entry_sku),
                price=get_Entry(entry_price),
                description=get_Text(entry_description),
                images=get_Text(entry_images),
                categories=get_Entry(entry_categories),
                tags=get_Entry(entry_tags)        
            )
        ),
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
        command=lambda: export_csv(
            get_product_data(
                name=get_Entry(entry_name),
                sku=get_Entry(entry_sku),
                price=get_Entry(entry_price),
                description=get_Text(entry_description),
                images=get_Text(entry_images),
                categories=get_Entry(entry_categories),
                tags=get_Entry(entry_tags)        
            )
        ),
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
