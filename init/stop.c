#include <stdio.h>

int main(){
    system("sh /Applications/MNPP/init/php-fpm.sh stop");
    system("sh /Applications/MNPP/init/mysql.sh stop");
    system("sh /Applications/MNPP/init/nginx.sh stop");
    return 0;
}