"""The GitTagPlugin class contains functionality to inject git tags in mkdocs."""
from git import Repo

from jinja2 import DebugUndefined, Template

from mkdocs.plugins import BasePlugin


class GitTagPlugin(BasePlugin):
    """GitTagPlugin extends the BasePlugin.

    Documentation: https://www.mkdocs.org/user-guide/plugins/#baseplugin
    """

    def on_page_markdown(self, markdown, page, config, files):
        """Inject git tag in markdown.

        Documentation for method: https://www.mkdocs.org/user-guide/plugins/#on_page_markdown
        Structure related src: https://github.com/mkdocs/mkdocs/tree/master/mkdocs/structure

        Args:
            markdown: Markdown source text of page as string
            page: mkdocs.nav.Page instance
            config: global configuration object (not used)
            files: global files collection      (not used)

        Returns:
            Markdown source text of page as string
        """
        repo = Repo(page.file.abs_src_path, search_parent_directories=True)
        current_tag = next(
            (tag for tag in repo.tags if tag.commit == repo.head.commit), None
        )
        template = Template(markdown, undefined=DebugUndefined)
        return template.render({"git_tag": current_tag})
