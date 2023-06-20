from tkinter import filedialog
import pandas as pd
import random
import tkinter.messagebox as tk


def export_csv(data_list: list, categories: str, tags: str, upload_option: int):
    df = pd.read_csv('./assets/template_woo.csv')

    row_to_append = df.iloc[0]
    
    if len(data_list) == 0:
        tk.showerror(
            title="Empty products!", message="Bạn chưa chọn sản phẩm")
        return
    
    if upload_option == 0:
        tk.showerror(
            title="Upload option!", message="Bạn chưa chọn upload option")
        return

    for data in data_list:
        length = len(df)
        df.loc[length] = row_to_append

        df.at[length, 'ID'] = random.randint(1e10, 1e11-1)
        df.at[length, 'SKU'] = data['sku']
        df.at[length, 'Name'] = data['name']
        df.at[length, 'Description'] = data['description']
        df.at[length, 'Regular price'] = data['regular_price']

        df.at[length, 'Categories'] = categories
        df.at[length, 'Tags'] = tags

        if upload_option == 1:
            urls = [x['src'] for x in data['images']]
            df.at[length, 'Images'] = ','.join(urls)
            df.at[length, 'Meta: fifu_list_url'] = ''
        else:
            df.at[length, 'Meta: fifu_list_url'] = data['meta_data'][0]['value']

    # Delete the first row and reset index
    df.drop(0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Open file dialog to choose save location
    file_path = filedialog.asksaveasfile(defaultextension='.csv',
                                         filetypes=[('CSV Files', '*.csv')])
    if file_path:
        # Export DataFrame to CSV file
        df.to_csv(file_path.name, index=False)
        tk.showinfo(
            "Success!", f"Export CSV file thành công tới:\n{file_path.name}")


def merge_products_info() -> list:
    """
    This product load file products (CSV) and return a list of json:
    {
        'sku' : ..., 
        'name' : ..., 
        'images_list' : ...
    }

    Returns:
        list: list of product info (JSON)
    """
    # Open file
    filepath = filedialog.askopenfilename(initialdir="./", title="Select file",
                                          filetypes=(("CSV files", "*.csv*"), ("All files", "*.*")))

    products_out = []
    # File process
    df = pd.read_csv(filepath)
    num_rows = df.shape[0]
    for i in range(num_rows):
        product_list = df.iloc[i, :].values.tolist()

        product_dict = {
            'sku': '',
            'name': '',
            'images_list': ''
        }

        product_dict['sku'] = product_list[0]
        product_dict['name'] = product_list[1]

        tmp_lst = []
        for url in product_list[2:]:
            if isinstance(url, str) and url != 'nan':
                tmp_lst.append(url)
        product_dict['images_list'] = '|'.join(tmp_lst)
        products_out.append(product_dict)

    return products_out
