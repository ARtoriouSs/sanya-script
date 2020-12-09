# SanyaScript

[![License](https://img.shields.io/github/license/ARtoriouSs/sanya-script.svg)](https://github.com/ARtoriouSs/sanya-script/blob/master/LICENSE)

Crutched graph language compilable into Python :)

## Install

First, you need to install [ANTLR](https://github.com/antlr/antlr4).

Then clone the project and install dependencies:

```bash
git clone https://github.com/ARtoriouSs/sanya-script
cd sanya-script
pip install -r requirements.txt
```

Generate parser with ANTLR:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener src/grammar/SanyaScript.g4
```

Now you can compile SanyaScript to Python and run it with:

```bash
./sanya example.sanya result
./result
```

You can also do `PATH=$PWD:$PATH` to run it from anywhere.

## Description

For better understanding of grammar structure check out [the grammar file](src/parser/grammar/SanyaScript.g4),
[example code file](example.sanya) and [runtime repo](https://github.com/ARtoriouSs/sanya-script-runtime).

### 1 - Types and values:

* `num` - numeric, it's both ints and floats:

```elixir
num n = 1
num n = 123.456
```

Note that variable names cannot start with number.

* `logic` - accepts boolean `yes` or `no`, because I can :)

```elixir
logic t = yes
logic f = no
```

* `node` - accepts weight prepended with '^':

```elixir
node n = ^3
node n = ^123.456
```

* `arc` - accepts two nodes separated by arc:

```elixir
arc a = ^1 -> ^2
arc a = ^1 -> n
```

Arcs can have weight in brackets (default is 0) and be undirected:

```elixir
arc a = ^1 -[3]> ^2
arc a = ^1 <-[5]-> ^2
```

* `graph` - contains arcs and nodes:

```elixir
graph g = [^1, ^2, ^1 -> ^2, n, a]
```

Graph can destructure other graphs:

```elixir
graph g = [
  ^1,
  ^2 -> ^3,
  [
    n,
    [
      a,
      []
    ]
  ]
]
```

Note that duplicate items will be removed as graph is a set.

### 1.1 - Default value

If you do not initialize variable it will store `nope` value (like null but not so corny).

### 1.2 - Arrays

Any type listed above can be an array defined like:

```elixir
node{} nodes
```

It cannot be initialized by default, but you can push items to it using `<<`:

```elixir
nodes << ^2
```

To access array elements use square brackets:

```elixir
node a = nodes[0]
```

#### 1.3 - Constants

Constants can be defined with `const` keyword, like:

```elixir
const node = ^2
```

### 2 - Casts

To cast any value to different type you can use the following syntax:

```elixir
graph g = (graph) ^2
node n = (node) 2
# or
node n = ^2
```

As you can see '#' is a comment and '^' is an alias for `(node)` cast.

Note that some types can't be casted to some others e.g. arc to node.

### 3 - Operations

You can use `and`, `or` and `not` with booleans, and anysimple arithmetic operations with other types:

```elixir
num m = 2 + 2 * 2
node n = ^m
arc a = ^m -> ^1
graph g = [^1] + (graph) a + [n]
```

Note that you may need to cast values to perform some operations.

### 4 - Blocks

Blocks for functions, cycles and conditional statements are defined using `go` and `end`

### 4.1 - Conditional statements

```elixir
logic a = yes
if no or a go
  node n = ^1
else
  node n = ^2
end
```

Any non-logical types will be casted to logical when using in if condition.
Everything is true unless it's `nope` or `no`.

### 4.2 - Functions

Functions can be defined either with return type or without it. In the second case it will return `nope`:

```elixir
node foo(num a, num b) go
  return (node) (a + b)
end

bar(node a) go
  puts(a)
end
```

To call a function simply do `foo(1, 2)` or so on.

#### 4.2.1 - Builtin functions

There are some builtin functions which precompiles before the program itself:

* `node{} nodes(graph)` - return array of graph's nodes,
* `arc{} arcs(graph)` - return array of graph's arcs,
* `num weight(arc)` - return arc's weight,
* `node source(arc)` - return arc's source node,
* `node target(arc)` - return arc's target node,
* `num value(graph)` - return value of the node,
* `puts(any)` and `put(any)` - prints given structure with and without newline respectively.

It searches signatures in [builtins_signatures.sanya](src/runtime/builtins_signatures.sanya) and use their implementations
from [runtime builtins.py](https://github.com/ARtoriouSs/sanya-script-runtime/blob/master/sanya_script_runtime/builtins.py).

### 4.3 - Cycles

There are for and while cycles. For cycles can be defined as enumeration over array or as from-to cycle:

```elixir
for num i to 10 go
  puts(i)
end

for node n in nodes(g) go
  puts(n)
end

while i < 5 go
  puts(i)
  i = i + 1
end
```

Any non-logical types will be casted to logical when using in while condition.

## P.S.

There should be a lot of imperfections and bugs as I wrote it with 0 lines of tests, but it works in general :)
