import os
import pickle
import argparse

# parse command line argument
def parse_args():
    '''
    Parse the TopoLSTM parameters
    '''
    parser = argparse.ArgumentParser(description="Create Html")

    parser.add_argument('--name',default='',type=str,help='name')

    return parser.parse_args()

def output_html(number, name):
    html_name_list = []
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

def output_linkcoin(number, name):
    with open('total.html', 'w') as f:
        for i in range(number):
            connect_html = "https://likecoin-2.github.io/{}_{}.html".format(i, name)
            embed_id = "likecoin{}".format(i)
            likecoin_embed_link = "<div> <iframe scrolling='no' frameborder='0' id = {} style='width:100%; max-width:100px; height:100px; margin:auto; overflow:hidden; display:block; float:left;' src='https://button.like.co/in/embed/champion516615/button?referrer={}' ></iframe> <div></div> </div>".format(embed_id, connect_html)
            f.write(likecoin_embed_link)
            f.write('\n')

if __name__ == "__main__":
    args = parse_args()
    output_html(84, args.name)
    output_linkcoin(84, args.name)