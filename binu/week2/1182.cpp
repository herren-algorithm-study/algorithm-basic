#include <stdio.h>

int arr[1048576];
int index = 0;

int checkSum(int newNum, int sum){
	int cur = index, cnt = 0;
	for(int i = 0; i < cur; i++){
		arr[index++] = arr[i] + newNum;
		if(arr[i] + newNum == sum){
			cnt += 1;
		}
	}
	return cnt;
}

int main(void){
	int i, num, sum, temp, ret=0;

	arr[index++] = 0;

	scanf("%d %d", &num, &sum);

	for(i = 0; i < num; i++){
		scanf("%d",&temp);
		ret += checkSum(temp, sum);
	}

	printf("%d\n", ret);

	return 0;
}
