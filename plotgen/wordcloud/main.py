import os
from wordcloud import WordCloud


def filter_words(words):
    result = []
    for word in words:
        if "/" in word:
            continue
        if ":" in word:
            continue
        if len(word)<4:
            continue
        result.append(word)
    return result


total_text = ""

files = os.listdir('../../content/posts')
for file in files:
    if file.endswith(".md"):
        print(file)
        p = os.path.join("../../content/posts", file)
        with open(p, 'r') as f:
            t = f.read()
            t= t.replace("\n", " ")
            t = t.replace('"','')
            words = t.split(' ')
            words = filter_words(words)
            print(words)
            total_text += " ".join(words)

word_cloud = WordCloud(
    collocations = False,
    width=1920*2, height=1080*2,
    colormap = 'bone',
    background_color = 'white').generate(total_text)
word_cloud.to_file('/Users/lukas/projects/my-hugo-site/static/images/post_banners/tags.png')