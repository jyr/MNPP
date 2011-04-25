#include <stdio.h>

int main(int argc, char *argv[]){
  char command[50];

  sprintf(command, "sh /Applications/MNPP/init/start.sh %s", argv[1]);
  system(command);

  return 0;
}