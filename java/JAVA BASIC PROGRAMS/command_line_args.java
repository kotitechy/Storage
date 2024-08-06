package java_programs1.src;
public class command_line_args {
    public static void main(String args[]) {
        int count,i=0;
        String string;
        count = args.length;
        System.out.println("Number of arguments = " + count);
        while(i < count){
            string = args[i];
            System.out.println(i + ":" + " Java is " + string + "!");
        }
    }
}
