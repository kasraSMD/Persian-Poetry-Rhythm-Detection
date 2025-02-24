from itertools import groupby

import pandas as pd

poem_id = 0
poet = "khajoo"
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
    "charpare": "چهارپاره",
    "mosammat": "مسمط",
}
book_labels_list = ["چهارپاره‌ها", "مسمطات", "ترجیعات", "رباعیات", "مثنویات", "قطعات", "قصاید", "غزلیات", "ترکیبیات",
                    "دوبیتی‌ها", "اشعار منتسب", "منظومه‌ها"]


def func(poem_id, book_name, number_of_poem, label, path_label, start=1, end=0, path_label_additional="",
         title_additional=""):
    count = 0
    end = number_of_poem
    for i in range(start, end + 1):
        # if path_label_additional:
        #     filename = fr"{folder}\{poet}_divan-{poet}_{path_label}-{path_label_additional}_sh{i:0{len(str(number_of_poem))}}.txt"
        # else:
        filename = fr"{folder}\{poet}_{path_label}_sh{i:0{len(str(number_of_poem))}}.txt"

        if filename == "shahriar__txt\\shahriar_torki_sh03.txt" or \
                filename == "shahriar__txt\\shahriar_torki_sh06.txt":
            # there is no such files
            continue

        poem_id += 1
        count += 1
        # print(f"{poem_id} {label} {i}\n")
        abyat = ""
        verse_number = 0
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if line_number == 4:
                    title = title_additional + line.strip()
                if line_number >= 6:
                    verse_number += 1
                    abyat += line

                    # print(f"{beit[0]} {beit[1]}")
            # print(abyat)
            if title == "":
                title = labels[label]

            new_row = {'poem_id': poem_id, 'book_name': book_name, 'count': count, 'title': title, 'verses': abyat,
                       "verse_number": verse_number, 'label': label, 'poet': poet}
            df.loc[len(df)] = new_row
        # print("***************************************")
    return poem_id


if __name__ == "__main__":
    import os
    #
    # ls = []
    # folder_path = folder
    # for filename in os.listdir(folder_path):
    #     if filename.endswith('.txt'):
    #         new_name = filename[:-4]  # Remove the last 4 characters (.txt)
    #         new_name = new_name.split("_")
    #         # print(" ".join(new_name[0:len(new_name)-1]))
    #         ls.append(" ".join(new_name[0:len(new_name) - 1]))
    #
    # # print(ls)
    # grouped_data = {key: list(group) for key, group in groupby(sorted(ls))}
    # print(grouped_data.keys())
    # for key, value in grouped_data.items():
    #     if len(value) == 17:
    #         print(key)



    poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=932, label="ghazal",
                   path_label="ghazal-khajoo")



    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
