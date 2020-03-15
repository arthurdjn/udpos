# udpos
Universal Dependencies (UD) datasets converter and autodownloads sources.

# About

This repository contains UD preprocessed datasets for Part of Speech (POS) tasks. The datasets are converted 
from `.conllu` to `.txt` format. They can be downloaded using the `torch.datasets.sequence_tagging.SequenceTaggingDataset` class, 
just change the `urls` to the dataset of your choice.


# Example

The datasets follows the orginal template from the **Universal Dependencies English Treebank**, available [here](https://bitbucket.org/sivareddyg/public/downloads/en-ud-v2.zip). Create your custom `UDPOS` dataset using the language of your choice.
Replace the `urls` and saving directory `dirname` to extract the downloaded files. That's it !

```python
from torchtext.datasets import SequenceTaggingDataset

class UDPOSFR(SequenceTaggingDataset):
    # Universal Dependencies French Web Treebank.
    # Download original at http://universaldependencies.org/
    # License: http://creativecommons.org/licenses/by-sa/4.0/
    urls = ['https://github.com/arthurdjn/udpos/raw/master/data/fr-gsd-ud-15032020.zip'] # change to the dataset of your choice
    dirname = 'fr-gsd-ud'  # don't forget to change me too !
    name = 'udpos'         # not obligatory to change here

    @classmethod
    def splits(cls, fields, root=".data", 
               train="fr_gsd-ud-dev.txt",
               validation="fr_gsd-ud-dev.txt",
               test="fr_gsd-ud-dev.txt", **kwargs):
        """Downloads and loads the Universal Dependencies Version 2 POS Tagged
        data.
        """

        return super(UDPOS, cls).splits(
            fields=fields, root=root, train=train, validation=validation,
            test=test, **kwargs)
```

Then,
```python
from torchtext import data
import UDPOSFR

TEXT = data.Field(lower = True)
LEMMATIZED = data.Field(unk_token = None)
UD_TAGS = data.Field(unk_token = None)
fields = (("text", TEXT), ("lemmatized", LEMMATIZED), ("udtags", UD_TAGS))

# Load the UD french dataset
train_data, eval_data, test_data = UDPOSFR.splits(fields)
```



# Source

Original datasets available at [Universal Dependencies repository](https://github.com/UniversalDependencies) and on their [official website](https://universaldependencies.org/).
All rights reserved to [Universal Dependencies](https://universaldependencies.org/).
