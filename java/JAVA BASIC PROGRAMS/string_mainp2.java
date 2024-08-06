
public class string_mainp2
{
    public static void main(String[] args) {
        StringBuffer str = new StringBuffer("Hello world");
        //getting length of string
        System.out.println("Length of String is : "  + str.length());
        //Accessing the string characters
        for (int i = 0; i < str.length(); i++) {
            System.out.println("Character at position: " + i + " is " + str.charAt(i));
        }
        //Appending 2 strings it may be any data-type (or) appending a String at end
        System.out.println("New String " + str.append(" shiva..."));
        //Modifying the characters in the string at the index
        str.setCharAt(5,'-');
        System.out.println("New String : " + str);
        //appending a string in the middle of the String
        StringBuffer str2 = new StringBuffer(str.toString());
        str2.insert(5," new");
        System.out.println(str2);
    }
}
