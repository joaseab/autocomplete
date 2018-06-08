from autocomplete import AutoComplete
from parsecommands import parseargs_autocomplete



def main(corpus, nmin, case_sensitive):

    ac = AutoComplete(corpus, nmin=nmin, case_sensitive=case_sensitive)

    msg = 'Insert words for autocompletion. To terminate, press Cntrl-C.'
    print('%s\n%s\n%s'%('='*len(msg),msg,'='*len(msg)))

    while True:
        user_word = raw_input()
        for completion in ac.completions(user_word):
            print('\t\t'+completion)


if __name__ == '__main__':

    # parse command line arguments
    args = parseargs_autocomplete()

    main(args.corpus, args.nmin, args.casesensitive)
