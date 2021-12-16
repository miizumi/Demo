using System;
					
public class Program
{
	public static void Main()
	{
		double a;
		double b;
		double c;
		Console.WriteLine("請輸入三個數的值：");
		a = Convert.ToDouble(Console.ReadLine());
		b = Convert.ToDouble(Console.ReadLine());
		c = Convert.ToDouble(Console.ReadLine());
		if (Math.Pow(a,2)-4*a*c>=0)
			{
			  Console.WriteLine("x1=" + (-b + Math.Sqrt(Math.Pow(b, 2) - 4 * a * c)) / 2 * a);
			  Console.WriteLine("x2=" + (-b - Math.Sqrt(Math.Pow(b, 2) - 4 * a * c)) / 2 * a);
			}
			 else
				{
				  Console.WriteLine("此方程無解！！！");
				}
				Console.ReadKey();
	}
}