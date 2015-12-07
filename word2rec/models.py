from gensim.models import Word2Vec

class Word2VecRecommender(object):
    DEFAULT_WORD2VEC_PARAMETERS = dict(size=200, window=6, min_count=5, workers=8)

    def __init__(self, **word2vec_parameters):
        # TODO : pass these as parameters
        self.word2vec_params = dict(Word2VecRecommender.DEFAULT_WORD2VEC_PARAMETERS)
        self.word2vec_params.update(word2vec_parameters)
        self.model = Word2Vec(**self.word2vec_params)

    def fit(self, items):
        """
            Fits the model to a given list of items.
            `items` is a list of lists of strings. Every list is a certain user's items (from the training set), and items are represented by str ids.
        """
        # TODO : Do we need to know which users these items are for?
        # TODO : add some input validation
        self.training_items = items
        self.unique_items = set(item for item_list in items for item in item_list)

        trim_rule = self.word2vec_params.get('trim_rule', None)
        self.model.build_vocab(self.training_items, trim_rule=trim_rule)
        self.model.train(self.training_items)
        self.model.init_sims(replace=True)

    def recommend(self, user_items):
        pass
