mkdocs git tag plugin
===

Acquire the latest git tag and put it in your mkdocs document!

## Example

Put `{{ git_tag }}` somewhere in your mkdocs document and the `{{ git_tag }}`
will be replaced with the tag for the current commit.

## Disclaimer

If the current commit does not have a tag, `{{ git_tag }}` will yield `None`.
