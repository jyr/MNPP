#include <stdio.h>

int main(){
    system("sh /Applications/MNPP/init/php.sh stop");
    system("sh /Applications/MNPP/init/percona.sh stop");
    system("sh /Applications/MNPP/init/nginx.sh stop");
    return 0;
}