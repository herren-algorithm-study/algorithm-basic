#include <stdio.h>

int num, min = 987654321;
int map[10][10];

int route(int before, int temp[10], int length){
        bool check = false;
        for(int i = 0; i < num; i++){
                if(temp[i] == 0){
                        check = true;
			if(map[before][i] <= 0){
				continue;
			}
                        temp[i] = 1;
			if(map[before][i] + length < min){
                        	route(i, temp, map[before][i] + length);
			}
                        temp[i] = 0;
                }
        }
        if(!check){
                if(map[before][0] > 0){
                        if(min > length + map[before][0]){
				min = length + map[before][0];
			};
			return map[before][0];
                }
                else{
                        return -1;
                }
        }
	else{
		return -1;
	}
}
int main(void){
        int temp[10] = { 0 };
        
	scanf("%d",&num);
        
	for(int i = 0; i < num; i++){
                for(int j = 0; j < num; j++){
                        scanf("%d", &map[i][j]);
                }
        }
	
	temp[0] = 1;
	route(0, temp, 0);
        printf("%d\n",min);
        
	return 0;
}
