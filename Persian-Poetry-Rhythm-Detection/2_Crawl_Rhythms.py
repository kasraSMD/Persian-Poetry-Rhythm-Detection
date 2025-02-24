import re
import shutil
import time
import pandas as pd
import os
import pickle
import urllib.parse
import requests
from bs4 import BeautifulSoup

name = "ouhadi"
poets_csv_folder = "1_output_DataFrames"
poet_df_path = f"{name}.csv"
base_url = "https://ganjoor.net/simi/"
save_csvs_folder = "2_output_RhythmDataFrames"
save_poet_folder = os.path.join(save_csvs_folder, name)
# Parameters
params = {
    "v": "",
    "a": 19,
    "c": 248,
    "page": 0,
    "l": "fa-IR",
    "f": 0
}

top_10_Rhythms = [
    "فعولن فعولن فعولن فعل (متقارب مثمن محذوف یا وزن شاهنامه)",
    "مفاعیلن مفاعیلن فعولن (هزج مسدس محذوف یا وزن دوبیتی)",
    "فاعلاتن فاعلاتن فاعلاتن فاعلن (رمل مثمن محذوف)",
    "فاعلاتن فاعلاتن فاعلن (رمل مسدس محذوف یا وزن مثنوی)",
    "مفاعلن فعلاتن مفاعلن فعلن (مجتث مثمن مخبون محذوف)",
    "مفعول فاعلات مفاعیل فاعلن (مضارع مثمن اخرب مکفوف محذوف)",
    "فعلاتن مفاعلن فعلن (خفیف مسدس مخبون)",
    "فعلاتن فعلاتن فعلاتن فعلن (رمل مثمن مخبون محذوف)",
    "مفاعیلن مفاعیلن مفاعیلن مفاعیلن (هزج مثمن سالم)",
    "مفعول مفاعیل مفاعیل فعولن (هزج مثمن اخرب مکفوف محذوف)"]

num_of_pages = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]


def convert_persian_to_english(persian_number):
    # Mapping of Persian digits to English digits
    persian_to_english = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9'
    }

    # Replace each Persian digit with its English counterpart
    english_number = ''.join(persian_to_english.get(ch, ch) for ch in persian_number)

    return english_number


if __name__ == "__main__":
    start_time = time.time()

    if os.path.exists(save_poet_folder):
        shutil.rmtree(save_poet_folder)
    os.makedirs(save_poet_folder)

    path = os.path.join(poets_csv_folder, f'{poet_df_path}')
    df = pd.read_csv(path)
    df["Rhythm"] = None
    for r, pages in zip(top_10_Rhythms, num_of_pages):
        page_is_not_fount = False
        deleted = []
        params['v'] = r
        total_poems = 0
        for page in range(1, pages + 1):
            if page_is_not_fount:
                page_is_not_fount = False
                break

            params['page'] = page

            encoded_params = urllib.parse.urlencode(params)
            full_url = f"{base_url}?{encoded_params}"
            response = requests.get(full_url)
            html_content = response.content

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")

            # Find all the elements with the class "sitem"
            sitem_elements = soup.find_all("div", class_="sitem")
            sitem_elements = [sitem for sitem in sitem_elements if sitem.get("class") == ["sitem"]]

            # Extract the text content from each "sitem" element
            for sitem_element in sitem_elements:
                sitem_text = sitem_element.get_text(strip=True)
                if sitem_text == "شعری با مشخصات مورد نظر شما پیدا نشد.":
                    page_is_not_fount = True
                    continue

                link = sitem_element.find('h2').find('a')
                if link:
                    # Get the text from the <a> tag
                    text = link.get_text(strip=True)
                    try:
                        text = text.strip().split(" » ")
                        # if len(text) == 4:
                        #     poet_name = text[0]
                        #     book_name = text[1] + "\n" + text[2]
                        #     title = text[3]
                        #
                        #     total_poems += 1
                        #     filtered_df = df.query('book_name == @book_name and title == @title')
                        # if len(text) == 3:
                        #     poet_name = text[0]
                        #     book_name = text[1]
                        #     if book_name == "جام جم":
                        #
                        #         title = text[2].split(" - ")[1].strip()
                        #         filtered_df = df.query('book_name == @book_name and title == @title')

                        if len(text) == 3:
                            poet_name = text[0]
                            book_name = text[1]
                            title = text[2]
                            filtered_df = df.query('book_name == @book_name and title == @title')

                        total_poems += 1

                        # Check if the filtered DataFrame is not empty
                        if not filtered_df.empty:
                            df.loc[filtered_df.index, 'Rhythm'] = r  # Update the 'Rhythm' column
                        else:
                            print("No matching rows found.")
                            print(book_name)
                            print(title)
                            deleted.append(f"{book_name} : {title}")
                            print()
                    except Exception as e:
                        print(e)

                    # print(df.loc[filtered_df.index, ['book_name']])
                    # print(df.loc[filtered_df.index, ['title']])
                    # print(df.loc[filtered_df.index, ['Rhythm']])
        print(f"{page - 2} " + r)
        dl = pd.DataFrame(deleted)
        dl.loc[0, "C1"] = total_poems

        # dl.to_csv(os.path.join(save_poet_folder, f'{r}_deleted.csv'), encoding='utf-8', index=False)
    df.to_csv(os.path.join(save_poet_folder, f'{poet_df_path}'), encoding='utf-8', index=False)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
