#!/usr/bin/python3
"""
The module starts a FileStorage instance, if doesn't exist.
If the file does exist just load from the available file
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
