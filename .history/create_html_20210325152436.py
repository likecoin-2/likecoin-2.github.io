def output_html(number):
    html_name_list = []
    for i in range(number):
        html_name = "demo_{}.html".format(i)
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
    return html_name_list

def output_linkcoin(number):
    with open('total.html', 'w') as f:
        for i in range(number):
            connect_html = "https://likecoin-2.github.io/demo_{}.html".format(i)
            embed_id = "likecoin{}".format(i)
            likecoin_embed_link = "<div> <iframe scrolling='no' frameborder='0' id = {} style='width:100%; max-width:100px; height:100px; margin:auto; overflow:hidden; display:block; float:left;' src='https://button.like.co/in/embed/champion516615/button?referrer={}' ></iframe> <div></div> </div>".format(embed_id, connect_html)
            f.write(likecoin_embed_link)
            f.write('\n')

if __name__ == "__main__":
    html_name_list = output_html(84)
    output_linkcoin(84)