import word2rec

def test_simple_instance():
    model = word2rec.models.Word2VecRecommender(size=80, window=10, min_count=1)
    items = [['item1', 'item2', 'item3'], ['item1', 'item3', 'item4', 'item5'], ['item5', 'item6', 'item7']]
    model.fit(items)
