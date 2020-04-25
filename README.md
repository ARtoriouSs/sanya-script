# SanyaScript

description -\_-

## Install

First you need to install [ANTLR](https://github.com/antlr/antlr4). Then clone the project:

```bash
git clone https://github.com/ARtoriouSs/sanya-script
cd sanya-script
```

Install dependencies

```bash
pip install -r requirements.txt
```

Then generate parser:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener src/grammar/SanyaScript.g4
```

That's all, now you can compile SanyaScript to Python and run it with:

```bash
./sanya example.sanya result
./result
```
