import os

import pandas as pd

poem_id = 0
poet = "saadi"
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


def func(poem_id, book_name, number_of_poem, label, path_label, path_label_additional="", title_additional=""):
    count = 0
    for i in range(1, number_of_poem + 1):
        # if path_label_additional:
        #     filename = fr"{folder}\{poet}_divan-{poet}_{path_label}-{path_label_additional}_sh{i:0{len(str(number_of_poem))}}.txt"
        # else:
        filename = fr"{folder}\{poet}_{path_label}_sh{i:0{len(str(number_of_poem))}}.txt"

        if filename == "saadi__txt\\saadi_golestan_gbab8_sh007.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh023.txt" or \
                filename == "saadi__txt\\saadi_golestan_gbab8_sh027.txt" or \
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
                    if title_additional:

                        title = title_additional + " " + line.strip()

                    else:
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
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب اول)", number_of_poem=41, label=None, path_label="boostan_bab1",
    #                title_additional="بوستان - باب اول در عدل و تدبیر و رای\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب دوم)", number_of_poem=30, label=None, path_label="boostan_bab2",
    #                title_additional="بوستان - باب دوم در احسان\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب سوم)", number_of_poem=25, label=None, path_label="boostan_bab3",
    #                title_additional="بوستان - باب سوم در عشق و مستی و شور\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب چهارم)", number_of_poem=28, label=None, path_label="boostan_bab4",
    #                title_additional="بوستان - باب چهارم در تواضع\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب پنجم)", number_of_poem=15, label=None, path_label="boostan_bab5",
    #                title_additional="بوستان - باب پنجم در رضا\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب ششم)", number_of_poem=15, label=None, path_label="boostan_bab6",
    #                title_additional="بوستان - باب ششم در قناعت\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب هفتم)", number_of_poem=29, label=None, path_label="boostan_bab7",
    #                title_additional="بوستان - باب هفتم در عالم تربیت\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب هشتم)", number_of_poem=15, label=None, path_label="boostan_bab8",
    #                title_additional="بوستان - باب هشتم در شکر بر عافیت\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب نهم)", number_of_poem=22, label=None, path_label="boostan_bab9",
    #                title_additional="بوستان - باب نهم در توبه و راه صواب\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (باب دهم)", number_of_poem=4, label=None, path_label="boostan_bab10",
    #                title_additional="بوستان - باب دهم در مناجات و ختم کتاب\n")
    # poem_id = func(poem_id=poem_id, book_name="بوستان (نیایش خداوند)", number_of_poem=6, label=None, path_label="boostan_niyayesh",
    #                title_additional="بوستان - در نیایش خداوند\n")
    # poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=637, label="ghazal", path_label="divan_ghazals")
    # poem_id = func(poem_id=poem_id, book_name="قطعات", number_of_poem=20, label="ghete", path_label="divan_ghetes")
    # poem_id = func(poem_id=poem_id, book_name="ملحقات و مفردات", number_of_poem=27, label=None,
    #                path_label="divan_molhaghat")
    # poem_id = func(poem_id=poem_id, book_name="رباعیات", number_of_poem=146, label="robaee", path_label="divan_robaees")
    # poem_id = func(poem_id=poem_id, book_name="ترجیع‌ بند", number_of_poem=1, label="tarjee", path_label="divan_tarjee")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (دیباچه)", number_of_poem=1, label=None, path_label="golestan_dibache")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب اول)", number_of_poem=41, label=None, path_label="golestan_gbab1",
    #                title_additional="گلستان - باب اول در سیرت پادشاهان\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب دوم)", number_of_poem=48, label=None, path_label="golestan_gbab2",
    #                title_additional="گلستان - باب دوم در اخلاق درویشان\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب سوم)", number_of_poem=28, label=None, path_label="golestan_gbab3",
    #                title_additional="گلستان - باب سوم در فضیلت قناعت\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب چهارم)", number_of_poem=14, label=None, path_label="golestan_gbab4",
    #                title_additional="گلستان - باب چهارم در فواید خاموشی\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب پنجم)", number_of_poem=21, label=None, path_label="golestan_gbab5",
    #                title_additional="گلستان - باب پنجم در عشق و جوانی\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب ششم)", number_of_poem=9, label=None, path_label="golestan_gbab6",
    #                title_additional="گلستان - باب ششم در ضعف و پیری\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب هفتم)", number_of_poem=20, label=None, path_label="golestan_gbab7",
    #                title_additional="گلستان - باب هفتم در تأثیر تربیت\n")
    # poem_id = func(poem_id=poem_id, book_name="گلستان (باب هشتم)", number_of_poem=109, label=None, path_label="golestan_gbab8",
    #                title_additional="گلستان - باب هشتم در آداب صحبت\n")
    # poem_id = func(poem_id=poem_id, book_name="مواعظ - قصاید", number_of_poem=61, label="ghaside",
    #                path_label="mavaez_ghasides", title_additional="مواعظ - قصاید\n")
    # poem_id = func(poem_id=poem_id, book_name="مواعظ - غزلیات", number_of_poem=65, label="ghazal",
    #                path_label="mavaez_ghazal2", title_additional="مواعظ - غزلیات\n")
    # poem_id = func(poem_id=poem_id, book_name="مواعظ - قطعات", number_of_poem=226, label="ghete",
    #                path_label="mavaez_ghete2", title_additional="مواعظ - قطعات\n")
    # poem_id = func(poem_id=poem_id, book_name="مواعظ - مراثی", number_of_poem=7, label=None, path_label="mavaez_marasi",
    #                title_additional="مواعظ - مراثی\n")
    # poem_id = func(poem_id=poem_id, book_name="مواعظ - مثنویات", number_of_poem=46, label="masnavi",
    #                path_label="mavaez_masnaviat", title_additional="مواعظ - مثنویات\n")
    # poem_id = func(poem_id=poem_id, book_name="مواعظ - رباعیات", number_of_poem=56, label="robaee",
    #                path_label="mavaez_robaees2", title_additional="مواعظ - رباعیات\n")
    # poem_id = func(poem_id=poem_id, book_name="رسائل نثر", number_of_poem=6, label=None, path_label="nasr",
    #                title_additional="رسائل نثر\n")

    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=41, label=None,
                   path_label="boostan_bab1",
                   title_additional="بوستان - باب اول در عدل و تدبیر و رای")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=30, label=None,
                   path_label="boostan_bab2",
                   title_additional="بوستان - باب دوم در احسان")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=25, label=None,
                   path_label="boostan_bab3",
                   title_additional="بوستان - باب سوم در عشق و مستی و شور")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=28, label=None,
                   path_label="boostan_bab4",
                   title_additional="بوستان - باب چهارم در تواضع")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=15, label=None,
                   path_label="boostan_bab5",
                   title_additional="بوستان - باب پنجم در رضا")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=15, label=None,
                   path_label="boostan_bab6",
                   title_additional="بوستان - باب ششم در قناعت")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=29, label=None,
                   path_label="boostan_bab7",
                   title_additional="بوستان - باب هفتم در عالم تربیت")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=15, label=None,
                   path_label="boostan_bab8",
                   title_additional="بوستان - باب هشتم در شکر بر عافیت")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=22, label=None,
                   path_label="boostan_bab9",
                   title_additional="بوستان - باب نهم در توبه و راه صواب")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=4, label=None,
                   path_label="boostan_bab10",
                   title_additional="بوستان - باب دهم در مناجات و ختم کتاب")
    poem_id = func(poem_id=poem_id, book_name="بوستان", number_of_poem=6, label=None,
                   path_label="boostan_niyayesh",
                   title_additional="بوستان - در نیایش خداوند\n")
    poem_id = func(poem_id=poem_id, book_name="غزلیات", number_of_poem=637, label="ghazal", path_label="divan_ghazals")
    poem_id = func(poem_id=poem_id, book_name="قطعات", number_of_poem=20, label="ghete", path_label="divan_ghetes")
    poem_id = func(poem_id=poem_id, book_name="ملحقات و مفردات", number_of_poem=27, label=None,
                   path_label="divan_molhaghat")
    poem_id = func(poem_id=poem_id, book_name="رباعیات", number_of_poem=146, label="robaee", path_label="divan_robaees")
    poem_id = func(poem_id=poem_id, book_name="ترجیع‌ بند", number_of_poem=1, label="tarjee", path_label="divan_tarjee")
    poem_id = func(poem_id=poem_id, book_name="گلستان (دیباچه)", number_of_poem=1, label=None,
                   path_label="golestan_dibache")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=41, label=None,
                   path_label="golestan_gbab1",
                   title_additional="گلستان - باب اول در سیرت پادشاهان")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=48, label=None,
                   path_label="golestan_gbab2",
                   title_additional="گلستان - باب دوم در اخلاق درویشان")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=28, label=None,
                   path_label="golestan_gbab3",
                   title_additional="گلستان - باب سوم در فضیلت قناعت")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=14, label=None,
                   path_label="golestan_gbab4",
                   title_additional="گلستان - باب چهارم در فواید خاموشی")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=21, label=None,
                   path_label="golestan_gbab5",
                   title_additional="گلستان - باب پنجم در عشق و جوانی")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=9, label=None,
                   path_label="golestan_gbab6",
                   title_additional="گلستان - باب ششم در ضعف و پیری")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=20, label=None,
                   path_label="golestan_gbab7",
                   title_additional="گلستان - باب هفتم در تأثیر تربیت")
    poem_id = func(poem_id=poem_id, book_name="گلستان", number_of_poem=109, label=None,
                   path_label="golestan_gbab8",
                   title_additional="گلستان - باب هشتم در آداب صحبت")
    poem_id = func(poem_id=poem_id, book_name="مواعظ - قصاید", number_of_poem=61, label="ghaside",
                   path_label="mavaez_ghasides", title_additional="مواعظ - قصاید\n")
    poem_id = func(poem_id=poem_id, book_name="مواعظ - غزلیات", number_of_poem=65, label="ghazal",
                   path_label="mavaez_ghazal2", title_additional="مواعظ - غزلیات\n")
    poem_id = func(poem_id=poem_id, book_name="مواعظ - قطعات", number_of_poem=226, label="ghete",
                   path_label="mavaez_ghete2", title_additional="مواعظ - قطعات\n")
    poem_id = func(poem_id=poem_id, book_name="مواعظ - مراثی", number_of_poem=7, label=None, path_label="mavaez_marasi",
                   title_additional="مواعظ - مراثی\n")
    poem_id = func(poem_id=poem_id, book_name="مواعظ - مثنویات", number_of_poem=46, label="masnavi",
                   path_label="mavaez_masnaviat", title_additional="مواعظ - مثنویات\n")
    poem_id = func(poem_id=poem_id, book_name="مواعظ - رباعیات", number_of_poem=56, label="robaee",
                   path_label="mavaez_robaees2", title_additional="مواعظ - رباعیات\n")
    poem_id = func(poem_id=poem_id, book_name="رسائل نثر", number_of_poem=6, label=None, path_label="nasr")

    path = os.path.join('..', '..', '1_output_DataFrames', f'{poet}.csv')
    df.to_csv(path, encoding='utf-8', index=False)
