* Bump version in `numpy_minmax/__init__.py`
* `CC=clang pip install -e . && pytest`
* Update CHANGELOG.md
* Commit and push the change with a commit message like this: "Release vx.y.z" (replace x.y.z with the package version)
* Wait for build workflow in Github Actions to complete
* Download wheels artifact from the build workflow
* Place all the fresh whl files in dist/
* `python -m twine upload dist/*`
* Add a tag with name "vx.y.z" to the commit
* Go to https://github.com/nomonosound/numpy-minmax/releases and create a release where you choose the new tag
