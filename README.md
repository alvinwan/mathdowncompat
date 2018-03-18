# MathDownCompat (MDC)
MathTex compatibility for in-browser markdown using MathJax, MathML, and/or images

Have delimited math formulas in your markdown? If you're fortunate enough to have control over the webpage containing your markdown, pretty math displays are just one `script` tag away, using MathJax. If otherwise, you're in a fix. This is where MDC comes in: pip install and with just one command, you'll have your math display ready to go in a jiffy. Math can be converted into one of the following alternatives:

1. MathML: a native markup language supported by Safari and Firefox
2. Images: All math is converted into images and saved to your local disk. You can configure a custom URL prefix, should you host the images on Github or elsewhere. (Automatic Imgur upload support coming soon)

To get started, download the package via `pip`.

```
pip install mathdowncompat
```

After installation, use the `mdcompat` command to process any markdown file's math excerpts. For example, consider the following sample file `sample.md`.

```markdown
# Hello World

This is some $\frac{1}{n} \sum_{i=1}^n x_i$ average math. ;)

$$\int e^{xy} dude$$
```

Run the following on the `sample.md` above. By default, MDC will search for all math environments delimited by `$` and `$$`, replacing all with paths to images. By default, these paths are relative to your current working directory.

```
mdcompat sample.md
```

With that one command, you are now done. Your output at `sample.md.converted` will match the following.

```markdown
# Hello World

This is some ![1](assets/1.png) average math. ;)

![2](assets/2.png)
```

Want to share this markdown file online? Say we upload all images to `alvinwan.com/static`. Then, we specify that as our image URL prefix.

```
mdcompat sample.md --image-url-prefix alvinwan.com/static
```

This gives us the following markdown file that we can then host online.

```markdown
# Hello World

This is some ![1](alvinwan.com/static/assets/1.png) average math. ;)

![2](alvinwan.com/static/assets/2.png)
```

You can use the options below to specify a host URL or convert to MathML instead of images. (In the future, you can specify an option to automatically upload images to Imgur) The output file is then the following

```
usage: mdcompat [-h] [--converter {mathml,image}] [--out OUT] [--verbose]
                [--image-assets IMAGE_ASSETS]
                [--image-url-prefix IMAGE_URL_PREFIX]
                path

positional arguments:
  path                  path to markdown file

optional arguments:
  -h, --help            show this help message and exit
  --converter {mathml,image}
                        math converter to apply
  --out OUT             path to output markdown file
  --verbose
  --image-assets IMAGE_ASSETS
                        path to assets
  --image-url-prefix IMAGE_URL_PREFIX
                        prefix for all image urls
```
