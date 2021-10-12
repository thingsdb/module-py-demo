# Demo ThingsDB Module (Python)

Demo module written using the [Python language](https://python.org).


## Installation

Install the module by running the following command in the `@thingsdb` scope:

```javascript
new_module('demo', 'github.com/thingsdb/module-py-demo');
```

Optionally, you can choose a specific version by adding a `@` followed with the release tag. For example: `@v0.1.0`.

## Configuration

*This module does *not* require any config.*


## Exposed functions

Name          | Description
------------- | -----------
[echo](#echo) | Accepts an input message (string) and returns the same message back in uppercase.
[ping](#ping) | Return with `pong`.
[msg](#msg)   | Accepts an input message (string) and extra options.


### echo

Syntax: `echo(message)`

#### Arguments

- `message`: The string which will be returned in uppercase.

#### Example:

```javascript
demo.echo("Hi Demo module!").then(|reply| {
    reply;
});
```
