import os

import pandas as pd

poem_id = 0
poet = "babataher"
folder = fr"{poet}__txt"
columns = ['poem_id', 'book_name', 'count', 'title', 'verses', 'verse_number', 'label', 'poet']
df = pd.DataFrame(columns=columns)

labels = {
    "dobeyti": "دوبیتی",
    "ghazal": "غزل",
    "ghaside": "قصیده",
    "ghete": "قطعه",
    "masnavi": "مثنوی",
    "robaee": "رباعی",
    "tarjee": "ترجیع‌بند",
    "tarkib": "ترکیب‌بند",
}

book_labels_list = ["چهارپاره‌ها", "مسمطات", "ترجیعات", "رباعیات", "مثنویات", "قطعات", "قصاید", "غزلیات", "ترکیبیات", "دوبیتی‌ها", "اشعار منتسب"]


def func(poem_id, book_name, number_of_poem, path_label, label):
    count = 0
    for i in range(1, number_of_poem + 1):
        filename = fr"{folder}\{poet}_{path_label}_sh{i:0{len(str(number_of_poem))}}.txt"
        poem_id += 1
        count += 1
        print(f"{poem_id} {path_label} {i}\n")
        abyat = ""
        verse_number = 0
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if line_number == 4:
                    title = line.strip()
                if line_number >= 6:
                    verse_number += 1
                    abyat += line

                    # print(f"{beit[0]} {beit[1]}")
            print(abyat)

            if title == "":
                title = labels[label]
            new_row = {'poem_id': poem_id, 'book_name': book_name, 'count': count, 'title': title, 'verses': abyat,
                       "verse_number": verse_number, 'label': label, 'poet': poet}
            df.loc[len(df)] = new_row
        print("***************************************")
    return poem_id


if __name__ == "__main__":
    poem_id = func(poem_id=poem_id, book_name="دوبیتی‌ها", number_of_poem=366, path_label="2beytiha", label="dobeyti")
    poem_id = func(poem_id=poem_id, book_name="قصاید", number_of_poem=1, path_label="ghaside", label="ghaside")
    poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=1, path_label="ghazal", label="ghazal")

    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
