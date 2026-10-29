from torchvision import datasets #To load dataset
from datasets import Dataset, DatasetDict
import datasets
from datasets import load_dataset
import pandas as pd

# Load the dataset
def get_dataset(canary,num,ratio=0.005, shuffle=True):
    dataset_all = load_dataset("zicsx/Wikipedia-Hindi", split="train")
    sub_dataset = dataset_all.select(range(int(ratio * len(dataset_all)))) # no shuffling. Exact same examples selected every time

    split_ratio = 0.1 
    train_test_split = sub_dataset.train_test_split(test_size=split_ratio, seed=42)

    dataset = DatasetDict({
        'train': train_test_split['train'],
        'validation': train_test_split['test']
    })
    A=[]  
    for i in range(0,num):
        A.append(canary)

    canary_train = {"text": A}
    canary_eval={"text":[]}

    canaries = Dataset.from_dict(canary_train)
    canary_eval = Dataset.from_dict(canary_eval)

    canaries = DatasetDict({"train": canaries, "validation": canary_eval})

    dd = DatasetDict()
    dd = datasets.concatenate_datasets([
        canaries["train"],
        dataset["train"]
    ])
    if shuffle==True:
        dd=dd.shuffle(seed=42)
    dataset = DatasetDict({"train": dd, "validation": dataset["validation"]})
    train_df = pd.DataFrame(dataset["train"])
    print(train_df.head(5))

    return dataset