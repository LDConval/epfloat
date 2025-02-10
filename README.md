## EPFloat

Implements floating point decimals in EUD.

### API (in epscript)

```javascript
import epfloat;

const f = epfloat.EPFloat("10.01");
f.add(5); // inplace addition
f.sub("1.1"); // subtraction
f.mul(f); // multiplication

var x = 3;
f.div(x); // division

const g = f * 5 / 7; // can use operators for non-inplace arithmetics

printAll("g = {:t}", g.stringbuffer()); // prints g = 46.0685951

var h = g.toint(); // convert to EUDVariable
Weapon("Kaiser Blades").damage = g.toshort(); // convert to 0-65535 range
```

### Demo map

Download it in the Releases tab.

Check source `demo/main.eps` as an example of usage.

### Range and precision

Theoretically, it can represent numbers from 1.0 x 10⁻¹⁰²³ to 9.99999999 x 10⁴²⁹⁴⁹⁶⁶²⁷².

However I only checked four digits at the print function, so going over 10⁹⁹⁹⁹ might cause problems.

Precision is always 8 digits of decimal points.

### Specification

EPFloat uses three EUDVariables: **sign, exponent** and **mantissa** to represent a decimal.

The **sign** takes an enum value: `zero = 0, positive = 1, negative = 2`.

The **exponent** is the 10-based order of magnitude plus a bias of `EXPONENT_BIAS = 1023`.

The **mantissa** is a number between `100000000` (`1e+8`) and `999999999` (`(1e+9)-1`), where the actual mantissa is `1e-8` times this value, i.e. `612345678` represents 6.12345678.

### Why not use IEEE754?

An important function of floating number is to **print** it out.

However, to print a binary-based number as text, it would involve base-changing from 2 to 10, which turns out to be a difficult problem and opens a [box of dragons](https://github.com/abolz/Drachennest).

Obviously I don't have the idea how to implement that into EUD, so I took the easier path of using 10-based decimals instead.



