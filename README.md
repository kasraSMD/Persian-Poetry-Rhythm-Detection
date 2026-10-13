<div align="center">

# 🪶 Persian Poetry Rhythm Detection

### Classifying the metrical rhythm (*vazn*, وزن) of Persian verses with a fine-tuned **GPT2-FA**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Transformers](https://img.shields.io/badge/🤗_Transformers-GPT2--FA-FFD21E)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Accuracy](https://img.shields.io/badge/Test_Accuracy-90.39%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

*Bachelor's Project at the [University of Isfahan](https://comp.ui.ac.ir/)*

</div>

---

## 📖 About

Persian classical poetry follows strict metrical patterns known as **rhythms** or **meters** (*vazn*, وزن), such as the *Shahnameh* meter or the *dobeyti* meter. Recognizing the meter of a verse is traditionally done by hand with the rules of Persian prosody (*arud*).

This project treats meter recognition as a **text classification** problem. It builds a large dataset of verses by 13 classical and modern Persian poets, labels each poem with its meter, and fine-tunes the Persian GPT-2 model [`HooshvareLab/gpt2-fa`](https://huggingface.co/HooshvareLab/gpt2-fa) to predict one of the **10 most common meters** from a single hemistich (half-verse, *mesra'*).

### ✨ Highlights

| | |
|---|---|
| 🎯 **Task** | Single-hemistich → meter (10-class classification) |
| 🧠 **Model** | `GPT2ForSequenceClassification` on `HooshvareLab/gpt2-fa` (12 layers, 768 hidden size) |
| 📚 **Data** | 18,616 poems from 13 poets → 200,000 hemistichs |
| 🏆 **Result** | **90.39 % accuracy** and **90.35 % weighted F1** on 20,000 held-out hemistichs |

---

## 🧭 Pipeline

<div align="center">

<img src="./assets/pipeline.svg" alt="Project pipeline: build DataFrames, crawl rhythm labels, preprocess and split, fine-tune GPT2-FA" width="100%"/>

</div>

| Step | Location | What happens |
|:-:|---|---|
| **1** | `1_Create_DataFrames/` → `1_output_DataFrames/` | One script per poet reads that poet's poem text files and writes a CSV (`poem_id`, `book_name`, `count`, `title`, `verses`, `verse_number`, `label`, `poet`). |
| **2** | `2_Crawl_Rhythms.py` → `2_output_RhythmDataFrames/` | Scrapes [Ganjoor](https://ganjoor.net/simi/) rhythm search pages for the 10 target meters and writes the matching meter into a new `Rhythm` column, matching poems by book name and title. |
| **3a** | `3_VerseModelTraining/Verse_Model_Training.ipynb` | Merges all poets, removes unlabeled poems, cleans text, splits poems into verses and hemistichs, removes duplicates, balances the classes, and encodes the labels. |
| **3b** | same notebook | Fine-tunes GPT2-FA, saves the best checkpoint by validation accuracy, and reports metrics on the test set. |
| **Demo** | `3_VerseModelTraining/Rhythm_Predictor.ipynb` | Loads the trained model and predicts the meter of new verses. |

---

## 🗂️ Repository Structure

```text
Persian-Poem-Rhythm-Detection/
├── Persian-Poetry-Rhythm-Detection/
│   ├── 1_Create_DataFrames/          # Step 1: one folder per poet
│   │   ├── hafez/
│   │   │   ├── Hafez_DataFrame.py    #   builds the poet's CSV from the text files
│   │   │   └── hafez__txt/           #   poem .txt files (not tracked by git)
│   │   └── ... (13 poets)
│   ├── 1_output_DataFrames/          # Step 1 output: one CSV per poet
│   ├── 2_Crawl_Rhythms.py            # Step 2: scrape meter labels from Ganjoor
│   ├── 2_output_RhythmDataFrames/    # Step 2 output: CSVs with a "Rhythm" column
│   └── 3_VerseModelTraining/
│       ├── Verse_Model_Training.ipynb   # preprocessing, training, evaluation
│       ├── Rhythm_Predictor.ipynb       # inference demo
│       ├── VersesRhythm_DataFrame.csv   # balanced 100,000-verse dataset
│       └── Rhythm_Encoder.pkl           # fitted scikit-learn LabelEncoder
├── LICENSE
└── README.md
```

---

## 🗃️ Dataset

### Poets covered

| Folder | Poet | Poems collected | Poems with a meter label |
|---|---|--:|--:|
| `babataher` | Baba Taher | 368 | 368 |
| `bahar` | Bahar | 1,079 | 452 |
| `bidel` | Bidel Dehlavi | 2,828 | 2,406 |
| `ferdousi` | Ferdowsi | 624 | 624 |
| `hafez` | Hafez | 630 | 511 |
| `khajoo` | Khaju Kermani | 932 | 171 |
| `moulavi` | Molavi (Rumi) | 6,102 | 2,177 |
| `ouhadi` | Owhadi | 131 | 129 |
| `parvin` | Parvin E'tesami | 223 | 12 |
| `saadi` | Saadi | 1,811 | 939 |
| `saeb` | Saeb Tabrizi | 3,049 | 2,832 |
| `shahriar` | Shahriar | 188 | 94 |
| `vahshi` | Vahshi Bafqi | 651 | 358 |
| | **Total** | **18,616** | **11,073** |

Poems without a label among the 10 target meters are dropped.

### From poems to training samples

| Stage | Count |
|---|--:|
| Poems with a meter label | 11,073 |
| Verses (*bayt*) after text cleaning | 156,712 |
| Verses after removing duplicates | 156,299 |
| Verses after class balancing (sampling) | 100,000 |
| **Hemistichs** (each verse split into two) | **200,000** |
| ↳ Train / Validation / Test | 162,000 / 18,000 / 20,000 |

Each verse is cleaned of digits, Latin letters, punctuation and diacritics, then split at the `/` separator into two hemistichs. Both hemistichs inherit the verse's meter label.

### 🎼 The 10 meters (classes)
| Rhythm (وزن عروضی) | Code | Number of verses |
|---|:-:|--:|
| فاعلاتن فاعلاتن فاعلاتن فاعلن (رمل مثمن محذوف) | 0 | 13,102 |
| فاعلاتن فاعلاتن فاعلن (رمل مسدس محذوف یا وزن مثنوی) | 1 | 20,128 |
| فعلاتن فعلاتن فعلاتن فعلن (رمل مثمن مخبون محذوف) | 2 | 10,228 |
| فعلاتن مفاعلن فعلن (خفیف مسدس مخبون) | 3 | 11,502 |
| فعولن فعولن فعولن فعل (متقارب مثمن محذوف یا وزن شاهنامه) | 4 | 53,604 |
| مفاعلن فعلاتن مفاعلن فعلن (مجتث مثمن مخبون محذوف) | 5 | 11,010 |
| مفاعیلن مفاعیلن فعولن (هزج مسدس محذوف یا وزن دوبیتی) | 6 | 10,486 |
| مفاعیلن مفاعیلن مفاعیلن مفاعیلن (هزج مثمن سالم) | 7 | 9,950 |
| مفعول فاعلات مفاعیل فاعلن (مضارع مثمن اخرب مکفوف محذوف) | 8 | 10,231 |
| مفعول مفاعیل مفاعیل فعولن (هزج مثمن اخرب مکفوف محذوف) | 9 | 6,058 |
| **Total** | | **156,299** |

<div align="center">

<img src="https://github.com/kasraSMD/Persian-Poetry-Rhythm-Detection/blob/main/Persian-Poetry-Rhythm-Detection/assets/class_distribution_raw.svg" alt="Distribution of verses per meter code before balancing" width="55%"/>

*Distribution of verses per meter code (before balancing)*

</div>

Counts are verses (*bayt*) after text cleaning and duplicate removal, before balancing. For training, the larger classes were sampled down to about 10,000 verses each, which gives the 100,000-verse dataset described above.

<div align="center">

<img src="https://github.com/kasraSMD/Persian-Poetry-Rhythm-Detection/blob/main/Persian-Poetry-Rhythm-Detection/assets/class_distribution_after_balancing.svg" alt="Distribution of verses per meter code after balancing" width="55%"/>

*Distribution of verses per meter code (after balancing)*

</div>

</div>

After balancing, each verse is split into two hemistichs, which gives the final 200,000 samples used for training, validation and testing:

| Rhythm (وزن عروضی) | Code | Number of hemistichs |
|---|:-:|--:|
| فاعلاتن فاعلاتن فاعلاتن فاعلن (رمل مثمن محذوف) | 0 | 20,000 |
| فاعلاتن فاعلاتن فاعلن (رمل مسدس محذوف یا وزن مثنوی) | 1 | 22,000 |
| فعلاتن فعلاتن فعلاتن فعلن (رمل مثمن مخبون محذوف) | 2 | 20,000 |
| فعلاتن مفاعلن فعلن (خفیف مسدس مخبون) | 3 | 20,000 |
| فعولن فعولن فعولن فعل (متقارب مثمن محذوف یا وزن شاهنامه) | 4 | 25,984 |
| مفاعلن فعلاتن مفاعلن فعلن (مجتث مثمن مخبون محذوف) | 5 | 20,000 |
| مفاعیلن مفاعیلن فعولن (هزج مسدس محذوف یا وزن دوبیتی) | 6 | 20,000 |
| مفاعیلن مفاعیلن مفاعیلن مفاعیلن (هزج مثمن سالم) | 7 | 19,900 |
| مفعول فاعلات مفاعیل فاعلن (مضارع مثمن اخرب مکفوف محذوف) | 8 | 20,000 |
| مفعول مفاعیل مفاعیل فعولن (هزج مثمن اخرب مکفوف محذوف) | 9 | 12,116 |
| **Total** | | **200,000** |

<div align="center">

<img src="https://github.com/kasraSMD/Persian-Poetry-Rhythm-Detection/blob/main/Persian-Poetry-Rhythm-Detection/assets/verse.svg" alt="Distribution of hemistichs per meter code" width="55%"/>

*Distribution of hemistichs per meter code*

</div>

> 📌 **Data availability.** The raw poem `.txt` files are excluded from the repository (see `.gitignore`). The prepared CSV files for each stage are included, and the full dataset is available on request.

---

## 🤖 Model and Training

| Setting | Value |
|---|---|
| Base model | `HooshvareLab/gpt2-fa` |
| Head | `GPT2ForSequenceClassification` with 10 output labels |
| Trainable parameters | All (full fine-tuning) |
| Tokenizer | GPT2-FA tokenizer with an added `<pad>` token |
| Max sequence length | 20 tokens (padded or truncated) |
| Optimizer | AdamW, learning rate `2e-5` |
| Batch size | 32 |
| Epochs | Up to 50, with early stopping (patience 4) |
| Model selection | Best validation accuracy |
| Data split | Train(162,000) / Validation(18,000) / Test(20,000) |
| Hardware | GPU (A100 Google Colab) |

Training stopped after **41 epochs**. The best checkpoint reached **90.57 % validation accuracy** (epoch 36).

---

## 📊 Results

Evaluated on the **20,000-hemistich test set**:

| Metric | Score |
|---|--:|
| Accuracy | **90.39 %** |
| Precision (weighted) | 90.37 % |
| Recall (weighted) | 90.39 % |
| F1 (weighted) | 90.35 % |
| Loss | 0.7388 |

### Per-class report

| Code | Precision | Recall | F1 | Support |
|:-:|--:|--:|--:|--:|
| 0 | 0.91 | 0.88 | 0.89 | 2,021 |
| 1 | 0.90 | 0.92 | 0.91 | 2,153 |
| 2 | 0.88 | 0.80 | 0.84 | 2,016 |
| 3 | 0.89 | 0.87 | 0.88 | 2,013 |
| 4 | 0.95 | 0.97 | 0.96 | 2,576 |
| 5 | 0.87 | 0.93 | 0.90 | 2,027 |
| 6 | 0.92 | 0.92 | 0.92 | 1,964 |
| 7 | 0.95 | 0.97 | 0.96 | 1,994 |
| 8 | 0.88 | 0.88 | 0.88 | 1,992 |
| 9 | 0.85 | 0.86 | 0.85 | 1,244 |

The *Shahnameh* meter (4) and the *Hazaj musamman salim* meter (7) are recognized best (F1 0.96). Class 2 (*Ramal musamman makhbun mahzuf*) is the hardest (F1 0.84).

### Confusion matrix

<div align="center">

<img src="https://github.com/kasraSMD/Persian-Poetry-Rhythm-Detection/blob/main/Persian-Poetry-Rhythm-Detection/assets/confusion matrix.svg" alt="Confusion matrix on the test set" width="60%"/>

</div>

Most errors happen between metrically similar pairs, for example classes 1 and 3, and classes 0 and 2.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kasraSMD/Persian-Poem-Rhythm-Detection.git
cd Persian-Poem-Rhythm-Detection/Persian-Poetry-Rhythm-Detection
```

### 2. Install dependencies

```bash
pip install torch transformers scikit-learn pandas numpy seaborn matplotlib tqdm \
            requests beautifulsoup4 gdown jupyter
```

### 3. Run the pipeline

**Step 1: build a poet's DataFrame** (run from the poet's folder, with that poet's `*__txt` files in place):

```bash
cd 1_Create_DataFrames/hafez
python Hafez_DataFrame.py          # writes ../../1_output_DataFrames/hafez.csv
```

**Step 2: crawl rhythm labels** (run from `Persian-Poetry-Rhythm-Detection/`). Set `name = "<poet>"` at the top of `2_Crawl_Rhythms.py`, then:

```bash
python 2_Crawl_Rhythms.py          # writes 2_output_RhythmDataFrames/<poet>/<poet>.csv
```

**Step 3: train.** Open `3_VerseModelTraining/Verse_Model_Training.ipynb` (written for Google Colab with a GPU) and run it top to bottom.

> 💡 The DataFrame scripts use Windows-style paths (`folder\\file.txt`) because they were written on Windows.

### 4. Predict the meter of your own verses

**To access the trained model, follow this link:** [Download `verse_best_model.pt`]([https://drive.google.com/uc?id=1-PjHXhVjhTc-hDr1kLrfkw7VeWE-lmgC) (about 472 MB). You can also fetch it from the command line:

```bash
cd 3_VerseModelTraining
pip install gdown
gdown 1-PjHXhVjhTc-hDr1kLrfkw7VeWE-lmgC -O verse_best_model.pt
```

Put `verse_best_model.pt` next to `Rhythm_Encoder.pkl` (already in the repo), then open `3_VerseModelTraining/Rhythm_Predictor.ipynb`, or run this code from the same folder. Enter your own hemistichs in `verse_texts`:

```python
import pickle
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. Label encoder: maps class codes (0-9) back to meter names
with open("Rhythm_Encoder.pkl", "rb") as f:
    rhythm_encoder = pickle.load(f)

# 2. Tokenizer and fine-tuned GPT2-FA model
tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/gpt2-fa")
tokenizer.add_special_tokens({"pad_token": "<pad>"})

model = AutoModelForSequenceClassification.from_pretrained(
    "HooshvareLab/gpt2-fa", num_labels=len(rhythm_encoder.classes_)
)
model.config.pad_token_id = tokenizer.pad_token_id
model.load_state_dict(torch.load("verse_best_model.pt", map_location=device, weights_only=True))
model.to(device)
model.eval()


# 3. Dataset that tokenizes each hemistich (max 20 tokens)
class PersianPoemDataset(Dataset):
    def __init__(self, texts, tokenizer):
        self.texts = texts
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        enc = self.tokenizer(self.texts[item], return_tensors="pt", truncation=True,
                             max_length=20, padding="max_length")
        return {"input_ids": enc["input_ids"].squeeze(0),
                "attention_mask": enc["attention_mask"].squeeze(0)}


# 4. Your verses: one hemistich (mesra') per item
verse_texts = [
    "بیا تا گل برافشانیم و می در ساغر اندازیم",
    "نذر کردم گر از این غم به درآیم روزی",
    "چو دیدم روی تو مردانه گشتم",
]
loader = DataLoader(PersianPoemDataset(verse_texts, tokenizer), batch_size=1)


# 5. Predict
def prediction(model, data_loader):
    all_preds = []
    with torch.no_grad():
        for batch in data_loader:
            logits = model(batch["input_ids"].to(device),
                           attention_mask=batch["attention_mask"].to(device)).logits
            all_preds.extend(torch.argmax(logits, dim=1).cpu().numpy())
    return all_preds


preds = prediction(model, loader)
results_df = pd.DataFrame({
    "Verse": verse_texts,
    "Rhythm code": preds,
    "Predicted Rhythm Label": rhythm_encoder.inverse_transform(preds),
})
print(results_df)
```

In the demo notebook, the model classifies all **10 of 10** sample hemistichs correctly (three different meters).

---

## 🔭 Future Work

- Evaluate with a poet-level or poem-level split
- Cover more meters and sub-meters
- Compare against other Persian language models and rule-based *arud* tools
- Release a ready-to-use model on Hugging Face and a small web demo

---

## 🙏 Acknowledgements

- [HooshvareLab/gpt2-fa](https://huggingface.co/HooshvareLab/gpt2-fa), the Persian GPT-2 model used as the base
- [Ganjoor](https://ganjoor.net), the source of meter labels
- [Hugging Face Transformers](https://huggingface.co/docs/transformers) and [PyTorch](https://pytorch.org/)

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

<div align="center">

⭐ If you find this project useful, please consider giving it a star! ⭐

Made with ❤️ by [Kasra](https://github.com/kasraSMD)

</div>
