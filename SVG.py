from fileinput import filename

_HTMLTEMPLATESTART = ['<!DOCTYPE html>\n', '<html lang="en">\n', '<head>\n', '\t<meta charset="UTF-8">\n', '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n', '</head>\n', '<body>\n']
_HTMLTEMPLATEEND = ['</body>\n', '</html>']

class SVG:
    def __init__(self, width = 100, height = 100):
        self.width = width
        self.height = height
        self.centerx = 0
        self.centery = 0
        self.elements = []
        self.styles = {}
    
    def _add(self, e):
        self.elements.append(e)
    
    def set_center(self, x, y):
        self.centerx = x
        self.centery = y

    def _get_styles(self):
        return " style=\"" + ";".join([k + ':' + self.styles[k] for k in self.styles]) + "\"" if self.styles else ""

    def reset(self):
        self.styles = {}
    
    def rect(self, x=0, y=0, rx=0, ry=0, width=0, height=0):
        self._add(f'<rect x="{x + self.centerx}" y="{y + self.centery}" rx="{rx}" ry="{ry}" width="{width}" height="{height}"{self._get_styles()}/>')

    def circle(self, cx=0, cy=0, r=0):
        self._add(f'<circle cx="{cx + self.centerx}" cy="{cy + self.centery}" r="{r}"{self._get_styles()}/>')
    
    def ellipse(self, cx=0, cy=0, rx=0, ry=0):
        self._add(f'<ellipse cx="{cx + self.centerx}" cy="{cy + self.centery}" rx="{rx}" ry="{ry}"{self._get_styles()}/>')

    def line(self, x1=0, y1=0, x2=0, y2=0):
        self._add(f'<line x1="{x1 + self.centerx}" y1="{y1 + self.centery}" x2="{x2 + self.centerx}" y2="{y2 + self.centery}"{self._get_styles()}/>')
    
    def poly(self, points=[(0,0), (0,0), (0,0)]):
        if not points or len(points) < 3:
            raise "To few points for a polygon!"
        points = [(x + self.centerx, y + self.centery) for x,y in points]
        self._add(f'<polygon points="{" ".join([str(x) + "," + str(y) for x,y in points])}"{self._get_styles()}/>')

    def polyline(self, points=[(0,0), (0,0)]):
        if not points or len(points) < 2:
            raise "To few points for a polyline!"
        points = [(x + self.centerx, y + self.centery) for x,y in points]
        self._add(f'<polyline points="{" ".join([str(x) + "," + str(y) for x,y in points])}"{self._get_styles()}/>')

    def text(self, x=0, y=0, txt="tmp"):
        self._add(f'<text x="{x + self.centerx}" y="{y + self.centery}"{self._get_styles()}>{txt}</text>')

    def fill(self, r=0, g=0, b=0):
        self.styles['fill'] = f'rgb({r},{g},{b})'
    
    def fills(self, style):
        self.styles['fill'] = f'{style}'
    
    def stroke_width(self, w):
        self.styles['stroke-width'] = f'{w}'
    
    def fill_opacity(self, o):
        self.styles['fill-opacity'] = f'{o}'
    
    def stroke_opacity(self, o):
        self.styles['stroke-opacity'] = f'{o}'

    def stroke(self, r=0, g=0, b=0):
        self.styles['stroke'] = f'rgb({r},{g},{b})'

    def write(self, file_name = 'file.svg'):
        with open(file_name, 'w+') as f:
            f.write(f'<svg width="{self.width}" height="{self.height}">\n')
            [f.write('\t'+e+'\n') for e in self.elements]
            f.write('</svg>')

    def write_html(self, file_name = 'index.html'):
        with open(file_name, 'w+') as f:
            f.writelines(_HTMLTEMPLATESTART)
            f.write(f'\t<svg style="width:{self.width}; height:{self.height};">\n')
            [f.write('\t\t'+e+'\n') for e in self.elements]
            f.write('\t</svg>\n')
            f.writelines(_HTMLTEMPLATEEND)