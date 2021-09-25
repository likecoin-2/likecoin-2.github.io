cd C:/Users/champ/Desktop/blog/likecoin/rgib37190.github.io-gh-pages
call python create_html.py
call git add .
call git commit -m "add change"
call git push -u origin gh-pages
call python clap.py
call python delete_html.py