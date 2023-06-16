from tkinter import filedialog
import pandas as pd
import random
import tkinter.messagebox as tk


def export_csv(data: dict):
    df = pd.read_csv('./assets/template_woo.csv')

    df.at[0, 'ID'] = random.randint(1e11, 1e12-1)
    df.at[0, 'SKU'] = data['sku']
    df.at[0, 'Name'] = data['name']
    df.at[0, 'Description'] = data['description']
    df.at[0, 'Regular price'] = data['regular_price']

    if 'categories' in data:
        cat_list = [x['name'] for x in data['categories']]
        df.at[0, 'Categories'] = ','.join(cat_list)
    if 'tags' in data:
        tags_list = [x['name'] for x in data['tags']]
        df.at[0, 'Tags'] = ','.join(tags_list)
    if 'meta_data' in data:
        df.at[0, 'Meta: fifu_list_url'] = data['meta_data'][0]['value']

    # Open file dialog to choose save location
    file_path = filedialog.asksaveasfile(defaultextension='.csv',
                                         filetypes=[('CSV Files', '*.csv')])
    if file_path:
        # Export DataFrame to CSV file
        df.to_csv(file_path.name, index=False)
        tk.showinfo(
            "Success!", f"Export CSV file thành công tới:\n{file_path.name}")
