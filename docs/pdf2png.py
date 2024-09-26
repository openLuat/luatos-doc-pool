#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, pymupdf

def pdf2png(pdf_file, png_file):
    doc = pymupdf.open(pdf_file)
    id = 0
    for page in doc.pages():
        # page.rotate(-90).render_image().writePNG(png_file)
        pix = page.get_pixmap()
        pix.save(png_file % id)
        id += 1

# main函数
if __name__ == '__main__':
    if len(sys.argv) == 3:
        pdf_file = sys.argv[1]
        png_file = sys.argv[2]
        #print('Usage: pdf2png <input.pdf> <output.png>' % (sys.argv[0]))
        #sys.exit(1)
    else :
        # python pdf2png.py root\docs\file\airm2m.pdf "..\image\airm2m_%02d.png"
        pdf_file = os.path.join('root','docs', 'file', 'airm2m.pdf')
        png_file = os.path.join("..", "image", "airm2m_%02d.png")

    pdf2png(pdf_file, png_file)
