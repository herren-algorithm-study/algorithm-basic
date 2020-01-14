#include <stdio.h>

void main()
{
	int count, i;
	scanf("%d", &count);
	
	int x[count], y[count];
	for(i = 0; i < count; i++) 
	{
		scanf("%d %d", &x[i], &y[i]);
	}
	
	for(i = 0; i < count; i++) 
	{
		int com = CommonFactor(x[i], y[i]);
		printf("%d\n", com * (x[i]/com) * (y[i]/com));
	}
}

int CommonFactor(int x, int y) 
{
	if (y == 0) 
	{
		return x;
	}
	else
	{
		return CommonFactor(y, x%y);
	}
}
