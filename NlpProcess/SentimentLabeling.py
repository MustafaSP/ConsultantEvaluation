import re
import pandas as pd
import numpy as np
import torch
from torch.utils.data import DataLoader, SequentialSampler
from transformers import BertTokenizer
from NlpProcess.Train import BertClassifier, TensorDataset
import torch.nn.functional as F
from transformers import BertModel

def text_preprocessing(text):
    try:
        text = re.sub(r'(@.*?)[\s]', ' ', text)
        text = re.sub(r'([\'\"\.\(\)\!\?\\\/\,])', r' \1 ', text)
        text = re.sub(r'[^\w\text\?]', ' ', text)
        text = re.sub(r'([\;\:\|•«\n])', ' ', text)
        text = re.sub(r'\text+', ' ', text).strip()
        text = text.lower()

    except:
        pass

    if text == None or type(text) != str:
        return ""
    else:
        return text

def preprocessing_for_bert(data,tokenizer,MAX_LEN):
    input_ids = []
    attention_masks = []

    for sent in data:
        encoded_sent = tokenizer.encode_plus(
            text=text_preprocessing(sent),
            add_special_tokens=True,
            max_length=MAX_LEN,
            pad_to_max_length=True,
            return_attention_mask=True
        )

        # Add the outputs to the lists
        input_ids.append(encoded_sent.get('input_ids'))
        attention_masks.append(encoded_sent.get('attention_mask'))

    # Convert lists to tensors
    input_ids = torch.tensor(input_ids)
    attention_masks = torch.tensor(attention_masks)

    return input_ids, attention_masks


def bert_predict(model, test_dataloader,device):
    model.eval()

    all_logits = []
    for batch in test_dataloader:
        b_input_ids, b_attn_mask = tuple(t.to(device) for t in batch)[:2]

        with torch.no_grad():
            logits = model(b_input_ids, b_attn_mask)
        all_logits.append(logits)

    all_logits = torch.cat(all_logits, dim=0)

    probs = F.softmax(all_logits, dim=1).cpu().numpy()

    return probs

def labeling(comments, modelPath):

    if torch.cuda.is_available():
        device = torch.device("cuda")

    else:
        device = torch.device("cpu")

    MAX_LEN=64
    Model = torch.load(f=modelPath)
    tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-turkish-uncased', do_lower_case=True)

    inputs, masks = preprocessing_for_bert(comments, tokenizer,MAX_LEN)
    dataset = TensorDataset(inputs, masks)
    sampler = SequentialSampler(dataset)
    dataloader = DataLoader(dataset, sampler=sampler, batch_size=32)
    probs = bert_predict(Model, dataloader,device)
    results = [np.argmax(sublist) for sublist in probs]

    return results
