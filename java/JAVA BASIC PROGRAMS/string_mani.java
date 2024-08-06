
public class string_mani {
    public static void main(String[] args) {
        StringBuffer str = new StringBuffer("Hello world1....");
        //string manipultion methods
        String s1 = new String("Hello wrld2!....");
        System.out.println(str.charAt(1)); //gives the character at the specified index
        System.out.println(str.append(s1));  //appends the main string str with another-string specified
        System.out.println(str.insert(1,s1));  //inserts the string at index of main string
        str.setLength(111);//1. sets a new length for string can't in sout
        //if number<str string is trimed
        //else number>str String Zero's are added
        System.out.println(str.length());




    }
}
