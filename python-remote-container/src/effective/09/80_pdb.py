"""
python src/effective/09/80_pdb.py 
  File "/code/src/effective/09/80_pdb.py", line 3
    print({"test": [1, 2.2, 3.0a]})
                               ^

"-m pdb -c continue"
を使うことで、詳しいエラー情報が出る

python -m pdb -c continue src/effective/09/80_pdb.py 
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/pdb.py", line 1704, in main
    pdb._runscript(mainpyfile)
  File "/usr/local/lib/python3.9/pdb.py", line 1573, in _runscript
    self.run(statement)
  File "/usr/local/lib/python3.9/bdb.py", line 580, in run
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "/code/src/effective/09/80_pdb.py", line 3
    print({"test": [1, 2.2, 3.0a]})
                               ^
SyntaxError: invalid syntax
"""

print("------------- start -------------")

test = [1, 2.2, 3.0]
# breakpoint()
print({"test": test})

print("------------- end -------------")
