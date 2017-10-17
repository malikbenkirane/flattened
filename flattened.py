model = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
         'brblack', 'brred', 'brgreen', 'bryellow', 'brblue', 'brmagenta',
         'brcyan', 'brwhite']

dark = ['#073642', '#dc322f', '#859900', '#b58900', '#268bd2', '#d33682',
        '#2aa198', '#eee8d5', '#002b36', '#cb4b16', '#586e75', '#657b83',
        '#839496', '#6c71c4', '#93a1a1', '#fdf6e3']
light = ['#eee8d5', '#dc322f', '#859900', '#b58900', '#268bd2', '#d33682',
         '#2aa198', '#073642', '#fdf6e3', '#cb4b16', '#93a1a1', '#839496',
         '#657b83', '#6c71c4', '#586e75', '#002b36']


def format_to_xresources(colors):
    xresources = '!xresources'
    for i, color in enumerate(colors):
        xresources += '\n*.color{}:\t{}'.format(i, color)
    return xresources


light_xresources = format_to_xresources(light)
dark_xresources = format_to_xresources(dark)
model_xresources = format_to_xresources(model)
