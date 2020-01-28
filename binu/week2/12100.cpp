#include <stdio.h>

int num, max = 0;
int initial[20][20];

int move(int cnt, int map[20][20], int way){
	int before, now, target, index;
	int after[20][20] = { 0, };

	for(int i = 0; i < num; i++){
		index = 0;
		before = 0;
		for(int j = 0; j < num; j++){
			switch(way){
				case 0:
					now = map[i][j];
					if(now == 0){
						break;
					}
					else if(before == now){
						target = before + now;
						before = 0;
					}
					else if(before != 0){
						target = before;
						before = now;
					}
					else{
						before = now;
						break;
					}
					if(target >= max){
						max = target;
					}
					after[i][index++] = target;
					break;
				case 1:
					now = map[i][num-j-1];
					if(now == 0){
						break;
					}
					else if(before == now){
						target = before + now;
						before = 0;
					}
					else if(before != 0){
						target = before;
						before = now;
					}
					else{
						before = now;
						break;
					}
					if(target >= max){
						max = target;
					}
					after[i][num - index++ -1] = target;
					break;
				case 2:
					now = map[j][i];
					if(now == 0){
						break;
					}
					else if(before == now){
						target = before + now;
						before = 0;
					}
					else if(before != 0){
						target = before;
						before = now;
					}
					else{
						before = now;
						break;
					}
					if(target >= max){
						max = target;
					}
					after[index++][i] = target;
					break;
				case 3:
					now = map[num-j-1][i];
					if(now == 0){
						break;
					}
					else if(before == now){
						target = before + now;
						before = 0;
					}
					else if(before != 0){
						target = before;
						before = now;
					}
					else{
						before = now;
						break;
					}
					if(target >= max){
						max = target;
					}
					after[num - index++ - 1][i] = target;
					break;
				default:
					break;
			}
		}
		switch(way){
			case 0:
				after[i][index] = before;
                                break;
                        case 1: 
                                after[i][num-index-1] = before;
                                break;
                        case 2: 
                                after[index][i] = before;
                                break;
                        case 3: 
                                after[num-index-1][i] = before;
                                break;
                        default:
                                break;
		}
		if(before >= max){
			max = before;
		}
	}
	if(cnt == 5){
		return 0;
	}

	for(int i = 0; i < 4; i++){
		move(cnt + 1, after, i);
	}
	return 0;
}

int main(void){
	
	scanf("%d",&num);

	for(int i = 0; i < num; i++){
		for(int j = 0; j < num; j++){
			scanf("%d",&initial[i][j]);
		}
	}
	
	for(int i = 0; i < 4; i++){
		move(1, initial, i);
	}

	printf("%d\n",max);

	return 0;
}
