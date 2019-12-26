package com.akshdeep;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final byte MONTHS = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        float annualInterestRate = scanner.nextFloat();
        float monthlyInterestRate = annualInterestRate / PERCENT / MONTHS;

        System.out.print("Period (years): ");
        byte period = scanner.nextByte();
        int numPayments = period * MONTHS;

        double mortgage = principal *
                ((monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numPayments)) /
                        (Math.pow(1 + monthlyInterestRate, numPayments) - 1));
        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.print("Mortgage: " + mortgageFormatted);
    }
}
