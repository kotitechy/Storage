import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Simple2DGame extends JPanel implements ActionListener, KeyListener {
    private int playerX = 100;
    private int playerY = 100;
    private int playerSpeed = 5;

    private Timer timer;

    public Simple2DGame() {
        timer = new Timer(1000 / 60, this); // 60 FPS
        timer.start();

        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Clear the screen
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, getWidth(), getHeight());

        // Draw the player
        g.setColor(Color.RED);
        g.fillRect(playerX, playerY, 50, 50);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Update the game logic here
        repaint();
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        if (key == KeyEvent.VK_LEFT) {
            playerX -= playerSpeed;
        } else if (key == KeyEvent.VK_RIGHT) {
            playerX += playerSpeed;
        } else if (key == KeyEvent.VK_UP) {
            playerY -= playerSpeed;
        } else if (key == KeyEvent.VK_DOWN) {
            playerY += playerSpeed;
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyReleased(KeyEvent e) {
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple 2D Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.add(new Simple2DGame());
        frame.setVisible(true);
    }
}