svg_tmpl = '''<svg width="10em" height="10em" version="1.1" viewBox="0 0 1000 1000" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="grad-circle" x1="0%%" y1="0%%" x2="50%%" y2="100%%">
<stop offset="0%%" stop-color="#1f7720" stop-opacity="1"></stop>
<stop offset="100%%" stop-color="#e5f9e0" stop-opacity="1"></stop>
</linearGradient>
<linearGradient id="grad-text" x1="0%%" y1="0%%" x2="50%%" y2="100%%">
<stop offset="0%%" stop-color="#446655" stop-opacity="1"></stop>
<stop offset="100%%" stop-color="#446655" stop-opacity="1"></stop>
</linearGradient>
</defs>
<circle fill="url(#grad-circle)" cx="500" cy="500" r="450"></circle>
<circle fill="#fff" cx="500" cy="500" r="350"></circle>
<text fill="url(#grad-text)" style="alignment-baseline: middle;font: 200pt Oxygen;text-anchor: middle;" x="500" y="500">%s</text>
<text fill="url(#grad-text)" style="alignment-baseline: baseline;font: 50pt Oxygen;text-anchor: middle;" x="500" y="700">%s</text>
</svg>

'''
