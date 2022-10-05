from data.textloader import TextParse
from data.markovmodel import makeMarkovModel
import argparse


def make_model(args) -> None:
    # Parse sample File
    clean = TextParse(filepath=args.file) 
  
    # Create model
    model =  makeMarkovModel(clean_txt=clean.text, n_gram=2)

    # Save Model
    save  = model.save_model(dir=args.model, type=args.category)
    if save == 0:
        print(f"Module {args.model}/{args.category}.pkl successfully built and saved")


def generate_text(args) -> None:
    # Load model
    model = makeMarkovModel.load_model(dir=args.model, type=args.category)

    seeds = args.seed.split(',')
    
    # Generate text
    for i in range(args.lines):
        print( makeMarkovModel.generate_text(limit=args.limit, start=seeds[i].strip(), markov_model=model) )
    

def update_model(args) -> None:
    # Load model
    old_model = makeMarkovModel.load_model(dir=args.model, type=args.category)
    
    # Parse sample File
    clean = TextParse(filepath=args.file) 

    # Create new model
    new_model =  makeMarkovModel(clean_txt=clean.text, n_gram=2)

    for k,v in new_model.markov_model.items():
        if k in old_model.keys():
            old_model[k] += v
        else:
            old_model[k] = v 

    # Save updated model
    save  = makeMarkovModel.save_updated_model(model=old_model, dir=args.model, type=args.category)
    if save == 0:
        print(f"Module {args.model}/{args.category}.pkl successfully updated")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A tool to Generate text from a test sample.")

    subparsers = parser.add_subparsers()

    # MODEL CREATION OPTIONS
    parser_model = subparsers.add_parser('model', 
                   description="Create a Markov Model from the sample file and store it in the model dir, with the category name")

    parser_model.add_argument('-f', '--file', action="store",
                        help='The file path to the text sample which will be used to create the model',
                        required=True)

    parser_model.add_argument('-m', '--model', action="store",
                        help='A path to the model dir',
                        required=True)

    parser_model.add_argument('-c', '--category', action="store",
                        help='A string with a category for your model ( i.e Abstract, introduction, poem .\
                         This will be used as a model file name when the model is saved to a file',
                        required=True)

    parser_model.set_defaults(func=make_model)


    # TEXT GENERATION OPTIONS
    parser_generate = subparsers.add_parser('generate',
                    description=" Generate a random text baseon on a pre-computed Markov Model")

    parser_generate.add_argument('-c', '--category', action="store",
                        help='A string with a category for your model ( i.e Abstract, introduction, poem).\
                         This will be used as a file name when the model is saved to a file',
                        required=True)

    parser_generate.add_argument('-m', '--model', action="store",
                        help='A path to the model dir',
                        required=True)

    parser_generate.add_argument('-s', '--seed', action="store", nargs='?',
                        help='A two word sentence to be used as seed for the text. Make sure the seed exists on the model.\
                            Make Sure to enclose the seed with " ". Separate the seed with ",". For example "the present,recruitment of" ',
                        required=True)

    parser_generate.add_argument('-l', '--limit', action="store", type=int,
                        help='The number of n-grams (pair of words) in the generated text.',
                        required=True)
    
    parser_generate.add_argument('-n', '--lines', action="store", type=int,
                        help='The number of text lines of "X" n-grams (i.e. if limit is 100 and lines is 2, then the program\
                            will output 2 lines, each with 100 n-grams)',
                        required=True)

    parser_generate.set_defaults(func=generate_text)


    # MODEL UPDATE OPTIONS
    parser_update = subparsers.add_parser('update',
                                          description="Update a pre-computed model from a new sample file.")

    parser_update.add_argument('-m', '--model', action="store",
                        help='A path to the model dir',
                        required=True)

    parser_update.add_argument('-f', '--file', action="store",
                        help='The file path to the text sample which will be used to create the model',
                        required=True)

    parser_update.add_argument('-c', '--category', action="store",
                        help='A string with a category for your model ( i.e Abstract, introduction, poem).\
                         This will be used as a file name when the model is saved to a file',
                        required=True)

    parser_update.set_defaults(func=update_model)
    

    args = parser.parse_args()
    args.func(args)
    