
/*
Unary Operator,
Arithmetic Operator,
Shift Operator,
Relational Operator,
Bitwise Operator,
Logical Operator,
Ternary Operator and
Assignment Operator.
 ==>> Unary operators
 1. prefix
 2. postfix

 ==>> There are 7 types of arithmetic operators in java
1. Addition +
2. Subtraction -
3. Multiplication *
4. Division /
5. Moduli Division
6. Increment ++
7. Decrement --

 ==>> Shift operator
 1. >>
 2. <<
 3. >>>

 ==>>Relational
 A. Comparison
 1. <
 2. >
 3. <=
 4. >=
 B. Equality
 5. !=
 6. ==

 ==>>Bitwise Operator
 1. & -> and
 2. | -> or
 3. ! -> not

 ==>>Logical
 1. && -> and
 2. || -> or

 ==>>Ternary
 1. ? :

 ==>> Assignment
 	1. =
    2. +=
    3. -=
    4. *=
    5. /=
    6. %=
    7. &=
    8. ^=
    9. |=
    10. <<=
    11. >>=
 	12. >>>=

 */
public class p_2_operators {
    public static void main(String[] args) {
        int a=20,b=30;
        System.out.println("Sum is     : " + (a+b));
        System.out.println("Sub is     : " + (a-b));
        System.out.println("Product is : " + (a*b));
        System.out.println("Div is     : " + (a/b));
        System.out.println("Moduli is  : " + (b%a));
        System.out.println("Increment  : " + ++a);
        System.out.println("Decrement  : " + --b);
    }
}
