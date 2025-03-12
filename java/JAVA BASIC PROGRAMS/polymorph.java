class camera{
    void takephoto(){
        System.out.println("Photo is Taken..");
    }
}
class phone extends camera{
    @Override
    void takephoto(){
        System.out.println("Photo is Taken from mobile..");
    }
    void recordvideo(){
        System.out.println("Video is Recorded...");
    }
}
public class polymorph {
    public static void main(String[] args) {
        camera p1 = new phone();
        p1.takephoto();
        // p1.recordvideo();
    }
}
