import os

import pandas as pd

poem_id = 0
poet = "bidel"
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
                    "دوبیتی‌ها", "اشعار منتسب"]


def func(poem_id, book_name, number_of_poem, label, path_label, start=1, end=0, path_label_additional="",
         title_additional=""):
    count = 0
    end = number_of_poem
    for i in range(start, end + 1):
        # if path_label_additional:
        #     filename = fr"{folder}\{poet}_divan-{poet}_{path_label}-{path_label_additional}_sh{i:0{len(str(number_of_poem))}}.txt"
        # else:
        filename = fr"{folder}\{poet}_{path_label}_sh{i:0{len(str(number_of_poem))}}.txt"

        if filename == "bahar__txt\\bahar_ghetebk_sh142.txt" or \
                filename == "bahar__txt\\bahar_manzoomebk_armaghanbk_sh111.txt" or \
                filename == "bahar__txt\\bahar_manzoomebk_armaghanbk_sh117.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh038.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh039.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh072.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh069.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh100.txt":
            # there is no such files
            continue

        poem_id += 1
        count += 1
        print(f"{poem_id} {label} {i}\n")
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
            print(abyat)
            if title == "":
                title = labels[label]

            new_row = {'poem_id': poem_id, 'book_name': book_name, 'count': count, 'title': title, 'verses': abyat,
                       "verse_number": verse_number, 'label': label, 'poet': poet}
            df.loc[len(df)] = new_row
        print("***************************************")
    return poem_id


if __name__ == "__main__":
    poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=2827, label="ghazal", path_label="ghazalbi")
    poem_id = func(poem_id=poem_id, book_name="ترجیعات", number_of_poem=1, label="tarjee", path_label="tarjee-band", title_additional="ترجیع‌بند")

    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
