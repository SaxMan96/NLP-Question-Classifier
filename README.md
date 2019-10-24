# Question Classification



## Data

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

```python
print(df.Type.unique())
>> ['summary' 'list' 'yesno' 'factoid']
```
```python
df.shape
>> (2251, 2)
```

## Preprocessing

```python
tokens = nltk.word_tokenize("Is Hirschsprung disease a mendelian or a multifactorial disorder?")
>> ['Is', 'Hirschsprung', 'disease', 'a', 'mendelian', 'or', 'a', 'multifactorial', 'disorder', '?']
```

```python
tokens = [token for token in tokens if token not in stopwords_en]
>> ['Is', 'Hirschsprung', 'disease', 'mendelian', 'multifactorial', 'disorder', '?']
```

```python
tokens = [token for token in tokens if token not in punctuation]
>> ['Is', 'Hirschsprung', 'disease', 'mendelian', 'multifactorial', 'disorder']
```

```python
# "123456 example! witho0ut non-letters"
tokens = [re.sub(r'[^a-zA-Z]', "", token) for token in tokens]
>> ['example', 'without', 'nonletters']
```

```python
# "LOWER Case"
tokens = [token.lower() for token in tokens]
>> ['lower', 'case']
```

```python
# ['list', 'signaling', 'molecules', 'ligands', 'interact', 'receptor']
tokens = [lemmatize(pair) for pair in pos_tag(tokens)]
>> ['list', 'signal', 'molecule', 'ligands', 'interact', 'receptor']
```

```python
#  ['list', 'signal', 'molecule', 'ligands', 'interact', 'receptor']
tokens = [porter.stem(token) for token in tokens]
>> ['list', 'signal', 'molecul', 'ligand', 'interact', 'receptor']
```

## Vectorization

```python
with StringIO('\n'.join([i for i in questions.values])) as text:
    count_vect = CountVectorizer(analyzer=preprocess_text)
    count_vect.fit_transform(text)
```

```python
len(count_vect.vocabulary_)
>> 3601
```

```python
words_sorted_by_index, _ = zip(*sorted(count_vect.vocabulary_.items(), key=itemgetter(1)))
words_sorted_by_index[:5]
>> ('aa', 'aagena', 'abacavir', 'abatacept', 'abc')

```

```python
count_vect.transform([i for i in questions.values]).toarray().shape
>> (2251, 3601)
```

## Classification





