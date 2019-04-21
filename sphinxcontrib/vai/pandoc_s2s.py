import os

import pypandoc


def pandoc_s2s(app, docname, source):
    """
    Convert content to rst using pandoc before processing. Probably a better
    way is to write a parser for specific formats (like org), but this way also
    works for me at the moment.
    """

    enabled_extensions = app.config.pandoc_s2s_formats

    noextpath = os.path.join(app.srcdir, docname)
    if not os.path.exists(noextpath + ".rst"):
        for ext in enabled_extensions:
            if os.path.exists(noextpath + ext):
                source[0] = pypandoc.convert_file(noextpath + ext, "rst")
                break


def setup(app):
    app.add_config_value("pandoc_s2s_formats", [".org", ".md"], "html")
    app.connect("source-read", pandoc_s2s)

    return {"version": "0.1"}
