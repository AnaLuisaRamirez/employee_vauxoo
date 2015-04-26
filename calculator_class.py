Python 2.7.3 (default, Mar 14 2014, 11:57:14) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> class calculator_class:
	a = int(raw_input("> primer numero: "));
	b = int(raw_input("> segunfo numero: "));

	sum = int(0);

	while b !=0:

		sum = sum + a;
		b = b -1;
	print "La suma es: "+str(sum);

	
> primer numero: 1
> segunfo numero: 1
La suma es: 1
>>> 
