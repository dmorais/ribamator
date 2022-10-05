# ribamator
A tool to Generate text from a test sample.

````
usage: ribamator.py [-h] {model,generate,update} ...

A tool to Generate text from a test sample.

positional arguments:
  {model,generate,update}

options:
  -h, --help            show this help message and exit

```


## Create Model

```
usage: ribamator.py model [-h] -f FILE -m MODEL -c CATEGORY

Create a Markov Model from the sample file and store it in the model dir, with the category name

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file path to the text sample which will be used to create the model
  -m MODEL, --model MODEL
                        A path to the model dir
  -c CATEGORY, --category CATEGORY
                        A string with a category for your model ( i.e Abstract, introduction, poem . This will be used as a model file
                        name when the model is saved to a file
```


## Generate Text

```

usage: ribamator.py generate [-h] -c CATEGORY -m MODEL -s [SEED] -l LIMIT -n LINES

Generate a random text baseon on a pre-computed Markov Model

options:
  -h, --help            show this help message and exit
  -c CATEGORY, --category CATEGORY
                        A string with a category for your model ( i.e Abstract, introduction, poem). This will be used as a file name
                        when the model is saved to a file
  -m MODEL, --model MODEL
                        A path to the model dir
  -s [SEED], --seed [SEED]
                        A two word sentence to be used as seed for the text. Make sure the seed exists on the model. Make Sure to
                        enclose the seed with " ". Separate the seed with ",". For example "the present,recruitment of"
  -l LIMIT, --limit LIMIT
                        The number of n-grams (pair of words) in the generated text.
  -n LINES, --lines LINES
                        The number of text lines of "X" n-grams (i.e. if limit is 100 and lines is 2, then the program will output 2
                        lines, each with 100 n-grams)

```


## UPDATE MODEL

```

usage: ribamator.py update [-h] -m MODEL -f FILE -c CATEGORY

Update a pre-computed model from a new sample file.

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        A path to the model dir
  -f FILE, --file FILE  The file path to the text sample which will be used to create the model
  -c CATEGORY, --category CATEGORY
                        A string with a category for your model ( i.e Abstract, introduction, poem). This will be used as a file name
                        when the model is saved to a file

```
