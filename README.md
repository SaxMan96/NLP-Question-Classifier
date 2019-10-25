# Question Classification

Classify questions to 4 different classes, using NLP methods and ML tools for classification

## Data

Data comes in `.xmlx` format, but better to read it from csv file.

```python
df = pd.read_csv("Questions.csv", sep=";")
df.head()
```
| Question                                                     | Type    |
| :----------------------------------------------------------- | :------ |
| Is Hirschsprung disease a mendelian or a multifactorial disorder? | summary |
| List signaling molecules (ligands) that interact with the receptor EGFR? | list    |
| Is the protein Papilin secreted?                             | yesno   |
| Are long non coding RNAs spliced?                            | yesno   |
| Is RANKL secreted from the cells?                            | yesno   |

For this problem we should use `multiclass` classifier.
```python
print(df.Type.unique())
>> ['summary' 'list' 'yesno' 'factoid']
```
```python
df.shape
>> (2251, 2)
```

## Preprocessing
First step of preprocessing string is to tokenize it - change each word into separate string and gather them into a list. I've used `nltk` method which has some additional features for example separates punctuation to different tokens. 
```python
tokens = nltk.word_tokenize("Is Hirschsprung disease a multifactorial disorder?")
>> ['Is', 'Hirschsprung', 'disease', 'a', 'multifactorial', 'disorder', '?']
```
In every language there are stop words, that actually don't give much information in a sentence. For example (a, the, in, or, ...).
```python
tokens = [token for token in tokens if token not in stopwords_en]
>> ['Is', 'Hirschsprung', 'disease', 'mendelian', 'multifactorial', 'disorder', '?']
```
Removing punctuation also helps reduce number of tokens that not necessary increase informative value of sentence.
```python
tokens = [token for token in tokens if token not in punctuation]
>> ['Is', 'Hirschsprung', 'disease', 'mendelian', 'multifactorial', 'disorder']
```

```python
# ['123a45n6', 'example!', 'witho0ut', 'non-letters']
tokens = [re.sub(r'[^a-zA-Z]', "", token) for token in tokens]
>> ['an', 'example', 'without', 'nonletters']
```

```python
# ['LOWER', 'Case']
tokens = [token.lower() for token in tokens]
>> ['lower', 'case']
```
> "Lemmatization (or lemmatization) in linguistics is the process of grouping together the inflected forms of a word so they can be analyzed as a single item, identified by the word's lemma, or dictionary form." (Wiki)

```python
# ['list', 'signaling', 'molecules', 'ligands', 'interact', 'receptor']
tokens = [lemmatize(pair) for pair in pos_tag(tokens)]
>> ['list', 'signal', 'molecule', 'ligands', 'interact', 'receptor']
```
Stemming has basically the same purpose as Lemmatization, but is performed with regex rules, which makes it way faster, and sometimes allow to decrease number of unique tokens in dataset even after lemmatization.
```python
# ['list', 'signal', 'molecule', 'ligands', 'interact', 'receptor']
tokens = [porter.stem(token) for token in tokens]
>> ['list', 'signal', 'molecul', 'ligand', 'interact', 'receptor']
```

## Vectorization

I've used `sklearn.feature_extraction.text.CountVectorizer` to Vectorize my data. It takes text file as input but there is a short trick with `StringIO` that allows me to transform data to proper format.

```python
with StringIO('\n'.join([i for i in questions.values])) as text:
    count_vect = CountVectorizer(analyzer=preprocess_text)
    count_vect.fit_transform(text)
```
In out dataset after preprocessing there are 3601 tokens (more than training examples) we will have to deal with it later.
```python
len(count_vect.vocabulary_)
>> 3601
```
There is a vocabulary of words. As we can see in first example not all of them are regular words in english.
```python
words_sorted_by_index, _ = zip(*sorted(count_vect.vocabulary_.items(), key=itemgetter(1)))
words_sorted_by_index[:5]
>> ('aa', 'aagena', 'abacavir', 'abatacept', 'abc')

```
This is our final dataset shape, time to do the classification.
```python
count_vect.transform([i for i in questions.values]).toarray().shape
>> (2251, 3601)
```

## Classification

I've tested 4 different classifers using GridSearch with wide param space and CrosValidation.

```python
Decision Tree		Accuracy Train: 99.8%	Accuracy Valid: 70.4%
Best params: class_weight = 'balanced', presort = False
```

![image-20191025033715676](https://github.com/SaxMan96/NLP-Question-Classifier/blob/master/images/DTConfM.png?raw=true)
```python
Random Forest		Accuracy Train: 93.5%	Accuracy Valid: 72.3%
Best params: class_weight = 'balanced', max_depth = 30
			 max_features = 19, n_estimators = 100
```
![image-20191025033701539](https://github.com/SaxMan96/NLP-Question-Classifier/blob/master/images/RFConfM.png?raw=true)
```python
K-Neares Neighbours		Accuracy Train: 99.8%	Accuracy Valid: 32.1%
Best params: n_neighbors = 10, weights = 'distance'
```
![image-20191025033633422](https://github.com/SaxMan96/NLP-Question-Classifier/blob/master/images/KNNConfM.png?raw=true)
```python
 Logistic Regression		Accuracy Train: 85.7%	Accuracy Valid: 74.6%
 Best params: C = 0.1, multi_class = 'multinomial', solver = 'lbfgs'
```

![image-20191025033545848](https://github.com/SaxMan96/NLP-Question-Classifier/blob/master/images/LRConfM.png?raw=true)

The winner is **Logistic Regression** 🏆

Notes:

* I've tested that `PCA` doesn't improve performance of any of classifiers.
* Also using a `StandarScaler()` wasn't a good idea due to binary character of data.
* My validation metric was accuracy due to even distibution in class.

## Testing On Production

I've written short function to classify inputed by user questions to one of 4 classes.

```python
def predict_question(question):
    x = count_vect.transform([question]).toarray()
    return classes[clf.predict(x)[0]]
```

These are results of my classification:

- **Do you like to study?** *yesno*

- **How do you feel rright now?** *summary*

- **What is your name?** *summary*

- **List two of your favourie films.** *list*

- **What is the biggest country in Europe?** *summary*

- **Where are you?** *factoid*

- **How old are you?** *summary*

  

25.10.2019 [Mateusz Dorobek](https://mateuszdorobek.github.io) UPC - Human Language Engineering
