
## Preface

* A datatype is a collection of values
* abstract class introduces a datatype
* class introduces a variant
* **extends** connects a variant to a datatype

## The First Bit of Advice

When specifying a collection of data, use abstract classes for datatypes and extended classes for variants.

## The Second Bit of Advice

When writing a function over a datatype, place a method in each of the variants that make up the datatype. If a field
of a variant belongs to the same datatype, the method may call the corresponding method of the field in computing the
function.

## The Third Bit of Advice

When writing a function that returns values of a datatype, use new to create these values.

## The Fourth Bit of Advice

When writing several functions for the same self-referential datatype, use visitor protocols so that all methods for
a function can be found in a single class.

## The Sixth Bit of Advice

When the additional consumed values change for a self-referential use of a visitor, don't forget to create a new
visitor.

## The Seventh Bit of Advice

When designing visitor protocols for many different types, create a unifying protocol using Object.

## The Eighth Bit of Advice

Like Father, Like Son When extending a class, use overriding to enrich its functionality.

## The Ninth Bit of Advice

If a datatype may have to be extended, be forward looking and use a constructor-like (overridable) method so that
visitors can be extended, too.

## The Tenth Bit of Advice

When modifications to objects are needed, use a class to insulate the operations that modify objects. Otherwise,
beware the consequences of your actions.

(The End)