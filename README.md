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
