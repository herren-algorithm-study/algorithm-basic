#include <stdio.h>

void main()
{
	int count, i, j, o;
	scanf("%d", &count);
	int result[count];
	
	for(i = 0; i < count; i++)
	{
		int caseCount;
		scanf("%d ", &caseCount);
		
		int arr[caseCount];
		for(j = 0; j < caseCount; j++) 
		{
			if(j == caseCount-1) 
			{
				scanf("%d", &arr[j]);
			}
			else 
			{
				scanf("%d ", &arr[j]);	
			}
		}
		
		int sum = 0;
		for(j = 0; j < caseCount-1; j++)
		{
			for(o = j; o < caseCount-1; o++)
			{
				sum += CommonFactor(arr[j], arr[o+1]);
			}
		}
		result[i] = sum;
	}
	
	for(i = 0; i < count; i++)
	{
		printf("%d\n", result[i]);
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
