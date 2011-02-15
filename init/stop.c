#include <stdio.h>

int main(){
    system("sh /Applications/MEPP/init/php-fpm.sh stop");
    system("sh /Applications/MEPP/init/mysql.sh stop");
    system("sh /Applications/MEPP/init/nginx.sh stop");
    return 0;
}