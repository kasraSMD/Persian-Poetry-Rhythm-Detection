from itertools import groupby

import pandas as pd

poem_id = 0
poet = "ferdousi"
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

        # if filename == "bahar__txt\\bahar_ghetebk_sh142.txt" or \
        #         filename == "bahar__txt\\bahar_manzoomebk_armaghanbk_sh111.txt" or \
        #         filename == "bahar__txt\\bahar_manzoomebk_armaghanbk_sh117.txt":
        #     # there is no such files
        #     continue

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

    ls = []
    folder_path = folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            new_name = filename[:-4]  # Remove the last 4 characters (.txt)
            new_name = new_name.split("_")
            # print(" ".join(new_name[0:len(new_name)-1]))
            ls.append(" ".join(new_name[0:len(new_name) - 1]))

    # print(ls)
    grouped_data = {key: list(group) for key, group in groupby(sorted(ls))}
    print(grouped_data.keys())
    for key, value in grouped_data.items():
        if len(value) == 17:
            print(key)

    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nآغاز کتاب", number_of_poem=12, label="masnavi",
                   path_label="shahname_aghaz")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nکیومرث", number_of_poem=2, label="masnavi",
                   path_label="shahname_qmars")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nهوشنگ", number_of_poem=3, label="masnavi",
                   path_label="shahname_hushang")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nطهمورث", number_of_poem=1, label="masnavi",
                   path_label="shahname_tahmoores")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nجمشید", number_of_poem=4, label="masnavi",
                   path_label="shahname_jamshid")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nضحاک", number_of_poem=12, label="masnavi",
                   path_label="shahname_zahak")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nفریدون", number_of_poem=20, label="masnavi",
                   path_label="shahname_fereydoon")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nمنوچهر", number_of_poem=28, label="masnavi",
                   path_label="shahname_manoochehr")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی نوذر", number_of_poem=13, label="masnavi",
                   path_label="shahname_nozar")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی زوطهماسپ", number_of_poem=1, label="masnavi",
                   path_label="shahname_zutahmasb")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی گرشاسپ", number_of_poem=5, label="masnavi",
                   path_label="shahname_garshasp")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nکیقباد", number_of_poem=5, label="masnavi",
                   path_label="shahname_kqobad")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی کی‌کاووس و رفتن او به مازندران", number_of_poem=17,
                   label="masnavi", path_label="shahname_kkavoos")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nرزم کاووس با شاه هاماوران", number_of_poem=12, label="masnavi",
                   path_label="shahname_hamavaran")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nسهراب", number_of_poem=21, label="masnavi",
                   path_label="shahname_sohrab")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان سیاوش", number_of_poem=22, label="masnavi",
                   path_label="shahname_siavosh")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی کیخسرو شصت سال بود", number_of_poem=1, label="masnavi",
                   path_label="shahname_kkhosro")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nگفتار اندر داستان فرود سیاوش", number_of_poem=1,
                   label="masnavi", path_label="shahname_forood")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان کاموس کشانی", number_of_poem=1, label="masnavi",
                   path_label="shahname_kamoos")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان خاقان چین", number_of_poem=1, label="masnavi",
                   path_label="shahname_khaghan")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان اکوان دیو", number_of_poem=1, label="masnavi",
                   path_label="shahname_akvan")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان بیژن و منیژه", number_of_poem=1, label="masnavi",
                   path_label="shahname_bizhan")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان دوازده رخ", number_of_poem=1, label="masnavi",
                   path_label="shahname_12rokh")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nجنگ بزرگ کیخسرو با افراسیاب", number_of_poem=1, label="masnavi",
                   path_label="shahname_mahmood")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی لهراسپ", number_of_poem=17, label="masnavi",
                   path_label="shahname_lohrasp")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی گشتاسپ صد و بیست سال بود", number_of_poem=33,
                   label="masnavi",
                   path_label="shahname_goshtasp")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان هفتخوان اسفندیار", number_of_poem=15,
                   label="masnavi",
                   path_label="shahname_7esfandyar")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان رستم و اسفندیار", number_of_poem=31,
                   label="masnavi",
                   path_label="shahname_esfandyar")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nداستان رستم و شغاد", number_of_poem=8,
                   label="masnavi",
                   path_label="shahname_shqad")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی بهمن اسفندیار صد و دوازده سال بود", number_of_poem=5,
                   label="masnavi",
                   path_label="shahname_bahman")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی همای چهرزاد سی و دو سال بود", number_of_poem=7,
                   label="masnavi",
                   path_label="shahname_homa")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی داراب دوازده سال بود", number_of_poem=4,
                   label="masnavi",
                   path_label="shahname_darab")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی دارای داراب چهارده سال بود", number_of_poem=10,
                   label="masnavi",
                   path_label="shahname_dara")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اسکندر", number_of_poem=47,
                   label="masnavi",
                   path_label="shahname_eskandar")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اشکانیان", number_of_poem=21,
                   label="masnavi",
                   path_label="shahname_ashkanian")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اردشیر", number_of_poem=14, label="masnavi",
                   path_label="shahname_ardeshir")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی شاپور پسر اردشیر سی و یک سال بود", number_of_poem=3,
                   label="masnavi", path_label="shahname_shapoor")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اورمزد", number_of_poem=2,
                   label="masnavi", path_label="shahname_oormazd")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی بهرام اورمزد", number_of_poem=2,
                   label="masnavi", path_label="shahname_bahram")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی بهرام نوزده سال بود", number_of_poem=1,
                   label="masnavi", path_label="shahname_bahram19")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی بهرام بهرامیان", number_of_poem=1,
                   label="masnavi", path_label="shahname_bahramian")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی نرسی بهرام", number_of_poem=1,
                   label="masnavi", path_label="shahname_nrsi")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اورمزد نرسی", number_of_poem=1,
                   label="masnavi", path_label="shahname_oorner")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی شاپور ذوالاکتاف", number_of_poem=16,
                   label="masnavi", path_label="shahname_zolaktaf")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اردشیر نکوکار", number_of_poem=1,
                   label="masnavi", path_label="shahname_nekookar")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی شاپور سوم", number_of_poem=1,
                   label="masnavi", path_label="shahname_shapoor3")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی بهرام شاپور", number_of_poem=1,
                   label="masnavi", path_label="shahname_bahpoor")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی یزدگرد بزه‌گر", number_of_poem=17,
                   label="masnavi", path_label="shahname_bezehgar")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی بهرام گور", number_of_poem=46,
                   label="masnavi", path_label="shahname_bahgoor")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی یزدگرد هجده سال بود", number_of_poem=4,
                   label="masnavi", path_label="shahname_yazdgerd")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی قباد چهل و سه سال بود", number_of_poem=2,
                   label="masnavi", path_label="shahname_qobad")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی کسری نوشین روان چهل و هشت سال بود", number_of_poem=12,
                   label="masnavi", path_label="shahname_anooshirvan")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی هرمزد دوازده سال بود", number_of_poem=10,
                   label="masnavi", path_label="shahname_hormozd")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی خسرو پرویز", number_of_poem=76,
                   label="masnavi", path_label="shahname_parviz")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی شیرویه", number_of_poem=6,
                   label="masnavi", path_label="shahname_shirooye")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی اردشیر شیروی", number_of_poem=2,
                   label="masnavi", path_label="shahname_ardeshiroo")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی فرایین", number_of_poem=1,
                   label="masnavi", path_label="shahname_farayeen")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی پوران دخت", number_of_poem=1,
                   label="masnavi", path_label="shahname_pooran")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی آزرم دخت", number_of_poem=1,
                   label="masnavi", path_label="shahname_azarmdokht")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی فرخ زاد", number_of_poem=1,
                   label="masnavi", path_label="shahname_farrokh")
    poem_id = func(poem_id=poem_id, book_name="شاهنامه\nپادشاهی یزدگرد", number_of_poem=17,
                   label="masnavi", path_label="shahname_yazdgerd3")

    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
