import os
import pickle

def load_corpus_name():
    with open('name_corpus.pickle', 'rb') as f:
        corpus = pickle.load(f)   
        names = corpus[:8]
        corpus = corpus[8:]
    with open('name_corpus.pickle', 'wb') as f:
        pickle.dump(corpus, f)
    return names

def output_html(number, names):
    html_name_list = []
    for name in names:
        for i in range(number):
            html_name = "{}_{}.html".format(name, i)
            with open(html_name,'w') as f:
                message = """
                <html>
                <head></head>
                <body>
                <p>Hello,World!</p>
                <p>demo</p>
                </body>
                </html>"""
                f.write(message)
                f.close()
            
        html_name_list.append(html_name)
    with open('html.pickle', 'wb') as f:
        pickle.dump(html_name_list, f)

def output_linkcoin(number, names):
    for index, name in enumerate(names):
        total_name = 'total{}.html'.format(index)
        with open(total_name, 'w') as f:
            for i in range(number):
                connect_html = "https://likecoin-2.github.io/{}_{}.html".format(i, name)
                embed_id = "likecoin{}".format(i)
                likecoin_embed_link = "<div> <iframe scrolling='no' frameborder='0' id = {} style='width:100%; max-width:100px; height:100px; margin:auto; overflow:hidden; display:block; float:left;' src='https://button.like.co/in/embed/champion516615/button?referrer={}' ></iframe> <div></div> </div>".format(embed_id, connect_html)
                f.write(likecoin_embed_link)
                f.write('\n')


if __name__ == "__main__":
    names = load_corpus_name()
    output_html(84, names)
    output_linkcoin(84, names)