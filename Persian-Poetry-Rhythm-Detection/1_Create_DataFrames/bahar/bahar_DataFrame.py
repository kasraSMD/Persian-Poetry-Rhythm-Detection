import os
import pandas as pd

poem_id = 0
poet = "bahar"
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
book_labels_list = ["چهارپاره‌ها", "مسمطات", "ترجیعات", "رباعیات", "مثنویات", "قطعات", "قصاید", "غزلیات", "ترکیبیات", "دوبیتی‌ها", "اشعار منتسب"]


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
                filename == "bahar__txt\\bahar_manzoomebk_armaghanbk_sh117.txt":
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
    poem_id = func(poem_id=poem_id, book_name="چهارپاره‌ها", number_of_poem=8, label="charpare", path_label="4parebk")
    poem_id = func(poem_id=poem_id, book_name="گزیده اشعار - قصاید", number_of_poem=34, label="ghaside",
                   path_label="divanb_ghasideb")
    poem_id = func(poem_id=poem_id, book_name="گزیده اشعار - غزلیات", number_of_poem=10, label="ghazal",
                   path_label="divanb_ghazalb")
    poem_id = func(poem_id=poem_id, book_name="گزیده اشعار- قطعات", number_of_poem=1, label="ghete",
                   path_label="divanb_ghete")
    poem_id = func(poem_id=poem_id, book_name="گزیده اشعار - مثنویات", number_of_poem=6, label="masnavi",
                   path_label="divanb_masnaviatb")
    poem_id = func(poem_id=poem_id, book_name="گزیده اشعار - مسمطها", number_of_poem=4, label="mosammat",
                   path_label="divanb_mosammatha")
    poem_id = func(poem_id=poem_id, book_name="گزیده اشعار - رباعیات", number_of_poem=2, label="robaee",
                   path_label="divanb_robaeeb")

    poem_id = func(poem_id=poem_id, book_name="قصاید", number_of_poem=276, label="ghaside", path_label="ghasidebk")
    poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=101, label="ghazal", path_label="ghazalbk")
    poem_id = func(poem_id=poem_id, book_name="قطعات", number_of_poem=191, label="ghete", path_label="ghetebk")
    poem_id = func(poem_id=poem_id, book_name="منظومه‌ها - چهار خطابه", number_of_poem=4, label=None,
                   path_label="manzoomebk_4khatabe")
    poem_id = func(poem_id=poem_id, book_name="منظومه‌ها - ارمغان بهار", number_of_poem=118, start=2, label=None,
                   path_label="manzoomebk_armaghanbk")
    poem_id = func(poem_id=poem_id, book_name="منظومه‌ها - آیینۀ عبرت", number_of_poem=3, label=None,
                   path_label="manzoomebk_ayeene-ebrat")
    poem_id = func(poem_id=poem_id, book_name="منظومه‌ها - کارنامهٔ زندان", number_of_poem=88, label=None,
                   path_label="manzoomebk_karnamez")
    poem_id = func(poem_id=poem_id, book_name="منظومه‌ها - دل مادر", number_of_poem=8, label=None,
                   path_label="manzoomebk_madarbk")
    poem_id = func(poem_id=poem_id, book_name="منظومه‌ها - مذمت مگس (ذوبحرین)", number_of_poem=3, label=None,
                   path_label="manzoomebk_magas")
    poem_id = func(poem_id=poem_id, book_name="جنگ تهمورث با دیوها", number_of_poem=10, label=None,
                   path_label="manzoomebk_tbad")
    poem_id = func(poem_id=poem_id, book_name="مثنویات", number_of_poem=84, label="masnavi", path_label="masnavibk")
    poem_id = func(poem_id=poem_id, book_name="مسمطات", number_of_poem=22, label="mosammat",
                   path_label="mosammatbk")
    poem_id = func(poem_id=poem_id, book_name="رباعیات", number_of_poem=71, label="robaee",
                   path_label="robaeebk")
    poem_id = func(poem_id=poem_id, book_name="ترجیعات", number_of_poem=9, label="tarjee",
                   path_label="tarjeebk")
    poem_id = func(poem_id=poem_id, book_name="ترکیبیات", number_of_poem=13, label="tarkib",
                   path_label="tarkibbk")
    poem_id = func(poem_id=poem_id, book_name="تصنیف‌ها", number_of_poem=18, start=2, label=None,
                   path_label="tasnifbk")

    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
