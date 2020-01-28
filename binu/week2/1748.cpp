#include <stdio.h>
#include <math.h>

int main(void){
	long num, temp;
	int ret=0;

	scanf("%ld",&num);

	for(int i = 1; i <= 10; i++){
		temp = pow(10,i);
		if(temp > num){
			ret += (num - pow(10,i-1) + 1) * i;
			break;
		}
		else{
			ret += (temp * 9 / 10) * i;
		}
	}	
	
	printf("%d\n",ret);	

	return 0;
}
