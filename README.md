# Introduction
This is a collection of personal tools I've made to help with different stuff,
it's all for personal use so there is no error checking and the like, proceed
with caution.

## TODO

### Bugfixing
#### fileManager.py
There is a bug, if you use the remove from back option and for example you have two files "t" and "ts", if you choose to remove 1 element then it doesn't do anything for "t", but it renames "ts" to 't' so then "t" and 't' share the same name and overwrite each other.