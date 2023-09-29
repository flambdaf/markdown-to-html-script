import sys


def markdown_end():
    with open('markdown_convert.html', mode='a', encoding='utf-8') as f:
        f.write('''
</body>
</html>''')


def markdown_input(flag, *args):
    with open('markdown_convert.html', mode='a', encoding='utf-8') as f:
        if flag:
            f.write(''.join(args))
        else:
            f.write(f'<p>\n  {"".join(args)}</p>\n')


def headings(text):
    h1_6 = ['<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>',
            '</h6>', '</h5>', '</h4>', '</h3>', '</h2>', '</h1>']
    markdown_input(True,
                   f"{h1_6[text.count('#') - 1]}\n {text.replace('#', '')}\n{h1_6[-(text.count('#'))]}\n")


def italic_or_bold(text):
    sym = ['**', '*', '__', '_']
    sym_repl = ['<strong>', '<em>', '<strong>', '<em>',
                '</em>', '</strong>', '</em>', '</strong>']
    for i in range(len(sym)):
        if sym[i] in text:
            while sym[i] in text:
                text = text.replace(sym[i], sym_repl[i], 1)
                text = text.replace(sym[i], f'{sym_repl[-i - 1]}\n', 1)
    markdown_input(False, text)


def markdown_check(text):
    for i in text:
        i = ''.join(i).replace('\n', '').rstrip()
        # headings
        if i[0] == '#':
            headings(i)
        elif '_' in i or i.count('*') > 1:
            italic_or_bold(i)
        else:
            markdown_input(False, i)


def reading(file):
    res = []
    with open(file, encoding='utf-8') as f:
        for i in f.readlines():
            i = i.split('\n\n')
            if i == ['\n']:
                continue
            else:
                res.append(i)
    return res


def make_html():
    with open('markdown_convert.html', mode='w', encoding='utf-8') as f:
        f.write('''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title></title>
  <link rel="stylesheet" href="style.css" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,500;1,300&display=swap" rel="stylesheet">
</head>
<body>
''')


def make_css():
    with open('style.css', mode='w', encoding='utf-8') as f:
        f.write('''
body {
  font-family: 'Poppins', sans-serif;
}

}
body {
  font-family: 'Poppins', sans-serif;
}
p {
  color: #717BD8;
  transition: .5s;
}
p:hover {
  color: #081272;
  text-decoration: none;
}''')


def main():
    make_html()
    markdown_check(reading(sys.argv[1]))
    markdown_end()
    make_css()


if __name__ == '__main__':
    main()
