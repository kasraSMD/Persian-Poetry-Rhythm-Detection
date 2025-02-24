import os

import pandas as pd

poem_id = 0
poet = "saeb"
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

def func(poem_id, book_name, number_of_poem, label, path_label, path_label_additional="", title_additional=""):
    count = 0
    for i in range(1, number_of_poem + 1):
        if path_label_additional:
            filename = fr"{folder}\{poet}_divan-{poet}_{path_label}-{path_label_additional}_sh{i:0{len(str(number_of_poem))}}.txt"
        else:
            filename = fr"{folder}\{poet}_divan-{poet}_{path_label}_sh{i:0{len(str(number_of_poem))}}.txt"

        if filename == "saeb__txt\\saeb_divan-saeb_matale_sh252.txt" or filename == "saeb__txt\\saeb_divan-saeb_motefarreghat_sh183.txt" or \
                filename == "saeb__txt\\saeb_divan-saeb_motefarreghat_sh609.txt":
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
    poem_id = func(poem_id=poem_id, book_name="قصاید", number_of_poem=45, label="ghaside", path_label="ghasayed")
    poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=180, label="ghazal", path_label="ghazal", path_label_additional="saeb")
    poem_id = func(poem_id=poem_id, book_name="غزلیات ترکی", number_of_poem=20, label="ghazal", path_label="ghtorki")
    poem_id = func(poem_id=poem_id, book_name="اشعار منتسب", number_of_poem=72, label=None, path_label="mansoobat")
    poem_id = func(poem_id=poem_id, book_name="مطالع", number_of_poem=515, label=None, path_label="matale")
    poem_id = func(poem_id=poem_id, book_name="متفرقات", number_of_poem=678, label=None, path_label="motefarreghat")
    poem_id = func(poem_id=poem_id, book_name="تک‌بیتهای برگزیده", number_of_poem=1542, label=None, path_label="takbeit")

    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
