import os 
import pickle

def remove_html():
    with open('html.pickle', 'rb') as f:
        html_name_list = pickle.load(f)
    for path in html_name_list:
        path = os.path.join('C:/Users/champ/Desktop/blog/likecoin/rgib37190.github.io-gh-pages', path)
        os.remove(path)

if __name__ == "__main__"