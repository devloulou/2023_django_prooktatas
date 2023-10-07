import random

post_model_path = r"C:\WORK\2023_django_szeptember\my_blog\core_blog\fixtures\post_model_data.json"

users = (4, 5, 6)

last_post_id = 8

temp = {
    "model": "core_blog.PostModel",
    "pk": 2,
    "fields": {
        "title": "Alien movie story",
        "content": "During its return to the earth, commercial spaceship Nostromo intercepts a distress signal from a distant planet. When a three-member team of the crew discovers a chamber containing thousands of eggs on the planet, a creature inside one of the eggs attacks an explorer. The entire crew is unaware of the impending nightmare set to descend upon them when the alien parasite planted inside its unfortunate host is birthed.",
        "author": 1
    }
}

posts = []

import copy

for item in range(50):
    last_post_id += 1
    data = copy.deepcopy(temp)
    data['pk'] = last_post_id
    data['fields']['title'] = data['fields']['title'] + "_" + str(last_post_id)
    data['fields']['author'] = random.choice(users)
    posts.append(data)

print(posts)

import json
with open(post_model_path, "w") as f:
    json.dump(posts, f, indent=4)
