import java.awt.*;
import javax.swing.*;

public class GaneshaSketch extends JPanel {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawGanesha(g);
    }

    private void drawGanesha(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        // Set rendering hints for better quality
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Draw the head
        g2d.setColor(Color.BLACK);
        g2d.drawOval(150, 100, 200, 200);

        // Draw the left ear
        g2d.drawOval(100, 150, 50, 100);

        // Draw the right ear
        g2d.drawOval(350, 150, 50, 100);

        // Draw the trunk
        g2d.drawArc(225, 200, 50, 100, 0, -180);
        g2d.drawLine(250, 300, 250, 350);
        g2d.drawArc(240, 350, 20, 20, 0, 180);

        // Draw the eyes
        g2d.fillOval(190, 160, 20, 20);
        g2d.fillOval(290, 160, 20, 20);

        // Draw the tusks
        g2d.drawLine(190, 240, 160, 260);
        g2d.drawLine(310, 240, 340, 260);

        // Draw the crown
        g2d.drawLine(230, 100, 250, 50);
        g2d.drawLine(250, 50, 270, 100);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Lord Ganesha Sketch");
        GaneshaSketch panel = new GaneshaSketch();
        frame.add(panel);
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
