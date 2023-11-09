import sass
from pathlib import Path

def build_sass():
    print(Path().cwd())
    sass.compile(dirname=(f'{Path().cwd()}/theme/resource/scss', f'{Path().cwd()}/theme/static/css'), output_style='compressed')
    