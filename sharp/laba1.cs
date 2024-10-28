using System;
using System.Collections.Generic;

class Program
{
    static List<double> Solve(double a, double b, double c)
    {
        double D = b * b - 4 * a * c;
        if (D < 0)
        {
            return null; 
        }

        double x1 = (-b + Math.Sqrt(D)) / (2 * a);
        double x2 = (-b - Math.Sqrt(D)) / (2 * a);

        HashSet<double> roots = new HashSet<double>(); //unic roots

        // Корни биквадратного уравнения
        if (x1 >= 0)
        {
            roots.Add(Math.Sqrt(x1));
            roots.Add(-Math.Sqrt(x1));
        }

        if (x2 >= 0)
        {
            roots.Add(Math.Sqrt(x2));
            roots.Add(-Math.Sqrt(x2));
        }

        return roots.Count > 0 ? new List<double>(roots) : null; // тернарный оператор)) если кол-во,то массив иначе none
    }

    static void Main()
    {
        double a, b, c;
        System.Globalization.CultureInfo.CurrentCulture = System.Globalization.CultureInfo.InvariantCulture; // чтобы точки хавал
        
        while (true)
        {
            string input = Console.ReadLine();
            string[] parts = input.Split();

            if (parts.Length == 3 && //check counts of coef
                double.TryParse(parts[0], out a) && //перевод в double
                double.TryParse(parts[1], out b) &&
                double.TryParse(parts[2], out c))
            {
                break; 
            }
            else
            {
                Console.WriteLine("error"); 
            }
        }

        List<double> result = Solve(a, b, c);
        
        if (result == null)
        {
            Console.WriteLine("Действительных корней нет");
        }
        else
        {
            Console.WriteLine(string.Join(" ", result)); 
        }
    }
}
