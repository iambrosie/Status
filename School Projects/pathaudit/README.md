# Description

pathaudit is a small python utility which allows one to *hash* (using the SHA-256 cryptographic hash function) a user provided path.

If an output file is specified during the hash operation, it may later be used as an input for an *audit* (checking whether the files in the audit file have changed since the audit file creation).

## Usage

```
$pathaudit.py -h
usage: pathaudit.py [-h] {hash,audit} ...

positional arguments:
  {hash,audit}  commands
    hash        Hash the supplied path
    audit       Audit mode

optional arguments:
  -h, --help    show this help message and exit
```

### Example Usage in Hash Mode

Hash the "README.md" file and write the output to the "outfile" file

```
$./pathaudit hash README.md -o outfile
```

Hash the "test" directory (this will actually process recursively the "test" directory and hash all the found files) and write the output to the "outfile" file

```
$./pathaudit hash test -o outfile
```

### Example Usage in Audit Mode

Take an audit file (actually a file that's been specified as an output file during a previously issued hash mode operation) and check its consistency (meaning compare the current hashes of the files contained with the hashes contained in the file.

```
$./pathaudit audit outfile
```