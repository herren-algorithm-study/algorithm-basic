#include <stdio.h>

void main() 
{
	int x, y, c;
	scanf("%d %d", &x, &y);
	c = CommonFactor(x, y);
	printf("%d", c * (x/c) * (y/c));
}

int CommonFactor(int x, int y) 
{
	if (y == 0) 
	{
		printf("%d\n", x);	
		return x;
	}
	else
	{
		return CommonFactor(y, x%y);
	}
}
