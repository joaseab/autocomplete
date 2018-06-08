import argparse



def parseargs_autocomplete():
    """Parses command line arguments for the autocomplete apps.

    Returns:
        object with fields:
            object.corpus        - path of the .csv file with the corpus
            object.casesensitive - boolean: defines if search is case sensitive
            object.nmin          - minimum number of letters for autocompletion

    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-n','--nmin', 
                        help='Minimum number of letters', 
                        required=False, default=1, type=int)

    parser.add_argument('-c','--corpus', 
                        help='Corpus filepath', required=True, default=None,
                        type=str)

    parser.add_argument('--casesensitive', 
                        help="Sets case sensitive completion",
                        action="store_true")

    return parser.parse_args()
