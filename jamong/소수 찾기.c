#include <stdio.h>

void main()
{
	int count, i;
	scanf("%d", &count);
	int put[count];
	
	for(i = 0; i < count; i++)
	{
		if(i == count-1) 
		{
			scanf("%d", &put[i]);
		}
		else 
		{
			scanf("%d ", &put[i]);	
		}
	}
	
	int sum = 0;
	for(i = 0; i < count; i++)
	{
		if(Prime(put[i]))
		{
			sum += 1;
		}
	}
	printf("%d", sum);
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
