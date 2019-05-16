# Tutorial on working with json

JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy to read and write. More details on the specification can be found [here](https://www.json.org/).

Python supports JSON natively with a built-in library for encoding (aka, serialization) and decoding (aka, deserialization):

```
import json
```

### Serialization

The json library provides a method to dump to file (`.dump`) or to string (`.dumps`) an object from memory, specifically the conversation follows"

|Python|Json|
|------|----|
|dict|object|
|list, tuple|array|
|str|string|
|int, long, float| number|
|True| true|
|False| false|
|None| null|

### Deserialization

The json library provides a method to load from a file (`.load`) or from a string (`.loads`). The conversation table, shows that the operation are not exactly symmetric with the serialization, look for example at `array`:

|Json|Python|
|------|----|
|object|dict|
|array|list|
|string|str|
|number(int)|int|
|number(real)|float|
|true|True|
|false|False|
|null|None|
