# Trumpifyve

T5 based model to translate text into Donald Trump's characteristic style. 

## Details

We use a novel back-translation scheme for unsupervised style transfer.

We use a pair of pretrained neural machine translation models[0] to round trip translate a corpus of text samples[1] from the style target, in our case Donald J. Trump. We then train a supervised text to text model (based on T5[2]) to map the round-trip normalized text samples back to the originals. By adjusting the model's temperature parameter at inference time we can affect the strength of the style transfer. We consider the increasing incoherence with greater temperature to be a positive feature of this technique. 

## Some Examples

Q: We have issued in a new era of economic prosperity for the american people.  
A: once again we'll usher in a new era of economic prosperity for the american people. do you think this sounds realistic? you tell me

Q: Slip inside the eye of your mind. Don't you know you might find a better place to play.  
A: drop within, at the edge of your brain. you might, you know what, you actually come up with a better place to play. lets go

Q: I did not have sexual relations with that woman.  
A: i have had no sexual relations with this woman. horrible.



## How to Run:

[Open and run the saved model](https://colab.research.google.com/github/JDBumgardner/Trumpifyve/blob/master/Trumpifyve_Run_Saved_Model.ipynb) 


## How to train

[Generate data using this colab](https://colab.research.google.com/github/JDBumgardner/Trumpifyve/blob/master/Trumpifyve_Training_Data_Generation.ipynb)

data is saved to your google drive /trump_pairs

[Train a T5 model using this colab](https://colab.research.google.com/github/JDBumgardner/Trumpifyve/blob/master/Trumpifyve_Train.ipynb)

## License

Licensed under the Apache 2.0 license. See LICENSE.txt for details.

## References 

[0] [Scaling Neural Machine Translation](https://arxiv.org/pdf/1806.00187.pdf) ([github](https://github.com/pytorch/fairseq/tree/master/examples/translation))  
[1] [Trump Campaign Corpus](https://github.com/unendin/Trump_Campaign_Corpus)  
[2] [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)([colab](https://colab.research.google.com/github/google-research/text-to-text-transfer-transformer/blob/master/notebooks/t5-trivia.ipynb))  



