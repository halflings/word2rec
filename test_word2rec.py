import word2rec

def test_simple_instance():
    model = word2rec.models.Word2VecRecommender(size=80, window=10, min_count=1)
    items = ["africa morocco capital rabat city mohammedia casablanca agadir marrakech fes meknes",
             "paris capital france city monument eiffel tower",
             "food morocco tagine france merguez couscous",
             "morocco moroccan food couscous chicken tagine kefta"]
    items = [s.split(' ') for s in items]
    model.fit(items)
    new_user = ['morocco', 'food']
    recommendations = model.recommend(new_user, num_items=5)
    print(recommendations)
