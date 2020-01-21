#include <stdio.h>

int main(void) {
        int rate, rate_init;
        long i, ret, play, win, lose;

        scanf("%ld %ld", &play, &win);
        rate_init = (win * 100) / play;

        if(rate_init >= 99){
                printf("-1\n");
                return 0;
        }

        lose = play - win;

        ret = ((rate_init+1) * lose)/(99-rate_init) - win;

        rate = (win + ret) * 100 / (play + ret);
        
	if(rate == rate_init){
                for(i = ret; rate==rate_init; i++){
                        rate = int((win + i) * 100 / (play + i));
                }
                i -= 1;
        }
        else{
                for(i = ret; rate!=rate_init; i--){
                        rate = int((win + i) * 100 / (play + i));
                }
                i += 2;
        }
        printf("%ld\n", i);

        return 0;
}
