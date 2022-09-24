import os
import os.path as op
from pathlib import Path
import shutil
import subprocess
import tempfile

from IPython.lib.latextools import genelatex


def latex_to_image(latex, eps_path):
    eps_path = op.realpath(eps_path)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpfile = os.path.join(tmpdir, "tmp.tex")
        dvifile = os.path.join(tmpdir, "tmp.dvi")
        psfile = os.path.join(tmpdir, "tmp.ps")
        pdffile = os.path.join(tmpdir, "tmp.pdf")
        epsfile = os.path.join(tmpdir, "tmp.eps")
        pngfile = os.path.join(tmpdir, "tmp.png")

        contents = list(genelatex(latex, False))
        with open(tmpfile, "w") as f:
            f.writelines(contents)

        with open(os.devnull, 'w') as devnull:
            try:
                subprocess.check_call(
                    ["latex", "-halt-on-error", tmpfile], cwd=tmpdir,
                    stdout=devnull, stderr=devnull)
            except Exception as e:
                print("************")
                print(len(contents))
                print('\n'.join(contents))
                raise(e)

            subprocess.check_call(
                ["dvips", dvifile, "-o", psfile], cwd=tmpdir,
                stdout=devnull, stderr=devnull)

            subprocess.check_call(
                ["gs",
                 "-o",
                 pdffile,
                 "-dNoOutputFonts",
                 "-sDEVICE=pdfwrite",
                 "-dEPSCrop",
                 psfile,
                 ], cwd=tmpdir,
                stdout=devnull, stderr=devnull)

            subprocess.check_call(
                ["pdf2ps", pdffile], cwd=tmpdir,
                stdout=devnull, stderr=devnull)

            subprocess.check_call(
                ["ps2eps", psfile], cwd=tmpdir,
                stdout=devnull, stderr=devnull)

            subprocess.check_call(
                ["dvipng", "-T", "tight", "-x", "6000", "-z", "9",
                 "-bg", "transparent", "-o", pngfile, dvifile], cwd=tmpdir,
                stdout=devnull, stderr=devnull)

        shutil.copy(epsfile, eps_path)
        shutil.copy(pngfile, Path(eps_path).with_suffix('.png'))


if __name__ == '__main__':
    latex_to_image(r'$$\sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$',
                   'zeta2.eps')
