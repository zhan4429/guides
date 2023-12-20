from datetime import date

project = "Research Technology Guides"
author = "Tufts University"

github_user = "tuftsrt"
github_repo = "guides"

copyright = "{:04} {}".format(date.today().year, author)

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
]

html_baseurl = "https://{}.github.io/{}".format(github_user, github_repo)
html_favicon = "_static/favicon.ico"
html_last_updated_fmt = ""
html_logo = "_static/jumbo.png"
html_show_sourcelink = False
html_static_path = ['_static']
html_theme = "pydata_sphinx_theme"
html_title = project

icon_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/{}/{}".format(github_user, github_repo),
        "icon": "fa-brands fa-github",
    },
]

html_theme_options = {
    "announcement": "Under active development. Content may be incomplete.",
    "footer_end": ["last-updated"],
    "footer_start": ["copyright"],
    "header_links_before_dropdown": 7,
    "icon_links": icon_links,
    "logo": {"text": project},
    "navbar_align": "left",
    "search_bar_text": "Search the guides...",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "linkify",
    "replacements",
    "substitution",
]
