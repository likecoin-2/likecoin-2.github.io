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