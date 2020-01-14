#include <stdio.h>

void main()
{
	int i, j, o;
	int putArray[100000] = {0}; 
	
	for(i = 0; i < 100000; i++)
	{
		scanf("%d", &putArray[i]);
		if(putArray[i] == 0)
		{
			break;
		}
	}
	
	for(i = 0; i < 100000; i++)
	{
		if (putArray[i] == 0)
		{
			break;
		}
		
		int a = 0;
		int b = 0;
		for(j = 1; j < putArray[i]; j++)
		{
			for(o = j+1; o < putArray[i]; o++)
			{
				int checkPrime1 = Prime(j);
				int checkPrime2 = Prime(o);
				if(j+o == putArray[i] && checkPrime1 && checkPrime2)
				{
					if(o-j > b-a)
					{
						a = j;
						b = o;	
					}
				}
			}
		}
		
		if(a != 0 && b != 0)
		{
			printf("%d = %d + %d\n", putArray[i], a, b);
		}
		else
		{
			printf("Goldbach's conjecture is wrong.\n");
		}
	}
}

int Prime(int num)
{	
	if(num < 2) 
	{
		return 0;
	}
	
	int i;	
	for(i = 2; i <= num/2; i++)
	{
		if(num % i == 0)
		{
			return 0;
		}
	}
	return 1;
} 
