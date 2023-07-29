# Codsoft-import java.util.Scanner;
public class Main{
    public static void
    guessingNumberGame() {
        Scanner sc = new Scanner(System.in);
        int number = 1 + (int) (100 * Math.random());
        int k = 5;
        int i, guess;
        System.out.println("A number is chosen" + "between 1 to 100" + "Guess the number" + "within 5 trails.");
        for (i = 0; i < 5; i++) {
            System.out.println("Guess the number:");
            guess = sc.nextInt();
            if (number == guess) {
                System.out.println("Congratulations you have guessed the number. ");
                break;
            } else if (number > guess && i != 5 - 1) {
                System.out.println("The number is" + "greater than" + guess);
            } else if (number < guess && i != 5 - 1) {
                System.out.println("The number is" + " less than " + guess);
            }
        }
        if (i == k) {
            System.out.println("you have exhausted" + " k trails. ");
            System.out.println("The number was " + number);
        }
    }
        public static void main(String args[])
        {
            guessingNumberGame();

        }

    }
    "C:\Users\MY PC\.jdks\openjdk-20.0.1\bin\java.exe" "-javaagent:C:\Users\MY PC\IntelliJ IDEA Educational Edition 2022.2.2\lib\idea_rt.jar=49269:C:\Users\MY PC\IntelliJ IDEA Educational Edition 2022.2.2\bin" -Dfile.encoding=UTF-8 -Dsun.stdout.encoding=UTF-8 -Dsun.stderr.encoding=UTF-8 -classpath "C:\Users\MY PC\IdeaProjects\untitled\out\production\untitled" Main
A number is chosenbetween 1 to 100Guess the numberwithin 5 trails.
Guess the number:
20
The number is less than 20
Guess the number:
55
The number is less than 55
Guess the number:
80
The number is less than 80
Guess the number:
10
The number is less than 10
Guess the number:
22
you have exhausted k trails. 
The number was 6

Process finished with exit code 0
#codsoft java program on character count 
import javax.swing.*;
import java.awt.event.*;
import java.awt.Font;

class Main{
    public static void main(String args[]){
        JFrame f=new JFrame("Character Count");
        JLabel l2,l3,l4;
        JTextArea text;
        JLabel l1;
        JButton submit,clear;
        text=new JTextArea("");
        submit=new JButton("SUBMIT");
        clear=new JButton("CLEAR");
        l1=new JLabel("Enter Your string Here:");
        l2=new JLabel("Character with Spaces:");
        l3=new JLabel("Character Without Spaces:");
        l4=new JLabel("Words:");
        Font txtFont=new Font(Font.SERIF,Font.PLAIN,16);
        l1.setFont(txtFont);
        l2.setFont(txtFont);
        l3.setFont(txtFont);
        l4.setFont(txtFont);
        l1.setBounds(10,25,200,30);
        text.setBounds(18,60,450,300);
        l2.setBounds(10,370,400,30);
        l3.setBounds(10,400,400,30);
        l4.setBounds(10,430,400,30);
        submit.setBounds(100,470,100,50);
        clear.setBounds(275,470,100,50);
        text.setLineWrap(true);
        text.setWrapStyleWord(true);
        submit.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
            String str=text.getText().strip();
            int count=0,i,word=0;
            l2.setText("Charcter with Spaces:"+str.length());
            for(i=0;i<str.length();i++) {
                if(str.charAt(i)!='A')
                    count++;
                else
                    word++;
            }
            l3.setText("Character Without Spaces:"+count);
            l4.setText("Words:"+(word+1));
            }
        });
        clear.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                text.setText("");
                l2.setText("Character with Spaces:");
                l3.setText("Character Without Spaces:");
                l4.setText("Words:");
            }
        });
        f.add(l1);
        f.add(text);
        f.add(l2);
        f.add(l3);
        f.add(l4);
        f.add(submit);
        f.add(clear);
        f.setSize(500,570);
        f.setResizable(false);
        f.setLayout(null);
        f.setLocationRelativeTo(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
hi
This is a sample text for testing purpose
We hope you will like this GUI word counter app in java
Thank you
