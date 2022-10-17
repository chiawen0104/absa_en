## Pipeline sequence labeling + relation classification

- [SemEval 2022 baseline: sequence labeling](https://github.com/jerbarnes/semeval22_structured_sentiment/tree/master/baselines/sequence_labeling). 
- Trained on 3 EN datasets, inferenced on SemEval 2016 Task 5. 

Here we provide starter code for a model that first learns to extract the sub-elements (holders, targets, expressions) using sequence labelers, and then tries to classify whether or not they have a relationship.

Specifically, we first train three separate BiLSTM models to extract holders, targets, and expressions, respectively (extraction_module.py). We then train a relation prediction model (relation_prediction_model.py), which uses a BiLSTM + max pooling to create contextualized representations of 1) the full text, 2) the first element (either a holder or target) and 3) the sentiment expression.

These three representations are then concatenated and passed to a linear layer followed by a sigmoid function. The training consists of predicting whether two elements have a relationship or not, converting the problem in binary classification.

During inference (inference.py), we first predict all sub-elements and then decide if they have a relationship (prediction > 0.5). Finally, the predictions are converted to the json format used in the shared task.


